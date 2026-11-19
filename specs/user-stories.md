# User Stories and Acceptance Criteria

These criteria describe required behavior, not completed tests.

## US1 — Log a performed set

As a lifter, I want to enter an exercise, weight, and reps so I can remember what I did.

- Given a nonblank exercise of up to 80 characters, a finite weight from 0 through 2000 pounds, and an integer rep count from 1 through 1000, saving creates exactly one dated entry.
- Weight accepts up to two decimal places; zero supports exercises without added weight.
- Invalid or missing values display a helpful field error, preserve the typed values, and create no entry.
- A successful save displays confirmation and makes the entry visible in history without a page refresh.
- A second deliberate save can create another set with identical values; unique entry IDs distinguish them.

## US2 — Review past performance

As a lifter, I want to review prior entries so I can compare my weights and reps over time.

- Each history entry displays exercise, weight with the lb unit, reps, and local date and time.
- Entries are ordered newest first.
- With no entries, history explains how to add the first set.
- Exercise names render as text, including names containing HTML characters.

## US3 — Keep entries after refresh

As a lifter, I want my entries to survive a refresh so I do not need to enter them again.

- A saved entry remains after refreshing or reopening the same site in the same browser profile.
- Entries are not promised to appear in another browser or device.
- If saving is blocked or storage is full, the app displays an error and does not claim success or clear the input.
- Unreadable saved data displays a recovery message without crashing or silently overwriting the stored value.

## US4 — Use a phone during a workout

As a lifter, I want a simple phone-friendly screen so logging is easy between sets.

- At 375 pixels wide, the form and history fit without horizontal scrolling.
- Every input has a visible label; numeric inputs request an appropriate mobile keyboard.
- The form can be completed with a keyboard; errors and save confirmation are accessible to assistive technology.
- No account or setup questionnaire is required in version 1.
