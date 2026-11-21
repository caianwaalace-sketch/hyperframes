#!/usr/bin/env python3
"""Gera o episódio (index.html + compositions/*) a partir do roteiro e dos tempos da narração."""
import json, os, random, re
import sys

W, H = 1080, 1920
T = json.load(open("timing.json"))
L = {l["id"]: l for l in T["lines"]}
last = T["lines"][-1]
TOTAL = float(sys.argv[1]) if len(sys.argv) > 1 else round(last["start"] + last["dur"] + 0.4, 2)
os.makedirs("compositions", exist_ok=True)

# ---------- cenas (host start/dur) ----------
_ids = [l["id"] for l in T["lines"]][:-1]
starts = [L[k]["start"] for k in _ids]
starts[0] = 0
ends = starts[1:] + [TOTAL]
SCENES = [f"s{i+1}" for i in range(len(_ids))]
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


exec(open("scenes_ep03-insta.py", encoding="utf-8").read())

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
    #at-badge {{ position:absolute; left:140px; width:800px; top:110px; text-align:center; font-family:'Space Mono',monospace; font-size:28px; letter-spacing:0.3em; color:#D7263D; text-shadow:0 2px 6px rgba(0,0,0,0.9); }}
  </style>
  <div id="root" data-composition-id="atmos" data-width="{W}" data-height="{H}">
    {''.join(flakes)}
    <div id="at-vig" data-layout-ignore></div>
    <div id="at-badge">● NÍVEL 0 · EP.03</div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join(fjs)}
    tl.to("#at-badge", {{ opacity: 0, duration: 0.3 }}, {slot[SCENES[-1]][0]});
    window.__timelines["atmos"] = tl;
  </script>
</template>
""")

# ---------- legendas ----------
G = G_EP


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
        if lid == lids[-1] and gix == len(groups) - 1:
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
    .cg {{ position:absolute; left:120px; width:840px; top:1430px; text-align:center; opacity:0; visibility:hidden;
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
SFX = SFX_EP
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
  <title>Nível 0 · EP.03 (Insta) · O confronto</title>
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
print("ok TOTAL=", TOTAL, slot)
