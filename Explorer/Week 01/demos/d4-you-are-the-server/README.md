---
week: 1
title: "D4 — You are the server"
owner: Salvaton Lloyd Stanley-Kemuel
cohorts: [EXP, BLD, CL]
status: ready-for-review
version: 1
---

<img src="../../../../assets/cwp-logo-primary-transparent-320w.png" alt="CodeWithProf logo" width="100">

# D4 — You are the server (W01-ALL-LO3, W01-ALL-LO5, W01-BLD-LO7)

Open the [request/response simulator](server-simulation.html) in a browser. It runs locally without a server or an installation. Ask students to click each route and read the request, response, and status shown on screen.

Project the simulator and ask students to predict the response before each click. A real server would also log exchange details such as these:

```
-> REQUEST: GET /about
     Host: studyhub.example
  <- RESPONSE: 200 OK (text/html)
```

| Click | Status | Teaching point |
|---|---|---|
| `/` | 200 | The page is not "in" the browser — the server sent it |
| `/about` | 200 | A new click = a new request |
| `/api/time` | 200 JSON | An **API** answers programs with data, not pages |
| `/does-not-exist` | 404 | Status codes are the server's way of saying how it went |

**Later coding preview:** [`tiny_server.py`](tiny_server.py) is an example of a real local HTTP server for a later week. Use the browser simulator for Week 01. It models the exchange without making HTTP requests.

**Cloud link (LO5):** "A real server can run on a laptop or a rented computer in a data centre. The location changes, but the request and response idea stays the same."
