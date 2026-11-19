# William Xue: Systems Analysis and Design project

## Context

- **My user:** People who lift weights and want a simple phone-friendly workout log.
- **Their problem:** Interviewed lifters forget previous weights and reps, and find notes or spreadsheets awkward during workouts.
- **The system:** A gym workout log for saving exercises, weights, and reps and reviewing dated history.
- **Working alone or in a pair:** Not yet recorded.
- **Status:** Sprint 1 app implemented locally; six automated tests and a production build pass. Public deployment and student review remain.

Context updated November 19, 2026, after three interviews confirmed difficulty remembering and finding previous workout results. Interview responses are anonymized; no interview recordings are stored here.

## Where the work lives

| What | Link |
|---|---|
| Live app | Not deployed yet |
| Requirements | [discovery/requirements.md](discovery/requirements.md) |
| v1 spec | [specs/v1-spec.md](specs/v1-spec.md) |
| Process flow | [design/process-flow.md](design/process-flow.md) |
| User stories | [specs/user-stories.md](specs/user-stories.md) |
| Architecture diagram | Planned for Sprint 2 |
| Data model | Planned for Sprint 2 |
| AI feature eval | Planned for Sprint 2 |

## Folders

| Folder | What goes in it |
|---|---|
| `labs/` | One folder per lab: `lab-01/` to `lab-08/` |
| `sprints/` | Sprint plans and reviews, written by `/sprint-plan` and `/sprint-review` |
| `discovery/` | Interview notes (names removed) and `requirements.md` |
| `design/` | Flows, mockups, design decisions, usability test notes |
| `specs/` | User stories, feature specs, task lists, AI evals |
| `architecture/` | Architecture diagrams, ERD, SQL schema and policies |
| `app/` | The code for your system |
| `peer-review/` | Your peer code review of a classmate's system |

## Run the workout log

From `app/`, run `pnpm install`, then `pnpm dev` and open the printed local URL. Use `pnpm test` for automated checks and `pnpm build` for a production build. npm equivalents are also available for scripts.

For Vercel deployment, import this GitHub repo, set the Root Directory to `app`, and use the Next.js preset. Link the verified public deployment above afterward. The app does not require environment variables for Sprint 1.
