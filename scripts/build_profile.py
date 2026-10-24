"""Deterministic, script-free SVG artwork and a short, non-looping boot GIF."""
from pathlib import Path
from html import escape
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)
BG, PANEL, LINE = '#101713', '#17211b', '#34483a'
GREEN, WHITE, MUTED, GOLD = '#b6f58a', '#eef3e7', '#a1b5a4', '#f2c879'
FONT = 'Consolas, DejaVu Sans Mono, monospace'

def text(x, y, value, size=14, color=WHITE, weight='400'):
    return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(str(value))}</text>'

def rect(x, y, w, h, fill=PANEL, radius=0, stroke='none'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'

def save(name, w, h, title, body):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>'
    svg += rect(0.5, .5, w-1, h-1, BG, 16, LINE) + ''.join(body) + '</svg>'
    (ASSETS / name).write_text(svg, encoding='utf-8')

ART = [
    '      .----------------------.',
    '      |                      |',
    '      |   > hello, world_    |',
    '      |   ideas -> reality   |',
    '      |                      |',
    "      '----------------------'",
    '           |          |',
    '       ____|__________|____',
    '      /___________________\\',
    '   __________________________',
    '  / [] [] [] [] [] [] [] [] /|',
    ' /________________________/ |',
    ' |________________________|/',
]

def hero(mobile=False):
    w, h = (480, 640) if mobile else (960, 470)
    p = [text(30, 35, 'A / H', 16, GREEN, '700'), text(110, 35, 'PERSONAL COMPUTING DEPT.', 11, MUTED),
         text(w-102, 35, 'SYS / 01', 11, GOLD), rect(30, 55, w-60, 1, LINE)]
    p += [text(30, 94, 'atharva@github:~$ whoami', 13, GREEN),
          text(26, 174, 'ATHARVA', 66 if mobile else 96, WHITE, '700'),
          text(30, 212 if mobile else 220, 'Curiosity, compiled.', 23, GREEN),
          text(30, 247 if mobile else 260, 'Web experiences. Useful experiments.', 13, MUTED),
          text(30, 270 if mobile else 283, 'A little personality in every build.', 13, MUTED)]
    if mobile:
        ax, ay, fs, step = 65, 322, 15, 18
    else:
        ax, ay, fs, step = 590, 148, 14, 17
        p += [rect(568, 92, 363, 301, PANEL, 12, LINE), text(590, 121, 'LOCAL MACHINE / ASCII EDITION', 11, GOLD)]
    for i, row in enumerate(ART):
        p.append(f'<text x="{ax}" y="{ay+i*step}" xml:space="preserve" font-family="{FONT}" font-size="{fs}" fill="{GREEN if i in (2,3) else MUTED}">{escape(row)}</text>')
    y = h-80
    p += [rect(30, y, w-60, 1, LINE), text(30, y+29, '01 / STUDENT', 12, GOLD),
          text(w-204, y+29, '02 / BUILDER', 12, GREEN), text(30, h-23, 'atharvanh.me', 12, MUTED),
          text(w-204, h-23, 'IDEAS WELCOME  +', 12, MUTED)]
    save('hero-mobile.svg' if mobile else 'hero.svg', w, h, 'Atharva. Curiosity, compiled. Student and builder of web experiences and useful experiments.', p)

def info():
    p = [text(28, 36, '$ neofetch --atharva', 15, GREEN), rect(28, 54, 424, 1, LINE)]
    rows = [('user', 'Atharva / @Atharvanh'), ('role', 'Student & developer'), ('web', 'React / JavaScript'),
            ('mobile', 'React Native / Expo'), ('backend', 'Python / Node.js'), ('style', 'Tailwind CSS / Three.js'), ('mindset', 'Build. Learn. Refine.')]
    for i, (k, v) in enumerate(rows):
        p += [text(28, 91+i*32, k, 13, GOLD), text(131, 91+i*32, v, 13)]
    for i, c in enumerate([GREEN, GOLD, '#82bab0', '#c3addc', WHITE, MUTED]):
        p.append(rect(28+i*27, 322, 24, 13, c, 2))
    save('info-card.svg', 480, 365, 'Profile: Atharva, student and developer. React, JavaScript, React Native, Expo, Python, Node.js, Tailwind CSS and Three.js.', p)

def heatmap(data, mobile=False):
    days = data['days']
    if mobile:
        days = days[-91:]
        # Start on Sunday to keep weekday positions honest.
        import datetime
        while days and (datetime.date.fromisoformat(days[0]['date']).weekday()+1)%7:
            days=days[1:]
    import datetime
    lead = (datetime.date.fromisoformat(days[0]['date']).weekday()+1)%7
    w, h = (480, 350) if mobile else (960, 315)
    step, cell = (31, 23) if mobile else (16, 12)
    p = [text(28, 37, '$ git log --every-day', 15, GREEN), text(28, 66, 'RECENT 13 WEEKS' if mobile else 'A YEAR OF SHOWING UP', 11, GOLD)]
    palette = ['#223027', '#39593b', '#5b854b', '#83b95d', GREEN]
    months=set()
    for i, d in enumerate(days):
        n=i+lead
        x,y = 29+(n//7)*step, (87 if mobile else 104)+(n%7)*step
        date=datetime.date.fromisoformat(d['date'])
        month=date.strftime('%b')
        if not mobile and date.day <= 7 and month not in months:
            p.append(text(x, 94, month, 10, MUTED))
            months.add(month)
        p.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="{palette[min(4,d["level"])]}"><title>{d["date"]}: {d["count"]} contributions</title></rect>')
    if not mobile:
        p += [text(28, 242, str(data['total_contributions']), 31, GREEN, '700'), text(150, 239, 'contributions / recorded year', 13, MUTED),
              text(560, 242, str(data['active_days']), 31, GOLD, '700'), text(642, 239, 'active days', 13, MUTED)]
        p += [text(28, 270, f'{data["range"]["start"]} → {data["range"]["end"]}', 11, MUTED), text(660, 270, 'LESS', 10, MUTED)]
        for i,color in enumerate(palette):
            p.append(rect(704+i*18, 259, 12, 12, color, 2))
        p.append(text(800,270,'MORE',10,MUTED))
    p += [text(28, h-22, f'GitHub public calendar / through {data["range"]["end"]}', 11, MUTED)]
    save('activity-mobile.svg' if mobile else 'activity.svg', w, h, f'Real GitHub activity for {data["username"]}, through {data["range"]["end"]}. {data["total_contributions"]} contributions in recorded year.', p)

def boot():
    # Finite animation: readable first frame; final frame stays in place.
    font_path = Path('C:/Windows/Fonts/consola.ttf')
    if not font_path.exists():
        font_path = Path('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf')
    font=ImageFont.truetype(str(font_path), 18)
    frames=[]
    for n in range(13):
        im=Image.new('RGB', (960, 60), BG)
        d=ImageDraw.Draw(im)
        d.text((24,19), '> ATHARVA.OS',font=font,fill=GREEN)
        d.text((245,19), 'BOOT SEQUENCE',font=font,fill=MUTED)
        for i in range(12):
            d.rounded_rectangle((450+i*20,21,462+i*20,38),radius=2,fill=GREEN if i<n else LINE)
        d.text((730,19), 'READY' if n==12 else 'INITIALIZING',font=font,fill=GREEN if n==12 else GOLD)
        frames.append(im)
    frames[0].save(ASSETS/'boot.gif', save_all=True, append_images=frames[1:], duration=[120]*12+[1500], optimize=False)

if __name__ == '__main__':
    data=json.loads((ROOT/'data/contributions.json').read_text(encoding='utf-8'))
    hero(); hero(True); info(); heatmap(data); heatmap(data, True); boot()
    for old, new in [('retro-computer.svg', 'hero.svg'), ('info-card.svg', 'info-card.svg'), ('contrib-heatmap.svg', 'activity.svg')]:
        (ROOT/old).write_bytes((ASSETS/new).read_bytes())
    print('Built five SVGs, compatibility assets and finite boot GIF.')
