"""Validate image safety, local README targets and contribution integrity."""
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT/'data/contributions.json').read_text())
assert data['username'].lower() == 'atharvanh'
assert sum(d['count'] for d in data['days']) == data['total_contributions']
for path in list((ROOT/'assets').glob('*.svg')) + list(ROOT.glob('*.svg')):
    svg = ET.parse(path).getroot()
    assert svg.get('viewBox') and svg.find('{http://www.w3.org/2000/svg}title') is not None, path
    for node in svg.iter():
        assert node.tag.split('}')[-1] not in ('script', 'foreignObject', 'animate', 'animateTransform', 'set'), path
        assert not any(k.lower().startswith('on') for k in node.attrib), path
        assert 'opacity: 0' not in node.get('style', ''), path
readme = (ROOT/'README.md').read_text(encoding='utf-8-sig')
for target in re.findall(r'(?:src|srcset)="(\./[^\"]+)"', readme):
    assert (ROOT/target).is_file(), target
for image in re.findall(r'<img\b[^>]+>', readme):
    assert re.search(r'alt="[^"]+"', image), image
for link in ('https://atharvanh.me', 'https://linkedin.com/in/atharvaharale', 'mailto:atharvapc1@gmail.com'):
    assert link in readme
with Image.open(ROOT/'assets/boot.gif') as im:
    assert im.n_frames > 1 and 'loop' not in im.info, 'Boot animation must finish'
print('SVG safety, data totals, README images, links and finite GIF: passed')
