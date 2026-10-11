---
week: 1
title: "D3 — DNS lookup"
owner: Salvaton Lloyd Stanley-Kemuel
cohorts: [EXP, BLD, CL]
status: ready
version: 2
---

<img src="../../../../assets/cwp-logo-primary-transparent-320w.png" alt="CodeWithProf logo" width="100">

# D3 — See a real IP address (W01-ALL-LO4)

DNS turns a website name into an IP address that computers can use. This activity needs a browser and an internet connection, but **no Python**.

## Browser activity

1. Open the [live DNS explorer](dns-explorer.html) by double-clicking the file.
2. Leave `example.com` in the box and click **Find IP address**.
3. Read the IPv4 address shown. If an IPv6 address appears, compare its shape with IPv4.
4. Try `www.wikipedia.org`. Are there one or several addresses? Results can vary by time and network.
5. Try a made-up name such as `this-name-should-not-exist.example`. Explain why DNS cannot find a real address for it.

The explorer asks [Google Public DNS](https://developers.google.com/speed/public-dns/docs/doh/json) for a live answer. It does not open the website you enter. If the request is blocked, use the **Open the raw DNS answer on dns.google** link shown in the page and find an A record's `data` value, or use the terminal activity below. The `.example` names and IP addresses in the [worksheet](../../lab/dns-phone-book-worksheet.md) are fictional classroom examples and will not return those numbers in a live lookup.

## Terminal option

```text
nslookup example.com
```

Look for `Address:` lines in the answer. The first address may belong to the DNS server that answered the query; the later address or addresses belong to `example.com`. On macOS or Linux, `dig example.com +short` gives a shorter answer if `dig` is installed.

## Later coding preview

The optional [Python DNS lookup script](dns_lookup.py) is a preview for a later coding week. Use the browser activity or terminal option above for Week 01.
