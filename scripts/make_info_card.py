

from pathlib import Path
from xml.sax.saxutils import escape
import os

# ---------- CUSTOMIZE YOUR PROFILE ----------

PROFILE = [
    ("Name", "Atharva"),
    ("User", "Atharvanh"),
    ("Role", "Creative Web Developer"),
    ("Focus", "UI / Animation / AI"),
    ("Stack", "Next.js / React / Python"),
    ("Tools", "GSAP / Tailwind / Git"),
    ("Now", "Building interactive websites"),
    ("Mode", "Always experimenting"),
]

# ---------- DESIGN SETTINGS ----------

WIDTH = 470
HEIGHT = 345

BG = "#0d1117"
GREEN = "#39d353"
WHITE = "#c9d1d9"
BORDER = "#30363d"

FONT = "Consolas, Courier New, monospace"

STATIC = os.getenv("STATIC") == "1"


def animation(delay):
    if STATIC:
        return ""

    return f'''
    <animate
        attributeName="opacity"
        from="0"
        to="1"
        begin="{delay:.2f}s"
        dur="0.3s"
        fill="freeze"/>
    '''


svg = [f'''
<svg xmlns="http://www.w3.org/2000/svg"
     width="{WIDTH}"
     height="{HEIGHT}"
     viewBox="0 0 {WIDTH} {HEIGHT}">

<rect width="100%" height="100%"
      rx="12" fill="{BG}"/>

<text x="26" y="35"
      fill="{GREEN}"
      font-family="{FONT}"
      font-size="13">
  developer@github:~$ whoami
</text>

<line x1="25" y1="49" x2="445" y2="49"
      stroke="{BORDER}"/>

<text x="28" y="77"
      fill="{WHITE}"
      font-family="{FONT}"
      font-weight="bold"
      font-size="15">
  SYSTEM PROFILE
</text>

<text x="355" y="77"
      fill="{GREEN}"
      font-family="{FONT}"
      font-size="11">
  ACTIVE
</text>

<line x1="28" y1="88" x2="442" y2="88"
      stroke="{BORDER}"/>
''']

# ---------- ANIMATED PROFILE ROWS ----------

for i, (key, value) in enumerate(PROFILE):

    y = 118 + (i * 25)
    delay = 0.4 + (i * 0.22)

    opacity = "1" if STATIC else "0"

    svg.append(f'''
<g opacity="{opacity}">
    {animation(delay)}

    <text x="28" y="{y}"
          fill="{GREEN}"
          font-family="{FONT}"
          font-size="13">
        {escape(key)}
    </text>

    <text x="145" y="{y}"
          fill="{WHITE}"
          font-family="{FONT}"
          font-size="13">
        {escape(value)}
    </text>
</g>
''')

# ---------- FOOTER ----------

footer_opacity = "1" if STATIC else "0"

svg.append(f'''
<line x1="28" y1="312" x2="442" y2="312"
      stroke="{BORDER}"/>

<text x="28" y="331"
      fill="{GREEN}"
      font-family="{FONT}"
      font-size="12"
      opacity="{footer_opacity}">
  Profile initialized successfully
  {animation(2.5)}
</text>

</svg>
''')

# ---------- SAVE SVG ----------

output = (
    Path(__file__).resolve().parent.parent
    / "info-card.svg"
)

output.write_text(
    "\n".join(svg),
    encoding="utf-8"
)

print(f"Created: {output}")
