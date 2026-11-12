"""A simple expense tracker built with Streamlit, using a JSON file as its database."""

import json
import os
import uuid
from datetime import date, datetime
from pathlib import Path

import streamlit as st

# The "database": a JSON file stored next to this script.
DB_PATH = Path(__file__).parent / "expenses.json"

CATEGORIES = ["Food", "Transport", "School", "Entertainment", "Bills", "Other"]


# ---------- Database helpers ----------

def load_expenses() -> list[dict]:
    """Read all expenses from the JSON file. Returns an empty list if the file doesn't exist yet."""
    if not DB_PATH.exists():
        return []
    try:
        with DB_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        st.error("expenses.json is not valid JSON. Fix or delete the file to continue.")
        st.stop()


def save_expenses(expenses: list[dict]) -> None:
    """Write all expenses to the JSON file safely (write to a temp file, then swap it in)."""
    tmp_path = DB_PATH.with_suffix(".json.tmp")
    with tmp_path.open("w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)
    os.replace(tmp_path, DB_PATH)


# ---------- Actions (each one loads, changes, and saves) ----------

def add_expense(amount: float, category: str, spent_on: date, note: str) -> None:
    expenses = load_expenses()
    expenses.append({
        "id": uuid.uuid4().hex,
        "amount": round(amount, 2),
        "category": category,
        "date": spent_on.isoformat(),
        "note": note.strip(),
        "created_at": datetime.now().isoformat(timespec="seconds"),
    })
    save_expenses(expenses)


def delete_expense(expense_id: str) -> None:
    save_expenses([e for e in load_expenses() if e["id"] != expense_id])


# ---------- Page layout ----------

st.set_page_config(page_title="Expense Tracker", page_icon="💵")
st.title("💵 Expense Tracker")

# A form groups the inputs so nothing is saved until "Add expense" is clicked.
with st.form("new_expense", clear_on_submit=True):
    amount_col, category_col, date_col = st.columns(3)
    with amount_col:
        amount = st.number_input("Amount ($)", min_value=0.0, step=1.0, format="%.2f")
    with category_col:
        category = st.selectbox("Category", CATEGORIES)
    with date_col:
        spent_on = st.date_input("Date", value=date.today())
    note = st.text_input("Note", placeholder="What was it for? (optional)")

    if st.form_submit_button("Add expense"):
        if amount <= 0:
            st.warning("Enter an amount greater than $0.")
        else:
            add_expense(amount, category, spent_on, note)
            st.success(f"Added ${amount:,.2f} for {category}.")

expenses = load_expenses()

if not expenses:
    st.info("No expenses yet. Add one above!")
else:
    total = sum(e["amount"] for e in expenses)
    st.metric("Total spent", f"${total:,.2f}")

    # Totals per category, largest first
    st.subheader("By category")
    by_category: dict[str, float] = {}
    for e in expenses:
        by_category[e["category"]] = by_category.get(e["category"], 0) + e["amount"]
    for cat, cat_total in sorted(by_category.items(), key=lambda kv: kv[1], reverse=True):
        st.write(f"**{cat}:** ${cat_total:,.2f}")

    # Every expense, newest date first
    st.subheader("All expenses")
    for e in sorted(expenses, key=lambda e: (e["date"], e["created_at"]), reverse=True):
        info_col, delete_col = st.columns([0.9, 0.1])
        with info_col:
            note_text = f" · {e['note']}" if e["note"] else ""
            st.write(f"{e['date']} · **${e['amount']:,.2f}** · {e['category']}{note_text}")
        with delete_col:
            st.button(
                "🗑️",
                key=f"delete_{e['id']}",
                help="Delete expense",
                on_click=delete_expense,
                args=(e["id"],),
            )
