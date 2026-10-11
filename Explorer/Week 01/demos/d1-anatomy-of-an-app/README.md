---
week: 1
title: "D1 — Anatomy of an app"
owner: Salvaton Lloyd Stanley-Kemuel
cohorts: [EXP, BLD, CL]
status: ready-for-review
version: 1
---

<img src="../../../../assets/cwp-logo-primary-transparent-320w.png" alt="CodeWithProf logo" width="100">

# D1 — Anatomy of an app (W01-ALL-LO1, W01-ALL-LO2)

No code. Use a whiteboard (or the Mermaid diagram below on screen). The app: **"StudyHub" — an invented school learning platform** (students see courses, submit homework, get AI revision help). It is the same kind of system the capstone builds in Week 16, so name it and come back to it.

```mermaid
flowchart TB
  U[Student on phone/laptop] --> FE[What you see<br/>Frontend: pages, buttons]
  FE --> BE[Behind the scenes<br/>Backend: rules, logins, homework]
  BE --> DB[(Database<br/>courses, grades)]
  BE --> AI[AI helper<br/>revision questions]
  BE -.runs on.-> CL[Cloud servers]
  SEC[Security: keeps accounts safe] -.protects.-> BE
  DES[Product design: decides what to build] -.shapes.-> FE
  OPS[DevOps: ships updates safely] -.deploys.-> CL
  DATA[Data: which lessons help most?] -.analyses.-> DB
```

## Script
1. **Ask:** "What can you DO in a learning app?" Write answers as features (log in, see homework, upload work…).
2. **Ask for each feature:** "What has to happen behind the scenes?" Draw boxes as answers come.
3. **Reveal roles:** label each box with the role that builds or looks after it (frontend, backend, data, AI, cloud, DevOps, security, product design).
4. **Land the point:** "Writing code is one part. Engineers also decide what to build, design it, test it, keep it safe, ship it and fix it. That's software *engineering*."
5. **CL extension (2 min):** add "QA/testing", "SRE/on-call", and "Product Manager" and ask who talks to whom when a bug is reported.
