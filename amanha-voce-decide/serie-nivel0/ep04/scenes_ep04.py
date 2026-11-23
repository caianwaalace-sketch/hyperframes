# NÍVEL 0 · EP.04: A marca. Incluído por build.py. Cenário muda de cor (camada .tint).
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

# caçador líder, em close: silhueta + pulso erguido com a marca
LEADER_MARK = ('<g id="lm-mark"><path d="M-30 -10 L-6 24 L18 -14 L34 18" stroke="#ff2a2a" stroke-width="10" fill="none" stroke-linecap="round"/>'
               '<circle cx="2" cy="4" r="46" fill="none" stroke="#ff2a2a" stroke-width="5" opacity="0.6"/></g>')


def leader_close():
    return (f'<g transform="translate(540 1200) scale(2.2)">'
            f'<path d="M-180 420 L-150 -200 Q0 -280 150 -200 L180 420 Z" fill="#050505"/>'
            f'<circle cx="0" cy="-330" r="110" fill="#050505"/>'
            f'<circle cx="-34" cy="-340" r="12" fill="#ff2a2a" class="hu-lan"/><circle cx="34" cy="-340" r="12" fill="#ff2a2a" class="hu-lan"/>'
            f'<g id="lm-arm" transform="translate(180 60)">{LEADER_MARK}</g>'
            f'</g>')


def headlights(pid):
    return (f'<svg id="{pid}" data-layout-ignore viewBox="0 0 1080 1920" class="fig" style="position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible">'
            f'<g id="{pid}-l" transform="translate(900 1180)"><circle r="12" fill="#f2f0e6"/><circle r="32" fill="#f2f0e6" opacity="0.35" filter="url(#blur18)"/></g>'
            f'<g id="{pid}-r" transform="translate(960 1180)"><circle r="12" fill="#f2f0e6"/><circle r="32" fill="#f2f0e6" opacity="0.35" filter="url(#blur18)"/></g>'
            f'</svg>')


# ---------- S1: a caminhonete bate no chão, olhos voltam ao normal, caçadores fecham o círculo ----------
scene("s1", CSS + """
""", f"""
      {layers("s1", highway("s1-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s1-truck" transform="translate(540 1500) scale(1.3)">{TRUCK}
          <g transform="translate(-260 -260) scale(0.55)">{teo("t1", "medo", glow=True, level="99", level_color="#5CE1E6", tag=False, power=True)}</g>
          <g transform="translate(-120 -260) scale(0.52)">{lia("l1", "medo")}</g>
        </g>
        <g id="s1-hunt">{HUNTERS}</g>
      </svg>
""", tint("s1", ["#5CE1E6", "#3a0a12", "#1d1416"], 7) + """
    tl.fromTo("#s1-truck", { y: -70 }, { y: 0, duration: 0.35, ease: "power3.in" }, 0.05);
    tl.to(".t1-pw", { opacity: 0, duration: 0.3 }, 0.35);
    tl.fromTo("#s1-hunt", { x: 220 }, { x: 0, duration: 2.6, ease: "power1.in" }, @l1:14@);
    tl.fromTo(".hu-lan", { opacity: 0.3 }, { opacity: 1, duration: 0.25, yoyo: true, repeat: 12, ease: "sine.inOut" }, 0);
""")

# ---------- S2: vocês escolheram B ----------
scene("s2", CSS + """
    #s2-b { position:absolute; left:390px; top:380px; width:300px; height:300px; background:#9b1b2b; color:#fff; font-size:260px; font-weight:700; text-align:center; line-height:300px; border:8px solid #E8E4DA; }
""", f"""
      {layers("s2", highway("s2-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 1500) scale(1.3)">{TRUCK}
          <g transform="translate(-260 -260) scale(0.55)">{teo("t2", "medo", glow=True, level="99", level_color="#5CE1E6", tag=False)}</g>
          <g transform="translate(-120 -260) scale(0.52)">{lia("l2", "medo")}</g>
        </g>
      </svg>
      <div id="s2-b">B</div>
""", tint("s2", ["#1d1416", "#9b1b2b", "#1d1416"], 4) + """
    tl.fromTo("#s2-b", { opacity: 0, scale: 2.2, rotation: 10 }, { opacity: 1, scale: 1, rotation: 4, duration: 0.25, ease: "power4.in" }, @l2:2@);
""")

# ---------- S3: o caçador líder, última chance ----------
scene("s3", CSS + """
    #s3-q { top:1480px; font-size:76px; line-height:1.15; }
""", f"""
      {layers("s3", highway("s3-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s3-lead">{leader_close()}</g>
      </svg>
      <div id="s3-q" class="big">"ÚLTIMA CHANCE.<br><span class="red">ENTREGA A LUVA.</span>"</div>
""", tint("s3", ["#1d1416", "#3a0a12"], 4.5) + """
    tl.fromTo("#s3-q", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l3:3@);
    tl.fromTo(".hu-lan", { opacity: 0.3 }, { opacity: 1, duration: 0.25, yoyo: true, repeat: 9, ease: "sine.inOut" }, 0);
""")

# ---------- S4: a menina se põe na frente ----------
scene("s4", CSS + """
""", f"""
      {layers("s4", highway("s4-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(700 1700) scale(1.3)">{lia("l4a", "medo", arm_out=True)}</g>
        <g transform="translate(380 1750) scale(0.95)">{teo("t4", "medo", glow=True, level="99", level_color="#5CE1E6", tag=False)}</g>
      </svg>
""", tint("s4", ["#D7263D", "#9b1b2b"], 5) + """
    tl.fromTo("#s4-cam", { x: -40 }, { x: 0, duration: 0.3, ease: "power2.out" }, 0.05);
""")

# ---------- S5: o caçador ri atrás da sombra ----------
scene("s5", CSS + """
    #s5-q { top:1480px; font-size:74px; line-height:1.15; }
""", f"""
      {layers("s5", highway("s5-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s5-hunt">{HUNTERS}</g>
      </svg>
      <div id="s5-q" class="big">"SÓ CUMPRIMOS <span class="red">ORDEM.</span>"</div>
""", tint("s5", ["#3a0a12", "#1d1416"], 4.5) + """
    tl.fromTo("#s5-q", { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power4.out" }, @l5:7@);
    tl.fromTo(".hu-lan", { opacity: 0.3 }, { opacity: 1, duration: 0.25, yoyo: true, repeat: 8, ease: "sine.inOut" }, 0);
""")

# ---------- S6: ordem de quem? (close no Téo) ----------
scene("s6", CSS + """
""", f"""
      {layers("s6", highway("s6-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g id="s6-z"><g transform="translate(540 2820) scale(2.4)">{teo("t6", "decidido", glow=True, level="99", level_color="#5CE1E6")}</g></g></svg>
""", tint("s6", ["#1d1416", "#2E9BFF", "#1d1416"], 3.2) + """
    tl.fromTo("#s6-z", { scale: 1, transformOrigin: "50% 40%" }, { scale: 1.08, duration: D, ease: "none" }, 0);
""")

# ---------- S7: o pulso erguido, a marca riscada ----------
scene("s7", CSS + """
    #s7-q { top:1500px; font-size:70px; line-height:1.15; }
""", f"""
      {layers("s7", highway("s7-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s7-arm" transform="translate(540 1300) scale(3)">{LEADER_MARK}</g>
      </svg>
      <div id="s7-q" class="big">"ISSO NÃO É <span class="red">DA SUA CONTA.</span>"</div>
""", tint("s7", ["#9b1b2b", "#D7263D", "#9b1b2b"], 5.6) + """
    tl.fromTo("#s7-arm", { scale: 1.5, opacity: 0 }, { scale: 3, opacity: 1, duration: 0.5, ease: "power3.out" }, 0.05);
    tl.fromTo("#s7-q", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l7:8@);
""")

# ---------- S8: close na menina, pálida ----------
scene("s8", CSS + """
""", f"""
      {layers("s8", highway("s8-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g id="s8-z"><g transform="translate(540 2900) scale(2.6)">{lia("l8", "medo")}</g></g></svg>
""", tint("s8", ["#D7263D", "#5a189a", "#D7263D"], 4) + """
    tl.fromTo("#s8-z", { scale: 1, transformOrigin: "50% 40%" }, { scale: 1.1, duration: D, ease: "none" }, 0);
""")

# ---------- S9: ela sussurra pro Téo ----------
scene("s9", CSS + """
    #s9-q { top:1500px; font-size:60px; line-height:1.2; }
""", f"""
      {layers("s9", highway("s9-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(620 1760) scale(1.0)">{lia("l9", "medo")}</g>
        <g transform="translate(340 1770) scale(0.95)">{teo("t9", "medo", glow=True, level="99", level_color="#5CE1E6", tag=False)}</g>
      </svg>
      <div id="s9-q" class="big">"NÃO SÃO SÓ <span class="red">CAÇADORES</span> ATRÁS DE VOCÊ."</div>
""", tint("s9", ["#5a189a", "#1d3557"], 5.7) + """
    tl.fromTo("#s9-q", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l9:3@);
""")

# ---------- S10: duas luzes na curva ----------
scene("s10", CSS + """
""", f"""
      {layers("s10", highway("s10-bg"))}
      {headlights("s10-lights")}
""", tint("s10", ["#1d3557", "#0c0e1a"], 5.9) + """
    tl.fromTo("#s10-lights-l", { x: 60, scale: 0.2, opacity: 0 }, { x: -720, scale: 1, opacity: 1, duration: D, ease: "power1.in" }, @l10:3@);
    tl.fromTo("#s10-lights-r", { x: 60, scale: 0.2, opacity: 0 }, { x: -660, scale: 1, opacity: 1, duration: D, ease: "power1.in" }, @l10:3@);
""")

# ---------- S11: não precisa de farol ----------
scene("s11", CSS + """
    #s11-t { top:360px; font-size:76px; line-height:1.15; }
""", f"""
      {layers("s11", highway("s11-bg"))}
      {headlights("s11-lights")}
      <div id="s11-t" class="big">ESSE TIPO DE GENTE<br><span class="red">NÃO PRECISA DE FAROL.</span></div>
""", tint("s11", ["#0c0e1a", "#232946"], 4.3) + """
    tl.set("#s11-lights-l", { x: -720, scale: 1 }, 0);
    tl.set("#s11-lights-r", { x: -660, scale: 1 }, 0);
    tl.fromTo("#s11-t", { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power4.out" }, @l11:2@);
""")

# ---------- S12: a menina puxa o braço do Téo ----------
scene("s12", CSS + """
""", f"""
      {layers("s12", highway("s12-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s12-duo"><g transform="translate(700 1760) scale(1.0)">{lia("l12", "medo", arm_out=True)}</g>
        <g transform="translate(380 1760) scale(0.95)">{teo("t12", "medo", glow=True, level="99", level_color="#5CE1E6", tag=False)}</g></g>
      </svg>
""", tint("s12", ["#232946", "#9b1b2b"], 5.2) + """
    tl.fromTo("#s12-duo", { x: 0 }, { x: -30, duration: 0.4, yoyo: true, repeat: 3, ease: "power1.inOut" }, @l12:3@);
""")

# ---------- S13: a escolha ----------
scene("s13", CSS + """
    #s13-k { top:330px; font-size:40px; color:#8FA3B0; }
    #s13-t { top:395px; font-size:72px; font-weight:700; line-height:1.1; }
    .s13-card { position:absolute; left:130px; width:820px; height:260px; border:4px solid #E8E4DA; background:#111318; box-sizing:border-box; }
    #s13-A { top:530px; } #s13-B { top:820px; }
    .s13-let { position:absolute; left:0; top:0; width:170px; height:252px; background:#D7263D; color:#fff; font-size:170px; font-weight:700; text-align:center; line-height:252px; }
    .s13-txt { position:absolute; left:200px; top:36px; width:590px; }
    .s13-txt b { display:block; font-size:44px; line-height:1.15; }
    .s13-txt span { display:block; margin-top:14px; font-size:30px; color:#8FA3B0; }
    #s13-bar { position:absolute; left:130px; top:1100px; width:820px; height:8px; background:#D7263D; transform-origin:0 50%; }
""", f"""
      {layers("s13", highway("s13-bg"))}
      <div id="s13-k" class="center mono">NÍVEL 0 · EP.05 · VOCÊ DECIDE</div>
      <div id="s13-t" class="center">O QUE ELES <span class="red">FAZEM?</span></div>
      <div id="s13-A" class="s13-card"><div class="s13-let">A</div><div class="s13-txt"><b>ENTREGA A LUVA</b><span class="mono">PROS CAÇADORES, PRA GANHAR TEMPO</span></div></div>
      <div id="s13-B" class="s13-card"><div class="s13-let">B</div><div class="s13-txt"><b>FOGE PRO MATO</b><span class="mono">ANTES DO CARRO CHEGAR</span></div></div>
      <div id="s13-bar"></div>
""", tint("s13", ["#9b1b2b", "#232946", "#5a189a"], 15.1) + """
    tl.fromTo("#s13-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.1);
    tl.fromTo("#s13-t", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.15);
    tl.fromTo("#s13-A", { opacity: 0, x: -1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l13:3@);
    tl.fromTo("#s13-B", { opacity: 0, x: 1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l13:19@);
    tl.fromTo("#s13-A", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 10, ease: "sine.inOut", immediateRender: false }, @l14:0@);
    tl.fromTo("#s13-B", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 10, ease: "sine.inOut", immediateRender: false }, @l14:0+0.25@);
    tl.fromTo("#s13-bar", { scaleX: 0 }, { scaleX: 1, duration: 5.5, ease: "none" }, @l14:0+0.5@);
""")
_p = "compositions/s13.html"
_c = open(_p).read()
open(_p, "w").write(_c.replace('tl.to("#s13-cam", { opacity: 0, duration: 0.14, ease: "power2.in" }, D - 0.16);', ""))

G_EP = [
 ("l1", [("A CAMINHONETE BATE", "A caminhonete bate"), ("NO CHÃO DE NOVO.", "no chão de novo."), ("OS OLHOS DO TÉO", "Os olhos do Téo"), ("VOLTAM AO CASTANHO,", "voltam ao castanho,"), ("A LUVA APAGA,", "a luva apaga,"), ("E OS TRÊS CAÇADORES", "e os três caçadores"), ("FECHAM O CÍRCULO.", "fecham o círculo.")]),
 ("l2", [("VOCÊS ESCOLHERAM B.", "Vocês escolheram B."), ("O TÉO ESCONDEU", "O Téo escondeu"), ("O PODER", "o poder"), ("E DEIXOU OS CAÇADORES", "e deixou os caçadores"), ("ALCANÇAREM ELES.", "alcançarem eles.")]),
 ("l3", [("O CAÇADOR MAIS ALTO", "O caçador mais alto"), ("LEVANTA A MÃO.", "levanta a mão."), ("ÚLTIMA CHANCE,", "Última chance,"), ("NÍVEL ZERO.", "nível zero."), ("ENTREGA A LUVA.", "Entrega a luva.")]),
 ("l4", [("A MENINA SE PÕE", "A menina se põe"), ("NA FRENTE DO TÉO.", "na frente do Téo."), ("ELE NEM SABE", "Ele nem sabe"), ("USAR ISSO DIREITO.", "usar isso direito."), ("DEIXA ELE EM PAZ.", "Deixa ele em paz.")]),
 ("l5", [("O CAÇADOR RI", "O caçador ri"), ("ATRÁS DA SOMBRA.", "atrás da sombra."), ("A GENTE NÃO DECIDE", "A gente não decide"), ("QUEM USA.", "quem usa."), ("SÓ CUMPRE ORDEM.", "Só cumpre ordem.")]),
 ("l6", [("O TÉO PERGUNTA:", "O Téo pergunta:"), ("ORDEM DE QUEM?", "ordem de quem?")]),
 ("l7", [("O CAÇADOR LEVANTA", "O caçador levanta"), ("O PULSO.", "o pulso."), ("UMA MARCA RISCADA,", "Uma marca riscada,"), ("QUEIMADA NA PELE.", "queimada na pele."), ("ISSO NÃO É", "Isso não é"), ("DA SUA CONTA.", "da sua conta.")]),
 ("l8", [("A MENINA TRAVA", "A menina trava"), ("O OLHAR NA MARCA.", "o olhar na marca."), ("O ROSTO DELA", "O rosto dela"), ("FICA PÁLIDO.", "fica pálido.")]),
 ("l9", [("ELA SUSSURRA", "Ela sussurra"), ("PRO TÉO:", "pro Téo:"), ("SE ESSA MARCA É REAL,", "se essa marca é real,"), ("NÃO SÃO SÓ CAÇADORES", "não são só caçadores"), ("ATRÁS DE VOCÊ.", "atrás de você.")]),
 ("l10", [("ATRÁS DO CAÇADOR,", "Atrás do caçador,"), ("DUAS LUZES APARECEM", "duas luzes aparecem"), ("NA CURVA DA ESTRADA.", "na curva da estrada."), ("BEM MAIS DEVAGAR.", "Bem mais devagar."), ("BEM MAIS QUIETAS.", "Bem mais quietas.")]),
 ("l11", [("NÃO PARECE CARRO", "Não parece carro"), ("DE CAÇADOR.", "de caçador."), ("ESSE TIPO DE GENTE", "Esse tipo de gente"), ("NÃO PRECISA DE FAROL.", "não precisa de farol.")]),
 ("l12", [("A MENINA PUXA", "A menina puxa"), ("O BRAÇO DO TÉO", "o braço do Téo"), ("COM FORÇA.", "com força."), ("ESSE CARRO", "Esse carro"), ("NÃO É DELES.", "não é deles."), ("PODE SER COISA PIOR.", "Pode ser coisa pior.")]),
 ("l13", [("AMANHÃ,", "Amanhã,"), ("VOCÊ DECIDE.", "você decide."), ("A: O TÉO ENTREGA", "A: o Téo entrega"), ("A LUVA PROS CAÇADORES,", "a luva pros caçadores,"), ("PRA GANHAR TEMPO.", "pra ganhar tempo."), ("OU B:", "Ou B:"), ("ELE FOGE PRO MATO", "ele foge pro mato"), ("ANTES DO CARRO CHEGAR.", "antes do carro chegar.")]),
 ("l14", [("COMENTA A OU B.", "Comenta A ou B."), ("E ME SEGUE", "E me segue"), ("PRA NÃO PERDER", "pra não perder"), ("A PARTE 5!", "a parte cinco!")]),
]
SFX_EP = [
    ("impact-bass-1.mp3", slot["s1"][0] + 0.05, 0.6), ("glitch-2.mp3", WT("l1", 10), 0.35),
    ("whoosh.mp3", slot["s2"][0], 0.4),
    ("impact-bass-1.mp3", WT("l3", 7), 0.45),
    ("whoosh-short.mp3", slot["s4"][0], 0.35),
    ("glitch-1.mp3", WT("l5", 6), 0.3),
    ("whoosh-short.mp3", slot["s6"][0], 0.35),
    ("impact-bass-2.mp3", WT("l7", 2), 0.55),
    ("glitch-2.mp3", slot["s8"][0], 0.3),
    ("whoosh.mp3", slot["s10"][0] + 0.2, 0.4),
    ("riser.mp3", slot["s11"][0], 0.4),
    ("impact-bass-1.mp3", WT("l12", 2), 0.45),
    ("whoosh-short.mp3", WT("l13", 3), 0.5), ("whoosh-short.mp3", WT("l13", 19), 0.5),
]
