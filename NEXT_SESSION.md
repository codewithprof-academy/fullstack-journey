# Next session handoff

Updated: 2026-10-11

Start with [`AGENTS.md`](AGENTS.md), then inspect the current files before editing. This handoff preserves the decisions from the current session; it is not a substitute for checking the repository.

## User's goal and decisions

- Organize Week 01 and build a reusable navigation structure for a 16-week cohort. Add each new week as files become available.
- Use the full brand name **CodeWithProf - NextGen Web, Cloud & AI Engineering Bootcamp - (Explorers) Cohort 1** and **Explorers ages 9–14**.
- Use `Salvaton Lloyd Stanley-Kemuel` as the owner in course Markdown frontmatter.
- Use the logos in `assets/` in READMEs and, where useful, the slides and PDF.
- Make demos practical for participants. Week 01 must not depend on running Python scripts or using them for tests. D3 should visibly show an IP address through a non-Python activity.

## Current structure and materials

- [`README.md`](README.md) → [`Explorer/README.md`](Explorer/README.md) → [`Explorer/Week 01/README.md`](Explorer/Week%2001/README.md) provide the main navigation. The root index reserves Weeks 02–16 for future material.
- Week 01 contains a [30-slide PPTX](Explorer/Week%2001/Code_with_Prof_Week_01_Fullstack_Journey.pptx), a [13-page reading PDF](Explorer/Week%2001/Code_with_Prof_Week_01_Student_Reading_Notes.pdf), assignment and project guides, two lab worksheets, and [D1–D5 demos](Explorer/Week%2001/demos/README.md).
- D2 is a browser URL Explorer. D3's browser [`dns-explorer.html`](Explorer/Week%2001/demos/d3-dns-lookup/dns-explorer.html) uses Google Public DNS over HTTPS to display IPv4/IPv6 answers; the demo README also gives a terminal `nslookup` route. D4 has an offline browser server conversation simulation. D5 uses browser developer tools, with `curl` optional.
- `dns_lookup.py` and `tiny_server.py` remain in the repository as later previews. Do not run them for Week 01 verification.
- The supplied logo variants and avatars are in [`assets/`](assets/). Main and demo READMEs reference the logo. The PDF cover and PPTX title use the supplied branding; the deck's age range and DNS activity were updated.

## Verification already done

- All 14 course Markdown files present before this handoff had the intended owner and working local links/image paths.
- The PDF was checked as 13 pages; the PPTX archive was checked for integrity and its title slide was visually inspected in WPS Office.
- The live DNS A and AAAA lookup approach was checked against Google Public DNS documentation and live responses. The local browser UI was not verified in a browser session.
- Python demo scripts were not run.

## Known gaps and next steps

- No Week 02–16 material is present. When it arrives, create `Explorer/Week NN/README.md`, link every real file there, and update the root and Explorer indexes.
- The reading PDF mentions a separate *Student Practical Guide* that is not in this repository. The current assignment and lab files supply Week 01 practice; add and link the guide only if it becomes available.
- If the DNS browser activity is changed, verify that an actual participant can see an IP address on a network with access to Google Public DNS. Keep the `nslookup` alternative.
- Recheck local links and owner values after future additions. Update this handoff with new work and unresolved items.
- Keep the learner-facing READMEs focused on how to use the course. Put file-maintenance instructions in `AGENTS.md` or this handoff instead of the public course guides.

## Git and session continuity

This folder is a Git repository on `main`, tracking `origin/main` at `https://github.com/codewithprof-academy/fullstack-journey.git`. The initial course-materials commit was pushed. Keep course materials, supplied assets, and agent handoff files tracked; `.gitignore` excludes generated graph data, local caches, and temporary files. Check `git status` before future changes.

To resume the requested Codex session from a terminal in this repository, run:

```sh
codex resume 01a12c10-fb2e-79e0-86aa-d75da51239c6
```

The command opens an interactive Codex session. This handoff remains the durable reference for repository decisions and current state.
