"""A simple to-do list app built with Streamlit, using a JSON file as its database."""

import json
import os
import uuid
from datetime import datetime
from pathlib import Path

import streamlit as st

# The "database": a JSON file stored next to this script.
DB_PATH = Path(__file__).parent / "todos.json"


# ---------- Database helpers ----------

def load_todos() -> list[dict]:
    """Read all tasks from the JSON file. Returns an empty list if the file doesn't exist yet."""
    if not DB_PATH.exists():
        return []
    try:
        with DB_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        st.error("todos.json is not valid JSON. Fix or delete the file to continue.")
        st.stop()


def save_todos(todos: list[dict]) -> None:
    """Write all tasks to the JSON file safely (write to a temp file, then swap it in)."""
    tmp_path = DB_PATH.with_suffix(".json.tmp")
    with tmp_path.open("w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2)
    os.replace(tmp_path, DB_PATH)


# ---------- Actions (each one loads, changes, and saves) ----------

def add_todo() -> None:
    title = st.session_state.new_task.strip()
    if not title:
        return
    todos = load_todos()
    todos.append({
        "id": uuid.uuid4().hex,
        "title": title,
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    })
    save_todos(todos)
    st.session_state.new_task = ""  # clear the input box


def toggle_todo(todo_id: str) -> None:
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
    save_todos(todos)


def delete_todo(todo_id: str) -> None:
    todos = [t for t in load_todos() if t["id"] != todo_id]
    save_todos(todos)


def clear_completed() -> None:
    save_todos([t for t in load_todos() if not t["done"]])


# ---------- Page layout ----------

st.set_page_config(page_title="To-Do List", page_icon="✅")
st.title("✅ To-Do List")

st.text_input(
    "Add a task",
    key="new_task",
    placeholder="What do you need to do? (press Enter to add)",
    on_change=add_todo,
)

todos = load_todos()
remaining = sum(1 for t in todos if not t["done"])

if not todos:
    st.info("No tasks yet. Add one above!")
else:
    st.caption(f"{remaining} of {len(todos)} task(s) remaining")

    for todo in todos:
        check_col, delete_col = st.columns([0.9, 0.1])
        with check_col:
            label = f"~~{todo['title']}~~" if todo["done"] else todo["title"]
            st.checkbox(
                label,
                value=todo["done"],
                key=f"check_{todo['id']}",
                on_change=toggle_todo,
                args=(todo["id"],),
            )
        with delete_col:
            st.button(
                "🗑️",
                key=f"delete_{todo['id']}",
                help="Delete task",
                on_click=delete_todo,
                args=(todo["id"],),
            )

    if any(t["done"] for t in todos):
        st.button("Clear completed", on_click=clear_completed)
