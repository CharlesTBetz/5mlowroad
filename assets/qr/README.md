# Print QR codes

Static QR codes for print. The brochure codes encode the site's own `/go/`
redirect stubs, so **the site is the dynamic layer** — change where a printed
code points by editing the stub (`go/listen.html` / `go/subscribe.html`), with
no reprint and no third-party QR service.

| File | Encodes | Redirects to | ECC | Modules |
|------|---------|--------------|-----|---------|
| `listen.svg` / `listen.png` | `https://5minlowroad.com/go/listen/` | `/listen/` | Q | 33 |
| `subscribe.svg` / `subscribe.png` | `https://5minlowroad.com/go/subscribe/` | `/subscribe/` | Q | 33 |
| `home.svg` / `home.png` | `https://5minlowroad.com/` | — (front door, no stub) | M | 25 |

`home` is the business-card code. It points straight at the site rather than
through a `/go/` stub, because the front door never needs repointing.

**Error correction is set per code and boosting is disabled**, so symbol sizes
are deterministic — print assets are sized around the module count. `home` uses
level M specifically to stay at 25 modules instead of 29: on the business card
it sits at roughly 0.57 in, which keeps modules near 0.58 mm. Raising it to Q or
H pushes them under the ~0.5 mm floor where laser toner spread starts closing
the gaps and scanning gets unreliable. The brochure codes have room, so they
stay at Q (~25%).

Use the **SVG** for print (vector, scales to any size). PNG is a convenience.
Black on white, and leave a quiet zone of at least 4 modules — the file has one
baked in, but if you trim it, the surrounding page must supply it.

## Regenerate

Our preferred generator is **[segno](https://segno.readthedocs.io/)** (open source,
offline, no tracking). Run:

```bash
python3 -m venv /tmp/qrvenv && /tmp/qrvenv/bin/pip install segno
/tmp/qrvenv/bin/python assets/qr/generate-qr.py
```

Edit the URLs in `generate-qr.py` to add or change codes.
