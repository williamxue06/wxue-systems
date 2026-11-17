# Lab 2 Reflection

**Live URL:** https://wxue-systems-problem-tracker.vercel.app/

### 1. Compare the one-shot build and the step-by-step build. Which would you rather maintain, and why?

I would rather maintain the step-by-step version because I had more control over what Claude was building. When I gave Claude one big prompt, it added features like exporting and importing data that I didn't really want. It also left out features I wanted, like charts and being able to change priorities and statuses. With the step-by-step approach, I could tell Claude exactly what to add and test each feature before moving on. I think this approach was better because it was easier to fix mistakes and make sure the app worked the way I wanted.

### 2. Did the fresh session follow your CLAUDE.md? What does that tell you about where to write down decisions?

Yes, Claude followed the rules in my CLAUDE.md when I started a new session. I asked it to add a search box using whatever library it thought was best, but it still used plain JavaScript without adding any libraries. This showed me that CLAUDE.md is useful for keeping important instructions and decisions in one place. Even when I restart Claude, it can still follow the same rules without me having to explain everything again.

### 3. What is the difference between a rule in CLAUDE.md and a rule in settings.json? When would you need the second kind?

The main difference is that CLAUDE.md gives Claude instructions to follow, while settings.json can actually block certain commands. For this lab, I added rules to prevent Claude from running rm -rf and git push --force. When I tested rm -rf test-folder, Claude was blocked from running it, which showed me that the permission rule worked. I think settings.json is important when working on bigger projects because it helps prevent dangerous actions, like accidentally deleting files or force-pushing changes to GitHub.
