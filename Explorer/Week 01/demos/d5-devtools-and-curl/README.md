---
week: 1
title: "D5 — DevTools Network tab and curl"
owner: Salvaton Lloyd Stanley-Kemuel
cohorts: [BLD, CL]
status: ready-for-review
version: 1
---

<img src="../../../../assets/cwp-logo-primary-transparent-320w.png" alt="CodeWithProf logo" width="100">

# D5 — Watching real requests (W01-BLD-LO7, W01-CL-LO8)

First use the [D4 simulator](../d4-you-are-the-server/server-simulation.html) to predict what a request and response look like. Then inspect a real, permitted public site. This activity does not need Python.

## Part 1 — Browser DevTools (BLD, CL; EXP watch only)
1. Open `https://example.com/` in Chrome, Edge, or Firefox. Press **F12** (Mac: **Cmd+Option+I**) and open the **Network** tab, then reload.
2. Select the document request. Find its **Request URL**, **Request Method**, **Status Code**, and **Response Headers**. Open **Response** to see the HTML. Header names and values vary by browser and server.
3. Compare the real request with the [D4 simulator](../d4-you-are-the-server/server-simulation.html). Identify which parts the simulator leaves out.
4. If the instructor chooses another permitted public site, reload it and watch the extra requests for images, scripts, and styles.

## Part 2 — curl (CL; BLD watch)
```bash
curl -i https://example.com/                   # status line, headers and body
curl -I https://example.com/                   # HEAD request, headers only
curl -v https://example.com/ -o /dev/null      # connection details and response
```
In the `-v` output, point out the connection, TLS lines, request and response. Exact output and status codes depend on the network and the public site.

## Status codes cheat-sheet
| Code | Meaning | Everyday example |
|---|---|---|
| 200 | OK | Page loaded |
| 301/302 | Moved — go here instead | `http://` sending you to `https://` |
| 404 | Not found | Mistyped link |
| 401/403 | Not logged in / not allowed | Visiting a teacher-only page as a student |
| 500 | The server broke | A bug on the server |
| 503 | Server unavailable | Too busy or down for maintenance |
