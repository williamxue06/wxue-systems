# Version 1 Verification — November 19, 2026

## Completed checks

- Vitest: six tests pass, covering valid and invalid values, storage round-trip, separate identical sets, corrupt data, failed writes, and ordering.
- Production build: `next build --webpack` passes, including TypeScript checks.
- Browser: saved Cable lateral raise, 17.5 lb, 10 reps; confirmation and one history entry appeared.
- Browser: refreshed the page; the saved entry remained.
- Browser: submitted blank fields; three field errors appeared with no new entry.
- Narrow preview: layout visually inspected; viewport tool returned a 416-pixel content width despite a requested 375-pixel width, so exact 375-pixel acceptance remains unverified.

## Remaining checks

- User must try the app and confirm it works for them.
- Complete keyboard and assistive-technology checks.
- Browser-level simulation of storage failures and corrupt data (logic is covered by automated tests).
- Usability sessions with the interviewed participants.

## Tooling note

The default Turbopack production build failed when creating a local process/port in this environment. Webpack compilation succeeds; the build script uses `next build --webpack` for reproducibility.

A sample set was entered in the local preview and in this browser on the public site. No sample workout histories are committed or shared across users.

## Public deployment

Deployed November 19, 2026: https://repbook-workout-log.vercel.app/

Vercel reported Deployed to Production for project `repbook-workout-log`, using the repository’s `app` root directory. The public app loaded, saved Cable lateral raise at 17.5 lb for 10 reps, and retained the entry after refreshing. This is an agent verification, not a completed student usability session.
