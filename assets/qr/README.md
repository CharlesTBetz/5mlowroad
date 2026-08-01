# Brochure QR codes

Static QR codes for the printed IANDS brochure. Each encodes one of the site's
own `/go/` redirect stubs, so **the site is the dynamic layer** — change where a
printed code points by editing the stub (`go/listen.html` / `go/subscribe.html`),
with no reprint and no third-party QR service.

| File | Encodes | Redirects to |
|------|---------|--------------|
| `listen.svg` / `listen.png` | `https://5mlowroad.com/go/listen/` | `/listen/` |
| `subscribe.svg` / `subscribe.png` | `https://5mlowroad.com/go/subscribe/` | `/subscribe/` |

Use the **SVG** for print (vector, scales to any size). PNG is a convenience.
Black-on-white, error-correction level **Q** (survives ink spread / smudges).

## Regenerate

Our preferred generator is **[segno](https://segno.readthedocs.io/)** (open source,
offline, no tracking). Run:

```bash
python3 -m venv /tmp/qrvenv && /tmp/qrvenv/bin/pip install segno
/tmp/qrvenv/bin/python assets/qr/generate-qr.py
```

Edit the URLs in `generate-qr.py` to add or change codes.
