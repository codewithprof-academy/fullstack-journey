"""Week 01 · Demo D3 — DNS lookup: turn domain names into IP addresses.

Run:  python3 dns_lookup.py example.com wikipedia.org
"""
import socket
import sys
import time


def lookup(name: str) -> None:
    start = time.perf_counter()
    try:
        results = socket.getaddrinfo(name, 443, proto=socket.IPPROTO_TCP)
    except socket.gaierror as err:
        print(f"{name:<22} could not be found ({err})")
        return
    ms = (time.perf_counter() - start) * 1000
    ipv4 = sorted({r[4][0] for r in results if r[0] == socket.AF_INET})
    ipv6 = sorted({r[4][0] for r in results if r[0] == socket.AF_INET6})
    print(f"{name:<22} answered in {ms:6.1f} ms")
    print(f"{'':<22} IPv4: {', '.join(ipv4) or '-'}")
    print(f"{'':<22} IPv6: {', '.join(ipv6) or '-'}")


if __name__ == "__main__":
    for domain in sys.argv[1:] or ["example.com", "localhost"]:
        lookup(domain)
