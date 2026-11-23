from teo import teo, DEFS
from bonecos import boneco
def street(pid):
    houses = ""
    for i, (x, w, h, c) in enumerate([(0, 230, 520, "#3d3346"), (220, 260, 600, "#4a3b4f"), (470, 220, 480, "#3a3044"), (680, 240, 640, "#45384d"), (910, 220, 540, "#3d3346")]):
        top = 1200 - h
        houses += f'<rect x="{x}" y="{top}" width="{w}" height="{h}" fill="{c}" stroke="#1a1410" stroke-width="5"/>'
        houses += f'<path d="M{x-10} {top} L{x + w/2} {top-90} L{x+w+10} {top} Z" fill="#2b2233" stroke="#1a1410" stroke-width="5"/>'
        for r in range(2):
            for k in range(2):
                wx = x + 40 + k * (w - 120); wy = top + 80 + r * 170
                houses += f'<rect x="{wx}" y="{wy}" width="60" height="80" fill="#f2c46d" stroke="#1a1410" stroke-width="5"/><path d="M{wx+30} {wy} V{wy+80}" stroke="#1a1410" stroke-width="4"/>'
    stones = "".join(f'<ellipse cx="{(c*120)+(60 if r%2 else 0)}" cy="{1250 + r*55}" rx="52" ry="20" fill="#5a4e48" stroke="#3a322e" stroke-width="4"/>' for r in range(13) for c in range(10))
    return f'''<svg id="{pid}" class="bg" data-layout-ignore viewBox="0 0 1080 1920" preserveAspectRatio="xMidYMid slice">
      <defs><linearGradient id="{pid}-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f2140"/><stop offset="1" stop-color="#b0596b"/></linearGradient></defs>
      <rect width="1080" height="1920" fill="url(#{pid}-sky)"/><circle cx="820" cy="260" r="70" fill="#f6e3b0" opacity="0.9"/>
      {houses}<rect y="1200" width="1080" height="720" fill="#4a403b"/>{stones}</svg>'''


def cellar(pid):
    bricks = "".join(f'<rect x="{(c*150)+(75 if r%2 else 0)-75}" y="{r*70}" width="140" height="60" rx="8" fill="#3b352d" stroke="#25211c" stroke-width="4"/>' for r in range(19) for c in range(9))
    planks = "".join(f'<path d="M{x} 1300 L{x*1.6-260} 1920" stroke="#2a1e16" stroke-width="5"/>' for x in range(0, 1200, 140))
    stairs = "".join(f'<rect x="{880 - i*0}" y="{1300 - (i+1)*110}" width="{200 + i*0}" height="24" fill="#4a3424" stroke="#1a1410" stroke-width="4"/>' for i in range(8))
    return f'''<svg id="{pid}" class="bg" data-layout-ignore viewBox="0 0 1080 1920" preserveAspectRatio="xMidYMid slice">
      <rect width="1080" height="1920" fill="#2b2620"/>{bricks}
      <rect x="860" y="0" width="240" height="1300" fill="#1b1714" opacity="0.7"/>{stairs}
      <rect y="1300" width="1080" height="620" fill="#3a2a1e"/>{planks}
      <rect width="1080" height="1920" fill="#000" opacity="0.35"/></svg>'''


CRATE = '<g><rect x="-150" y="-180" width="300" height="180" fill="#7a5533" stroke="#1a1410" stroke-width="6"/><path d="M-150 -120 H150 M-150 -60 H150 M-150 -180 L150 0" stroke="#5b3e24" stroke-width="8"/></g>'

COMMON_SCENE_CSS = """
    .bg { position:absolute; left:0; top:0; width:1080px; height:1920px; }
    .fig { position:absolute; left:0; top:0; width:1080px; height:1920px; overflow:visible; }
"""


def road_sign(city, km):
    """Placa verde de rodovia brasileira."""
    w = max(420, 60 + len(city) * 26)
    return (f'<g><rect x="-14" y="0" width="28" height="260" fill="#8D99AE" stroke="#1a1410" stroke-width="4"/>'
            f'<rect x="{-w / 2:.0f}" y="-210" width="{w:.0f}" height="190" rx="8" fill="#0b6e3a" stroke="#fff" stroke-width="8"/>'
            f'<text x="0" y="-130" font-family="Oswald, Osw" font-weight="700" font-size="54" text-anchor="middle" fill="#fff">{city.upper()}</text>'
            f'<text x="0" y="-70" font-family="Oswald, Osw" font-weight="700" font-size="44" text-anchor="middle" fill="#fff">{km} KM</text></g>')


def highway(pid):
    """Rodovia à noite: pista, faixas, mato dos lados."""
    dashes = "".join(f'<rect x="520" y="{y}" width="40" height="70" fill="#f2c46d" opacity="0.85"/>' for y in range(-200, 2200, 220))
    xs = list(range(-60, 220, 90)) + list(range(860, 1150, 90))
    trees = "".join(f'<ellipse cx="{x}" cy="{1180 + (i % 3) * 20}" rx="{70 + (i % 4) * 14}" ry="{90 + (i % 3) * 16}" fill="#13241a"/>' for i, x in enumerate(xs))
    return (f'<svg id="{pid}" class="bg" data-layout-ignore viewBox="0 0 1080 1920" preserveAspectRatio="xMidYMid slice">'
            f'<defs><linearGradient id="{pid}-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c0e1a"/><stop offset="1" stop-color="#232946"/></linearGradient></defs>'
            f'<rect width="1080" height="1200" fill="url(#{pid}-sky)"/>'
            f'<circle cx="860" cy="220" r="60" fill="#f6e3b0" opacity="0.9"/>'
            f'{trees}'
            f'<rect y="1150" width="1080" height="770" fill="#2b2b33"/>'
            f'<rect x="0" y="1150" width="60" height="770" fill="#d9d2c0"/><rect x="1020" y="1150" width="60" height="770" fill="#d9d2c0"/>'
            f'{dashes}</svg>')

