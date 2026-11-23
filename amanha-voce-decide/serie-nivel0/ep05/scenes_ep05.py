# NÍVEL 0 · EP.05: dentro do armazém. Incluído por build.py. Cenário muda de cor (camada .tint).
# Abertura direta (sem "no episódio anterior"): entram no armazém já na primeira cena.
from teo import teo, DEFS
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


def warehouse_in(pid):
    """Dentro do armazém: vigas, caixas no fundo, luzes industriais piscando no teto."""
    beams = "".join(f'<rect x="{x}" y="120" width="26" height="1800" fill="#14141a" stroke="#05050a" stroke-width="3"/>' for x in range(60, 1080, 220))
    lamps = "".join(f'<circle id="{pid}-l{i}" cx="{x}" cy="180" r="34" fill="#f2c46d" opacity="0.7"/>' for i, x in enumerate(range(150, 1080, 220)))
    crates = "".join(f'<rect x="{x}" y="{1600 - h}" width="150" height="{h}" fill="#5b3e24" stroke="#1a1410" stroke-width="5"/><path d="M{x} {1600 - h} L{x + 150} {1600}" stroke="#3b2a18" stroke-width="5"/>'
                      for x, h in [(40, 260), (210, 180), (780, 300), (930, 200)])
    return (f'<svg id="{pid}" class="bg" data-layout-ignore viewBox="0 0 1080 1920" preserveAspectRatio="xMidYMid slice">'
            f'<defs><linearGradient id="{pid}-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0a0f"/><stop offset="1" stop-color="#1a1820"/></linearGradient></defs>'
            f'<rect width="1080" height="1920" fill="url(#{pid}-sky)"/>'
            f'{beams}{lamps}'
            f'<rect y="1600" width="1080" height="320" fill="#0e0e12"/>{crates}</svg>')


def glove_wall(pid):
    """Parede com dezenas de luvas penduradas, cada uma com etiqueta."""
    gloves = []
    for i in range(18):
        x = 90 + (i % 6) * 170
        y = 300 + (i // 6) * 300
        gloves.append(f'<g id="{pid}-g{i}" transform="translate({x} {y})">'
                       f'<path d="M-24 -22 Q-30 18 -6 26 Q22 30 26 6 L22 -26 Z" fill="#8a8378" stroke="#1a1410" stroke-width="4"/>'
                       f'<rect x="-30" y="34" width="60" height="26" fill="#E8E4DA" stroke="#1a1410" stroke-width="3"/></g>')
    return f'<g id="{pid}">{"".join(gloves)}</g>'


LABEL_T = ('<g><rect x="-170" y="-110" width="340" height="220" fill="#E8E4DA" stroke="#1a1410" stroke-width="6" transform="rotate(-3)"/>'
           '<path d="M-110 -60 L110 -60 M-110 -20 L110 -20 M-110 20 L60 20 M-110 60 L80 60" stroke="#8a8378" stroke-width="6" transform="rotate(-3)"/></g>')

# o homem: silhueta parecida com o Téo, só mais velho (cabelo grisalho, jaqueta desbotada)
MAN = boneco("man", 0, 0, s=1.6, jacket="#4a5a3a", hat="", scarf="#8a7a3a", pants="#2b2f3a", hair="#9a9a9a", worried=False, eyes_closed=False)

# ---------- S1: a porta range, entram agora (abertura direta, sem recap) ----------
scene("s1", CSS + """
""", f"""
      {layers("s1", warehouse_in("s1-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(360 1760) scale(1.0)">{teo("t1", "medo", glow=True, level="99", level_color="#5CE1E6")}</g>
        <g transform="translate(730 1760) scale(0.95)">{lia("l1", "medo", arm_out=True)}</g>
      </svg>
""", tint("s1", ["#000000", "#1d3557", "#0a0a0f"], 5.0) + """
    tl.fromTo("#s1-bg-l0, #s1-bg-l2, #s1-bg-l4", { opacity: 0.1 }, { opacity: 0.7, duration: 0.3 }, 0.1);
    tl.fromTo("#s1-bg-l1, #s1-bg-l3", { opacity: 0.1 }, { opacity: 0.6, duration: 0.3 }, 0.3);
""")

# ---------- S2: vocês escolheram A ----------
scene("s2", CSS + """
    #s2-a { position:absolute; left:390px; top:380px; width:300px; height:300px; background:#2E9BFF; color:#fff; font-size:260px; font-weight:700; text-align:center; line-height:300px; border:8px solid #E8E4DA; }
""", f"""
      {layers("s2", warehouse_in("s2-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(360 1760) scale(0.95)">{teo("t2", "decidido", glow=True, level="99", level_color="#5CE1E6")}</g>
        <g transform="translate(730 1760) scale(0.9)">{lia("l2", "neutro")}</g>
      </svg>
      <div id="s2-a">A</div>
""", tint("s2", ["#0a0a0f", "#2E9BFF", "#0a0a0f"], 3.9) + """
    tl.fromTo("#s2-a", { opacity: 0, scale: 2.2, rotation: -10 }, { opacity: 1, scale: 1, rotation: -4, duration: 0.25, ease: "power4.in" }, @l2:2@);
""")

# ---------- S3: o celular vira lanterna, luzes no mesmo ritmo da luva ----------
scene("s3", CSS + """
""", f"""
      {layers("s3", warehouse_in("s3-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 1760) scale(1.1)">{lia("l3", "neutro", arm_out=True)}</g>
      </svg>
""", tint("s3", ["#0a0a0f", "#5CE1E6", "#0a0a0f"], 7.2) + """
    tl.fromTo("#s3-bg-l0, #s3-bg-l1, #s3-bg-l2, #s3-bg-l3, #s3-bg-l4", { opacity: 0.6 }, { opacity: 0.15, duration: 0.3, yoyo: true, repeat: 9, ease: "none" }, @l3:5@);
""")

# ---------- S4: parede de luvas ----------
scene("s4", CSS + """
""", f"""
      {layers("s4", warehouse_in("s4-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{glove_wall("s4-wall")}</svg>
""", tint("s4", ["#0a0a0f", "#5a189a"], 7.9) + """
    tl.fromTo("#s4-wall", { opacity: 0, scale: 0.9, transformOrigin: "50% 50%" }, { opacity: 1, scale: 1, duration: 0.6, ease: "power2.out" }, 0.1);
""")

# ---------- S5: cada luva tem etiqueta ----------
scene("s5", CSS + """
""", f"""
      {layers("s5", warehouse_in("s5-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g transform="translate(540 960) scale(1.5)">{LABEL_T}</g></svg>
""", tint("s5", ["#5a189a", "#1d3557"], 5.9) + """
    tl.fromTo("#s5-cam .fig", { opacity: 0, y: -40 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, 0.1);
""")

# ---------- S6: o Téo acha a luva dela, "quinto dono" ----------
scene("s6", CSS + """
    #s6-t { top:1500px; font-size:60px; line-height:1.15; color:#E9C46A; }
""", f"""
      {layers("s6", warehouse_in("s6-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g transform="translate(540 960) scale(1.6)">{LABEL_T}</g></svg>
      <div id="s6-t" class="big mono">"QUINTO DONO"</div>
""", tint("s6", ["#1d3557", "#9b1b2b"], 9.2) + """
    tl.fromTo("#s6-t", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.3, ease: "power4.out" }, @l6:5@);
""")

# ---------- S7: a voz do fundo ----------
scene("s7", CSS + """
    #s7-q { top:400px; font-size:76px; line-height:1.2; }
""", f"""
      {layers("s7", warehouse_in("s7-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(360 1760) scale(1.0)">{teo("t7", "medo", glow=True, level="99", level_color="#5CE1E6")}</g>
        <g transform="translate(730 1760) scale(0.95)">{lia("l7", "medo")}</g>
      </svg>
      <div id="s7-q" class="big">"VOCÊS NÃO DEVIAM<br>ESTAR AQUI."</div>
""", tint("s7", ["#1d3557", "#000000"], 5.9) + """
    tl.fromTo("#s7-q", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l7:4@);
    tl.fromTo("#s7-bg-l0, #s7-bg-l1, #s7-bg-l2, #s7-bg-l3, #s7-bg-l4", { opacity: 0.7 }, { opacity: 0, duration: 0.4 }, @l7:4@);
""")

# ---------- S8: o homem sai da escuridão, rosto parecido com o do Téo ----------
scene("s8", CSS + """
""", f"""
      {layers("s8", warehouse_in("s8-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g id="s8-man" opacity="0"><g transform="translate(540 1820) scale(1.6)">{MAN}</g></g></svg>
""", tint("s8", ["#000000", "#1d3557", "#000000"], 10.6) + """
    tl.fromTo("#s8-man", { opacity: 0 }, { opacity: 1, duration: 0.6, ease: "power2.out" }, 0.2);
""")

# ---------- S9: a menina recua, "isso não é possível" ----------
scene("s9", CSS + """
""", f"""
      {layers("s9", warehouse_in("s9-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g id="s9-z"><g transform="translate(540 2820) scale(2.3)">{lia("l9", "medo")}</g></g></svg>
""", tint("s9", ["#1d3557", "#2E9BFF", "#1d3557"], 7.9) + """
    tl.fromTo("#s9-z", { scale: 1, transformOrigin: "50% 45%" }, { scale: 1.08, duration: D, ease: "none" }, 0);
""")

# ---------- S10: "eu fui o primeiro dono" ----------
scene("s10", CSS + """
    #s10-q { top:380px; font-size:62px; line-height:1.2; }
""", f"""
      {layers("s10", warehouse_in("s10-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g transform="translate(540 1820) scale(1.6)">{MAN}</g></svg>
      <div id="s10-q" class="big">"ELA SEMPRE VOLTA<br><span class="red">PRA FAMÍLIA.</span>"</div>
""", tint("s10", ["#000000", "#9b1b2b"], 9.7) + """
    tl.fromTo("#s10-q", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l10:11@);
""")

# ---------- S11: a luva esquenta, olhos azuis de novo (close) ----------
scene("s11", CSS + """
""", f"""
      {layers("s11", warehouse_in("s11-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g id="s11-z"><g transform="translate(540 2820) scale(2.4)">{teo("t11", "decidido", glow=True, level="99", level_color="#5CE1E6")}</g></g></svg>
""", tint("s11", ["#9b1b2b", "#2E9BFF", "#5CE1E6"], 9.4) + """
    tl.fromTo("#s11-z", { scale: 1, transformOrigin: "50% 40%" }, { scale: 1.08, duration: D, ease: "none" }, 0);
    tl.fromTo("#t11-glow", { scale: 1, opacity: 0.4, transformOrigin: "50% 50%" }, { scale: 2.2, opacity: 1, duration: 0.5, ease: "power2.out" }, @l11:5@);
    tl.fromTo(".t11-pw", { opacity: 0 }, { opacity: 1, duration: 0.15, immediateRender: false }, @l11:10@);
""")

# ---------- S12: "me dá a luva, filho" ----------
scene("s12", CSS + """
    #s12-q { top:360px; font-size:70px; line-height:1.2; }
""", f"""
      {layers("s12", warehouse_in("s12-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g transform="translate(540 1820) scale(1.7)">{MAN}</g></svg>
      <div id="s12-q" class="big">"ME DÁ A LUVA,<br><span class="red">FILHO.</span>"</div>
""", tint("s12", ["#5CE1E6", "#9b1b2b"], 7.2) + """
    tl.fromTo("#s12-q", { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.3, ease: "power4.out" }, @l12:3@);
""")

# ---------- S13: a escolha ----------
scene("s13", CSS + """
    #s13-k { top:330px; font-size:40px; color:#8FA3B0; }
    #s13-t { top:395px; font-size:76px; font-weight:700; line-height:1.1; }
    .s13-card { position:absolute; left:130px; width:820px; height:260px; border:4px solid #E8E4DA; background:#111318; box-sizing:border-box; }
    #s13-A { top:530px; } #s13-B { top:820px; }
    .s13-let { position:absolute; left:0; top:0; width:170px; height:252px; background:#D7263D; color:#fff; font-size:170px; font-weight:700; text-align:center; line-height:252px; }
    .s13-txt { position:absolute; left:200px; top:36px; width:590px; }
    .s13-txt b { display:block; font-size:40px; line-height:1.15; }
    .s13-txt span { display:block; margin-top:14px; font-size:30px; color:#8FA3B0; }
    #s13-bar { position:absolute; left:130px; top:1100px; width:820px; height:8px; background:#D7263D; transform-origin:0 50%; }
""", f"""
      {layers("s13", warehouse_in("s13-bg"))}
      <div id="s13-k" class="center mono">NÍVEL 0 · EP.06 · VOCÊ DECIDE</div>
      <div id="s13-t" class="center">O QUE O TÉO <span class="red">FAZ?</span></div>
      <div id="s13-A" class="s13-card"><div class="s13-let">A</div><div class="s13-txt"><b>ENTREGA A LUVA</b><span class="mono">PRA OUVIR A VERDADE INTEIRA</span></div></div>
      <div id="s13-B" class="s13-card"><div class="s13-let">B</div><div class="s13-txt"><b>LUTA</b><span class="mono">PRA PROTEGER O QUE É DELE</span></div></div>
      <div id="s13-bar"></div>
""", tint("s13", ["#9b1b2b", "#2E9BFF", "#9b1b2b"], 10.5) + """
    tl.fromTo("#s13-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.1);
    tl.fromTo("#s13-t", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.15);
    tl.fromTo("#s13-A", { opacity: 0, x: -1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l13:3@);
    tl.fromTo("#s13-B", { opacity: 0, x: 1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l13:14@);
    tl.fromTo("#s13-A", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l14:0@);
    tl.fromTo("#s13-B", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l14:0+0.25@);
    tl.fromTo("#s13-bar", { scaleX: 0 }, { scaleX: 1, duration: 4, ease: "none" }, @l14:0+0.5@);
""")
_p = "compositions/s13.html"
_c = open(_p).read()
open(_p, "w").write(_c.replace('tl.to("#s13-cam", { opacity: 0, duration: 0.14, ease: "power2.in" }, D - 0.16);', ""))

G_EP = [
 ("l1", [("A PORTA ENFERRUJADA", "A porta enferrujada"), ("DO ARMAZÉM RANGE", "do armazém range"), ("AO ABRIR.", "ao abrir."), ("LÁ DENTRO, SÓ AS LUZES", "Lá dentro, só as luzes"), ("PISCANDO GUIAM OS DOIS.", "piscando guiam os dois.")]),
 ("l2", [("VOCÊS ESCOLHERAM A.", "Vocês escolheram A."), ("ELES ENTRARAM AGORA,", "Eles entraram agora,"), ("ANTES QUE A SOMBRA", "antes que a sombra"), ("LÁ FORA PERCEBESSE.", "lá fora percebesse.")]),
 ("l3", [("O CELULAR DA MENINA", "O celular da menina"), ("VIROU LANTERNA.", "virou lanterna."), ("AS LUZES PISCAVAM", "As luzes piscavam"), ("NO MESMO RITMO", "no mesmo ritmo"), ("DA LUVA DO TÉO.", "da luva do Téo.")]),
 ("l4", [("ENTRE AS CAIXAS", "Entre as caixas"), ("EMPILHADAS,", "empilhadas,"), ("TINHA LUVAS.", "tinha luvas."), ("DEZENAS DELAS,", "Dezenas delas,"), ("PENDURADAS NUMA", "penduradas numa"), ("PAREDE INTEIRA.", "parede inteira.")]),
 ("l5", [("CADA LUVA TINHA", "Cada luva tinha"), ("UMA ETIQUETA AMARRADA.", "uma etiqueta amarrada."), ("NOMES, DATAS,", "Nomes, datas,"), ("E UM NÚMERO RISCADO.", "e um número riscado.")]),
 ("l6", [("O TÉO ENCONTROU UMA", "O Téo encontrou uma"), ("COM O NOME DELA.", "com o nome dela."), ("QUINTO DONO,", "Quinto dono,"), ("DIZIA A ETIQUETA.", "dizia a etiqueta."), ("IGUAL ELA TINHA", "Igual ela tinha"), ("CONTADO.", "contado.")]),
 ("l7", [("DO FUNDO DO ARMAZÉM,", "Do fundo do armazém,"), ("UMA VOZ:", "uma voz:"), ("VOCÊS NÃO DEVIAM", "vocês não deviam"), ("ESTAR AQUI.", "estar aqui.")]),
 ("l8", [("UM HOMEM SAIU", "Um homem saiu"), ("DA ESCURIDÃO.", "da escuridão."), ("NÃO USAVA CAPUZ.", "Não usava capuz."), ("O ROSTO DELE ERA", "O rosto dele era"), ("PARECIDO COM O DO TÉO,", "parecido com o do Téo,"), ("SÓ MAIS VELHO.", "só mais velho.")]),
 ("l9", [("A MENINA DEU", "A menina deu"), ("UM PASSO PRA TRÁS.", "um passo pra trás."), ("ELA SUSSURROU:", "Ela sussurrou:"), ("ISSO NÃO É POSSÍVEL.", "isso não é possível.")]),
 ("l10", [("O HOMEM DISSE:", "O homem disse:"), ("EU FUI O PRIMEIRO DONO", "eu fui o primeiro dono"), ("DESSA LUVA.", "dessa luva."), ("E ELA SEMPRE VOLTA", "E ela sempre volta"), ("PRA FAMÍLIA.", "pra família.")]),
 ("l11", [("A LUVA DO TÉO", "A luva do Téo"), ("ESQUENTOU COM MAIS", "esquentou com mais"), ("FORÇA DO QUE NUNCA.", "força do que nunca."), ("OS OLHOS DELE", "Os olhos dele"), ("FICARAM AZUIS DE NOVO.", "ficaram azuis de novo.")]),
 ("l12", [("O HOMEM ESTICOU", "O homem esticou"), ("A MÃO.", "a mão."), ("ME DÁ A LUVA, FILHO.", "Me dá a luva, filho."), ("OU EU TIRO NA FORÇA.", "Ou eu tiro na força.")]),
 ("l13", [("AMANHÃ,", "Amanhã,"), ("VOCÊ DECIDE.", "você decide."), ("A: O TÉO ENTREGA", "A: o Téo entrega"), ("A LUVA PRA OUVIR", "a luva pra ouvir"), ("A VERDADE INTEIRA.", "a verdade inteira."), ("OU B:", "Ou B:"), ("ELE LUTA PRA PROTEGER", "ele luta pra proteger"), ("O QUE É DELE.", "o que é dele.")]),
 ("l14", [("COMENTA A OU B.", "Comenta A ou B."), ("E ME SEGUE", "E me segue"), ("PRA NÃO PERDER", "pra não perder"), ("A PARTE 6!", "a parte seis!")]),
]
SFX_EP = [
    ("whoosh.mp3", slot["s1"][0], 0.4), ("glitch-2.mp3", WT("l1", 8), 0.3),
    ("impact-bass-1.mp3", WT("l2", 2), 0.5),
    ("glitch-1.mp3", WT("l3", 5), 0.3),
    ("pop.mp3", WT("l4", 7), 0.35),
    ("typing.mp3", WT("l5", 4), 0.25),
    ("whoosh-short.mp3", WT("l6", 5), 0.4),
    ("riser.mp3", WT("l7", 2), 0.4), ("impact-bass-2.mp3", WT("l7", 4), 0.55),
    ("whoosh-cinematic.mp3", slot["s8"][0], 0.45),
    ("glitch-2.mp3", WT("l9", 6), 0.35),
    ("impact-bass-1.mp3", WT("l10", 7), 0.4),
    ("riser.mp3", WT("l11", 0), 0.35), ("impact-bass-2.mp3", WT("l11", 8), 0.55),
    ("whoosh-short.mp3", WT("l12", 5), 0.45),
    ("whoosh-short.mp3", WT("l13", 3), 0.5), ("whoosh-short.mp3", WT("l13", 14), 0.5),
]
