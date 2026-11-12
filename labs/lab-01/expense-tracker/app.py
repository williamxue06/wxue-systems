"""A simple expense tracker built with Streamlit, using a JSON file as its database."""

import json
import os
import uuid
from datetime import date, datetime
from pathlib import Path

import streamlit as st

# The "database": a JSON file stored next to this script.
DB_PATH = Path(__file__).parent / "expenses.json"
# The monthly budget limit is saved in its own small JSON file.
BUDGET_PATH = Path(__file__).parent / "budget.json"

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


def load_budget() -> float:
    """Read the monthly budget limit. Returns 0 (meaning "not set") if there isn't one yet."""
    if not BUDGET_PATH.exists():
        return 0.0
    try:
        with BUDGET_PATH.open("r", encoding="utf-8") as f:
            return float(json.load(f).get("monthly_budget", 0.0))
    except (json.JSONDecodeError, ValueError, AttributeError):
        return 0.0


def save_budget() -> None:
    """Save the limit typed into the budget box (runs whenever that box changes)."""
    tmp_path = BUDGET_PATH.with_suffix(".json.tmp")
    with tmp_path.open("w", encoding="utf-8") as f:
        json.dump({"monthly_budget": round(st.session_state.budget_input, 2)}, f, indent=2)
    os.replace(tmp_path, BUDGET_PATH)


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


def update_expense(expense_id: str, amount: float, category: str, spent_on: date, note: str) -> None:
    """Change an existing expense in place. Its id and created_at stay the same."""
    expenses = load_expenses()
    for e in expenses:
        if e["id"] == expense_id:
            e["amount"] = round(amount, 2)
            e["category"] = category
            e["date"] = spent_on.isoformat()
            e["note"] = note.strip()
    save_expenses(expenses)


def start_editing(expense_id: str) -> None:
    st.session_state.editing_id = expense_id


def stop_editing() -> None:
    st.session_state.editing_id = None


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

# Which expense (if any) is currently open for editing.
if "editing_id" not in st.session_state:
    st.session_state.editing_id = None

# ---------- Monthly budget ----------
st.subheader("Monthly budget")
st.number_input(
    "Spending limit for this month ($)",
    min_value=0.0,
    step=10.0,
    format="%.2f",
    value=load_budget(),
    key="budget_input",
    on_change=save_budget,
)
budget = st.session_state.budget_input
this_month = date.today().strftime("%Y-%m")  # e.g. "2026-11"
spent_this_month = sum(e["amount"] for e in expenses if e["date"].startswith(this_month))

if budget > 0:
    remaining_budget = budget - spent_this_month
    spent_col, remaining_col = st.columns(2)
    spent_col.metric(f"Spent in {date.today():%B}", f"${spent_this_month:,.2f}")
    sign = "-" if remaining_budget < 0 else ""
    remaining_col.metric("Remaining", f"{sign}${abs(remaining_budget):,.2f}")
    st.progress(min(spent_this_month / budget, 1.0))
    if remaining_budget < 0:
        st.error(f"You are ${-remaining_budget:,.2f} over your budget this month.")
else:
    st.caption("Enter a limit above to track how much of your budget is left this month.")

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
        # If this is the expense being edited, show a pre-filled form instead of the row.
        if st.session_state.editing_id == e["id"]:
            with st.form(f"edit_{e['id']}"):
                st.write("**Edit expense**")
                a_col, c_col, d_col = st.columns(3)
                with a_col:
                    new_amount = st.number_input(
                        "Amount ($)", min_value=0.0, step=1.0, format="%.2f", value=float(e["amount"])
                    )
                with c_col:
                    current = e["category"] if e["category"] in CATEGORIES else "Other"
                    new_category = st.selectbox("Category", CATEGORIES, index=CATEGORIES.index(current))
                with d_col:
                    new_date = st.date_input("Date", value=date.fromisoformat(e["date"]))
                new_note = st.text_input("Note", value=e["note"])

                save_col, cancel_col = st.columns(2)
                saved = save_col.form_submit_button("Save")
                cancelled = cancel_col.form_submit_button("Cancel")

            if saved:
                if new_amount <= 0:
                    st.warning("Enter an amount greater than $0.")
                else:
                    update_expense(e["id"], new_amount, new_category, new_date, new_note)
                    stop_editing()
                    st.rerun()  # redraw the page so totals and the budget update right away
            if cancelled:
                stop_editing()
                st.rerun()
            continue

        info_col, edit_col, delete_col = st.columns([0.8, 0.1, 0.1])
        with info_col:
            note_text = f" · {e['note']}" if e["note"] else ""
            st.write(f"{e['date']} · **${e['amount']:,.2f}** · {e['category']}{note_text}")
        with edit_col:
            st.button(
                "✏️",
                key=f"edit_btn_{e['id']}",
                help="Edit expense",
                on_click=start_editing,
                args=(e["id"],),
            )
        with delete_col:
            st.button(
                "🗑️",
                key=f"delete_{e['id']}",
                help="Delete expense",
                on_click=delete_expense,
                args=(e["id"],),
            )
