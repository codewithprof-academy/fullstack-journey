---
week: 1
title: "W01-EXP-L2 DNS phone book and URL detective — worksheet"
owner: Salvaton Lloyd Stanley-Kemuel
cohorts: [EXP]
status: ready-for-review
version: 1
---

# DNS Phone Book & URL Detective 🔎  (W01-EXP-L2)

**Assesses:** W01-ALL-LO3, W01-ALL-LO4 · **Time:** 40 minutes · **Work:** pairs

## Part A — The DNS phone book (15 min)

Computers find each other with numbers called **IP addresses**. People prefer names. **DNS** is the phone book that turns a name into a number.

| Name (domain) | IP address |
|---|---|
| studyhub.example | 203.0.113.10 |
| funmaths.example | 203.0.113.25 |
| codeclub.example | 198.51.100.7 |
| weatherkids.example | 198.51.100.42 |

*(These are pretend names and numbers, made just for this lesson.)*

1. Your friend types `codeclub.example`. Which IP address does the computer really go to? ____________
2. Which website lives at `203.0.113.25`? ____________
3. Someone types `codeclubb.example` (two b's). What do you think happens? ____________
4. Why do we use names instead of numbers? ____________

## Part B — URL detective (20 min)

Open the [URL Explorer](../demos/d2-url-explorer/index.html) your teacher shows you. Paste each URL and fill in the table.

| URL | Protocol | Domain name | Path | Anything after `?` |
|---|---|---|---|---|
| `https://www.studyhub.example/homework` | | | | |
| `https://funmaths.example/games/times-tables?level=3` | | | | |
| `http://codeclub.example/` | | | | |
| `https://weatherkids.example/forecast?city=london#today` | | | | |

5. Which URL does **not** have the padlock (`https`)? ____________ Why does that matter? ____________

## Part C — Draw it! (5 min)
Draw the journey: **Browser → Internet → Server → Database**, and add a speech bubble for the **request** and one for the **response**.

### Try This ⭐
Change `level=3` to `level=10` in the URL Explorer. What changed? Who do you think reads that number — the browser or the server?
