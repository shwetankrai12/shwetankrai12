#!/usr/bin/env python3
"""Generate the animated SVG assets for the profile README.

Edit the CONFIG block, then run:
    pip install pyfiglet
    python tools/build_assets.py
Outputs: assets/banner.svg, assets/ticker.svg, assets/divider.svg
"""
import math
import os
import random
from xml.sax.saxutils import escape

import pyfiglet

# ======================= CONFIG: EDIT ME =======================
NAME = "SHWETANK"
FONT = "ansi_shadow"  # try: ansi_shadow, slant, big, doom, block, standard
TAGLINE = "C++  |  QUANT SYSTEMS  |  MACHINE LEARNING"
STATUS = "building QuantKernel: research + backtesting infrastructure"
WATCHLIST = [
    "C++", "PYTHON", "QUANT SYSTEMS", "ORDER BOOKS", "CONCURRENCY",
    "BACKTESTING", "MACHINE LEARNING", "FASTAPI", "POSTGRESQL",
]
CYAN, VIOLET, GREEN, AMBER, BG = "#00f0ff", "#7c5cff", "#22c55e", "#ffb000", "#0a0e14"
# ===============================================================

MONO = "SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
HEAD = '<?xml version="1.0" encoding="UTF-8"?>\n'


def banner():
    art = pyfiglet.figlet_format(NAME, font=FONT, width=300).split("\n")
    while art and not art[-1].strip():
        art.pop()
    while art and not art[0].strip():
        art.pop(0)

    fs, cw, lh = 15, 9.0, 17
    maxlen = max(len(l) for l in art)
    art_w = maxlen * cw
    W = int(max(1000, art_w + 120))
    top = 84
    art_end = top + len(art) * lh
    tag_y = art_end + 34
    st_y = tag_y + 30
    H = st_y + 36
    ax = (W - art_w) / 2

    # art lines (staggered fade-in; base opacity 1 so static renderers show it)
    T = len(art) * 0.12 + 0.5
    lines = []
    for i, l in enumerate(art):
        d = i * 0.12
        xs = " ".join(f"{ax + j * cw:.1f}" for j in range(len(l)))  # fixed x per glyph = font-independent
        lines.append(
            f'<text x="{xs}" y="{top + i * lh}" font-size="{fs}" '
            f'xml:space="preserve" fill="url(#g)">{escape(l)}'
            f'<animate attributeName="opacity" values="0;0;1" keyTimes="0;{d / T:.3f};{(d + 0.5) / T:.3f}" '
            f'dur="{T:.2f}s" fill="freeze"/></text>'
        )

    # typing status line
    sfs, scw = 14, 7.9
    stext = "> " + STATUS
    tw = len(stext) * scw
    sx = (W - tw) / 2
    tb, td = 1.0, 2.6
    T2 = tb + td
    kt = f"0;{tb / T2:.3f};1"

    return f'''{HEAD}<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{MONO}">
<defs>
  <linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="{top - fs}" x2="0" y2="{art_end}">
    <stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{VIOLET}"/>
  </linearGradient>
  <linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0.07"/>
  </linearGradient>
  <filter id="glow" x="-10%" y="-30%" width="120%" height="160%">
    <feGaussianBlur stdDeviation="3" result="b"><animate attributeName="stdDeviation" values="2;4.5;2" dur="4s" repeatCount="indefinite"/></feGaussianBlur>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="{CYAN}" stroke-opacity="0.05"/></pattern>
  <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#000" fill-opacity="0.28"/></pattern>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="14"/></clipPath>
  <clipPath id="type"><rect x="{sx:.1f}" y="{st_y - 17}" width="{tw:.1f}" height="24">
    <animate attributeName="width" values="0;0;{tw:.1f}" keyTimes="{kt}" dur="{T2}s" fill="freeze"/></rect></clipPath>
</defs>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>
  <rect width="{W}" height="36" fill="#0d131c"/>
  <circle cx="24" cy="18" r="5" fill="#ff5f56"/><circle cx="44" cy="18" r="5" fill="#ffbd2e"/><circle cx="64" cy="18" r="5" fill="#27c93f"/>
  <text x="{W / 2}" y="22" font-size="12" fill="#6e7681" text-anchor="middle">~/profile : zsh</text>
  <text x="{W - 24}" y="22" font-size="12" fill="{GREEN}" text-anchor="end">● ONLINE<animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/></text>

  <g filter="url(#glow)">{''.join(lines)}</g>

  <text x="{W / 2}" y="{tag_y}" font-size="15" font-weight="bold" letter-spacing="3" fill="#e6edf3" text-anchor="middle" xml:space="preserve">{escape(TAGLINE)}</text>

  <g clip-path="url(#type)"><text x="{sx:.1f}" y="{st_y}" font-size="{sfs}" fill="{AMBER}">&gt;</text><text x="{" ".join(f"{sx + (j + 2) * scw:.1f}" for j in range(len(STATUS)))}" y="{st_y}" font-size="{sfs}" xml:space="preserve" fill="#9aa7b4">{escape(STATUS)}</text></g>
  <rect x="{sx + tw + 2:.1f}" y="{st_y - 13}" width="8" height="16" fill="{CYAN}">
    <animate attributeName="x" values="{sx:.1f};{sx:.1f};{sx + tw + 2:.1f}" keyTimes="{kt}" dur="{T2}s" fill="freeze"/>
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </rect>

  <rect y="-40" width="{W}" height="40" fill="url(#bar)">
    <animateTransform attributeName="transform" type="translate" values="0 0;0 {H + 80}" dur="5s" repeatCount="indefinite"/>
  </rect>
  <rect width="{W}" height="{H}" fill="url(#scan)"/>
</g>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="none" stroke="#1f2a37"/>
<g fill="none" stroke="{CYAN}" stroke-width="2" stroke-opacity="0.85" stroke-linecap="round">
  <path d="M10 30V12a2 2 0 0 1 2-2h18"/><path d="M{W - 30} 10h18a2 2 0 0 1 2 2v18"/>
  <path d="M10 {H - 30}v18a2 2 0 0 0 2 2h18"/><path d="M{W - 30} {H - 10}h18a2 2 0 0 0 2-2v-18"/>
</g>
</svg>
'''


def ticker():
    W, H = 1000, 40
    fs, cw, label_w = 13, 7.8, 124

    def seq(items):
        plain = "".join(f"{t} ▲     " for t in items)
        spans = "".join(
            f'<tspan fill="#e6edf3">{escape(t)}</tspan><tspan fill="{GREEN}"> ▲</tspan><tspan>     </tspan>'
            for t in items
        )
        return plain, spans

    items = list(WATCHLIST)
    plain, spans = seq(items)
    while len(plain) * cw < W:
        items += WATCHLIST
        plain, spans = seq(items)
    sw = len(plain) * cw
    dur = sw / 55
    txt = lambda x: (
        f'<text x="{" ".join(f"{x + j * cw:.1f}" for j in range(len(plain)))}" y="25" font-size="{fs}" '
        f'xml:space="preserve" fill="#3b4654">{spans}</text>'
    )
    return f'''{HEAD}<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{MONO}">
<defs><clipPath id="c"><rect x="{label_w}" width="{W - label_w}" height="{H}"/></clipPath></defs>
<rect width="{W}" height="{H}" rx="8" fill="#0d131c"/>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="8" fill="none" stroke="#1f2a37"/>
<g clip-path="url(#c)"><g>
  {txt(label_w + 14)}{txt(label_w + 14 + sw)}
  <animateTransform attributeName="transform" type="translate" values="0 0;-{sw:.1f} 0" dur="{dur:.1f}s" repeatCount="indefinite"/>
</g></g>
<rect width="{label_w}" height="{H}" rx="8" fill="#1a1405"/>
<rect x="{label_w - 8}" width="8" height="{H}" fill="#1a1405"/>
<text x="14" y="25" font-size="12" font-weight="bold" letter-spacing="2" fill="{AMBER}">◆ WATCHLIST</text>
</svg>
'''


def divider():
    W, H, n = 1000, 44, 64
    random.seed(7)
    walk, w = [], 0.0
    for _ in range(n + 1):
        w += random.gauss(0.35, 1.0)
        walk.append(w)
    lo, hi = min(walk), max(walk)
    pts = [(20 + i * (W - 40) / n, 37 - (v - lo) / (hi - lo) * 28) for i, v in enumerate(walk)]
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    L = sum(math.dist(pts[i], pts[i + 1]) for i in range(n)) + 1
    ex, ey = pts[-1]
    return f'''{HEAD}<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs><filter id="glow" x="-5%" y="-50%" width="110%" height="200%"><feGaussianBlur stdDeviation="2.5"/></filter></defs>
<line x1="20" y1="22" x2="{W - 20}" y2="22" stroke="#1f2a37" stroke-dasharray="3 6"/>
<path d="{d}" fill="none" stroke="{CYAN}" stroke-width="3" stroke-opacity="0.5" filter="url(#glow)" stroke-dasharray="{L:.0f}">
  <animate attributeName="stroke-dashoffset" values="{L:.0f};0;0" keyTimes="0;0.55;1" dur="7s" repeatCount="indefinite"/></path>
<path d="{d}" fill="none" stroke="{CYAN}" stroke-width="1.6" stroke-linejoin="round" stroke-dasharray="{L:.0f}">
  <animate attributeName="stroke-dashoffset" values="{L:.0f};0;0" keyTimes="0;0.55;1" dur="7s" repeatCount="indefinite"/></path>
<circle cx="{ex:.1f}" cy="{ey:.1f}" r="4" fill="{GREEN}"><animate attributeName="r" values="3;6;3" dur="1.6s" repeatCount="indefinite"/></circle>
</svg>
'''


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in (("banner", banner), ("ticker", ticker), ("divider", divider)):
        with open(os.path.join(OUT, f"{name}.svg"), "w", encoding="utf-8") as f:
            f.write(fn())
        print("wrote", f"assets/{name}.svg")
