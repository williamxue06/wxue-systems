# CLAUDE.md

## Project overview

A personal problem tracker for capturing problems I notice throughout the day. It was built in
small, checkable steps for BMIS 301 Lab 2.

## Tech stack

- Deployed as a static site on Vercel (root directory `labs/lab-02/problem-tracker`)

## Development Notes

- No frameworks and no build step: everything stays in index.html.
- Never store data on a server; localStorage only.
- Problems saved before the frequency field existed have no `frequency` value. Keep handling that
  case (they show "Not rated") instead of assuming every problem has every field.
- Find problems by their `id`, not by their position in the list. The list is shown newest first,
  so on-screen order does not match the saved array.
- Always ask the user for confirmation before deleting a problem. Never automatically delete problems.
