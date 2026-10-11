---
week: 1
title: "Week 01 assignment guide — Explorers"
owner: Salvaton Lloyd Stanley-Kemuel
cohorts: [EXP]
status: ready-for-review
version: 1
---

# CodeWithProf - NextGen Web, Cloud & AI Engineering Bootcamp - (Explorers) Cohort 1
## Week 01 Assignment Guide · Explorers (Ages 9–14)
### In-Class Lab: DNS Phone Book & URL Detective

---

## W01-EXP-A1 · DNS Phone Book & URL Detective

**Assesses:** W01-ALL-LO3, W01-ALL-LO4  
**Time:** 40 minutes (Session B)  
**Work mode:** Pairs (work with a lab buddy)  
**Starter worksheet:** [DNS phone book and URL detective](lab/dns-phone-book-worksheet.md)  
**Tool used:** [URL Explorer](demos/d2-url-explorer/index.html) (open the file in a browser)

---

### Goal

Become an internet detective! In this two-part mission, you will:
1. Crack the mystery of how computers find each other using the **DNS phone book**.
2. Dissect four fictional web addresses using our interactive **URL Explorer** tool.
3. Draw the complete journey of a web message from your browser to a data centre and back.

---

### What You Start With

- A printed or digital copy of the **DNS Phone Book & URL Detective Worksheet**.
- The interactive **URL Explorer** web app opened in your browser (your instructor will show you the link or open it together).
- Coloured pens or highlighters (green, orange, purple, blue, yellow, and pink).

---

### Steps & Requirements

#### Part A: The DNS Phone Book (15 minutes)

Computers find each other with numbers called **IP addresses**. People find websites with friendly names called **domain names**. **DNS** is the phone book that turns a name into a number.

Look at this lesson lookup table (all numbers and names are pretend):

| Domain Name | IP Address |
|---|---|
| `studyhub.example` | `203.0.113.10` |
| `funmaths.example` | `203.0.113.25` |
| `codeclub.example` | `198.51.100.7` |
| `weatherkids.example` | `198.51.100.42` |

Complete these detective questions on your worksheet:
1. Your friend types `codeclub.example` into their browser. Which IP address does the computer actually visit?
2. Which website lives at `203.0.113.25`?
3. A student accidentally types `codeclubb.example` with two "b"s. What do you think happens? Does the computer reach the right club? Why or why not?
4. Explain in one sentence: Why do humans use domain names instead of just typing IP addresses?

#### Part B: URL Detective (20 minutes)

Open the **URL Explorer** tool. Paste each of the four addresses below into the box and record the pieces shown in your worksheet table:

1. `https://www.studyhub.example/homework`
2. `https://funmaths.example/games/times-tables?level=3`
3. `http://codeclub.example/`
4. `https://weatherkids.example/forecast?city=london#today`

| URL | Protocol | Domain Name | Path | Anything after `?` (Query) |
|---|---|---|---|---|
| `https://www.studyhub.example/homework` | | | | |
| `https://funmaths.example/games/times-tables?level=3` | | | | |
| `http://codeclub.example/` | | | | |
| `https://weatherkids.example/forecast?city=london#today` | | | | |

Detective questions:
5. Which of the four addresses does **not** have the `https` padlock?
6. Why does the missing padlock matter if you were typing in a password or private note?
7. In the weather address, what does `#today` do? Does that part travel across the internet to the server?

#### Part C: Draw the Journey! (5 minutes)

In the drawing box on your worksheet, sketch the four main stops in order:
`Browser (Client) → Internet → Server → Database`

Add two speech bubbles:
- A bubble pointing to the server: **Request** (*"Please send me the times-tables game!"*)
- A bubble pointing back to the browser: **Response** (*"200 OK — here is your game!"*)

---

### Try This Twist ⭐

Change `level=3` to `level=10` in the funmaths address inside the URL Explorer.
- What changed in the breakdown?
- Who reads that number — your browser or the server computer in the data centre?

---

### Done When (Checklist)

- [ ] All four DNS lookup questions in Part A are answered correctly.
- [ ] The URL Detective table in Part B is completely filled in.
- [ ] Questions 5, 6, and 7 about security and URL fragments are answered.
- [ ] The Part C journey diagram has all 4 stops and both speech bubbles (Request & Response).
- [ ] You can explain to your teacher in plain words what DNS does.

---

### How to Submit

- Hold up your completed worksheet to your instructor during the Session B lab check-in.
- If using a digital worksheet, save your file and submit it to your classroom folder.
- Pair buddies: Both of you must write out your own worksheet!

---

### AI Use Declaration

Fill in this box at the bottom of your worksheet:

```text
I used AI for: ___________________________________________________________
(e.g., "None" or "Brainstorming an analogy for DNS")
I understand and can explain every answer on this sheet in my own words.
```

---

### Rubric Reference

Your instructor will check the [completion checklist above](#done-when-checklist). Complete Parts A and B and explain DNS in your own words to demonstrate the Week 01 learning goals.
