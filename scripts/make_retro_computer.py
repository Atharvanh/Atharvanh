
from pathlib import Path
from xml.sax.saxutils import escape

# Retro computer ASCII artwork
ART = [
    "          .----------------------------.",
    "          |  _                         |",
    "          |  > HELLO, WORLD!           |",
    "          |  > building cool stuff...  |",
    "          |                            |",
    "          '----------------------------'",
    "              |                |",
    "          ____|________________|____",
    "         /__________________________\\",
    "",
    "      ________________________________",
    "     / _ _ _ _ _ _ _ _ _ _ _ _ _ _ /|",
    "    /______________________________/ |",
    "    |______________________________|/",
]

WIDTH = 470
HEIGHT = 345

BG = "#0d1117"
TEXT = "#c9d1d9"
GREEN = "#39d353"

svg = [f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="{WIDTH}" height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}">

<rect width="100%" height="100%" rx="12" fill="{BG}"/>

<text x="26" y="35"
    fill="{GREEN}"
    font-family="monospace"
    font-size="13">developer@github:~$ boot</text>

<line x1="25" y1="49" x2="445" y2="49"
    stroke="#30363d"/>

''']

for i, line in enumerate(ART):
    y = 78 + i * 17
    delay = round(i * 0.17, 2)
    color = GREEN if i in (2, 3) else TEXT

    svg.append(f'''
<defs>
  <clipPath id="row{i}">
    <rect x="28" y="{y - 15}" width="0" height="18">
      <animate
        attributeName="width"
        from="0" to="430"
        begin="{delay}s"
        dur="0.8s"
        fill="freeze"/>
    </rect>
  </clipPath>
</defs>

<text x="28" y="{y}"
    fill="{color}"
    font-family="Consolas, 'Courier New', monospace"
    font-size="13"
    xml:space="preserve"
    clip-path="url(#row{i})">{escape(line)}</text>
''')

svg.append(f'''
<text x="28" y="330"
    fill="{GREEN}"
    font-family="monospace"
    font-size="12">
  system ready
  <animate attributeName="opacity"
    values="0;0;1"
    keyTimes="0;0.8;1"
    dur="3.8s"
    fill="freeze"/>
</text>

</svg>''')

output = Path(__file__).resolve().parent.parent / "retro-computer.svg"
output.write_text("\n".join(svg), encoding="utf-8")

print(f"Created: {output}")
