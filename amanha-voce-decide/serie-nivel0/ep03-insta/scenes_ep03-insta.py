# NÍVEL 0 · EP.03 (ramo Instagram): o confronto. Incluído por build.py. Cenário muda de cor (camada .tint).
from bg import street
from teo import teo, DEFS
from lia import lia
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


HUNTERS = "".join(f'<g transform="translate({x} 1400)"><path d="M-50 0 L-40 -250 Q0 -290 40 -250 L50 0 Z" fill="#050505"/><circle cx="0" cy="-310" r="48" fill="#050505"/><circle class="hu-lan" cx="70" cy="-150" r="22" fill="#ff2a2a"/></g>' for x in (300, 540, 780))
HUNTER_1 = '<g id="hunter1" transform="translate(540 1400)"><path d="M-50 0 L-40 -250 Q0 -290 40 -250 L50 0 Z" fill="#050505"/><circle cx="0" cy="-310" r="48" fill="#050505"/><circle class="hu-lan" cx="70" cy="-150" r="22" fill="#ff2a2a"/></g>'
PHONE = ('<g><path d="M-130 -40 L-60 -170 Q-30 -220 30 -190 L-20 -60 Q-50 -10 -130 -40 Z" fill="#8D5B3E" stroke="#1a1410" stroke-width="5"/>'
         '<rect x="-20" y="-220" width="70" height="130" rx="10" transform="rotate(-20)" fill="#111318" stroke="#5CE1E6" stroke-width="5"/>'
         '<rect x="-10" y="-210" width="50" height="108" rx="4" transform="rotate(-20)" fill="#5CE1E6" opacity="0.55"/></g>')

# ---------- S1: recap + "você decide de novo" ----------
scene("s1", CSS + """
    #s1-t { top:400px; font-size:150px; line-height:0.95; }
    #s1-k { top:340px; font-size:44px; color:#5CE1E6; }
    #s1-dec { top:1000px; font-size:58px; color:#E8E4DA; background:#D7263D; padding:8px 0; }
""", f"""
      {layers("s1", street("s1-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(360 1760) scale(1.0)">{teo("t1", "decidido", glow=True, level="99", level_color="#5CE1E6", power=True)}</g>
        <g transform="translate(730 1760) scale(0.95)">{lia("l1", "neutro")}</g>
      </svg>
      <div id="s1-k" class="big mono">NO EPISÓDIO ANTERIOR…</div>
      <div id="s1-dec" class="big">VOCÊ DECIDE DE NOVO</div>
""", tint("s1", ["#1d3557", "#D7263D", "#1d3557"], 8.5) + """
    tl.fromTo("#s1-dec", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power4.out" }, @l1:21@);
    tl.fromTo("#s1-k", { opacity: 1 }, { opacity: 0, duration: 0.3, immediateRender: false }, @l1:20@);
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
""", tint("s2", ["#9b1b2b", "#D7263D", "#9b1b2b"], 3.3) + """
    tl.fromTo("#s2-b", { opacity: 0, scale: 2.2, rotation: 10 }, { opacity: 1, scale: 1, rotation: 4, duration: 0.25, ease: "power4.in" }, @l2:2@);
""")

# ---------- S3: os caçadores encostam, "entrega a luva" ----------
scene("s3", CSS + """
    #s3-q { top:1500px; font-size:72px; line-height:1.15; }
""", f"""
      {layers("s3", street("s3-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g id="s3-hunt">{HUNTERS}</g></svg>
      <div id="s3-q" class="big">"ENTREGA A <span class="red">LUVA</span>,<br>MOLEQUE."</div>
""", tint("s3", ["#1d3557", "#3a0a12"], 8.4) + """
    tl.fromTo("#s3-hunt", { x: 500 }, { x: 0, duration: 1.0, ease: "power2.out" }, 0.1);
    tl.fromTo(".hu-lan", { opacity: 0.3 }, { opacity: 1, duration: 0.25, yoyo: true, repeat: 14, ease: "sine.inOut" }, 0.2);
    tl.fromTo("#s3-q", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l3:12@);
""")

# ---------- S4: a menina grita (close) ----------
scene("s4", CSS + """
""", f"""
      {layers("s4", street("s4-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g id="s4-z"><g transform="translate(540 2820) scale(2.4)">{lia("l4", "medo", arm_out=True)}</g></g></svg>
""", tint("s4", ["#D7263D", "#9b1b2b", "#D7263D"], 6.2) + """
    tl.fromTo("#s4-z", { scale: 1, transformOrigin: "50% 40%" }, { scale: 1.1, duration: D, ease: "none" }, 0);
""")

# ---------- S5: a luva esquenta, o chão racha ----------
scene("s5", CSS + """
""", f"""
      {layers("s5", street("s5-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(360 1760) scale(1.05)">{teo("t5", "decidido", glow=True, level="99", level_color="#5CE1E6")}</g>
        <g id="s5-crack" opacity="0"><path d="M300 1870 L340 1830 L330 1870 L380 1840 L360 1880 L420 1860" stroke="#5CE1E6" stroke-width="6" fill="none" stroke-linecap="round"/></g>
      </svg>
""", tint("s5", ["#1d3557", "#2E9BFF", "#1d3557"], 7.5) + """
    tl.fromTo("#t5-glow", { scale: 1, opacity: 0.35 }, { scale: 1.8, opacity: 0.9, duration: D, ease: "power1.in" }, 0);
    tl.fromTo("#s5-crack", { opacity: 0 }, { opacity: 1, duration: 0.5 }, @l5:12@);
""")

# ---------- S6: a onda de energia joga o caçador pra trás ----------
scene("s6", CSS + """
    #s6-flash { position:absolute; inset:0; background:#5CE1E6; }
""", f"""
      {layers("s6", street("s6-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s6-wave"><ellipse cx="540" cy="1650" rx="260" ry="80" fill="#5CE1E6" opacity="0.55" filter="url(#blur18)"/></g>
        <g transform="translate(360 1760) scale(1.05)">{teo("t6", "decidido", glow=True, level="99", level_color="#5CE1E6", power=True)}</g>
        {HUNTER_1}
      </svg>
      <div id="s6-flash"></div>
""", tint("s6", ["#1d3557", "#5CE1E6", "#1d3557"], 8.3) + """
    tl.fromTo("#s6-flash", { opacity: 0 }, { opacity: 0.6, duration: 0.08, yoyo: true, repeat: 1, ease: "none" }, @l6:9@);
    tl.fromTo("#s6-wave", { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1.4, duration: 0.5, ease: "power2.out" }, @l6:9@);
    tl.fromTo("#hunter1", { x: 0, y: 0, rotation: 0 }, { x: 420, y: -60, rotation: 35, duration: 0.6, ease: "power3.out" }, @l6:9@);
    tl.to("#hunter1", { opacity: 0, duration: 0.4 }, @l6:13@);
""")

# ---------- S7: tem gente filmando, ao vivo ----------
scene("s7", CSS + """
    #s7-live { position:absolute; top:260px; left:390px; width:300px; text-align:center; font-family:'Space Mono',monospace; font-size:40px; color:#fff; background:#D7263D; padding:10px 0; border-radius:8px; }
""", f"""
      {layers("s7", street("s7-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(830 1680) scale(1.3)">{PHONE}</g>
      </svg>
      <div id="s7-live">● AO VIVO</div>
""", tint("s7", ["#1d3557", "#1d6f8a"], 9.5) + """
    tl.fromTo("#s7-live", { opacity: 0.3 }, { opacity: 1, duration: 0.4, yoyo: true, repeat: 11, ease: "sine.inOut" }, 0);
""")

# ---------- S8: o segundo caçador avança, a menina se joga na frente ----------
scene("s8", CSS + """
""", f"""
      {layers("s8", street("s8-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s8-hunt" transform="translate(780 1400)"><path d="M-50 0 L-40 -250 Q0 -290 40 -250 L50 0 Z" fill="#050505"/><circle cx="0" cy="-310" r="48" fill="#050505"/><circle class="hu-lan" cx="70" cy="-150" r="22" fill="#ff2a2a"/></g>
        <g id="s8-lia" transform="translate(600 1760) scale(1.0)">{lia("l8", "medo", arm_out=True)}</g>
        <g transform="translate(360 1760) scale(1.0)">{teo("t8", "medo", glow=True, level="99", level_color="#5CE1E6")}</g>
      </svg>
""", tint("s8", ["#1d6f8a", "#9b1b2b"], 8.9) + """
    tl.fromTo("#s8-hunt", { x: 0 }, { x: -260, duration: 0.6, ease: "power2.in" }, 0.1);
    tl.fromTo(".hu-lan", { opacity: 0.3 }, { opacity: 1, duration: 0.2, yoyo: true, repeat: 20, ease: "sine.inOut" }, 0.1);
    tl.fromTo("#s8-lia", { x: 0 }, { x: -90, duration: 0.3, ease: "power3.out" }, @l8:8@);
""")

# ---------- S9: ela cai, o nível pisca ----------
scene("s9", CSS + """
""", f"""
      {layers("s9", street("s9-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920"><g id="s9-z"><g transform="translate(540 2900) scale(2.3) rotate(-8)">{lia("l9", "medo")}</g></g></svg>
""", tint("s9", ["#9b1b2b", "#3a0a12", "#9b1b2b"], 8.1) + """
    tl.fromTo("#s9-z", { scale: 1, transformOrigin: "50% 40%" }, { scale: 1.1, duration: D, ease: "none" }, 0);
    tl.fromTo("#l9-lvl", { opacity: 1 }, { opacity: 0.15, duration: 0.18, yoyo: true, repeat: 11, ease: "none" }, @l9:9@);
""")

# ---------- S10: Téo vê a menina caída, olhos azuis de novo ----------
scene("s10", CSS + """
""", f"""
      {layers("s10", street("s10-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g id="s10-z"><g transform="translate(540 2820) scale(2.4)">{teo("t10", "decidido", glow=True, level="99", level_color="#5CE1E6")}</g></g></svg>
""", tint("s10", ["#2E9BFF", "#1d3557", "#5CE1E6"], 9.4) + """
    tl.fromTo("#t10-glow", { scale: 1, opacity: 0.4, transformOrigin: "50% 50%" }, { scale: 2.4, opacity: 1, duration: 0.6, ease: "power2.out" }, @l10:12@);
    tl.fromTo(".t10-pw", { opacity: 0 }, { opacity: 1, duration: 0.15, immediateRender: false }, @l10:13@);
""")

# ---------- S11: ele solta tudo, brilho toma a rua ----------
scene("s11", CSS + """
    #s11-flash { position:absolute; inset:0; background:#5CE1E6; }
""", f"""
      {layers("s11", street("s11-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s11-glow"><ellipse cx="540" cy="1650" rx="460" ry="140" fill="#5CE1E6" opacity="0.55" filter="url(#blur18)"/></g>
        <g transform="translate(540 1760) scale(1.15)">{teo("t11", "decidido", glow=True, level="99", level_color="#5CE1E6", power=True)}</g>
        <g id="s11-hunt">{HUNTERS}</g>
      </svg>
      <div id="s11-flash"></div>
""", tint("s11", ["#1d3557", "#5CE1E6", "#1d3557"], 8.7) + """
    tl.fromTo("#s11-flash", { opacity: 0 }, { opacity: 0.7, duration: 0.1, yoyo: true, repeat: 1, ease: "none" }, @l11:7@);
    tl.fromTo("#s11-glow", { opacity: 0, scale: 0.3 }, { opacity: 1, scale: 1.6, duration: 0.6, ease: "power2.out", immediateRender: false }, @l11:7@);
    tl.fromTo("#s11-hunt", { x: 0, opacity: 1 }, { x: 600, opacity: 0, duration: 1.0, ease: "power3.in" }, @l11:16@);
""")

# ---------- S12: a cidade toda assistiu ----------
scene("s12", CSS + """
    #s12-t { top:360px; font-size:76px; line-height:1.15; }
""", f"""
      {layers("s12", street("s12-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 1760) scale(1.15)">{teo("t12", "decidido", glow=True, level="99", level_color="#5CE1E6")}</g>
      </svg>
      <div id="s12-t" class="big">A CIDADE TODA<br><span class="red">ASSISTIU.</span></div>
""", tint("s12", ["#2E9BFF", "#5a189a", "#2E9BFF"], 8.0) + """
    tl.fromTo("#s12-t", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l12:3@);
    tl.fromTo("#t12-lvl", { scale: 1 }, { scale: 1.15, duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut" }, @l12:9@);
""")

# ---------- S13: a escolha ----------
scene("s13", CSS + """
    #s13-k { top:330px; font-size:40px; color:#8FA3B0; }
    #s13-t { top:395px; font-size:84px; font-weight:700; line-height:1.1; }
    .s13-card { position:absolute; left:130px; width:820px; height:260px; border:4px solid #E8E4DA; background:#111318; box-sizing:border-box; }
    #s13-A { top:530px; } #s13-B { top:820px; }
    .s13-let { position:absolute; left:0; top:0; width:170px; height:252px; background:#D7263D; color:#fff; font-size:170px; font-weight:700; text-align:center; line-height:252px; }
    .s13-txt { position:absolute; left:200px; top:36px; width:590px; }
    .s13-txt b { display:block; font-size:46px; line-height:1.1; }
    .s13-txt span { display:block; margin-top:14px; font-size:30px; color:#8FA3B0; }
    #s13-bar { position:absolute; left:130px; top:1100px; width:820px; height:8px; background:#D7263D; transform-origin:0 50%; }
""", f"""
      {layers("s13", street("s13-bg"))}
      <div id="s13-k" class="center mono">NÍVEL 0 · EP.04 · VOCÊ DECIDE</div>
      <div id="s13-t" class="center">O QUE O TÉO <span class="red">FAZ?</span></div>
      <div id="s13-A" class="s13-card"><div class="s13-let">A</div><div class="s13-txt"><b>LEVA A MENINA PRA SE CURAR</b><span class="mono">E FOGE DA CIDADE</span></div></div>
      <div id="s13-B" class="s13-card"><div class="s13-let">B</div><div class="s13-txt"><b>FICA NA CIDADE</b><span class="mono">DESCOBRE QUEM MANDOU OS CAÇADORES</span></div></div>
      <div id="s13-bar"></div>
""", tint("s13", ["#5a189a", "#D7263D", "#2E9BFF", "#5a189a"], 9.5) + """
    tl.fromTo("#s13-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.1);
    tl.fromTo("#s13-t", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.15);
    tl.fromTo("#s13-A", { opacity: 0, x: -1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l13:3@);
    tl.fromTo("#s13-B", { opacity: 0, x: 1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l13:17@);
    tl.fromTo("#s13-A", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l14:0@);
    tl.fromTo("#s13-B", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l14:0+0.25@);
    tl.fromTo("#s13-bar", { scaleX: 0 }, { scaleX: 1, duration: 4, ease: "none" }, @l14:0+0.5@);
""")
_p = "compositions/s13.html"
_c = open(_p).read()
open(_p, "w").write(_c.replace('tl.to("#s13-cam", { opacity: 0, duration: 0.14, ease: "power2.in" }, D - 0.16);', ""))

G_EP = [
 ("l1", [("NO EPISÓDIO ANTERIOR,", "No episódio anterior,"), ("A LUVA DO TÉO ESQUENTOU", "a luva do Téo esquentou"), ("BEM NA FRENTE", "bem na frente"), ("DOS CAÇADORES.", "dos caçadores."), ("E DESSA VEZ,", "E dessa vez,"), ("ELE NÃO FUGIU.", "ele não fugiu."), ("NO FINAL,", "No final,"), ("VOCÊ DECIDE DE NOVO.", "você decide de novo.")]),
 ("l2", [("VOCÊS ESCOLHERAM B.", "Vocês escolheram B."), ("O TÉO DECIDIU", "O Téo decidiu"), ("ENFRENTAR OS CAÇADORES", "enfrentar os caçadores"), ("COM O PODER", "com o poder"), ("DA LUVA.", "da luva.")]),
 ("l3", [("AS TRÊS SOMBRAS", "As três sombras"), ("PARARAM BEM NA FRENTE DELES.", "pararam bem na frente deles."), ("UM DOS CAÇADORES DISSE:", "Um dos caçadores disse:"), ("ENTREGA A LUVA,", "entrega a luva,"), ("MOLEQUE.", "moleque.")]),
 ("l4", [("A MENINA GRITOU:", "A menina gritou:"), ("NÃO ENTREGA NADA,", "não entrega nada,"), ("TÉO!", "Téo!"), ("ESSA LUVA É SUA", "Essa luva é sua"), ("AGORA!", "agora!")]),
 ("l5", [("O BRILHO AZUL", "O brilho azul"), ("FICOU MAIS FORTE.", "ficou mais forte."), ("O CHÃO PERTO", "O chão perto"), ("DOS PÉS DELE", "dos pés dele"), ("COMEÇOU A RACHAR.", "começou a rachar.")]),
 ("l6", [("TÉO ERGUEU A MÃO,", "Téo ergueu a mão,"), ("E UMA ONDA", "e uma onda"), ("DE ENERGIA", "de energia"), ("JOGOU O PRIMEIRO", "jogou o primeiro"), ("CAÇADOR LONGE,", "caçador longe,"), ("PRA TRÁS.", "pra trás.")]),
 ("l7", [("SÓ QUE TINHA GENTE", "Só que tinha gente"), ("FILMANDO COM O CELULAR.", "filmando com o celular."), ("E O VÍDEO", "E o vídeo"), ("JÁ ESTAVA AO VIVO,", "já estava ao vivo,"), ("PRA CIDADE INTEIRA VER.", "pra cidade inteira ver.")]),
 ("l8", [("O SEGUNDO CAÇADOR", "O segundo caçador"), ("AVANÇOU RÁPIDO,", "avançou rápido,"), ("MAS A MENINA", "mas a menina"), ("SE JOGOU NA FRENTE", "se jogou na frente"), ("E TOMOU O GOLPE", "e tomou o golpe"), ("POR ELE.", "por ele.")]),
 ("l9", [("ELA CAIU NO CHÃO", "Ela caiu no chão"), ("SEGURANDO O BRAÇO.", "segurando o braço."), ("O NÚMERO EM CIMA", "O número em cima"), ("DA CABEÇA DELA", "da cabeça dela"), ("COMEÇOU A PISCAR.", "começou a piscar.")]),
 ("l10", [("TÉO VIU A MENINA", "Téo viu a menina"), ("CAÍDA.", "caída."), ("A LUVA ESQUENTOU", "A luva esquentou"), ("MAIS DO QUE NUNCA.", "mais do que nunca."), ("OS OLHOS DELE", "Os olhos dele"), ("FICARAM AZUIS DE NOVO.", "ficaram azuis de novo.")]),
 ("l11", [("ELE SOLTOU TUDO", "Ele soltou tudo"), ("QUE TINHA GUARDADO.", "que tinha guardado."), ("UM BRILHO TOMOU", "Um brilho tomou"), ("A RUA INTEIRA,", "a rua inteira,"), ("E OS CAÇADORES", "e os caçadores"), ("QUE SOBRARAM", "que sobraram"), ("FUGIRAM CORRENDO.", "fugiram correndo.")]),
 ("l12", [("A CIDADE TODA", "A cidade toda"), ("ASSISTIU, AO VIVO,", "assistiu, ao vivo,"), ("O NÍVEL ZERO", "o nível zero"), ("VIRAR O NÍVEL", "virar o nível"), ("MAIS ALTO", "mais alto"), ("QUE JÁ SE VIU.", "que já se viu.")]),
 ("l13", [("AMANHÃ,", "Amanhã,"), ("VOCÊ DECIDE.", "você decide."), ("A: O TÉO LEVA", "A: o Téo leva"), ("A MENINA PRA SE CURAR", "a menina pra se curar"), ("E FOGE DA CIDADE.", "e foge da cidade."), ("OU B:", "Ou B:"), ("ELE FICA PRA DESCOBRIR", "ele fica pra descobrir"), ("QUEM MANDOU", "quem mandou"), ("OS CAÇADORES.", "os caçadores.")]),
 ("l14", [("COMENTA A OU B.", "Comenta A ou B."), ("E ME SEGUE", "E me segue"), ("PRA PARTE 4!", "pra parte quatro.")]),
]
SFX_EP = [
    ("impact-bass-2.mp3", WT("l1", 21), 0.5),
    ("whoosh.mp3", slot["s2"][0], 0.45), ("impact-bass-1.mp3", WT("l2", 2), 0.55),
    ("whoosh-short.mp3", WT("l3", 12), 0.4),
    ("whoosh-short.mp3", slot["s4"][0], 0.35),
    ("impact-bass-1.mp3", WT("l5", 12), 0.45),
    ("impact-bass-2.mp3", WT("l6", 9), 0.6), ("whoosh-cinematic.mp3", WT("l6", 13), 0.45),
    ("glitch-1.mp3", slot["s7"][0], 0.3),
    ("impact-bass-1.mp3", WT("l8", 8), 0.5),
    ("glitch-2.mp3", WT("l9", 9), 0.35),
    ("impact-bass-2.mp3", WT("l10", 13), 0.55),
    ("impact-bass-2.mp3", WT("l11", 7), 0.65), ("whoosh-cinematic.mp3", WT("l11", 16), 0.45),
    ("whoosh-short.mp3", WT("l13", 3), 0.5), ("whoosh-short.mp3", WT("l13", 17), 0.5),
]
