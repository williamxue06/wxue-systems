# Sprint 1 Review

## Report

**Plan goal:** A user can log a workout by entering the exercise, weight, and reps.

**What was produced:**

- Project context and public app link: [README](../README.md).
- Three anonymized interviews: [Participant 1](../discovery/interview-1.md), [Participant 2](../discovery/interview-2.md), [Participant 3](../discovery/interview-3.md).
- [Requirements summary](../discovery/requirements.md), including the problem, job to be done, persona, riskiest assumption, and MVP scope.
- [User stories and acceptance criteria](../specs/user-stories.md), [process flow](../design/process-flow.md), and [version 1 spec](../specs/v1-spec.md).
- [App](../app/src/app/page.tsx) with exercise, weight, and rep entry, dated history, validation, and browser-local persistence.
- [Six automated tests](../app/src/lib/log.test.ts) and [verification report](../specs/v1-verification.md), including the successful production build and public-site save/refresh check.
- [Public deployment](https://repbook-workout-log.vercel.app/).

**When the work happened:** Before this review, the repository contains 18 commits across 4 days in the Sprint 1 window. Daily counts: 2026-11-12: 8, 2026-11-16: 5, 2026-11-17: 2, 2026-11-19: 3. The busiest day was 2026-11-12. The three gym-project commits (plan, implementation, and deployment documentation) were all made November 19. Earlier commits concern the starter and Labs 1–2.

**Where it got stuck:** Lab 2's one-shot tracker was added and then removed on November 12 before being added again on November 16. For the gym app, the verification report records a failed Turbopack build involving local process/port access and a successful Webpack build. No gym-app revert is present in the commit history.

**SDLC phases covered:** Analysis: interviews and requirements. Design: user stories, flow, and version 1 spec. Implementation: Next.js app and browser storage. Testing: automated tests and documented browser checks. Deployment: Vercel URL recorded in README and verification report. Architecture and database work remain for Sprint 2.

**Against the plan:** The stated completion condition was saving an exercise with weight and reps and finding it in history after refreshing. The implementation includes these actions, and the verification report records this behavior on the public site. Exact 375-pixel layout, full accessibility checks, and participant usability sessions remain unverified. The student's retro answers are recorded below. The Loom demo is still pending.

## Retro

Student answers are preserved as supplied. Question 4 includes the follow-up explanation.

### 1. Did you hit the goal? Yes, partly, or no, and why.

yes u can track everything propely

### 2. About how many hours did you spend on this sprint, all in?

2hrs

### 3. If the plan changed, why?

no

### 4. Actual difficulty, 1 to 5, and why it differed from what you predicted.

2

ai wsa very helpful

### 5. What will you change next sprint (or on your next project)?

put more thought into more things i can add
