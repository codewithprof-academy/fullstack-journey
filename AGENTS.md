# Agent guide

Read [NEXT_SESSION.md](NEXT_SESSION.md) before changing course materials. It records the current state and known gaps; check the files themselves because the handoff may become outdated. The user's latest instructions take precedence over this guide.

## Cohort facts

- Official name: **CodeWithProf - NextGen Web, Cloud & AI Engineering Bootcamp - (Explorers) Cohort 1**.
- Track: **Explorers**, ages **9–14**; **16 weeks** total.
- Use `Salvaton Lloyd Stanley-Kemuel` for the `owner` value in course Markdown frontmatter.
- Reuse the supplied logos in [`assets/`](assets/) for course materials. Keep image paths relative to each file.

## Repository structure

- [`README.md`](README.md) is the cohort entry point and week index.
- [`Explorer/README.md`](Explorer/README.md) is the Explorer track entry point.
- Each week belongs in `Explorer/Week NN/`, with a `README.md` linking to every available file for that week. Link new weeks from both higher-level indexes when the files exist.
- Keep demo instructions beside each demo and include a practical way for a participant to perform it.
- Use relative links. Do not add links to missing files or assume future weeks' content exists.

## Week 01 constraints

- Participants must be able to complete Week 01 without Python. Do not use the Python demo scripts for Week 01 testing. They are retained as later previews.
- D3 uses [`dns-explorer.html`](Explorer/Week%2001/demos/d3-dns-lookup/dns-explorer.html) for a live DNS lookup that displays IP addresses; [`nslookup` instructions](Explorer/Week%2001/demos/d3-dns-lookup/README.md) are an alternative. The browser activity needs internet access.
- Review the Week 01 PDF and PPTX alongside Markdown when changing lesson content, branding, or ages, so they remain consistent.

## Before handing off changes

- Check all course Markdown frontmatter owner values, local links, and image paths.
- Check that any added week is reachable from the root and Explorer indexes.
- Record meaningful changes, verification, and remaining gaps in [`NEXT_SESSION.md`](NEXT_SESSION.md).
