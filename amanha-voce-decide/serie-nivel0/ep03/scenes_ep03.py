# NÍVEL 0 · EP.03: A estrada. Incluído por build.py. Cenário muda de cor (camada .tint).
from bg import street, cellar, highway, road_sign
from teo import teo, teo_back, DEFS
from lia import lia
from bonecos import boneco
INV = SHRUG = ""

CSS = """
    .bg { position:absolute; left:0; top:0; width:1080px; height:1920px; }
    .fig { position:absolute; left:0; top:0; width:1080px; height:1920px; overflow:visible; }
    .tint { position:absolute; inset:0; mix-blend-mode:color; opacity:0.75; }
    .big { position:absolute; left:110px; width:860px; text-align:center; font-weight:700; }
"""


def tint(sid, colors, dur, start=0.0):
    js = f'    tl.fromTo("#{sid}-tint", {{ backgroundColor: "{colors[0]}" }}, {{ backgroundColor: "{colors[0]}", duration: 0.01 }}, 0);\n'
    step = dur / max(1, len(colors) - 1)
    for i, c in enumerate(colors[1:]):
        js += f'    tl.to("#{sid}-tint", {{ backgroundColor: "{c}", duration: {step:.2f}, ease: "sine.inOut" }}, {start + i * step:.2f});\n'
    return js


def layers(sid, bg_svg):
    return f'{bg_svg}<div id="{sid}-tint" class="tint"></div>'


TRUCK = ('<g><path d="M-220 0 L220 0 L220 -140 L120 -140 L90 -220 L-220 -220 Z" fill="#8D99AE" stroke="#1a1410" stroke-width="6"/>'
         '<rect x="-190" y="-200" width="90" height="70" fill="#1d3557" stroke="#1a1410" stroke-width="5"/>'
         '<circle cx="-140" cy="10" r="38" fill="#111318" stroke="#1a1410" stroke-width="6"/><circle cx="130" cy="10" r="38" fill="#111318" stroke="#1a1410" stroke-width="6"/>'
         '<circle cx="-140" cy="10" r="14" fill="#8D99AE"/><circle cx="130" cy="10" r="14" fill="#8D99AE"/>'
         '<circle cx="200" cy="-170" r="10" fill="#f2c46d"/></g>')

HUNTERS = "".join(f'<g transform="translate({x} 1400)"><path d="M-50 0 L-40 -250 Q0 -290 40 -250 L50 0 Z" fill="#050505"/><circle cx="0" cy="-310" r="48" fill="#050505"/><circle class="hu-lan" cx="70" cy="-150" r="22" fill="#ff2a2a"/></g>' for x in (300, 540, 780))

# ---------- S1: recap + "você decide de novo" ----------
scene("s1", CSS + """
    #s1-t { top:400px; font-size:150px; line-height:0.95; }
    #s1-k { top:340px; font-size:44px; color:#5CE1E6; }
    #s1-dec { top:1000px; font-size:58px; color:#E8E4DA; background:#D7263D; padding:8px 0; }
""", f"""
      {layers("s1", cellar("s1-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(280 1760) scale(1.0)">{teo("t1", "decidido", glow=True, level="99", level_color="#5CE1E6")}</g>
        <g transform="translate(790 1760) scale(0.95)">{lia("l1", "neutro")}</g>
      </svg>
      <div id="s1-k" class="big mono">NO EPISÓDIO ANTERIOR…</div>
      <div id="s1-dec" class="big">VOCÊ DECIDE DE NOVO</div>
""", tint("s1", ["#5a189a", "#D7263D", "#5a189a"], 7) + """
    tl.fromTo("#s1-dec", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power4.out" }, @l1:21@);
    tl.fromTo("#s1-k", { opacity: 1 }, { opacity: 0, duration: 0.3, immediateRender: false }, @l1:20@);
""")

# ---------- S2: vocês escolheram A ----------
scene("s2", CSS + """
    #s2-a { position:absolute; left:390px; top:380px; width:300px; height:300px; background:#2A9D8F; color:#fff; font-size:260px; font-weight:700; text-align:center; line-height:300px; border:8px solid #E8E4DA; }
""", f"""
      {layers("s2", street("s2-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s2-run"><g transform="translate(300 1700) scale(0.95)">{teo_back("t2b")}</g><g transform="translate(500 1700) scale(0.9)">{lia("l2", "neutro")}</g></g>
      </svg>
      <div id="s2-a">A</div>
""", tint("s2", ["#1d6f8a", "#2A9D8F", "#1d6f8a"], 3) + """
    tl.fromTo("#s2-a", { opacity: 0, scale: 2.2, rotation: -10 }, { opacity: 1, scale: 1, rotation: -4, duration: 0.25, ease: "power4.in" }, @l2:2@);
    tl.fromTo("#s2-run", { x: 0 }, { x: 300, duration: 2.6, ease: "power1.inOut" }, @l2:3@);
""")

# ---------- S3: a placa de Pindamonhangaba ----------
scene("s3", CSS + """
""", f"""
      {layers("s3", highway("s3-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s3-sign" transform="translate(1250 1300) scale(1.1)">{road_sign("Pindamonhangaba", 12)}</g>
        <g transform="translate(360 1760) scale(0.95)">{teo("t3", "medo", glow=True, level="99", level_color="#5CE1E6")}</g>
        <g transform="translate(700 1760) scale(0.9)">{lia("l3", "neutro")}</g>
      </svg>
""", tint("s3", ["#1d3557", "#1d3557"], 1) + """
    tl.fromTo("#s3-sign", { x: 1250 }, { x: -280, duration: 2.6, ease: "power1.in" }, @l3:9@);
""")

# ---------- S4: fora da cidade dos níveis ----------
scene("s4", CSS + """
    #s4-t { top:340px; font-size:72px; line-height:1.15; color:#E8E4DA; }
""", f"""
      {layers("s4", highway("s4-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g id="s4-z"><g transform="translate(540 2900) scale(2.6)">{lia("l4", "neutro")}</g></g></svg>
      <div id="s4-t" class="big">"NINGUÉM VÊ<br><span class="red">O NÚMERO</span>."</div>
""", tint("s4", ["#2A9D8F", "#1d6f8a", "#2A9D8F"], 6) + """
    tl.fromTo("#s4-z", { scale: 1, transformOrigin: "50% 40%" }, { scale: 1.08, duration: D, ease: "none" }, 0);
    tl.fromTo("#s4-t", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l4:8@);
""")

# ---------- S5: a caminhonete, placa de Lorena ----------
scene("s5", CSS + """
""", f"""
      {layers("s5", highway("s5-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s5-truck" transform="translate(540 1500) scale(1.3)">{TRUCK}
          <g transform="translate(-260 -260) scale(0.55)">{teo("t5", "neutro", glow=True, level="99", level_color="#5CE1E6", tag=False)}</g>
          <g transform="translate(-120 -260) scale(0.52)">{lia("l5", "neutro")}</g>
        </g>
        <g id="s5-sign" transform="translate(1250 1250) scale(1.1)">{road_sign("Lorena", 32)}</g>
      </svg>
""", tint("s5", ["#5a189a", "#1d3557"], 5) + """
    tl.fromTo("#s5-truck", { x: -200 }, { x: 0, duration: 0.6, ease: "power2.out" }, 0.1);
    tl.fromTo("#s5-truck", { y: 0 }, { y: -6, duration: 0.12, yoyo: true, repeat: 30, ease: "sine.inOut" }, 0.1);
    tl.fromTo("#s5-sign", { x: 1250 }, { x: -280, duration: 2.2, ease: "power1.in" }, @l5:8@);
""")

# ---------- S6: quem é você? ----------
scene("s6", CSS + """
    #s6-q { top:360px; font-size:86px; line-height:1.15; }
""", f"""
      {layers("s6", highway("s6-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 1500) scale(1.3)">{TRUCK}
          <g transform="translate(-260 -260) scale(0.55)">{teo("t6", "decidido", glow=True, level="99", level_color="#5CE1E6", tag=False)}</g>
          <g transform="translate(-120 -260) scale(0.52)">{lia("l6", "neutro")}</g>
        </g>
      </svg>
      <div id="s6-q" class="big">"QUEM É <span class="red">VOCÊ?</span>"</div>
""", tint("s6", ["#1d3557", "#2E9BFF", "#1d3557"], 5) + """
    tl.fromTo("#s6-q", { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power4.out" }, @l6:3@);
""")

# ---------- S7: eu também já fui nível zero (close na menina) ----------
scene("s7", CSS + """
""", f"""
      {layers("s7", highway("s7-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g id="s7-z"><g transform="translate(540 2900) scale(2.6)">{lia("l7", "neutro")}</g></g></svg>
""", tint("s7", ["#D7263D", "#9b1b2b", "#D7263D"], 7) + """
    tl.fromTo("#s7-z", { scale: 1, transformOrigin: "50% 40%" }, { scale: 1.1, duration: D, ease: "none" }, 0);
""")

# ---------- S8: a caminhonete para, sombras na pista ----------
scene("s8", CSS + """
""", f"""
      {layers("s8", highway("s8-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s8-truck" transform="translate(540 1500) scale(1.3)">{TRUCK}</g>
        <g id="s8-hunt" opacity="0">{HUNTERS}</g>
      </svg>
""", tint("s8", ["#1d3557", "#3a0a12"], 6) + """
    tl.fromTo("#s8-truck", { x: 400 }, { x: 0, duration: 1.0, ease: "power3.out" }, 0.1);
    tl.fromTo("#s8-hunt", { opacity: 0 }, { opacity: 1, duration: 0.6 }, @l8:11@);
    tl.fromTo(".hu-lan", { opacity: 0.3 }, { opacity: 1, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut" }, @l8:11@);
""")

# ---------- S9: eles sentem o nível ----------
scene("s9", CSS + """
    #s9-t { top:360px; font-size:84px; line-height:1.15; }
""", f"""
      {layers("s9", highway("s9-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g id="s9-hunt">{HUNTERS}</g></svg>
      <div id="s9-t" class="big">SENTEM O <span class="red">NÍVEL</span><br>DE LONGE.</div>
""", tint("s9", ["#3a0a12", "#D7263D", "#3a0a12"], 4.5) + """
    tl.fromTo(".hu-lan", { opacity: 0.3 }, { opacity: 1, duration: 0.25, yoyo: true, repeat: 9, ease: "sine.inOut" }, 0);
    tl.fromTo("#s9-t", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l9:3@);
""")

# ---------- S10: a luva esquenta, olhos azuis ----------
scene("s10", CSS + """
""", f"""
      {layers("s10", highway("s10-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g id="s10-z"><g transform="translate(540 2820) scale(2.4)">{teo("t10", "decidido", glow=True, level="99", level_color="#5CE1E6")}</g></g></svg>
""", tint("s10", ["#2E9BFF", "#1d3557", "#5CE1E6"], 4.4) + """
    tl.fromTo("#t10-glow", { scale: 1, opacity: 0.4, transformOrigin: "50% 50%" }, { scale: 2.2, opacity: 1, duration: 0.5, ease: "power2.out" }, @l10:4@);
    tl.to("#t10-x-decidido", { opacity: 0, duration: 0.1 }, @l10:8@);
    tl.fromTo(".t10-pw", { opacity: 0 }, { opacity: 1, duration: 0.15, immediateRender: false }, @l10:8@);
""")

# ---------- S11: não usa o poder na estrada! ----------
scene("s11", CSS + """
    #s11-q { top:360px; font-size:78px; line-height:1.15; }
""", f"""
      {layers("s11", highway("s11-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 1500) scale(1.3)">{TRUCK}
          <g transform="translate(-260 -260) scale(0.55)">{teo("t11", "decidido", glow=True, level="99", level_color="#5CE1E6", tag=False)}</g>
          <g transform="translate(-120 -260) scale(0.52)">{lia("l11", "medo")}</g>
        </g>
      </svg>
      <div id="s11-q" class="big">"TEM GENTE <span class="red">VENDO!</span>"</div>
""", tint("s11", ["#D7263D", "#9b1b2b"], 3.5) + """
    tl.fromTo("#s11-q", { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.22, ease: "power4.out" }, @l11:2@);
""")

# ---------- S12: a caminhonete levanta do chão ----------
scene("s12", CSS + """
    #s12-flash { position:absolute; inset:0; background:#5CE1E6; }
""", f"""
      {layers("s12", highway("s12-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s12-glow"><ellipse cx="540" cy="1640" rx="320" ry="60" fill="#5CE1E6" opacity="0.5" filter="url(#blur18)"/></g>
        <g id="s12-truck" transform="translate(540 1500) scale(1.3)">{TRUCK}</g>
      </svg>
      <div id="s12-flash"></div>
""", tint("s12", ["#1d3557", "#5CE1E6", "#1d3557"], 3.3) + """
    tl.fromTo("#s12-flash", { opacity: 0 }, { opacity: 0.55, duration: 0.08, yoyo: true, repeat: 1, ease: "none" }, @l12:5@);
    tl.fromTo("#s12-truck", { y: 0 }, { y: -70, duration: 0.6, ease: "power2.out" }, @l12:5@);
    tl.fromTo("#s12-glow", { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1.3, duration: 0.6, ease: "power2.out", immediateRender: false }, @l12:5@);
    tl.fromTo("#s12-truck", { rotation: 0, svgOrigin: "540 1500" }, { rotation: 2, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut" }, @l12:5+0.3@);
""")

# ---------- S13: a escolha ----------
scene("s13", CSS + """
    #s13-k { top:330px; font-size:40px; color:#8FA3B0; }
    #s13-t { top:395px; font-size:84px; font-weight:700; line-height:1.1; }
    .s13-card { position:absolute; left:130px; width:820px; height:260px; border:4px solid #E8E4DA; background:#111318; box-sizing:border-box; }
    #s13-A { top:530px; } #s13-B { top:820px; }
    .s13-let { position:absolute; left:0; top:0; width:170px; height:252px; background:#D7263D; color:#fff; font-size:170px; font-weight:700; text-align:center; line-height:252px; }
    .s13-txt { position:absolute; left:200px; top:36px; width:590px; }
    .s13-txt b { display:block; font-size:50px; line-height:1.1; }
    .s13-txt span { display:block; margin-top:14px; font-size:26px; color:#8FA3B0; }
    #s13-bar { position:absolute; left:130px; top:1100px; width:820px; height:8px; background:#D7263D; transform-origin:0 50%; }
""", f"""
      {layers("s13", highway("s13-bg"))}
      <div id="s13-k" class="center mono">NÍVEL 0 · EP.04 · VOCÊ DECIDE</div>
      <div id="s13-t" class="center">O QUE O TÉO <span class="red">FAZ?</span></div>
      <div id="s13-A" class="s13-card"><div class="s13-let">A</div><div class="s13-txt"><b>SOLTA O PODER</b><span class="mono">ARRISCA MOSTRAR A VERDADE</span></div></div>
      <div id="s13-B" class="s13-card"><div class="s13-let">B</div><div class="s13-txt"><b>APAGA A LUVA</b><span class="mono">DEIXA OS CAÇADORES CHEGAREM</span></div></div>
      <div id="s13-bar"></div>
""", tint("s13", ["#5a189a", "#D7263D", "#2E9BFF", "#5a189a"], 9.5) + """
    tl.fromTo("#s13-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.1);
    tl.fromTo("#s13-t", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.15);
    tl.fromTo("#s13-A", { opacity: 0, x: -1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l13:3@);
    tl.fromTo("#s13-B", { opacity: 0, x: 1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l13:19@);
    tl.fromTo("#s13-A", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l14:0@);
    tl.fromTo("#s13-B", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l14:0+0.25@);
    tl.fromTo("#s13-bar", { scaleX: 0 }, { scaleX: 1, duration: 4, ease: "none" }, @l14:0+0.5@);
""")
_p = "compositions/s13.html"
_c = open(_p).read()
open(_p, "w").write(_c.replace('tl.to("#s13-cam", { opacity: 0, duration: 0.14, ease: "power2.in" }, D - 0.16);', ""))

G_EP = [
 ("l1", [("NO EPISÓDIO ANTERIOR,", "No episódio anterior,"), ("UMA MENINA", "uma menina"), ("DE NÍVEL 500", "de nível quinhentos"), ("DISSE QUE A LUVA", "disse que a luva"), ("ESCOLHEU O TÉO.", "escolheu o Téo."), ("E OS CAÇADORES DE NÍVEL", "E os caçadores de nível"), ("ESTAVAM VINDO.", "estavam vindo."), ("NO FINAL,", "No final,"), ("VOCÊ DECIDE DE NOVO.", "você decide de novo.")]),
 ("l2", [("VOCÊS ESCOLHERAM A.", "Vocês escolheram A."), ("O TÉO CONFIOU", "O Téo confiou"), ("NA MENINA,", "na menina,"), ("E OS DOIS FUGIRAM", "e os dois fugiram"), ("PELA CIDADE.", "pela cidade.")]),
 ("l3", [("ELES CORRERAM", "Eles correram"), ("POR BECOS ESCUROS", "por becos escuros"), ("ATÉ CHEGAR NUMA ESTRADA.", "até chegar numa estrada."), ("UMA PLACA VERDE,", "Uma placa verde,"), ("NA BEIRA DA PISTA:", "na beira da pista:"), ("PINDAMONHANGABA,", "Pindamonhangaba,"), ("12 KM.", "doze quilômetros.")]),
 ("l4", [("A MENINA DISSE:", "A menina disse:"), ("FORA DA CIDADE", "fora da cidade"), ("DOS NÍVEIS,", "dos níveis,"), ("NINGUÉM VÊ O NÚMERO", "ninguém vê o número"), ("EM CIMA DA SUA CABEÇA.", "em cima da sua cabeça.")]),
 ("l5", [("ELES PEGARAM", "Eles pegaram"), ("UMA CARONA", "uma carona"), ("NUMA CAMINHONETE.", "numa caminhonete."), ("DEPOIS DE PINDAMONHANGABA,", "Depois de Pindamonhangaba,"), ("A PRÓXIMA PLACA DIZIA:", "a próxima placa dizia:"), ("LORENA,", "Lorena,"), ("32 KM.", "trinta e dois quilômetros.")]),
 ("l6", [("O TÉO PERGUNTOU:", "O Téo perguntou:"), ("QUEM É VOCÊ?", "quem é você?"), ("POR QUE SEU NÍVEL", "Por que seu nível"), ("É TÃO ALTO?", "é tão alto?")]),
 ("l7", [("ELA RESPONDEU:", "Ela respondeu:"), ("EU TAMBÉM", "eu também"), ("JÁ FUI NÍVEL ZERO.", "já fui nível zero."), ("ESSA LUVA JÁ TEVE", "Essa luva já teve"), ("6 DONOS", "seis donos"), ("ANTES DE VOCÊ.", "antes de você."), ("EU FUI O QUINTO.", "Eu fui o quinto.")]),
 ("l8", [("PERTO DE LORENA,", "Perto de Lorena,"), ("O MOTORISTA DA CAMINHONETE", "o motorista da caminhonete"), ("PAROU DE REPENTE.", "parou de repente."), ("NA ESTRADA,", "Na estrada,"), ("TRÊS SOMBRAS", "três sombras"), ("BLOQUEAVAM A PISTA.", "bloqueavam a pista.")]),
 ("l9", [("OS CAÇADORES", "Os caçadores"), ("NÃO PRECISAM DE CARRO.", "não precisam de carro."), ("ELES SENTEM O NÍVEL", "Eles sentem o nível"), ("DE LONGE.", "de longe.")]),
 ("l10", [("A LUVA DO TÉO", "A luva do Téo"), ("COMEÇOU A ESQUENTAR.", "começou a esquentar."), ("OS OLHOS DELE", "Os olhos dele"), ("FICARAM AZUIS DE NOVO.", "ficaram azuis de novo.")]),
 ("l11", [("A MENINA GRITOU:", "A menina gritou:"), ("NÃO USA O PODER", "não usa o poder"), ("NA ESTRADA!", "na estrada!"), ("TEM GENTE NORMAL", "Tem gente normal"), ("VENDO!", "vendo!")]),
 ("l12", [("MAS ERA TARDE.", "Mas era tarde."), ("UM BRILHO AZUL", "Um brilho azul"), ("SAIU DA LUVA,", "saiu da luva,"), ("E A CAMINHONETE INTEIRA", "e a caminhonete inteira"), ("LEVANTOU 10 CM", "levantou dez centímetros"), ("DO CHÃO.", "do chão.")]),
 ("l13", [("AMANHÃ,", "Amanhã,"), ("VOCÊ DECIDE.", "você decide."), ("A: O TÉO SOLTA", "A: o Téo solta"), ("O PODER E ARRISCA", "o poder e arrisca"), ("MOSTRAR A VERDADE", "mostrar a verdade"), ("PARA O MUNDO NORMAL.", "para o mundo normal."), ("OU B:", "Ou B:"), ("ELE APAGA A LUVA", "ele apaga a luva"), ("E DEIXA OS CAÇADORES", "e deixa os caçadores"), ("ALCANÇAREM ELES.", "alcançarem eles.")]),
 ("l14", [("COMENTA A OU B.", "Comenta A ou B."), ("E ME SEGUE", "E me segue"), ("PRA PARTE 4!", "pra parte quatro.")]),
]
SFX_EP = [
    ("impact-bass-2.mp3", WT("l1", 20), 0.5),
    ("whoosh.mp3", slot["s2"][0], 0.45), ("impact-bass-1.mp3", WT("l2", 2), 0.55),
    ("whoosh-short.mp3", slot["s3"][0], 0.4),
    ("whoosh.mp3", slot["s4"][0], 0.4),
    ("whoosh-short.mp3", slot["s5"][0], 0.4), ("impact-bass-1.mp3", WT("l5", 12), 0.45),
    ("whoosh.mp3", slot["s6"][0], 0.35),
    ("impact-bass-1.mp3", WT("l8", 7), 0.55), ("glitch-2.mp3", WT("l8", 11), 0.3),
    ("glitch-1.mp3", WT("l9", 9), 0.3),
    ("impact-bass-2.mp3", WT("l10", 8), 0.55),
    ("whoosh-short.mp3", WT("l11", 2), 0.45),
    ("impact-bass-2.mp3", WT("l12", 5), 0.6), ("whoosh-cinematic.mp3", WT("l12", 9), 0.45),
    ("whoosh-short.mp3", WT("l13", 3), 0.5), ("whoosh-short.mp3", WT("l13", 19), 0.5),
]
