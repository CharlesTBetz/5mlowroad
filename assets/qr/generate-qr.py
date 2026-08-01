#!/usr/bin/env python3
"""Generate the brochure QR codes for 5mlowroad.com.

These are STATIC QR codes that encode the site's own /go/ redirect stubs. The
site is the "dynamic" layer: to change where a printed code points, edit the
stub (go/listen.html, go/subscribe.html) — no reprint, no third-party service.

Setup + run (disposable venv, doesn't touch system Python):
    python3 -m venv /tmp/qrvenv && /tmp/qrvenv/bin/pip install segno
    /tmp/qrvenv/bin/python assets/qr/generate-qr.py
"""
import os
import segno

OUT = os.path.dirname(os.path.abspath(__file__))
CODES = {
    "listen":    "https://5mlowroad.com/go/listen/",
    "subscribe": "https://5mlowroad.com/go/subscribe/",
}

for name, url in CODES.items():
    qr = segno.make(url, error="q")          # error-correction level Q (~25%), good for print
    qr.save(os.path.join(OUT, f"{name}.svg"), scale=16, border=4)   # vector — primary print asset
    qr.save(os.path.join(OUT, f"{name}.png"), scale=32, border=4)   # high-res raster convenience
    print(f"{name:9s} -> {url}   (QR {qr.designator})")
