# Gym Workout Log — Requirements

Status: Interview synthesis and first-version requirements. The first version is built and deployed; see the version 1 verification report for checks completed.

## Problem statement

The interviewed lifters use notes, spreadsheets, or memory to track workouts. All three described forgetting previous weights or reps. Finding past numbers and entering new results can interrupt a workout.

## Job to be done

When I am logging an exercise at the gym, I want to quickly see what I lifted previously and record today’s weight and reps, so I can track changes without relying on memory.

## Persona

A lifter who uses a phone during workouts, wants to record weights and reps with little effort, and needs previous results easy to find. This is a synthesis of the interviews rather than an additional participant.

## Evidence

- [Participant 1](interview-01.md): messy notes are difficult to search; wants previous numbers beside new entry fields.
- [Participant 2](interview-02.md): spreadsheet cells are awkward on a phone; wants fast logging and accessible history.
- [Participant 3](interview-03.md): relies mainly on memory; wants minimal setup and logging in about ten seconds per exercise.

## Riskiest assumption

A simple form plus accessible previous results will be fast enough that users keep logging during actual workouts. The interviews show interest but do not demonstrate continued use.

Proposed validation: ask the three participants to log an exercise and find its previous result on their phones without help. Record time, errors, and their feedback. No usability testing has been completed yet.

## MVP scope

- Enter an exercise, weight in pounds, and reps.
- Save a dated entry and show a clear confirmation.
- View workout history with the exercise, weight, reps, and date.
- Keep saved entries after refreshing in the same browser.
- Use a phone-friendly layout with minimal setup.

Each saved entry represents one performed set. Users can add more entries for additional sets. History provides access to previous results; an inline previous-result display remains a future enhancement.

## Deferred features

Inline previous results, rest timers, repeat-session shortcuts, exercise swaps, progression recommendations, charts, accounts, cloud synchronization, and AI features. These requests are recorded but are not all necessary for the first version.

## Limits and implementation decisions

- Version 1 uses browser local storage. Data stays in the same browser profile and site, does not synchronize, and can be lost if browser data is cleared. Accounts and a database belong to Sprint 2.
- Interview dates and methods were not supplied.
- Exercise names are free text, trimmed before saving. Entries are displayed newest first and dated automatically; there is no separate workout-session object in version 1.
- This document records proposed requirements, not completed app behavior.
