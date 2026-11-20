#!/usr/bin/env python3
"""Gera o episódio (index.html + compositions/*) a partir do roteiro e dos tempos da narração."""
import json, os, random, re
from bonecos import boneco

W, H, TOTAL = 1080, 1920, 60
T = json.load(open("timing.json"))
L = {l["id"]: l for l in T["lines"]}
os.makedirs("compositions", exist_ok=True)

# ---------- cenas (host start/dur) ----------
starts = [L[k]["start"] for k in ["l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8", "l9"]]
starts[0] = 0
ends = starts[1:] + [TOTAL]
SCENES = [f"s{i+1}" for i in range(9)]
slot = {s: (round(a, 2), round(b - a, 2)) for s, a, b in zip(SCENES, starts, ends)}

COMMON_CSS = """
    #root { position:absolute; inset:0; overflow:hidden; font-family:'Oswald',sans-serif; color:#E8E4DA; }
    .mono { font-family:'Space Mono',monospace; letter-spacing:0.06em; }
    .red { color:#D7263D; }
    .center { position:absolute; left:110px; width:860px; text-align:center; }
    .cam { position:absolute; inset:0; }
"""


def WT(lid, i, off=0.0):
    return T["words"][lid][i][1] + off


def scene(sid, css, body, js):
    js = re.sub(r"@(l\d+):(\d+)([+-][\d.]+)?@", lambda m: str(round(WT(m.group(1), int(m.group(2)), float(m.group(3) or 0)) - slot[sid][0], 3)), js)
    for k in ("INV", "SHRUG"):
        body = body.replace("{" + k + "}", globals().get(k, ""))
    start, dur = slot[sid]
    html = f"""<template>
  <style>{COMMON_CSS}{css}
  </style>
  <div id="root" data-composition-id="{sid}" data-width="{W}" data-height="{H}">
    <div id="{sid}-cam" class="cam">
{body}
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    const D = {dur};
    tl.fromTo("#{sid}-cam", {{ scale: 1 }}, {{ scale: 1.07, duration: D, ease: "none" }}, 0);
{js}
    tl.to("#{sid}-cam", {{ opacity: 0, duration: 0.14, ease: "power2.in" }}, D - 0.16);
    window.__timelines["{sid}"] = tl;
  </script>
</template>
"""
    open(f"compositions/{sid}.html", "w").write(html)


MOUNTAIN = '<path d="M0 760 L170 520 L260 600 L420 330 L560 520 L640 450 L820 640 L930 560 L1080 700 L1080 900 L0 900 Z" fill="#12141a"/><path d="M420 330 L470 400 L445 395 L420 430 L395 400 L380 410 Z" fill="#cfd6dc" opacity="0.55"/>'


JACKETS = ["#3A6EA5", "#6A994E", "#BC6C25", "#7B2CBF", "#2A9D8F", "#E76F51", "#457B9D", "#9C6644", "#588157"]
HATS = ["#C1121F", "#E9C46A", "#264653", "#F4A261", "#C1121F", "#8D99AE", "#E9C46A", "#2A9D8F", "#D62828"]
CREW = "".join(f'<g class="s1-who">{boneco(f"c{i}", 120 + i*105, 280, 0.66, jacket=JACKETS[i], hat_color=HATS[i], worried=False)}</g>' for i in range(9))
RUNNER = boneco("r3", 930, 600, 0.55, jacket="#3A6EA5", socks=True, scarf="#C1121F")
GEIGER = '<g transform="translate(40 -112)"><rect x="0" y="-18" width="62" height="40" rx="6" fill="#E9C46A" stroke="#111" stroke-width="4"/><circle cx="31" cy="2" r="11" fill="#fff" stroke="#111" stroke-width="3"/><path d="M31 2 L39 -6" stroke="#C1121F" stroke-width="3"/></g>'
INV = boneco("i6", 0, 0, 1.0, jacket="#B08D57", hat="fedora", hat_color="#3b3024", scarf="#5a4632", hand_prop=GEIGER)
SHRUG = boneco("h8", 0, 0, 1.0, jacket="#6A994E", hat="beanie", hat_color="#E9C46A", scarf="#3A6EA5")

# ---------- S1: gancho ----------
scene("s1", """
    #s1-big1 { top:380px; font-size:140px; font-weight:700; line-height:0.95; }
    #s1-big2 { top:560px; font-size:140px; font-weight:700; line-height:0.95; color:#D7263D; }
    #s1-tag { top:1010px; font-size:32px; color:#8FA3B0; }
    #s1-mt { position:absolute; left:0; top:700px; width:1080px; height:900px; }
    #s1-crew { position:absolute; left:0; top:720px; width:1080px; height:290px; }
""", f"""
      <svg id="s1-mt" data-layout-ignore viewBox="0 0 1080 900">{MOUNTAIN}</svg>
      <div id="s1-big1" class="center">9 SUBIRAM.</div>
      <div id="s1-big2" class="center">0 VOLTARAM.</div>
      <svg id="s1-crew" data-layout-ignore viewBox="0 0 1080 290">{CREW}</svg>
      <div id="s1-tag" class="center mono">FEV · 1959 · MONTES URAIS · URSS</div>
""", """
    tl.fromTo("#s1-big1", { y: 0, opacity: 1 }, { y: -10, duration: 1.2, ease: "power2.out" }, 0);
    tl.fromTo("#s1-mt", { y: 120, opacity: 0.4 }, { y: 0, opacity: 1, duration: 2.4, ease: "power3.out" }, 0);
    tl.fromTo("#s1-tag", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.5, ease: "power4.out" }, 0.6);
    tl.fromTo("#s1-big2", { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, duration: 0.22, ease: "power4.out" }, @l1:14@);
    tl.fromTo(".s1-who", { y: 0 }, { y: -8, duration: 0.35, yoyo: true, repeat: 3, ease: "sine.inOut", stagger: 0.08 }, 0.2);
    tl.fromTo(".s1-who", { opacity: 1 }, { opacity: 0.08, duration: 0.35, stagger: 0.12, ease: "power2.in", immediateRender: false }, @l1:14+0.1@);
    tl.fromTo("#s1-big1", { opacity: 1 }, { opacity: 0.35, duration: 0.4, immediateRender: false }, @l1:14@);
""")

# ---------- S2: barraca rasgada ----------
scene("s2", """
    #s2-title { top:330px; font-size:64px; font-weight:700; color:#8FA3B0; }
    #s2-tent { position:absolute; left:150px; top:420px; width:780px; height:520px; }
    #s2-in { top:950px; font-size:92px; font-weight:700; color:#D7263D; }
""", """
      <div id="s2-title" class="center mono">BARRACA ENCONTRADA</div>
      <svg id="s2-tent" viewBox="0 0 900 600">
        <path d="M60 540 L450 90 L840 540 Z" fill="#2a2d33" stroke="#E8E4DA" stroke-width="6"/>
        <path d="M450 90 L450 540" stroke="#E8E4DA" stroke-width="3" opacity="0.4"/>
        <path d="M20 560 L880 560" stroke="#cfd6dc" stroke-width="6" opacity="0.6"/>
        <path id="s2-cut" d="M500 200 L530 280 L515 310 L555 400 L540 430 L580 510" fill="none" stroke="#D7263D" stroke-width="12" stroke-linecap="round" stroke-dasharray="420" stroke-dashoffset="420"/>
        <path id="s2-cut2" d="M560 300 L585 370 L575 400 L610 470" fill="none" stroke="#D7263D" stroke-width="9" stroke-linecap="round" stroke-dasharray="260" stroke-dashoffset="260"/>
      </svg>
      <div id="s2-in" class="center">DE DENTRO PRA FORA</div>
""", """
    tl.fromTo("#s2-title", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.4, ease: "power4.out" }, 0.1);
    tl.fromTo("#s2-tent", { opacity: 0, y: 80 }, { opacity: 1, y: 0, duration: 0.6, ease: "power4.out" }, 0.15);
    tl.fromTo("#s2-cut", { strokeDashoffset: 420 }, { strokeDashoffset: 0, duration: 0.28, ease: "power4.out" }, @l2:10@);
    tl.fromTo("#s2-cut2", { strokeDashoffset: 260 }, { strokeDashoffset: 0, duration: 0.22, ease: "power4.out" }, @l2:10+0.15@);
    tl.fromTo("#s2-tent", { x: 0 }, { x: 14, duration: 0.05, yoyo: true, repeat: 5, ease: "none", immediateRender: false }, @l2:10@);
    tl.fromTo("#s2-in", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.22, ease: "power4.out" }, @l2:11@);
""")

# ---------- S3: frio e pegadas ----------
prints = "\n".join(
    f'<ellipse class="s3-fp" cx="{140 + i*62 + (i%2)*0}" cy="{560 - i*14 + (18 if i%2 else -18)}" rx="13" ry="22" fill="#E8E4DA" opacity="0.85" transform="rotate(70 {140 + i*62} {560 - i*14 + (18 if i%2 else -18)})"/>'
    for i in range(12)
)
scene("s3", """
    #s3-temp { top:320px; font-size:250px; font-weight:700; line-height:1; color:#8FA3B0; }
    #s3-sub { top:590px; font-size:44px; color:#E8E4DA; }
    #s3-trail { position:absolute; left:0; top:440px; width:1080px; height:620px; }
    #s3-socks { top:670px; font-size:68px; font-weight:700; }
""", f"""
      <div id="s3-temp" class="center"><span id="s3-num">0</span>°C</div>
      <div id="s3-sub" class="center mono">NO MEIO DA NOITE</div>
      <svg id="s3-trail" data-layout-ignore viewBox="0 0 1080 620">
        <path d="M0 600 C300 520 700 520 1080 590 L1080 620 L0 620 Z" fill="#1a1d22"/>
        {prints}
        <g id="s3-run">{RUNNER}</g>
      </svg>
      <div id="s3-socks" class="center">SÓ DE MEIAS. <span class="red">SEM CASACOS.</span></div>
""", """
    const t3 = { v: 0 };
    tl.fromTo(t3, { v: 0 }, { v: -30, duration: 2.0, ease: "power2.out",
      onUpdate: () => { document.getElementById("s3-num").textContent = Math.round(t3.v); } }, @l3:6@);
    tl.fromTo("#s3-temp", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.4, ease: "power4.out" }, 0.05);
    tl.fromTo("#s3-temp", { color: "#E8E4DA" }, { color: "#8FD3FF", duration: 2.0, immediateRender: false }, @l3:6@);
    tl.fromTo("#s3-sub", { opacity: 0 }, { opacity: 1, duration: 0.4 }, 0.3);
    tl.fromTo(".s3-fp", { opacity: 0, scale: 0.4, transformOrigin: "50% 50%" }, { opacity: 0.85, scale: 1, duration: 0.18, stagger: 0.16, ease: "power3.out" }, @l3:9@);
    tl.fromTo("#s3-run", { x: -260, opacity: 0 }, { x: 0, opacity: 1, duration: 2.6, ease: "power1.out" }, @l3:9-0.2@);
    tl.fromTo("#r3-legL", { rotation: -28, transformOrigin: "50% 0%" }, { rotation: 28, duration: 0.16, yoyo: true, repeat: 15, ease: "sine.inOut" }, 2.4);
    tl.fromTo("#r3-legR", { rotation: 28, transformOrigin: "50% 0%" }, { rotation: -28, duration: 0.16, yoyo: true, repeat: 15, ease: "sine.inOut" }, 2.4);
    tl.fromTo("#r3-armL", { rotation: 35, transformOrigin: "50% 0%" }, { rotation: -35, duration: 0.16, yoyo: true, repeat: 15, ease: "sine.inOut" }, 2.4);
    tl.fromTo("#r3-armR", { rotation: -35, transformOrigin: "50% 0%" }, { rotation: 35, duration: 0.16, yoyo: true, repeat: 15, ease: "sine.inOut" }, 2.4);
    tl.fromTo("#r3-fig", { x: 0 }, { x: 4, duration: 0.05, yoyo: true, repeat: 15, ease: "none" }, @l3:14@);
    tl.fromTo("#s3-socks", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l3:10@);
""")

# ---------- S4: mapa ----------
rnd = random.Random(1959)
dots = "\n".join(
    f'<circle class="s4-dot" cx="{x}" cy="{y}" r="16" fill="#D7263D"/>'
    for x, y in [(720, 210), (760, 260), (690, 300), (610, 330), (540, 380), (470, 420), (790, 180), (650, 250), (580, 300)]
)
topo = "\n".join(
    f'<ellipse cx="{540 + rnd.randint(-30,30)}" cy="{420 + rnd.randint(-20,20)}" rx="{120 + i*70}" ry="{80 + i*48}" fill="none" stroke="#8FA3B0" stroke-width="2" opacity="{0.35 - i*0.04:.2f}"/>'
    for i in range(7)
)
scene("s4", """
    #s4-map { position:absolute; left:110px; top:460px; width:860px; height:600px; }
    #s4-km { position:absolute; left:110px; width:860px; top:320px; text-align:center; font-size:120px; font-weight:700; }
""", f"""
      <div id="s4-km">+1,5 KM</div>
      <svg id="s4-map" viewBox="0 0 1000 760">
        {topo}
        <path d="M150 620 L210 540 L270 620 Z" fill="#E8E4DA"/>
        <text x="210" y="680" fill="#E8E4DA" font-family="Space Mono" font-size="30" text-anchor="middle">BARRACA</text>
        <path id="s4-path" d="M210 580 C330 520 420 470 520 400 S700 240 760 200" fill="none" stroke="#E8E4DA" stroke-width="6" stroke-dasharray="14 14"/>
        <rect id="s4-mask" x="0" y="0" width="1000" height="760" fill="#070708"/>
        {dots}
      </svg>
""", """
    tl.fromTo("#s4-map", { opacity: 0, scale: 0.92 }, { opacity: 1, scale: 1, duration: 0.5, ease: "power4.out" }, 0.05);
    tl.fromTo("#s4-mask", { x: 0 }, { x: 1000, duration: 1.6, ease: "power2.inOut" }, 0.3);
    tl.fromTo(".s4-dot", { opacity: 0, scale: 0, transformOrigin: "50% 50%" }, { opacity: 1, scale: 1, duration: 0.2, stagger: 0.09, ease: "back.out(3)" }, @l4:3@);
    tl.fromTo("#s4-km", { opacity: 0, y: -30 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, @l4:7@);
""")

# ---------- S5: ferimentos ----------
scene("s5", """
    #s5-head { top:330px; font-size:40px; color:#8FA3B0; }
    .s5-row { position:absolute; left:120px; width:840px; font-size:60px; font-weight:700; border-bottom:2px solid #33363d; padding-bottom:12px; }
    #s5-r1 { top:420px; } #s5-r2 { top:540px; }
    #s5-ext { top:720px; font-size:58px; }
    #s5-none { top:800px; font-size:170px; font-weight:700; color:#D7263D; line-height:1; }
""", """
      <div id="s5-head" class="center mono">LAUDO · FERIMENTOS</div>
      <div id="s5-r1" class="s5-row">COSTELAS ......... <span class="red">ESMAGADAS</span></div>
      <div id="s5-r2" class="s5-row">CRÂNIOS .......... <span class="red">FRATURADOS</span></div>
      <div id="s5-ext" class="center mono">FERIMENTOS POR FORA:</div>
      <div id="s5-none" class="center">NENHUM</div>
""", """
    tl.fromTo("#s5-head", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.05);
    tl.fromTo("#s5-r1", { opacity: 0, x: -60 }, { opacity: 1, x: 0, duration: 0.3, ease: "power4.out" }, @l5:2@);
    tl.fromTo("#s5-r2", { opacity: 0, x: -60 }, { opacity: 1, x: 0, duration: 0.3, ease: "power4.out" }, @l5:4@);
    tl.fromTo("#s5-ext", { opacity: 0 }, { opacity: 1, duration: 0.3 }, @l5:6@);
    tl.fromTo("#s5-none", { opacity: 0, scale: 1.8 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.out" }, @l5:7@);
""")

# ---------- S6: língua + radiação ----------
scene("s6", """
    #s6-a { top:330px; font-size:44px; color:#8FA3B0; }
    #s6-b { top:390px; font-size:110px; font-weight:700; }
    #s6-rad { position:absolute; left:560px; top:620px; width:300px; height:300px; }
    #s6-inv { position:absolute; left:190px; top:590px; width:300px; height:345px; }
    #s6-radt { top:955px; font-size:76px; font-weight:700; color:#E9C46A; }
""", """
      <div id="s6-a" class="center mono">VÍTIMA Nº 7</div>
      <div id="s6-b" class="center">SEM A <span class="red">LÍNGUA</span></div>
      <svg id="s6-rad" viewBox="-100 -100 200 200">
        <circle r="96" fill="#E9C46A"/>
        <g fill="#070708">
          <circle r="16"/>
          <path d="M0 0 L26 -45 A52 52 0 0 1 52 0 Z" transform="scale(1.6)"/>
          <path d="M0 0 L26 -45 A52 52 0 0 1 52 0 Z" transform="rotate(120) scale(1.6)"/>
          <path d="M0 0 L26 -45 A52 52 0 0 1 52 0 Z" transform="rotate(240) scale(1.6)"/>
        </g>
      </svg>
      <svg id="s6-inv" data-layout-ignore viewBox="-150 -345 300 345">{INV}</svg>
      <div id="s6-radt" class="center">TRAÇOS DE RADIAÇÃO</div>
""", """
    tl.fromTo("#s6-a", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.05);
    tl.fromTo("#s6-b", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l6:4@);
    tl.fromTo("#s6-rad", { opacity: 0, scale: 0.3, rotation: -90 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.45, ease: "power4.out" }, @l6:13@);
    tl.fromTo("#s6-rad", { x: 0 }, { x: 10, duration: 0.04, yoyo: true, repeat: 7, ease: "none", immediateRender: false }, @l6:13+0.45@);
    tl.fromTo("#s6-inv", { x: -400, opacity: 0 }, { x: 0, opacity: 1, duration: 0.5, ease: "power4.out" }, @l6:10@);
    tl.fromTo("#i6-armR", { rotation: 0, transformOrigin: "50% 0%" }, { rotation: -70, duration: 0.3, ease: "back.out(2)" }, @l6:12@);
    tl.fromTo("#i6-eyes", { scale: 1, transformOrigin: "50% 50%" }, { scale: 1.6, duration: 0.15, ease: "power4.out" }, @l6:13@);
    tl.fromTo("#i6-head", { y: 0 }, { y: -14, duration: 0.15, ease: "power4.out" }, @l6:13@);
    tl.fromTo("#i6-fig", { x: 0 }, { x: 5, duration: 0.04, yoyo: true, repeat: 11, ease: "none" }, @l6:13+0.05@);
    tl.fromTo("#s6-radt", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l6:13+0.3@);
""")

# ---------- S7: arquivado ----------
scene("s7", """
    #s7-doc { position:absolute; left:130px; top:330px; width:820px; height:700px; background:#d9d2c0; color:#1a1a1a; padding:50px; box-sizing:border-box; }
    #s7-doc .mono { font-size:28px; color:#333; }
    .s7-l { height:16px; background:#b9b19c; margin-top:26px; }
    #s7-q { font-family:'Playfair Display',serif; font-style:italic; font-size:64px; line-height:1.15; margin-top:50px; color:#111; }
    #s7-stamp { position:absolute; left:250px; top:830px; width:580px; text-align:center; font-size:96px; font-weight:700; color:#C1121F; border:10px solid #C1121F; padding:6px 0; }
""", """
      <div id="s7-doc">
        <div class="mono">URSS · PROCURADORIA · CASO Nº 1959/02</div>
        <div class="s7-l" style="width:90%"></div><div class="s7-l" style="width:75%"></div>
        <div id="s7-q">“Uma força natural irresistível.”</div>
        <div class="s7-l" style="width:85%"></div><div class="s7-l" style="width:60%"></div>
      </div>
      <div id="s7-stamp">ARQUIVADO</div>
""", """
    tl.fromTo("#s7-doc", { opacity: 0, y: 120, rotation: 3 }, { opacity: 1, y: 0, rotation: -1.5, duration: 0.55, ease: "power4.out" }, 0.05);
    tl.fromTo("#s7-q", { opacity: 0 }, { opacity: 1, duration: 0.5 }, @l7:9@);
    tl.fromTo("#s7-stamp", { opacity: 0, scale: 2.2, rotation: -14 }, { opacity: 0.92, scale: 1, rotation: -9, duration: 0.16, ease: "power4.in" }, @l7:12+0.35@);
""")

# ---------- S8: avalanche? ----------
scene("s8", """
    #s8-year { top:330px; font-size:200px; font-weight:700; color:#8FA3B0; line-height:1; }
    #s8-av { top:560px; font-size:120px; font-weight:700; }
    #s8-closed { top:780px; font-size:64px; }
    #s8-strike { position:absolute; left:290px; top:822px; width:500px; height:10px; background:#D7263D; transform-origin:0 50%; }
    #s8-shrug { position:absolute; left:600px; top:870px; width:240px; height:250px; }
    #s8-q { top:870px; left:240px; width:330px; font-size:190px; font-weight:700; color:#D7263D; line-height:1; }
""", """
      <div id="s8-year" class="center">2020</div>
      <div id="s8-av" class="center">AVALANCHE</div>
      <div id="s8-closed" class="center mono">CASO ENCERRADO</div>
      <div id="s8-strike"></div>
      <svg id="s8-shrug" data-layout-ignore viewBox="-140 -345 280 350">{SHRUG}</svg>
      <div id="s8-q" class="center">?</div>
""", """
    tl.fromTo("#s8-year", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.05);
    tl.fromTo("#s8-av", { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power4.out" }, @l8:9@);
    tl.fromTo("#s8-closed", { opacity: 0 }, { opacity: 1, duration: 0.3 }, @l8:9+0.4@);
    tl.fromTo("#s8-strike", { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: "power4.out" }, @l8:10@);
    tl.fromTo("#s8-shrug", { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, @l8:10@);
    tl.fromTo("#h8-armL", { rotation: 0, transformOrigin: "50% 0%" }, { rotation: 120, duration: 0.25, ease: "back.out(2)" }, @l8:13@);
    tl.fromTo("#h8-armR", { rotation: 0, transformOrigin: "50% 0%" }, { rotation: -120, duration: 0.25, ease: "back.out(2)" }, @l8:13@);
    tl.fromTo("#h8-head", { rotation: 0, transformOrigin: "50% 100%" }, { rotation: -10, duration: 0.3, ease: "power2.out" }, @l8:13+0.05@);
    tl.fromTo("#s8-q", { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.5)" }, @l8:13@);
""")

# ---------- S9: a pergunta ----------
scene("s9", """
    #s9-k { top:330px; font-size:40px; color:#8FA3B0; }
    #s9-t { top:395px; font-size:96px; font-weight:700; line-height:1; }
    .s9-card { position:absolute; left:130px; width:820px; height:260px; border:4px solid #E8E4DA; background:#111318; box-sizing:border-box; }
    #s9-A { top:510px; } #s9-B { top:800px; }
    .s9-let { position:absolute; left:0; top:0; width:170px; height:252px; background:#D7263D; color:#fff; font-size:170px; font-weight:700; text-align:center; line-height:252px; }
    .s9-txt { position:absolute; left:200px; top:40px; width:590px; }
    .s9-txt b { display:block; font-size:56px; line-height:1.05; }
    .s9-txt span { display:block; margin-top:14px; font-size:28px; color:#8FA3B0; }
    #s9-cta { top:1110px; font-size:78px; font-weight:700; color:#E9C46A; }
    #s9-bar { position:absolute; left:130px; top:1080px; width:820px; height:8px; background:#D7263D; transform-origin:0 50%; }
""", """
      <div id="s9-k" class="center mono">EPISÓDIO 02 · VOCÊ DECIDE</div>
      <div id="s9-t" class="center">AMANHÃ, <span class="red">QUAL?</span></div>
      <div id="s9-A" class="s9-card"><div class="s9-let">A</div><div class="s9-txt"><b>ELISA LAM E O HOTEL CECIL</b><span class="mono">LOS ANGELES · 2013</span></div></div>
      <div id="s9-B" class="s9-card"><div class="s9-let">B</div><div class="s9-txt"><b>O HOMEM DE SOMERTON</b><span class="mono">AUSTRÁLIA · 1948</span></div></div>
      <div id="s9-bar"></div>
""", """
    tl.fromTo("#s9-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.1);
    tl.fromTo("#s9-t", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.15);
    tl.fromTo("#s9-A", { opacity: 0, x: -1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l9:3@);
    tl.fromTo("#s9-B", { opacity: 0, x: 1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l9:13@);
    // "Comenta A ou B": as duas cartas pulsam alternadas
    tl.fromTo("#s9-A", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l10:0@);
    tl.fromTo("#s9-B", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l10:0+0.25@);
    tl.fromTo("#s9-bar", { scaleX: 0 }, { scaleX: 1, duration: 4, ease: "none" }, @l10:0+1.4@);
""")
# a cena 9 não deve escurecer no final: remove o fade de saída
p = "compositions/s9.html"
_c = open(p).read()
open(p, "w").write(_c.replace('tl.to("#s9-cam", { opacity: 0, duration: 0.14, ease: "power2.in" }, D - 0.16);', ""))

# ---------- atmosfera: neve, vinheta, selo da série ----------
rs = random.Random(7)
flakes, fjs = [], []
for i in range(60):
    x = rs.randint(0, W); sz = rs.choice([3, 4, 5, 6, 8]); dur = rs.uniform(6, 12); y0 = rs.uniform(-1920, 0)
    op = rs.uniform(0.25, 0.7)
    flakes.append(f'<div id="sn{i}" class="flake" data-layout-ignore style="left:{x}px;top:0px;width:{sz}px;height:{sz}px;opacity:{op:.2f}"></div>')
    fjs.append(f'tl.fromTo("#sn{i}", {{ y: {y0:.0f}, x: 0 }}, {{ y: {y0 + 2100*TOTAL/dur:.0f}, x: {rs.randint(-160,160)}, duration: {TOTAL}, ease: "none", modifiers: {{ y: v => ((parseFloat(v) % 2100) + 2100) % 2100 - 100 + "px" }} }}, 0);')
open("compositions/atmos.html", "w").write(f"""<template>
  <style>
    #root {{ position:absolute; inset:0; pointer-events:none; overflow:hidden; }}
    .flake {{ position:absolute; border-radius:50%; background:#E8E4DA; }}
    #at-vig {{ position:absolute; inset:0; background:radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 45%, rgba(0,0,0,0.75) 100%); }}
    #at-badge {{ position:absolute; left:140px; width:800px; top:262px; text-align:center; font-family:'Space Mono',monospace; font-size:28px; letter-spacing:0.3em; color:#D7263D; }}
  </style>
  <div id="root" data-composition-id="atmos" data-width="{W}" data-height="{H}">
    {''.join(flakes)}
    <div id="at-vig" data-layout-ignore></div>
    <div id="at-badge">● AMANHÃ VOCÊ DECIDE · EP.01</div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join(fjs)}
    tl.to("#at-badge", {{ opacity: 0, duration: 0.3 }}, {slot["s9"][0]});
    window.__timelines["atmos"] = tl;
  </script>
</template>
""")

# ---------- legendas ----------
G = [
 ("l1", [("EM 1959,", "em mil novecentos e cinquenta e nove,"), ("NOVE JOVENS", "nove jovens"), ("SUBIRAM UMA MONTANHA", "subiram uma montanha"), ("NA RÚSSIA.", "na Rússia."), ("NENHUM", "nenhum"), ("VOLTOU VIVO.", "voltou vivo.")]),
 ("l2", [("SEMANAS DEPOIS,", "semanas depois,"), ("AS EQUIPES DE BUSCA", "as equipes de busca"), ("ACHARAM A BARRACA", "acharam a barraca deles."), ("RASGADA.", "rasgada."), ("DE DENTRO PRA FORA.", "de dentro pra fora.")]),
 ("l3", [("ELES FUGIRAM", "eles fugiram"), ("NO MEIO DA NOITE,", "no meio da noite,"), ("A 30 GRAUS NEGATIVOS.", "a trinta graus negativos."), ("MUITOS SÓ DE MEIAS.", "muitos só de meias."), ("SEM CASACOS.", "sem casacos.")]),
 ("l4", [("OS CORPOS", "os corpos"), ("ESPALHADOS PELA NEVE,", "estavam espalhados pela neve,"), ("A MAIS DE UM QUILÔMETRO", "a mais de um quilômetro dali.")]),
 ("l5", [("COSTELAS", "alguns tinham costelas"), ("E CRÂNIOS ESMAGADOS.", "e crânios esmagados."), ("MAS NENHUM", "mas nenhum"), ("FERIMENTO POR FORA.", "ferimento por fora.")]),
 ("l6", [("UMA DAS VÍTIMAS", "uma das vítimas"), ("ESTAVA SEM A LÍNGUA.", "estava sem a língua."), ("E NAS ROUPAS,", "e nas roupas,"), ("OS PERITOS ACHARAM", "os peritos acharam"), ("TRAÇOS DE RADIAÇÃO.", "traços de radiação.")]),
 ("l7", [("A UNIÃO SOVIÉTICA", "a União Soviética"), ("FECHOU O CASO", "fechou o caso com uma frase:"), ("UMA FORÇA NATURAL", "uma força natural"), ("IRRESISTÍVEL.", "irresistível.")]),
 ("l8", [("EM 2020,", "em dois mil e vinte,"), ("A RÚSSIA CULPOU", "a Rússia culpou"), ("UMA AVALANCHE.", "uma avalanche."), ("MAS MUITA GENTE", "mas muita gente"), ("AINDA NÃO ACREDITA.", "ainda não acredita.")]),
 ("l9", [("AMANHÃ,", "amanhã,"), ("VOCÊ DECIDE.", "você decide."), ("A: ELISA LAM,", "A: o mistério de Elisa Lam,"), ("NO HOTEL CECIL.", "no Hotel Cecil."), ("OU B:", "ou B:"), ("O HOMEM DE SOMERTON,", "o Homem de Somerton,"), ("E O BILHETE NO BOLSO.", "e o bilhete escondido no bolso.")]),
 ("l10", [("COMENTA A OU B!", "comenta A ou B.")]),
]


def wt(s):
    return len(s) + (6 if s.rstrip()[-1] in ".:!" else 3 if s.rstrip()[-1] == "," else 0)


cap_html, cap_js, gi = [], [], 0
lids = [l["id"] for l in T["lines"]]
for lid, groups in G:
    WS = T["words"][lid]
    assert sum(len(sp.split()) for _, sp in groups) == len(WS), lid
    nxt_line = L[lids[lids.index(lid) + 1]]["start"] if lid != lids[-1] else TOTAL
    k = 0
    for gix, (disp, sp) in enumerate(groups):
        n = len(sp.split()); gw = WS[k:k + n]; k += n
        a = round(max(gw[0][1] - 0.04, 0.15), 3)
        if gix < len(groups) - 1:
            b = round(WS[k][1] - 0.04, 3)
        else:
            b = round(min(gw[-1][2] + 0.35, nxt_line - 0.04), 3)
        if lid == lids[-1]:
            b = TOTAL
        words = disp.split()
        spans = "".join(f'<span class="w" id="c{gi}w{j}">{w}</span> ' for j, w in enumerate(words))
        cap_html.append(f'<div id="c{gi}" class="cg">{spans.strip()}</div>')
        cap_js.append(f'tl.fromTo("#c{gi}", {{ opacity: 0, scale: 0.85, visibility: "visible" }}, {{ opacity: 1, scale: 1, duration: 0.1, ease: "power4.out" }}, {a});')
        if len(words) == n:
            ts = [w[1] for w in gw]
        else:
            ww = [len(w) + 2 for w in words]; span = gw[-1][2] - gw[0][1]; ts = []; c = gw[0][1]
            for x in ww:
                ts.append(c); c += span * x / sum(ww)
        for j in range(len(words)):
            cap_js.append(f'tl.fromTo("#c{gi}w{j}", {{ backgroundColor: "rgba(215,38,61,0)" }}, {{ backgroundColor: "rgba(215,38,61,1)", duration: 0.06 }}, {round(max(ts[j], a), 3)});')
            if j < len(words) - 1:
                cap_js.append(f'tl.to("#c{gi}w{j}", {{ backgroundColor: "rgba(215,38,61,0)", duration: 0.06 }}, {round(ts[j + 1], 3)});')
        cap_js.append(f'tl.to("#c{gi}", {{ opacity: 0, duration: 0.08, ease: "power2.in" }}, {round(b - 0.08, 3)});')
        cap_js.append(f'tl.set("#c{gi}", {{ opacity: 0, visibility: "hidden" }}, {round(b, 3)});')
        gi += 1

open("compositions/captions.html", "w").write(f"""<template>
  <style>
    #root {{ position:absolute; inset:0; pointer-events:none; }}
    .cg {{ position:absolute; left:120px; width:840px; top:1110px; text-align:center; opacity:0; visibility:hidden;
          font-family:'Oswald',sans-serif; font-weight:700; font-size:74px; line-height:1.15; color:#fff;
          text-shadow:0 4px 0 #000, 0 0 18px rgba(0,0,0,0.9); box-sizing:border-box; }}
    .w {{ padding:0 10px; border-radius:6px; }}
  </style>
  <div id="root" data-composition-id="captions" data-width="{W}" data-height="{H}">
    {chr(10).join(cap_html)}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join(cap_js)}
    window.__timelines["captions"] = tl;
  </script>
</template>
""")

# ---------- índice ----------
hosts = []
for i, s in enumerate(SCENES):
    a, d = slot[s]
    hosts.append(f'<div id="{s}" data-composition-id="{s}" data-composition-src="compositions/{s}.html" data-start="{a}" data-duration="{d}" data-track-index="1" data-track-kind="graphics" data-width="{W}" data-height="{H}" style="z-index:2"></div>')
voices = [f'<audio id="bed" class="clip" src="assets/music/ambience.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="4" data-volume="0.2"></audio>']
for l in T["lines"]:
    voices.append(f'<audio id="vo-{l["id"]}" class="clip" src="assets/voice-el/{l["id"]}.mp3" data-start="{l["start"]}" data-duration="{l["dur"]}" data-track-index="5" data-volume="1"></audio>')
# efeitos: (arquivo, tempo do pico desejado, volume)
SFX = [
    ("whoosh.mp3", slot["s2"][0], 0.5), ("impact-bass-1.mp3", WT("l2", 10), 0.7),
    ("whoosh-short.mp3", slot["s3"][0], 0.5), ("whoosh.mp3", slot["s4"][0], 0.45),
    ("whoosh-short.mp3", slot["s5"][0], 0.5), ("impact-bass-2.mp3", WT("l5", 7), 0.6),
    ("whoosh.mp3", slot["s6"][0], 0.45), ("glitch-1.mp3", WT("l6", 13), 0.35),
    ("whoosh-short.mp3", slot["s7"][0], 0.5), ("impact-bass-1.mp3", WT("l7", 12, 0.51), 0.7),
    ("whoosh.mp3", slot["s8"][0], 0.45), ("pop.mp3", WT("l8", 13), 0.5),
    ("impact-bass-2.mp3", WT("l1", 14), 0.6),
    ("whoosh-short.mp3", WT("l9", 3), 0.5), ("whoosh-short.mp3", WT("l9", 13), 0.5),
]
PEAK = json.load(open("peaks.json")) if os.path.exists("peaks.json") else {}
import subprocess
def fdur(f):
    return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"assets/sfx/{f}"]).decode())
sfx_html, lanes = [], []
for i, (f, t, v) in sorted(enumerate(SFX), key=lambda x: x[1][1]):
    st = max(0, round(t - PEAK.get(f, 0) + 1 / 30, 3)); d = round(fdur(f), 3)
    k = next((j for j, e in enumerate(lanes) if e <= st), None)
    if k is None: lanes.append(0); k = len(lanes) - 1
    lanes[k] = st + d
    sfx_html.append(f'<audio id="fx{i}" class="clip" src="assets/sfx/{f}" data-start="{st}" data-duration="{d}" data-track-index="{6 + k}" data-volume="{v}"></audio>')

open("index.html", "w").write(f"""<!doctype html>
<html>
  <head><meta charset="utf-8"><meta name="viewport" content="width=1080, height=1920" />
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
  <title>Amanhã Você Decide · EP.01 · Passo Dyatlov</title>
  <style> * {{ margin:0; padding:0; box-sizing:border-box; }} html,body {{ margin:0; width:1080px; height:1920px; overflow:hidden; background:#070708; }} #bg {{ position:absolute; inset:0; background:#070708; }} </style></head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="{W}" data-height="{H}">
      <div id="bg"></div>
      {chr(10).join('      ' + h for h in hosts).strip()}
      <div id="atmos" data-composition-id="atmos" data-composition-src="compositions/atmos.html" data-start="0" data-duration="{TOTAL}" data-track-index="2" data-track-kind="graphics" data-width="{W}" data-height="{H}" style="z-index:5"></div>
      <div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{TOTAL}" data-track-index="3" data-track-kind="captions" data-width="{W}" data-height="{H}" style="z-index:10"></div>
      {chr(10).join('      ' + v for v in voices).strip()}
      {chr(10).join('      ' + s for s in sfx_html).strip()}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
""")
print("ok", slot)
