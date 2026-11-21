# NÍVEL 0 · EP.04 (Instagram, ramo B): a Confraria. Incluído por build.py. Cenário muda de cor (camada .tint).
from bg import street, cellar
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


def warehouse(pid):
    """Armazém abandonado à noite, perto do porto: galpão com janelas quebradas e luzes piscando."""
    panels = "".join(f'<rect x="{x}" y="900" width="150" height="500" fill="#2a2a30" stroke="#1a1410" stroke-width="5"/>' for x in range(-20, 1100, 160))
    windows = "".join(f'<rect id="{pid}-w{i}" x="{x}" y="1000" width="90" height="120" fill="#f2c46d" opacity="0.7" stroke="#1a1410" stroke-width="4"/>' for i, x in enumerate(range(20, 1060, 160)))
    crane = '<path d="M900 900 L900 300 L1060 300" stroke="#5a4e48" stroke-width="14" fill="none"/><path d="M900 420 L760 480" stroke="#5a4e48" stroke-width="10"/>'
    water = ''.join(f'<path d="M{x} 1870 Q {x+40} 1860 {x+80} 1870" stroke="#2b3a4a" stroke-width="4" fill="none" opacity="0.6"/>' for x in range(-20, 1100, 90))
    return (f'<svg id="{pid}" class="bg" data-layout-ignore viewBox="0 0 1080 1920" preserveAspectRatio="xMidYMid slice">'
            f'<defs><linearGradient id="{pid}-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0a12"/><stop offset="1" stop-color="#1d2433"/></linearGradient></defs>'
            f'<rect width="1080" height="1920" fill="url(#{pid}-sky)"/>'
            f'<circle cx="160" cy="220" r="58" fill="#e8e4da" opacity="0.85"/>'
            f'{crane}{panels}{windows}'
            f'<rect y="1400" width="1080" height="520" fill="#12161c"/>{water}</svg>')


def lamp(pid):
    """Poste de luz quebrado, piscando."""
    return (f'<g id="{pid}"><rect x="-10" y="-520" width="20" height="520" fill="#2b2b33" stroke="#1a1410" stroke-width="4"/>'
            f'<path d="M-10 -520 L-70 -560 L-50 -580 L10 -540 Z" fill="#2b2b33" stroke="#1a1410" stroke-width="4"/>'
            f'<circle id="{pid}-bulb" cx="-50" cy="-566" r="20" fill="#f2c46d"/></g>')


PHONE = ('<g><path d="M-130 -40 L-60 -170 Q-30 -220 30 -190 L-20 -60 Q-50 -10 -130 -40 Z" fill="#8D5B3E" stroke="#1a1410" stroke-width="5"/>'
         '<rect x="-20" y="-220" width="70" height="130" rx="10" transform="rotate(-20)" fill="#111318" stroke="#5CE1E6" stroke-width="5"/>'
         '<rect x="-10" y="-210" width="50" height="108" rx="4" transform="rotate(-20)" fill="#5CE1E6" opacity="0.55"/></g>')

# silhueta encapuzada do informante (reaproveita o formato dos caçadores, lanterna ciano em vez de vermelha)
INFORMANT = ('<g id="inf1" transform="translate(540 1400)">'
             '<path d="M-50 0 L-40 -250 Q0 -290 40 -250 L50 0 Z" fill="#050505"/>'
             '<circle cx="0" cy="-310" r="48" fill="#050505"/>'
             '<circle class="inf-eye" cx="0" cy="-310" r="10" fill="#5CE1E6"/></g>')

# símbolo da Confraria: uma luva riscada (ícone pequeno)
SYMBOL = ('<g><path d="M-24 -22 Q-30 18 -6 26 Q22 30 26 6 L22 -26 Z" fill="none" stroke="#E9C46A" stroke-width="6"/>'
          '<path d="M-36 -36 L36 36" stroke="#D7263D" stroke-width="7" stroke-linecap="round"/></g>')

PAPER = ('<g><rect x="-80" y="-100" width="160" height="200" fill="#E8E4DA" stroke="#1a1410" stroke-width="5" transform="rotate(-6)"/>'
         '<path d="M-50 -60 L50 -60 M-50 -30 L50 -30 M-50 0 L20 0 M-50 30 L30 30" stroke="#8a8378" stroke-width="5" transform="rotate(-6)"/></g>')

# ---------- S1: recap + "você decide de novo" ----------
scene("s1", CSS + """
    #s1-t { top:400px; font-size:150px; line-height:0.95; }
    #s1-k { top:340px; font-size:44px; color:#5CE1E6; }
    #s1-dec { top:1000px; font-size:58px; color:#E8E4DA; background:#D7263D; padding:8px 0; }
""", f"""
      {layers("s1", street("s1-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(360 1760) scale(1.0)">{teo("t1", "decidido", glow=True, level="99", level_color="#5CE1E6", power=True)}</g>
        <g transform="translate(730 1760) scale(0.95)">{lia("l1", "medo", arm_out=True)}</g>
      </svg>
      <div id="s1-k" class="big mono">NO EPISÓDIO ANTERIOR…</div>
      <div id="s1-dec" class="big">VOCÊ DECIDE DE NOVO</div>
""", tint("s1", ["#5CE1E6", "#9b1b2b", "#1d3557"], 10.5) + """
    tl.fromTo("#s1-dec", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power4.out" }, @l1:28@);
    tl.fromTo("#s1-k", { opacity: 1 }, { opacity: 0, duration: 0.3, immediateRender: false }, @l1:27@);
""")

# ---------- S2: vocês escolheram B ----------
scene("s2", CSS + """
    #s2-b { position:absolute; left:390px; top:380px; width:300px; height:300px; background:#D7263D; color:#fff; font-size:260px; font-weight:700; text-align:center; line-height:300px; border:8px solid #E8E4DA; }
""", f"""
      {layers("s2", street("s2-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(360 1760) scale(0.95)">{teo("t2", "decidido", glow=True, level="99", level_color="#5CE1E6")}</g>
        <g transform="translate(730 1760) scale(0.9)">{lia("l2", "neutro")}</g>
      </svg>
      <div id="s2-b">B</div>
""", tint("s2", ["#9b1b2b", "#D7263D", "#9b1b2b"], 4.0) + """
    tl.fromTo("#s2-b", { opacity: 0, scale: 2.2, rotation: 10 }, { opacity: 1, scale: 1, rotation: 4, duration: 0.25, ease: "power4.in" }, @l2:2@);
""")

# ---------- S3: a rua inteira já viu o vídeo ----------
scene("s3", CSS + """
    #s3-cnt { position:absolute; top:260px; left:340px; width:400px; text-align:center; font-family:'Space Mono',monospace; font-size:52px; color:#5CE1E6; background:#111318; padding:14px 0; border-radius:10px; border:4px solid #5CE1E6; }
""", f"""
      {layers("s3", street("s3-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        {boneco("b3a", 180, 1820, s=1.1, jacket="#8D99AE", hat="", hand_prop=PHONE)}
        {boneco("b3b", 880, 1820, s=1.1, jacket="#6a7a8a", hat="fedora", hand_prop=PHONE)}
        {boneco("b3c", 540, 1860, s=1.2, jacket="#4a3b4f", hat="", hand_prop=PHONE)}
      </svg>
      <div id="s3-cnt" class="mono">👁 500 MIL VIEWS</div>
""", tint("s3", ["#1d6f8a", "#2E9BFF"], 8.4) + """
    tl.fromTo("#s3-cnt", { opacity: 0, y: -20 }, { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, @l3:6@);
    tl.fromTo("#s3-cnt", { scale: 1 }, { scale: 1.06, duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut" }, @l3:8@);
""")

# ---------- S4: a menina manca, o nível pisca ----------
scene("s4", CSS + """
""", f"""
      {layers("s4", street("s4-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g id="s4-z"><g transform="translate(540 2900) scale(2.2) rotate(-4)">{lia("l4", "medo", arm_out=True)}</g></g></svg>
""", tint("s4", ["#2E9BFF", "#9b1b2b", "#2E9BFF"], 7.7) + """
    tl.fromTo("#s4-z", { scale: 1, transformOrigin: "50% 40%" }, { scale: 1.08, duration: D, ease: "none" }, 0);
    tl.fromTo("#l4-lvl", { opacity: 1 }, { opacity: 0.2, duration: 0.16, yoyo: true, repeat: 13, ease: "none" }, @l4:13@);
""")

# ---------- S5: os caçadores não agem sozinhos ----------
scene("s5", CSS + """
    #s5-q { top:300px; font-size:72px; line-height:1.15; }
""", f"""
      {layers("s5", street("s5-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(360 1760) scale(1.0)">{teo("t5", "neutro", glow=True, level="99", level_color="#5CE1E6")}</g>
        <g transform="translate(730 1760) scale(0.95)">{lia("l5", "neutro")}</g>
      </svg>
      <div id="s5-q" class="big">"OS <span class="red">CAÇADORES</span><br>NÃO AGEM SOZINHOS."</div>
""", tint("s5", ["#1d3557", "#3a0a12"], 6.9) + """
    tl.fromTo("#s5-q", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l5:2@);
""")

# ---------- S6: o homem de capuz encosta, mostra o pulso ----------
scene("s6", CSS + """
""", f"""
      {layers("s6", street("s6-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        {INFORMANT}
        <g id="s6-sym" transform="translate(540 1200) scale(0)">{SYMBOL}</g>
      </svg>
""", tint("s6", ["#1d3557", "#2a1a3a"], 10.9) + """
    tl.fromTo("#inf1", { x: -100, opacity: 0 }, { x: 540, opacity: 1, duration: 0.8, ease: "power2.out" }, 0.1);
    tl.fromTo(".inf-eye", { opacity: 0.3 }, { opacity: 1, duration: 0.3, yoyo: true, repeat: 16, ease: "sine.inOut" }, 0.3);
    tl.fromTo("#s6-sym", { scale: 0, opacity: 0 }, { scale: 2.6, opacity: 1, duration: 0.4, ease: "back.out(1.6)" }, @l6:13@);
""")

# ---------- S7: "esse símbolo é da Confraria" ----------
scene("s7", CSS + """
    #s7-t { top:360px; font-size:84px; line-height:1.15; }
""", f"""
      {layers("s7", street("s7-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">
        <g transform="translate(540 1400) scale(2.4)">{SYMBOL}</g>
      </svg>
      <div id="s7-t" class="big">A <span class="red">CONFRARIA.</span></div>
""", tint("s7", ["#2a1a3a", "#5a189a", "#2a1a3a"], 7.4) + """
    tl.fromTo("#s7-t", { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.3, ease: "power4.out" }, @l7:6@);
""")

# ---------- S8: a menina fica pálida, "quinto dono" (close) ----------
scene("s8", CSS + """
""", f"""
      {layers("s8", street("s8-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g id="s8-z"><g transform="translate(540 2820) scale(2.4)">{lia("l8", "medo")}</g></g></svg>
""", tint("s8", ["#5a189a", "#D7263D", "#5a189a"], 9.1) + """
    tl.fromTo("#s8-z", { scale: 1, transformOrigin: "50% 45%" }, { scale: 1.1, duration: D, ease: "none" }, 0);
""")

# ---------- S9: o endereço, e o homem some ----------
scene("s9", CSS + """
""", f"""
      {layers("s9", street("s9-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        {INFORMANT}
        <g id="s9-paper" transform="translate(540 1500) scale(0)">{PAPER}</g>
      </svg>
""", tint("s9", ["#2a1a3a", "#1d3557"], 9.9) + """
    tl.fromTo("#s9-paper", { scale: 0, opacity: 0 }, { scale: 1.4, opacity: 1, duration: 0.35, ease: "back.out(1.7)" }, @l9:4@);
    tl.fromTo("#inf1", { opacity: 1, y: 1400 }, { opacity: 0, y: 1360, duration: 0.6, ease: "power2.in" }, @l9:9@);
""")

# ---------- S10: o armazém abandonado, luzes piscando ----------
scene("s10", CSS + """
""", f"""
      {layers("s10", warehouse("s10-bg"))}
""", tint("s10", ["#1d3557", "#0a0a12"], 11.1) + """
    tl.fromTo("#s10-bg-w0, #s10-bg-w2, #s10-bg-w4, #s10-bg-w6", { opacity: 0.7 }, { opacity: 0.1, duration: 0.2, yoyo: true, repeat: 9, ease: "none" }, @l10:11@);
    tl.fromTo("#s10-bg-w1, #s10-bg-w3, #s10-bg-w5", { opacity: 0.7 }, { opacity: 0.15, duration: 0.25, yoyo: true, repeat: 7, ease: "none" }, @l10:11+0.3@);
""")

# ---------- S11: a menina segura o braço dele ----------
scene("s11", CSS + """
    #s11-q { top:280px; font-size:66px; line-height:1.15; }
""", f"""
      {layers("s11", warehouse("s11-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(360 1760) scale(1.0)">{teo("t11", "neutro", glow=True, level="99", level_color="#5CE1E6")}</g>
        <g transform="translate(730 1760) scale(0.95)">{lia("l11", "medo", arm_out=True)}</g>
      </svg>
      <div id="s11-q" class="big">"SE A GENTE ENTRAR AGORA,<br>NÃO TEM MAIS COMO VOLTAR ATRÁS."</div>
""", tint("s11", ["#0a0a12", "#1d3557"], 10.6) + """
    tl.fromTo("#s11-q", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l11:9@);
""")

# ---------- S12: a sombra observa, debaixo do poste ----------
scene("s12", CSS + """
""", f"""
      {layers("s12", street("s12-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(860 1620) scale(1.3)">{lamp("s12-lamp")}</g>
        <g id="s12-shadow" transform="translate(860 1700) scale(1.0)"><path d="M-50 0 L-40 -250 Q0 -290 40 -250 L50 0 Z" fill="#050505"/><circle cx="0" cy="-310" r="48" fill="#050505"/></g>
      </svg>
""", tint("s12", ["#0a0a12", "#1d1424"], 8.6) + """
    tl.fromTo("#s12-lamp-bulb", { opacity: 1 }, { opacity: 0.1, duration: 0.12, yoyo: true, repeat: 23, ease: "none" }, 0);
    tl.fromTo("#s12-shadow", { opacity: 0 }, { opacity: 1, duration: 0.5 }, @l12:5@);
""")

# ---------- S13: a escolha ----------
scene("s13", CSS + """
    #s13-k { top:330px; font-size:40px; color:#8FA3B0; }
    #s13-t { top:395px; font-size:84px; font-weight:700; line-height:1.1; }
    .s13-card { position:absolute; left:130px; width:820px; height:260px; border:4px solid #E8E4DA; background:#111318; box-sizing:border-box; }
    #s13-A { top:530px; } #s13-B { top:820px; }
    .s13-let { position:absolute; left:0; top:0; width:170px; height:252px; background:#D7263D; color:#fff; font-size:170px; font-weight:700; text-align:center; line-height:252px; }
    .s13-txt { position:absolute; left:200px; top:36px; width:590px; }
    .s13-txt b { display:block; font-size:44px; line-height:1.1; }
    .s13-txt span { display:block; margin-top:14px; font-size:30px; color:#8FA3B0; }
    #s13-bar { position:absolute; left:130px; top:1100px; width:820px; height:8px; background:#D7263D; transform-origin:0 50%; }
""", f"""
      {layers("s13", warehouse("s13-bg"))}
      <div id="s13-k" class="center mono">NÍVEL 0 · EP.05 · VOCÊ DECIDE</div>
      <div id="s13-t" class="center">O QUE ELES <span class="red">FAZEM?</span></div>
      <div id="s13-A" class="s13-card"><div class="s13-let">A</div><div class="s13-txt"><b>ENTRAM NO ARMAZÉM AGORA</b><span class="mono">ENQUANTO AINDA DÁ TEMPO</span></div></div>
      <div id="s13-B" class="s13-card"><div class="s13-let">B</div><div class="s13-txt"><b>ESPERAM ESCURECER</b><span class="mono">E SEGUEM A SOMBRA PRIMEIRO</span></div></div>
      <div id="s13-bar"></div>
""", tint("s13", ["#1d1424", "#D7263D", "#2E9BFF", "#1d1424"], 10.3) + """
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
 ("l1", [("NO EPISÓDIO ANTERIOR,", "No episódio anterior,"), ("O TÉO SOLTOU TUDO", "o Téo soltou tudo"), ("QUE TINHA GUARDADO", "que tinha guardado"), ("BEM NA FRENTE", "bem na frente"), ("DE QUEM ESTAVA FILMANDO", "de quem estava filmando"), ("AO VIVO.", "ao vivo."), ("A MENINA CAIU MACHUCADA,", "A menina caiu machucada,"), ("TENTANDO PROTEGER ELE.", "tentando proteger ele."), ("NO FINAL,", "No final,"), ("VOCÊ DECIDE DE NOVO.", "você decide de novo.")]),
 ("l2", [("VOCÊS ESCOLHERAM B.", "Vocês escolheram B."), ("OS DOIS FICARAM", "Os dois ficaram"), ("NA CIDADE PRA DESCOBRIR", "na cidade pra descobrir"), ("QUEM MANDOU OS CAÇADORES.", "quem mandou os caçadores.")]),
 ("l3", [("O VÍDEO DO CONFRONTO", "O vídeo do confronto"), ("JÁ TINHA QUINHENTAS MIL", "já tinha quinhentas mil"), ("VISUALIZAÇÕES.", "visualizações."), ("TODO MUNDO NA RUA", "Todo mundo na rua"), ("RECONHECIA O ROSTO", "reconhecia o rosto"), ("DO TÉO.", "do Téo.")]),
 ("l4", [("A MENINA MANCAVA,", "A menina mancava,"), ("SEGURANDO O BRAÇO.", "segurando o braço."), ("O NÚMERO EM CIMA", "O número em cima"), ("DA CABEÇA DELA", "da cabeça dela"), ("AINDA PISCAVA, SEM PARAR.", "ainda piscava, sem parar.")]),
 ("l5", [("ELA DISSE:", "Ela disse:"), ("OS CAÇADORES NÃO AGEM", "os caçadores não agem"), ("SOZINHOS.", "sozinhos."), ("ALGUÉM PAGA A CONTA", "Alguém paga a conta"), ("DELES.", "deles.")]),
 ("l6", [("UM HOMEM DE CAPUZ", "Um homem de capuz"), ("PAROU DO LADO", "parou do lado"), ("DOS DOIS.", "dos dois."), ("ELE APONTOU PRO PULSO:", "Ele apontou pro pulso:"), ("UMA LUVA RISCADA,", "uma luva riscada,"), ("TATUADA NA PELE.", "tatuada na pele.")]),
 ("l7", [("ELE DISSE:", "Ele disse:"), ("ESSE SÍMBOLO É DA", "esse símbolo é da"), ("CONFRARIA.", "Confraria."), ("ELES COLECIONAM LUVAS", "Eles colecionam luvas"), ("COMO A SUA.", "como a sua.")]),
 ("l8", [("A MENINA FICOU PÁLIDA.", "A menina ficou pálida."), ("ELA SUSSURROU:", "Ela sussurrou:"), ("FOI A CONFRARIA", "foi a Confraria"), ("QUE TIROU A LUVA", "que tirou a luva"), ("DO QUINTO DONO.", "do quinto dono.")]),
 ("l9", [("O HOMEM ENTREGOU", "O homem entregou"), ("UM PAPEL COM", "um papel com"), ("UM ENDEREÇO,", "um endereço,"), ("E SUMIU ANTES", "e sumiu antes"), ("QUE ALGUÉM VISSE", "que alguém visse"), ("O ROSTO DELE.", "o rosto dele.")]),
 ("l10", [("ERA UM ARMAZÉM", "Era um armazém"), ("ABANDONADO, PERTO DO PORTO.", "abandonado, perto do porto."), ("AS LUZES DE DENTRO", "As luzes de dentro"), ("PISCAVAM,", "piscavam,"), ("DO MESMO JEITO", "do mesmo jeito"), ("QUE A LUVA", "que a luva"), ("DO TÉO.", "do Téo.")]),
 ("l11", [("A MENINA SEGUROU", "A menina segurou"), ("O BRAÇO DO TÉO.", "o braço do Téo."), ("ELA DISSE:", "Ela disse:"), ("SE A GENTE", "se a gente"), ("ENTRAR AGORA,", "entrar agora,"), ("NÃO TEM MAIS", "não tem mais"), ("COMO VOLTAR ATRÁS.", "como voltar atrás.")]),
 ("l12", [("DO OUTRO LADO", "Do outro lado"), ("DA RUA,", "da rua,"), ("UMA SOMBRA OBSERVAVA", "uma sombra observava"), ("OS DOIS,", "os dois,"), ("PARADA DEBAIXO DE UM", "parada debaixo de um"), ("POSTE QUEBRADO.", "poste quebrado.")]),
 ("l13", [("AMANHÃ,", "Amanhã,"), ("VOCÊ DECIDE.", "você decide."), ("A: ELES ENTRAM", "A: eles entram"), ("NO ARMAZÉM AGORA,", "no armazém agora,"), ("ENQUANTO AINDA DÁ TEMPO.", "enquanto ainda dá tempo."), ("OU B:", "Ou B:"), ("ELES ESPERAM ESCURECER,", "eles esperam escurecer,"), ("E SEGUEM A SOMBRA", "e seguem a sombra"), ("PRIMEIRO.", "primeiro.")]),
 ("l14", [("COMENTA A OU B.", "Comenta A ou B."), ("E ME SEGUE", "E me segue"), ("PRA PARTE 5!", "pra parte cinco.")]),
]
SFX_EP = [
    ("pop.mp3", WT("l1", 20), 0.35), ("impact-bass-2.mp3", WT("l1", 28), 0.5),
    ("whoosh.mp3", slot["s2"][0], 0.4), ("impact-bass-1.mp3", WT("l2", 2), 0.55),
    ("typing.mp3", WT("l3", 6), 0.3), ("pop.mp3", WT("l3", 8), 0.4),
    ("glitch-2.mp3", WT("l4", 13), 0.35),
    ("whoosh-short.mp3", WT("l5", 2), 0.4),
    ("whoosh.mp3", slot["s6"][0], 0.4), ("pop.mp3", WT("l6", 13), 0.45),
    ("riser.mp3", slot["s7"][0], 0.35), ("impact-bass-1.mp3", WT("l7", 6), 0.5),
    ("glitch-1.mp3", WT("l8", 8), 0.4),
    ("whoosh-short.mp3", WT("l9", 9), 0.4),
    ("glitch-2.mp3", WT("l10", 11), 0.3),
    ("impact-bass-1.mp3", WT("l11", 12), 0.4),
    ("whoosh-cinematic.mp3", WT("l12", 5), 0.45),
    ("whoosh-short.mp3", WT("l13", 3), 0.5), ("whoosh-short.mp3", WT("l13", 14), 0.5),
]
