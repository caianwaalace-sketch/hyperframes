# NÍVEL 0 · EP.01: A luva azul. Incluído por build.py.
from teo import teo, DEFS
INV = SHRUG = ""
RED = "#D7263D"; CYAN = "#5CE1E6"


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

# ---------- S1: o mundo dos níveis ----------
PEOPLE = "".join(
    f'<g class="s1-p" transform="translate({x} 1560) scale({s})">{boneco(f"q{i}", 0, 0, 1.0, jacket=j, hat=h, hat_color=hc, worried=False)}'
    f'<g class="s1-l"><rect x="-60" y="-470" width="120" height="74" rx="14" fill="#111318" stroke="#E9C46A" stroke-width="5"/><text x="0" y="-417" font-family="Oswald" font-weight="700" font-size="52" text-anchor="middle" fill="#E9C46A">{lv}</text></g></g>'
    for i, (x, s, j, h, hc, lv) in enumerate([(200, 1.25, "#6A994E", "beanie", "#E8E4DA", "12"), (540, 1.35, "#457B9D", "ushanka", "#5c6370", "30"), (880, 1.2, "#BC6C25", "beanie", "#7B2CBF", "7")]))
scene("s1", COMMON_SCENE_CSS + """
""", f"""
      {street("s1-bg")}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{PEOPLE}</svg>
""", """
    tl.fromTo(".s1-l", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, stagger: 0.25, ease: "back.out(2)" }, @l1:7@);
    tl.fromTo(".s1-l", { scale: 1, transformOrigin: "50% 50%" }, { scale: 1.15, duration: 0.2, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, @l1:13@);
""")

# ---------- S2: padeiro 12, guarda 30, Téo 0 ----------
scene("s2", COMMON_SCENE_CSS + """
    #s2-pan { position:absolute; left:0; top:0; width:3240px; height:1920px; }
""", f"""
      <div id="s2-pan">
        <div style="position:absolute;left:0;top:0;width:1080px;height:1920px">{street("s2-bg1")}</div>
        <div style="position:absolute;left:1080px;top:0;width:1080px;height:1920px">{street("s2-bg2")}</div>
        <div style="position:absolute;left:2160px;top:0;width:1080px;height:1920px">{street("s2-bg3")}</div>
        <svg class="fig" data-layout-ignore viewBox="0 0 3240 1920" style="width:3240px">{DEFS}
          <g transform="translate(540 1600) scale(1.7)">{boneco("bk", 0, 0, 1.0, jacket="#F4F4F0", hat="nurse", scarf="#E9C46A", worried=False).replace('fill="#C1121F"', 'fill="#F4F4F0"')}
            <rect x="-60" y="-470" width="120" height="74" rx="14" fill="#111318" stroke="#E9C46A" stroke-width="5"/><text x="0" y="-417" font-family="Oswald" font-weight="700" font-size="52" text-anchor="middle" fill="#E9C46A">12</text></g>
          <g transform="translate(1620 1600) scale(1.7)">{boneco("gd", 0, 0, 1.0, jacket="#3a3f4a", hat="ushanka", hat_color="#5c6370", scarf="#8D99AE", worried=False)}
            <rect x="-60" y="-470" width="120" height="74" rx="14" fill="#111318" stroke="#E9C46A" stroke-width="5"/><text x="0" y="-417" font-family="Oswald" font-weight="700" font-size="52" text-anchor="middle" fill="#E9C46A">30</text></g>
          <g transform="translate(2700 1640) scale(1.15)">{teo("t2", "neutro", glow=False, level="0")}</g>
        </svg>
      </div>
""", """
    tl.fromTo("#s2-pan", { x: 0 }, { x: 0, duration: 0.01 }, 0);
    tl.to("#s2-pan", { x: -1080, duration: 0.55, ease: "power3.inOut" }, @l2:5-0.3@);
    tl.to("#s2-pan", { x: -2160, duration: 0.55, ease: "power3.inOut" }, @l2:10-0.3@);
    tl.fromTo("#t2-lvl", { scale: 1, transformOrigin: "50% 50%" }, { scale: 1.4, duration: 0.25, ease: "back.out(3)" }, @l2:14@);
    tl.to("#t2-x-neutro", { opacity: 0, duration: 0.1 }, @l2:14+0.3@);
    tl.fromTo("#t2-x-medo", { opacity: 0 }, { opacity: 1, duration: 0.1, immediateRender: false }, @l2:14+0.3@);
""")

# ---------- S3: close no rosto, "zero" ----------
scene("s3", COMMON_SCENE_CSS + """
    #s3-face { position:absolute; left:0; top:0; width:1080px; height:1920px; }
""", f"""
      {street("s3-bg")}
      <svg id="s3-face" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g id="s3-zoom"><g transform="translate(540 2700) scale(2.6)">{teo("t3", "medo", glow=False, level="0")}</g></g></svg>
""", """
    tl.fromTo("#s3-zoom", { scale: 1, transformOrigin: "50% 30%" }, { scale: 1.12, duration: D, ease: "none" }, 0);
    tl.fromTo("#t3-lvl", { opacity: 1 }, { opacity: 0.25, duration: 0.12, yoyo: true, repeat: 5, ease: "none" }, @l3:0@);
    tl.to("#t3-x-medo", { opacity: 0, duration: 0.15 }, @l3:1@);
    tl.fromTo("#t3-x-neutro", { opacity: 0 }, { opacity: 1, duration: 0.15, immediateRender: false }, @l3:1@);
    tl.fromTo("#t3-head", { rotation: 0, transformOrigin: "50% 100%" }, { rotation: -6, duration: 1.2, ease: "sine.inOut" }, @l3:2@);
""")

# ---------- S4: fugindo dos garotos ----------
KIDS = "".join(f'<g transform="translate({x} 1640) scale(1.0)">{boneco(f"k{i}", 0, 0, 1.0, jacket=c, hat="beanie", hat_color="#1a1a1a", worried=False)}</g>' for i, (x, c) in enumerate([(-200, "#7B2CBF"), (-60, "#264653"), (80, "#9C6644")]))
scene("s4", COMMON_SCENE_CSS + """
    .s4-ha { position:absolute; font-size:64px; font-weight:700; color:#E9C46A; }
""", f"""
      {street("s4-bg")}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s4-kids">{KIDS}</g>
        <g id="s4-run" transform="translate(0 0)"><g transform="translate(420 1680) scale(1.1)">{teo("t4", "medo", glow=False, level="0")}</g></g>
      </svg>
      <div class="s4-ha" id="s4-ha1" style="left:120px;top:880px">HAHA!</div>
      <div class="s4-ha" id="s4-ha2" style="left:300px;top:800px">NÍVEL ZERO!</div>
""", """
    tl.fromTo("#s4-kids", { x: -200 }, { x: 260, duration: D, ease: "none" }, 0);
    tl.fromTo("#s4-run", { x: 0 }, { x: 900, duration: D - 0.4, ease: "power1.in" }, 0.2);
    tl.fromTo("#t4-legL", { rotation: -30, transformOrigin: "50% 0%" }, { rotation: 30, duration: 0.14, yoyo: true, repeat: 25, ease: "sine.inOut" }, 0);
    tl.fromTo("#t4-legR", { rotation: 30, transformOrigin: "50% 0%" }, { rotation: -30, duration: 0.14, yoyo: true, repeat: 25, ease: "sine.inOut" }, 0);
    tl.fromTo("#t4-armL", { rotation: 30, transformOrigin: "50% 0%" }, { rotation: -30, duration: 0.14, yoyo: true, repeat: 25, ease: "sine.inOut" }, 0);
    tl.fromTo("#t4-armR", { rotation: -30, transformOrigin: "50% 0%" }, { rotation: 30, duration: 0.14, yoyo: true, repeat: 25, ease: "sine.inOut" }, 0);
    tl.fromTo("#s4-ha1", { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 0.2, ease: "back.out(3)" }, @l4:4@);
    tl.fromTo("#s4-ha2", { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 0.2, ease: "back.out(3)" }, @l4:6@);
""")

# ---------- S5: o porão e a luz azul ----------
scene("s5", COMMON_SCENE_CSS + """
    #s5-glow { position:absolute; left:340px; top:1150px; width:400px; height:400px; border-radius:50%; background:radial-gradient(circle, rgba(92,225,230,0.85) 0%, rgba(92,225,230,0) 70%); }
""", f"""
      {cellar("s5-bg")}
      <div id="s5-glow"></div>
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 1520)">{CRATE}<g id="s5-glove" transform="translate(0 -190) scale(1.3)"><path d="M-24 -22 Q-30 18 -6 26 Q22 30 26 6 L22 -26 Z" fill="{CYAN}" stroke="#1a1410" stroke-width="4"/></g></g>
        <g id="s5-teo"><g transform="translate(250 1700) scale(1.05)">{teo("t5", "medo", glow=False, level="0")}</g></g>
      </svg>
""", """
    tl.fromTo("#s5-glow", { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.6, ease: "power2.out" }, @l5:3@);
    tl.fromTo("#s5-glow", { scale: 1 }, { scale: 1.15, duration: 0.5, yoyo: true, repeat: 5, ease: "sine.inOut", immediateRender: false }, @l5:3+0.6@);
    tl.fromTo("#s5-glove", { opacity: 0 }, { opacity: 1, duration: 0.3 }, @l5:5@);
    tl.fromTo("#s5-teo", { x: -300 }, { x: 0, duration: 1.2, ease: "power2.out" }, 0.2);
    tl.fromTo("#t5-eyes-medo", { scaleY: 1, transformOrigin: "50% 50%" }, { scaleY: 0.1, duration: 0.06, yoyo: true, repeat: 1 }, @l5:7@);
""")

# ---------- S6: vestindo a luva ----------
scene("s6", COMMON_SCENE_CSS + """
    #s6-flash { position:absolute; inset:0; background:#5CE1E6; }
""", f"""
      {cellar("s6-bg")}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s6-zoom"><g transform="translate(470 1700) scale(1.6)">{teo("t6", "neutro", glow=True, level="0")}</g></g>
      </svg>
      <div id="s6-flash"></div>
""", """
    tl.fromTo("#s6-zoom", { scale: 2.3, svgOrigin: "939 964" }, { scale: 2.3, svgOrigin: "939 964", duration: 0.01 }, 0);
    tl.fromTo("#t6-armR", { rotation: 0, transformOrigin: "50% 0%" }, { rotation: -60, duration: 0.4, ease: "power2.out" }, 0.2);
    tl.fromTo("#t6-glow", { scale: 0.5, opacity: 0.3, transformOrigin: "50% 50%" }, { scale: 2.2, opacity: 1, duration: 0.5, ease: "power2.out" }, @l6:2@);
    tl.fromTo("#s6-flash", { opacity: 0 }, { opacity: 0.55, duration: 0.08, yoyo: true, repeat: 1, ease: "none" }, @l6:4@);
    tl.to("#s6-zoom", { scale: 1, duration: 0.8, ease: "power3.inOut" }, @l6:5@);
    tl.fromTo("#t6-lvl", { opacity: 1 }, { opacity: 0.15, duration: 0.08, yoyo: true, repeat: 11, ease: "none" }, @l6:12@);
    tl.to("#t6-x-neutro", { opacity: 0, duration: 0.1 }, @l6:12@);
    tl.fromTo("#t6-x-medo", { opacity: 0 }, { opacity: 1, duration: 0.1, immediateRender: false }, @l6:12@);
""")

# ---------- S7: 0 · 1 · 0 · 99 ----------
scene("s7", COMMON_SCENE_CSS + """
    .s7-n { position:absolute; left:0; top:520px; width:1080px; text-align:center; font-size:520px; font-weight:700; line-height:1; }
""", f"""
      {cellar("s7-bg")}
      <div class="s7-n red" id="s7-0a">0</div>
      <div class="s7-n" id="s7-1" style="color:#E8E4DA">1</div>
      <div class="s7-n red" id="s7-0b">0</div>
      <div class="s7-n" id="s7-99" style="color:#5CE1E6;text-shadow:0 0 60px #5CE1E6">99</div>
""", """
    tl.fromTo("#s7-0a", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.12 }, @l7:0@);
    tl.to("#s7-0a", { opacity: 0, duration: 0.05 }, @l7:1@);
    tl.fromTo("#s7-1", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.12 }, @l7:1@);
    tl.to("#s7-1", { opacity: 0, duration: 0.05 }, @l7:2@);
    tl.fromTo("#s7-0b", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.12 }, @l7:2@);
    tl.to("#s7-0b", { opacity: 0, duration: 0.05 }, @l7:3@);
    tl.fromTo("#s7-99", { opacity: 0, scale: 2 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power4.out" }, @l7:3@);
    tl.fromTo("#s7-99", { x: 0 }, { x: 14, duration: 0.04, yoyo: true, repeat: 9, ease: "none", immediateRender: false }, @l7:3+0.25@);
""")

# ---------- S8: alguém na escada ----------
scene("s8", COMMON_SCENE_CSS + """
    #s8-door { position:absolute; left:870px; top:110px; width:190px; height:320px; background:linear-gradient(#f6e3b0, #f2c46d); box-shadow:0 0 80px #f2c46d; opacity:0; }
""", f"""
      {cellar("s8-bg")}
      <div id="s8-door"></div>
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(965 425) scale(0.8)"><g id="s8-shadow"><path d="M-50 0 L-40 -260 Q0 -300 40 -260 L50 0 Z" fill="#000"/><circle cx="0" cy="-320" r="56" fill="#000"/></g></g>
        <g transform="translate(380 1720) scale(1.15)">{teo("t8", "medo", glow=True, level="99", level_color="#5CE1E6")}</g>
      </svg>
""", """
    tl.fromTo("#s8-door", { opacity: 0 }, { opacity: 0.9, duration: 0.4 }, @l8:1@);
    tl.fromTo("#s8-shadow", { opacity: 0, y: -40 }, { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, @l8:2@);
    tl.fromTo("#t8-head", { rotation: 0, transformOrigin: "50% 100%" }, { rotation: 10, duration: 0.3, ease: "power2.out" }, @l8:7@);
    tl.fromTo("#t8-eyes-medo", { scale: 1, transformOrigin: "50% 50%" }, { scale: 1.25, duration: 0.15, ease: "back.out(3)" }, @l8:7@);
""")

# ---------- S9: a escolha ----------
scene("s9", COMMON_SCENE_CSS + """
    #s9-k { top:330px; font-size:40px; color:#8FA3B0; }
    #s9-t { top:395px; font-size:96px; font-weight:700; line-height:1; }
    .s9-card { position:absolute; left:130px; width:820px; height:260px; border:4px solid #E8E4DA; background:#111318; box-sizing:border-box; }
    #s9-A { top:510px; } #s9-B { top:800px; }
    .s9-let { position:absolute; left:0; top:0; width:170px; height:252px; background:#D7263D; color:#fff; font-size:170px; font-weight:700; text-align:center; line-height:252px; }
    .s9-txt { position:absolute; left:200px; top:60px; width:590px; }
    .s9-txt b { display:block; font-size:64px; line-height:1.05; }
    .s9-txt span { display:block; margin-top:14px; font-size:28px; color:#8FA3B0; }
    #s9-bar { position:absolute; left:130px; top:1080px; width:820px; height:8px; background:#D7263D; transform-origin:0 50%; }
""", f"""
      {cellar("s9-bg")}
      <div id="s9-k" class="center mono">NÍVEL 0 · EP.02 · VOCÊ DECIDE</div>
      <div id="s9-t" class="center">O QUE O TÉO <span class="red">FAZ?</span></div>
      <div id="s9-A" class="s9-card"><div class="s9-let">A</div><div class="s9-txt"><b>SE ESCONDE</b><span class="mono">ATRÁS DA CAIXA</span></div></div>
      <div id="s9-B" class="s9-card"><div class="s9-let">B</div><div class="s9-txt"><b>SOBE A ESCADA</b><span class="mono">E ENCARA QUEM CHAMOU</span></div></div>
      <div id="s9-bar"></div>
""", """
    tl.fromTo("#s9-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.1);
    tl.fromTo("#s9-t", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.15);
    tl.fromTo("#s9-A", { opacity: 0, x: -1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l9:3@);
    tl.fromTo("#s9-B", { opacity: 0, x: 1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l9:9@);
    tl.fromTo("#s9-A", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l10:0@);
    tl.fromTo("#s9-B", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l10:0+0.25@);
    tl.fromTo("#s9-bar", { scaleX: 0 }, { scaleX: 1, duration: 2.6, ease: "none" }, @l10:0+0.8@);
""")
_p = "compositions/s9.html"
_c = open(_p).read()
open(_p, "w").write(_c.replace('tl.to("#s9-cam", { opacity: 0, duration: 0.14, ease: "power2.in" }, D - 0.16);', ""))

G_EP = [
 ("l1", [("NESTE MUNDO,", "Neste mundo,"), ("TODO MUNDO NASCE", "todo mundo nasce"), ("COM UM NÚMERO", "com um número"), ("EM CIMA DA CABEÇA.", "em cima da cabeça."), ("O NÍVEL.", "O nível.")]),
 ("l2", [("O DO PADEIRO", "O do padeiro"), ("É 12.", "é doze."), ("O DA GUARDA", "O da guarda"), ("É 30.", "é trinta."), ("O DO TÉO", "O do Téo"), ("É ZERO.", "é zero.")]),
 ("l3", [("ZERO.", "Zero."), ("O ÚNICO", "O único"), ("DA CIDADE INTEIRA.", "da cidade inteira.")]),
 ("l4", [("NUMA NOITE,", "Numa noite,"), ("FUGINDO DOS GAROTOS", "fugindo dos garotos"), ("QUE RIAM DELE,", "que riam dele,"), ("O TÉO SE ESCONDEU", "o Téo se escondeu"), ("NUM PORÃO ABANDONADO.", "num porão abandonado.")]),
 ("l5", [("NO ESCURO,", "No escuro,"), ("UMA LUZ AZUL.", "uma luz azul."), ("UMA LUVA,", "Uma luva,"), ("ESQUECIDA", "esquecida"), ("NUMA CAIXA DE MADEIRA.", "numa caixa de madeira.")]),
 ("l6", [("QUANDO ELE", "Quando ele"), ("VESTIU A LUVA,", "vestiu a luva,"), ("O NÚMERO", "o número"), ("EM CIMA DA CABEÇA DELE", "em cima da cabeça dele"), ("COMEÇOU A PISCAR.", "começou a piscar.")]),
 ("l7", [("ZERO.", "Zero."), ("UM.", "Um."), ("ZERO.", "Zero."), ("NOVENTA E NOVE.", "Noventa e nove.")]),
 ("l8", [("E ALGUÉM,", "E alguém,"), ("LÁ EM CIMA DA ESCADA,", "lá em cima da escada,"), ("CHAMOU O NOME DELE.", "chamou o nome dele.")]),
 ("l9", [("AMANHÃ,", "Amanhã,"), ("VOCÊ DECIDE.", "você decide."), ("A: O TÉO SE ESCONDE.", "A: o Téo se esconde."), ("OU B:", "Ou B:"), ("O TÉO SOBE A ESCADA.", "o Téo sobe a escada.")]),
 ("l10", [("COMENTA A OU B!", "Comenta A ou B.")]),
]
SFX_EP = [
    ("pop.mp3", WT("l1", 7), 0.4), ("pop.mp3", WT("l1", 7, 0.25), 0.35), ("pop.mp3", WT("l1", 7, 0.5), 0.4),
    ("whoosh-short.mp3", WT("l2", 5, -0.3), 0.45), ("whoosh-short.mp3", WT("l2", 10, -0.3), 0.45), ("impact-bass-2.mp3", WT("l2", 14), 0.5),
    ("whoosh.mp3", slot["s4"][0], 0.45),
    ("whoosh.mp3", slot["s5"][0], 0.4), ("glitch-1.mp3", WT("l5", 3), 0.25),
    ("impact-bass-1.mp3", WT("l6", 4), 0.6), ("glitch-2.mp3", WT("l6", 12), 0.3),
    ("pop.mp3", WT("l7", 0), 0.45), ("pop.mp3", WT("l7", 1), 0.45), ("pop.mp3", WT("l7", 2), 0.45), ("impact-bass-2.mp3", WT("l7", 3), 0.6),
    ("whoosh-short.mp3", WT("l9", 3), 0.5), ("whoosh-short.mp3", WT("l9", 9), 0.5),
]
