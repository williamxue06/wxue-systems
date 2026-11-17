# Plan: Add a "status" field and a status filter to the problem tracker

## Context
Lab 2, Part C asks for a planned (not improvised) feature: each problem gets a status of
**open**, **in progress**, or **solved**, and the list can be filtered by status. Today problems
only have title, description, frequency, and timestamp, so there is no way to mark a problem as
handled or hide solved ones.

Only one file changes: `labs/lab-02/problem-tracker/index.html`. The rules in this folder's
`CLAUDE.md` apply: no frameworks or libraries, localStorage only, find problems by `id`, and
older saved problems may be missing newer fields.

## Approach

### 1. Data
- Add a `status` field to each problem: `"open"`, `"in-progress"`, or `"solved"`.
- New problems start as `"open"`. (No status dropdown on the Add form, since a problem you just
  noticed is open by definition.)
- **Older problems have no `status`.** Treat a missing status as `"open"` when drawing and
  filtering, the same way a missing frequency shows "Not rated". Don't rewrite old saved data.
- Add a `STATUS_LABELS` object next to the existing `FREQUENCY_LABELS`
  (`open: "Open"`, `"in-progress": "In progress"`, `solved: "Solved"`).

### 2. Changing a problem's status
- On each problem card, add a small dropdown (`<select>`) showing the current status.
- When it changes, find the problem **by `id`** (same pattern as `deleteProblem`), set the new
  status, call the existing `saveProblems()`, then `renderProblems()`.
- Solved problems get a muted look (lighter text) so open ones stand out.

### 3. Filtering by status
- Add a "Show" dropdown next to the existing search box: **All**, **Open**, **In progress**,
  **Solved**. Default: All.
- In `renderProblems()`, extend the existing `visible` filter so a problem must match **both**
  the title search **and** the chosen status.
- Add an `input`/`change` listener on the new dropdown that calls `renderProblems()`, the same
  way the search box does.
- The existing "No problems match your search." message also covers "no problems with this
  status"; reword it to "No problems match your search or filter."

### 4. Status counter (change requested during plan review)
- Above the problem list, show a one-line summary such as **Open: 3 · In progress: 1 · Solved: 2**.
- Add an empty `<p id="status-counts">` in the HTML just above the list.
- In `renderProblems()`, count **all** problems by `getStatus()` (so old problems with no status
  count as Open). Counts always describe the whole list, not just what the search or filter shows,
  so the totals don't jump around while you search.
- Because `renderProblems()` already runs after every add, delete, status change, search, and
  filter change, the counter stays current with no extra listeners.
- Hide the counter when there are no problems at all (the "No problems yet" message shows instead).

### 5. Styling
- Reuse the existing input/select styles. Put the search box and status filter side by side
  on wide screens and stacked on phones.
- Optional status badge colors, following the frequency badge pattern (`.badge.daily` etc.).

## What stays the same
- No libraries, no build step, localStorage only.
- Delete still asks for confirmation and works by `id`.
- Old problems without `frequency` still show "Not rated".

## How to verify
1. Open `index.html`. Old problems should show status **Open** with no errors.
2. Add a problem: it starts as Open.
3. Change one problem to In progress and one to Solved. Refresh the page; the statuses stay.
4. Use the Show filter: each option shows only matching problems; All shows everything.
5. Combine filter + search (e.g. Show: Open, search "print"): only problems matching both.
6. Choose a filter with no matches: the "no match" message appears.
7. Delete a problem while a filter is on: the confirm appears and the right problem is removed.
8. Counter: check that it matches the list. Change a status, add a problem, and delete one; the
   counts update each time. Searching or filtering does **not** change the counts.
