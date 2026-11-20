# NÍVEL 0 · EP.02: A menina de capuz vermelho. Incluído por build.py. Cenário muda de cor (camada .tint).
from bg import street, cellar, CRATE
from teo import teo, teo_back, DEFS
from lia import lia
INV = SHRUG = ""

CSS = """
    .bg { position:absolute; left:0; top:0; width:1080px; height:1920px; }
    .fig { position:absolute; left:0; top:0; width:1080px; height:1920px; overflow:visible; }
    .tint { position:absolute; inset:0; mix-blend-mode:color; opacity:0.75; }
    .tint2 { position:absolute; inset:0; mix-blend-mode:soft-light; opacity:0.5; }
    .big { position:absolute; left:110px; width:860px; text-align:center; font-weight:700; }
"""


def tint(sid, colors, dur, start=0.0, extra=""):
    """Gera tweens que passam o cenário por uma sequência de cores."""
    js = f'    tl.fromTo("#{sid}-tint", {{ backgroundColor: "{colors[0]}" }}, {{ backgroundColor: "{colors[0]}", duration: 0.01 }}, 0);\n'
    step = dur / max(1, len(colors) - 1)
    for i, c in enumerate(colors[1:]):
        js += f'    tl.to("#{sid}-tint", {{ backgroundColor: "{c}", duration: {step:.2f}, ease: "sine.inOut" }}, {start + i * step:.2f});\n'
    return js + extra


def layers(sid, bg):
    return f'{bg}<div id="{sid}-tint" class="tint"></div>'


# ---------- S1: recap + "no final você decide" ----------
scene("s1", CSS + """
    #s1-t { top:400px; font-size:150px; line-height:0.95; }
    #s1-k { top:340px; font-size:44px; color:#5CE1E6; }
    #s1-dec { top:1000px; font-size:64px; color:#E8E4DA; background:#D7263D; padding:8px 0; }
""", f"""
      {layers("s1", cellar("s1-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g transform="translate(540 1760) scale(1.1)">{teo("t1", "decidido", glow=True, level="99", level_color="#5CE1E6")}</g></svg>
      <div id="s1-k" class="big mono">ONTEM…</div>
      <div id="s1-dec" class="big">NO FINAL, VOCÊ DECIDE</div>
""", tint("s1", ["#1d6f8a", "#2E9BFF", "#1d6f8a"], 6) + """
    tl.fromTo("#t1-lvlt", { opacity: 1 }, { opacity: 0.3, duration: 0.1, yoyo: true, repeat: 5, ease: "none" }, @l1:15@);
    tl.fromTo("#t1-glow", { scale: 1, transformOrigin: "50% 50%" }, { scale: 1.8, duration: 0.4, yoyo: true, repeat: 3, ease: "sine.inOut" }, @l1:5@);
    tl.fromTo("#s1-dec", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power4.out" }, @l1:21@);
    tl.fromTo("#s1-k", { opacity: 1 }, { opacity: 0, duration: 0.3, immediateRender: false }, @l1:20@);
""")

# ---------- S2: vocês escolheram B ----------
STAIRS = "".join(f'<rect x="{180 + i*90}" y="{1700 - i*110}" width="360" height="30" fill="#4a3424" stroke="#1a1410" stroke-width="5"/>' for i in range(10))
scene("s2", CSS + """
    #s2-b { position:absolute; left:390px; top:380px; width:300px; height:300px; background:#D7263D; color:#fff; font-size:260px; font-weight:700; text-align:center; line-height:300px; border:8px solid #E8E4DA; }
""", f"""
      {layers("s2", cellar("s2-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{STAIRS}<g id="s2-climb"><g transform="translate(420 1700) scale(0.9)">{teo_back("t2b")}</g></g></svg>
      <div id="s2-b">B</div>
""", tint("s2", ["#6b1d2a", "#D7263D", "#6b1d2a"], 3) + """
    tl.fromTo("#s2-b", { opacity: 0, scale: 2.2, rotation: -10 }, { opacity: 1, scale: 1, rotation: -4, duration: 0.25, ease: "power4.in" }, @l2:2@);
    tl.fromTo("#s2-climb", { x: 0, y: 0 }, { x: 270, y: -330, duration: 2.2, ease: "power1.inOut" }, @l2:3@);
    tl.fromTo("#s2-climb", { rotation: -2, transformOrigin: "50% 100%" }, { rotation: 2, duration: 0.25, yoyo: true, repeat: 8, ease: "sine.inOut", immediateRender: false }, @l2:3@);
""")

# ---------- S3: a porta e a luz que mudou de cor ----------
scene("s3", CSS + """
    #s3-door { position:absolute; left:330px; top:300px; width:420px; height:760px; background:#f2c46d; border:16px solid #2b1d14; box-shadow:0 0 120px #f2c46d; }
""", f"""
      {layers("s3", cellar("s3-bg"))}
      <div id="s3-door"></div>
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g transform="translate(540 1820) scale(1.25)">{teo_back("t3b")}</g></svg>
""", tint("s3", ["#3a2a1e", "#3a2a1e"], 1) + """
    tl.fromTo("#s3-door", { backgroundColor: "#f2c46d", boxShadow: "0 0 120px #f2c46d" }, { backgroundColor: "#a64dff", boxShadow: "0 0 160px #a64dff", duration: 1.2, ease: "sine.inOut" }, @l3:12@);
    tl.fromTo("#s3-door", { scaleX: 0.3, transformOrigin: "0% 50%" }, { scaleX: 1, duration: 0.8, ease: "power2.out", immediateRender: false }, @l3:6@);
""")

# ---------- S4: a cidade roxa ----------
scene("s4", CSS + """
""", f"""
      {layers("s4", street("s4-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g transform="translate(540 1720) scale(1.1)">{teo("t4", "medo", glow=True, level="99", level_color="#5CE1E6")}</g></svg>
""", tint("s4", ["#a64dff", "#7B2CBF", "#c03cff", "#5a189a", "#a64dff"], 5.5) + """
    tl.fromTo("#t4-head", { rotation: -8, transformOrigin: "50% 100%" }, { rotation: 8, duration: 1.2, yoyo: true, repeat: 2, ease: "sine.inOut" }, 0.3);
""")

# ---------- S5: a menina, nível 500 ----------
scene("s5", CSS + """
    #s5-500 { position:absolute; left:560px; top:330px; width:440px; text-align:center; font-size:56px; color:#E9C46A; font-weight:700; }
""", f"""
      {layers("s5", street("s5-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(300 1760) scale(1.0)">{teo("t5", "medo", glow=True, level="99", level_color="#5CE1E6")}</g>
        <g id="s5-lia"><g transform="translate(780 1700) scale(1.05)">{lia("l5", "neutro")}</g></g>
      </svg>
""", tint("s5", ["#7B2CBF", "#9b1b2b", "#D7263D", "#9b1b2b"], 7) + """
    tl.fromTo("#s5-lia", { opacity: 0, x: 200 }, { opacity: 1, x: 0, duration: 0.6, ease: "power3.out" }, @l5:6@);
    tl.fromTo("#l5-lvl", { scale: 0.3, opacity: 0, transformOrigin: "50% 50%" }, { scale: 1.3, opacity: 1, duration: 0.3, ease: "back.out(3)" }, @l5:24@);
    tl.to("#l5-lvl", { scale: 1, duration: 0.3 }, @l5:24+0.3@);
""")

# ---------- S6: "essa luva não é sua" (close na menina) ----------
scene("s6", CSS + """
    #s6-quote { top:340px; font-size:72px; line-height:1.1; color:#E8E4DA; }
""", f"""
      {layers("s6", street("s6-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g id="s6-z"><g transform="translate(540 2900) scale(2.6)">{lia("l6", "neutro")}</g></g></svg>
      <div id="s6-quote" class="big">"ELA <span class="red">TE ESCOLHEU</span>."</div>
""", tint("s6", ["#2E9BFF", "#1d3557", "#5CE1E6", "#2E9BFF"], 7) + """
    tl.fromTo("#s6-z", { scale: 1, transformOrigin: "50% 40%" }, { scale: 1.08, duration: D, ease: "none" }, 0);
    tl.fromTo("#s6-quote", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l6:16@);
""")

# ---------- S7: os sinos ----------
BELL = '<g><path d="M-80 60 Q-80 -60 0 -80 Q80 -60 80 60 L100 90 L-100 90 Z" fill="#c9a227" stroke="#1a1410" stroke-width="6"/><circle cx="0" cy="105" r="18" fill="#8a6d16" stroke="#1a1410" stroke-width="5"/><rect x="-10" y="-110" width="20" height="34" fill="#1a1410"/></g>'
scene("s7", CSS + """
    .s7-dong { position:absolute; left:110px; width:860px; text-align:center; font-size:110px; font-weight:700; color:#E9C46A; }
""", f"""
      {layers("s7", street("s7-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g transform="translate(540 560)"><g id="s7-bell">{BELL}</g></g></svg>
      <div class="s7-dong" id="s7-d1" style="top:780px">DONG</div>
      <div class="s7-dong" id="s7-d2" style="top:880px">DONG</div>
      <div class="s7-dong" id="s7-d3" style="top:980px">DONG</div>
""", tint("s7", ["#5a189a", "#5a189a"], 1) + """
    tl.fromTo("#s7-bell", { rotation: -25, svgOrigin: "0 -100" }, { rotation: 25, duration: 0.35, yoyo: true, repeat: 7, ease: "sine.inOut" }, @l7:7@);
    tl.fromTo("#s7-tint", { backgroundColor: "#5a189a" }, { backgroundColor: "#F4A261", duration: 0.12, yoyo: true, repeat: 1, immediateRender: false }, @l7:10@);
    tl.fromTo("#s7-d1", { opacity: 0, scale: 1.5 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.out" }, @l7:10@);
    tl.fromTo("#s7-d2", { opacity: 0, scale: 1.5 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.out" }, @l7:11@);
    tl.fromTo("#s7-d3", { opacity: 0, scale: 1.5 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.out" }, @l7:12@);
""")

# ---------- S8: caçadores de nível ----------
scene("s8", CSS + """
    #s8-t { top:340px; font-size:110px; line-height:1; color:#D7263D; }
""", f"""
      {layers("s8", street("s8-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g transform="translate(540 1760) scale(1.15)">{lia("l8", "neutro")}</g></svg>
      <div id="s8-t" class="big">CAÇADORES<br>DE NÍVEL</div>
""", tint("s8", ["#9b1b2b", "#3a0a12", "#D7263D", "#3a0a12"], 6) + """
    tl.to("#l8-x-neutro", { opacity: 0, duration: 0.15 }, @l8:2@);
    tl.fromTo("#l8-x-medo", { opacity: 0 }, { opacity: 1, duration: 0.15, immediateRender: false }, @l8:2@);
    tl.fromTo("#s8-t", { opacity: 0, scale: 1.5 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power4.out" }, @l8:11@);
""")

# ---------- S9: sobe rápido demais ----------
LANTERNS = "".join(f'<g transform="translate({x} 1300)"><path d="M-50 0 L-40 -250 Q0 -290 40 -250 L50 0 Z" fill="#050505"/><circle cx="0" cy="-310" r="48" fill="#050505"/><circle class="s9-lan" cx="70" cy="-150" r="22" fill="#ff2a2a"/></g>' for x in (300, 540, 780))
scene("s9", CSS + """
    #s9-jump { position:absolute; left:110px; top:380px; width:860px; text-align:center; font-size:150px; font-weight:700; line-height:1; }
""", f"""
      {layers("s9", street("s9-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g id="s9-hunt">{LANTERNS}</g></svg>
      <div id="s9-jump"><span style="color:#D7263D">0</span> → <span style="color:#5CE1E6">99</span></div>
""", tint("s9", ["#3a0a12", "#D7263D", "#3a0a12", "#D7263D"], 6.5) + """
    tl.fromTo("#s9-hunt", { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.8, ease: "power2.out" }, @l9:0@);
    tl.fromTo(".s9-lan", { opacity: 0.4 }, { opacity: 1, duration: 0.3, yoyo: true, repeat: 9, ease: "sine.inOut" }, @l9:0@);
    tl.fromTo("#s9-jump", { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.5)" }, @l9:12@);
""")

# ---------- S10: vem comigo ----------
scene("s10", CSS + """
    #s10-t { top:350px; font-size:110px; color:#E8E4DA; }
""", f"""
      {layers("s10", street("s10-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(260 1760) scale(0.95)">{lia("l10", "neutro", arm_out=True)}</g>
        <g transform="translate(790 1760) scale(0.95)">{teo("t10", "medo", glow=True, level="99", level_color="#5CE1E6")}</g>
      </svg>
      <div id="s10-t" class="big">"VEM <span class="red">COMIGO</span>."</div>
""", tint("s10", ["#2A9D8F", "#1d6f8a", "#2A9D8F"], 3.5) + """
    tl.fromTo("#l10-armR", { scaleX: 0.3, svgOrigin: "70 -520" }, { scaleX: 1, svgOrigin: "70 -520", duration: 0.4, ease: "back.out(2)" }, @l10:1@);
    tl.fromTo("#s10-t", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.22, ease: "power4.out" }, @l10:4@);
""")

# ---------- S11: o poder acorda ----------
scene("s11", CSS + """
    #s11-flash { position:absolute; inset:0; background:#5CE1E6; }
""", f"""
      {layers("s11", street("s11-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s11-hunt" transform="translate(0 -360) scale(1)">{LANTERNS.replace("s9-lan", "s11-lan")}</g>
        <g id="s11-z"><g transform="translate(540 1820) scale(1.3)">{teo("t11", "decidido", glow=True, level="99", level_color="#5CE1E6")}</g></g>
      </svg>
      <div id="s11-flash"></div>
""", tint("s11", ["#1d3557", "#5CE1E6", "#1d3557", "#D7263D", "#5CE1E6"], 8) + """
    tl.fromTo("#t11-glow", { scale: 1, opacity: 0.4, transformOrigin: "50% 50%" }, { scale: 2.6, opacity: 1, duration: 0.6, ease: "power2.out" }, @l11:4@);
    tl.fromTo("#s11-z", { scale: 1, svgOrigin: "540 900" }, { scale: 1.9, svgOrigin: "540 900", duration: 0.6, ease: "power3.inOut" }, @l11:6@);
    tl.fromTo(".t11-pw", { opacity: 0 }, { opacity: 1, duration: 0.25 }, @l11:10@);
    tl.fromTo("#s11-flash", { opacity: 0 }, { opacity: 0.5, duration: 0.08, yoyo: true, repeat: 1, ease: "none" }, @l11:10@);
    tl.to("#s11-z", { scale: 1, duration: 0.6, ease: "power3.inOut" }, @l11:12@);
    tl.fromTo("#s11-hunt", { opacity: 0 }, { opacity: 1, duration: 0.8 }, @l11:17@);
    tl.fromTo(".s11-lan", { opacity: 0.3 }, { opacity: 1, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut" }, @l11:17@);
""")

# ---------- S12: a escolha ----------
scene("s12", CSS + """
    #s12-k { top:330px; font-size:40px; color:#8FA3B0; }
    #s12-t { top:395px; font-size:96px; font-weight:700; line-height:1; }
    .s12-card { position:absolute; left:130px; width:820px; height:260px; border:4px solid #E8E4DA; background:#111318; box-sizing:border-box; }
    #s12-A { top:510px; } #s12-B { top:800px; }
    .s12-let { position:absolute; left:0; top:0; width:170px; height:252px; background:#D7263D; color:#fff; font-size:170px; font-weight:700; text-align:center; line-height:252px; }
    .s12-txt { position:absolute; left:200px; top:46px; width:590px; }
    .s12-txt b { display:block; font-size:58px; line-height:1.05; }
    .s12-txt span { display:block; margin-top:14px; font-size:28px; color:#8FA3B0; }
    #s12-bar { position:absolute; left:130px; top:1080px; width:820px; height:8px; background:#D7263D; transform-origin:0 50%; }
""", f"""
      {layers("s12", street("s12-bg"))}
      <div id="s12-k" class="center mono">NÍVEL 0 · EP.03 · VOCÊ DECIDE</div>
      <div id="s12-t" class="center">O QUE O TÉO <span class="red">FAZ?</span></div>
      <div id="s12-A" class="s12-card"><div class="s12-let">A</div><div class="s12-txt"><b>FOGE COM A MENINA</b><span class="mono">CONFIA NELA</span></div></div>
      <div id="s12-B" class="s12-card"><div class="s12-let">B</div><div class="s12-txt"><b>ENFRENTA OS CAÇADORES</b><span class="mono">USA O PODER DA LUVA</span></div></div>
      <div id="s12-bar"></div>
""", tint("s12", ["#5a189a", "#D7263D", "#2E9BFF", "#5a189a"], 9) + """
    tl.fromTo("#s12-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.1);
    tl.fromTo("#s12-t", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.15);
    tl.fromTo("#s12-A", { opacity: 0, x: -1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l12:3@);
    tl.fromTo("#s12-B", { opacity: 0, x: 1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l12:14@);
    tl.fromTo("#s12-A", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l13:0@);
    tl.fromTo("#s12-B", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l13:0+0.25@);
    tl.fromTo("#s12-bar", { scaleX: 0 }, { scaleX: 1, duration: 3.5, ease: "none" }, @l13:0+0.5@);
""")
_p = "compositions/s12.html"
_c = open(_p).read()
open(_p, "w").write(_c.replace('tl.to("#s12-cam", { opacity: 0, duration: 0.14, ease: "power2.in" }, D - 0.16);', ""))

G_EP = [
 ("l1", [("ONTEM,", "Ontem,"), ("O TÉO ACHOU", "o Téo achou"), ("UMA LUVA AZUL", "uma luva azul"), ("NUM PORÃO,", "num porão,"), ("E O NÍVEL DELE", "e o nível dele"), ("PULOU DE 0", "pulou de zero"), ("PARA 99.", "para noventa e nove."), ("E NO FINAL", "E no final"), ("DESTE EPISÓDIO,", "deste episódio,"), ("VOCÊ DECIDE", "você decide"), ("O QUE ACONTECE.", "o que acontece.")]),
 ("l2", [("VOCÊS ESCOLHERAM B.", "Vocês escolheram B."), ("O TÉO", "O Téo"), ("SUBIU A ESCADA.", "subiu a escada.")]),
 ("l3", [("CADA DEGRAU RANGIA.", "Cada degrau rangia."), ("LÁ EM CIMA,", "Lá em cima,"), ("A PORTA ESTAVA ABERTA,", "a porta estava aberta,"), ("E A LUZ LÁ FORA", "e a luz lá fora"), ("TINHA MUDADO DE COR.", "tinha mudado de cor.")]),
 ("l4", [("A CIDADE INTEIRA", "A cidade inteira"), ("ESTAVA ROXA.", "estava roxa."), ("O CÉU, AS CASAS,", "O céu, as casas,"), ("ATÉ A LUA.", "até a lua.")]),
 ("l5", [("E PARADA NO TOPO", "E parada no topo"), ("DA ESCADA,", "da escada,"), ("UMA MENINA", "uma menina"), ("DE CAPUZ VERMELHO.", "de capuz vermelho."), ("EM CIMA DA CABEÇA DELA,", "Em cima da cabeça dela,"), ("UM NÍVEL QUE O TÉO", "um nível que o Téo"), ("NUNCA TINHA VISTO:", "nunca tinha visto:"), ("500.", "quinhentos.")]),
 ("l6", [("ELA OLHOU PARA A LUVA", "Ela olhou para a luva"), ("E DISSE:", "e disse:"), ("ESSA LUVA NÃO É SUA.", "essa luva não é sua."), ("ELA ESCOLHE O DONO.", "Ela escolhe o dono."), ("E ELA TE ESCOLHEU.", "E ela te escolheu.")]),
 ("l7", [("ANTES QUE ELE PERGUNTASSE", "Antes que ele perguntasse"), ("QUALQUER COISA,", "qualquer coisa,"), ("OS SINOS DA CIDADE", "os sinos da cidade"), ("TOCARAM.", "tocaram."), ("TRÊS VEZES.", "Três vezes.")]),
 ("l8", [("A MENINA", "A menina"), ("FICOU PÁLIDA.", "ficou pálida."), ("TRÊS SINOS", "Três sinos"), ("SIGNIFICAM UMA COISA SÓ:", "significam uma coisa só:"), ("OS CAÇADORES DE NÍVEL", "os caçadores de nível"), ("ESTÃO VINDO.", "estão vindo.")]),
 ("l9", [("ELES CAÇAM", "Eles caçam"), ("QUEM SOBE DE NÍVEL", "quem sobe de nível"), ("RÁPIDO DEMAIS.", "rápido demais."), ("E O TÉO TINHA PULADO", "E o Téo tinha pulado"), ("99 DE UMA VEZ.", "noventa e nove de uma vez.")]),
 ("l10", [("ELA ESTENDEU A MÃO.", "Ela estendeu a mão."), ("VEM COMIGO.", "Vem comigo."), ("AGORA.", "Agora.")]),
 ("l11", [("A LUVA COMEÇOU", "A luva começou"), ("A BRILHAR SOZINHA.", "a brilhar sozinha."), ("OS OLHOS DO TÉO", "Os olhos do Téo"), ("FICARAM AZUIS.", "ficaram azuis."), ("E NO FIM DA RUA,", "E no fim da rua,"), ("APARECERAM TRÊS SOMBRAS", "apareceram três sombras"), ("COM LANTERNAS VERMELHAS.", "com lanternas vermelhas.")]),
 ("l12", [("AMANHÃ,", "Amanhã,"), ("VOCÊ DECIDE.", "você decide."), ("A: O TÉO CONFIA", "A: o Téo confia"), ("NA MENINA", "na menina"), ("E FOGE COM ELA.", "e foge com ela."), ("OU B:", "Ou B:"), ("O TÉO FICA", "o Téo fica"), ("E USA O PODER DA LUVA", "e usa o poder da luva"), ("CONTRA OS CAÇADORES.", "contra os caçadores.")]),
 ("l13", [("COMENTA A OU B.", "Comenta A ou B."), ("ME SEGUE PRA NÃO PERDER", "E me segue pra não perder"), ("A PARTE 3!", "a parte três.")]),
]
SFX_EP = [
    ("glitch-1.mp3", WT("l1", 15), 0.25), ("impact-bass-2.mp3", WT("l1", 21), 0.5),
    ("whoosh.mp3", slot["s2"][0], 0.45), ("impact-bass-1.mp3", WT("l2", 2), 0.55),
    ("whoosh-short.mp3", slot["s3"][0], 0.45), ("whoosh.mp3", slot["s4"][0], 0.45),
    ("whoosh-short.mp3", WT("l5", 6), 0.45), ("impact-bass-2.mp3", WT("l5", 24), 0.6),
    ("whoosh.mp3", slot["s6"][0], 0.4),
    ("impact-bass-1.mp3", WT("l7", 10), 0.55), ("impact-bass-1.mp3", WT("l7", 11), 0.5), ("impact-bass-1.mp3", WT("l7", 12), 0.55),
    ("glitch-2.mp3", WT("l8", 11), 0.3), ("whoosh.mp3", slot["s9"][0], 0.45), ("pop.mp3", WT("l9", 12), 0.45),
    ("whoosh-short.mp3", slot["s10"][0], 0.45), ("impact-bass-2.mp3", WT("l11", 10), 0.6), ("glitch-1.mp3", WT("l11", 17), 0.3),
    ("whoosh-short.mp3", WT("l12", 3), 0.5), ("whoosh-short.mp3", WT("l12", 14), 0.5),
]
