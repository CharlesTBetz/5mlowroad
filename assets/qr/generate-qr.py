#!/usr/bin/env python3
"""Generate the print QR codes for 5minlowroad.com.

The brochure codes encode the site's own /go/ redirect stubs. The site is the
"dynamic" layer: to change where a printed code points, edit the stub
(go/listen.html, go/subscribe.html) — no reprint, no third-party service.

Error correction is set per code, not globally, and error boosting is disabled
so the symbol size is deterministic. Re-running this must not silently change a
code's module count — print assets are sized around it.

Setup + run (disposable venv, doesn't touch system Python):
    python3 -m venv /tmp/qrvenv && /tmp/qrvenv/bin/pip install segno
    /tmp/qrvenv/bin/python assets/qr/generate-qr.py
"""
import os
import segno

OUT = os.path.dirname(os.path.abspath(__file__))

# name -> (url, error correction level)
CODES = {
    # Brochure codes. Level Q (~25%) survives ink spread and smudging.
    "listen":    ("https://5minlowroad.com/go/listen/", "q"),
    "subscribe": ("https://5minlowroad.com/go/subscribe/", "q"),

    # Business-card code. Skips /go/ on purpose — the front door never needs
    # repointing. Level M (~15%) keeps this at 25 modules instead of 29, which
    # is what lets it sit at ~0.57 in on the card with modules still near
    # 0.58 mm. Do not "upgrade" this to Q or H: at card size that pushes the
    # modules under the ~0.5 mm floor where laser toner spread starts closing
    # the gaps and scanning gets unreliable.
    "home":      ("https://5minlowroad.com/", "m"),
}

for name, (url, ecc) in CODES.items():
    qr = segno.make(url, error=ecc, boost_error=False)
    qr.save(os.path.join(OUT, f"{name}.svg"), scale=16, border=4)   # vector — primary print asset
    qr.save(os.path.join(OUT, f"{name}.png"), scale=40, border=4)   # high-res raster convenience
    modules = qr.symbol_size(border=0)[0]
    print(f"{name:9s} -> {url}   (QR {qr.designator}, {modules} modules)")
