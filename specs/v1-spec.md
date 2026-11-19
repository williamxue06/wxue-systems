# Gym Workout Log — Version 1 Spec

## Purpose and evidence

Help lifters record performed sets and find previous results instead of relying on memory. See [requirements](../discovery/requirements.md) and the three interviews linked there. This spec describes a build that has not yet been implemented.

## Scope

One phone-friendly page with a logging form and dated workout history. Each saved entry is one performed set. Rest timers, charts, automatic recommendations, editing, deleting, accounts, AI, and cloud synchronization are outside version 1.

## Interface

- Heading: Gym Workout Log.
- Form labels: Exercise, Weight (lb), Reps. Action: Save set.
- History displays newest entries first, with an empty-state prompt before the first save.
- Explain that entries are saved in this browser only.
- Keep the exercise and weight after a successful save to simplify logging another set; clear reps and return focus there.
- Preserve all form values when validation or saving fails.

## Input rules

Trim the exercise name; require 1–80 characters. Weight is required, finite, between 0 and 2000 inclusive, with at most two decimal places. Reps is a required integer between 1 and 1000 inclusive. These are data-validation limits, not training recommendations. All weight is in pounds for version 1.

## Data and storage

Use the course stack: Next.js, TypeScript, Tailwind, with Vitest for tests. Store entries under a versioned local-storage key, `gym-workout-log:v1`, using an object containing `version: 1` and an `entries` array. Each entry has a unique `id`, trimmed `exercise` string, numeric `weightLb`, integer `reps`, and ISO `createdAt` timestamp generated at save time.

Load storage only in the browser. Validate loaded structure and values. Display a recovery message and disable writes if stored data is unreadable, retaining the original value. On a failed save, preserve inputs and do not show success. Only update the visible saved history after storage succeeds. Render exercise names as text.

Storage is specific to the browser profile and site origin. Clearing browser data can remove history. There are no accounts, server database, or cross-device guarantees in this version.

## Acceptance and verification

The [user stories](user-stories.md) define the acceptance criteria. Verify:

1. Save Cable lateral raise, 17.5 lb, 10 reps; confirm one dated history entry.
2. Save another set with identical values; confirm two separate entries.
3. Save a different exercise; confirm newest-first ordering.
4. Refresh; confirm all entries remain unchanged.
5. Try blank exercise, whitespace, negative or blank weight, and zero or fractional reps; confirm errors and no new entry. Confirm 0 lb is accepted.
6. Check storage failures and malformed stored data; confirm honest errors and no silent data loss.
7. Check keyboard use and a 375-pixel phone layout.

Use Vitest for meaningful validation and storage-behavior tests, plus manual browser checks for the main flow and layout. Record actual outcomes after implementation; no checks are claimed as passed yet.

## Deployment

Deploy on Vercel at a public URL and link it in README.md. A public app URL does not make browser-local histories shared. Deployment has not yet happened.
