# "Você sabia?" #02: celular antes de dormir, com o Téo. Incluído por build.py.
from bg import street, bedroom
from teo import teo, DEFS
INV = SHRUG = ""
CSS = """
    .bg { position:absolute; left:0; top:0; width:1080px; height:1920px; }
    .fig { position:absolute; left:0; top:0; width:1080px; height:1920px; overflow:visible; }
    .tint { position:absolute; inset:0; mix-blend-mode:color; opacity:0.6; }
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


PHONE = '<g><rect x="-60" y="-120" width="120" height="220" rx="18" fill="#111318" stroke="#5CE1E6" stroke-width="5"/><rect x="-50" y="-105" width="100" height="190" rx="4" fill="#5CE1E6" opacity="0.85"/></g>'
BRAIN_SHAPE = ('<path d="M-72 12 Q-92 -55 -42 -78 Q-24 -98 8 -88 Q48 -98 70 -68 Q100 -58 90 -8 Q112 30 82 50 Q90 80 58 90 '
               'Q38 110 6 90 Q-22 110 -46 90 Q-76 84 -70 55 Q-100 40 -72 12 Z" fill="{fill}" stroke="#1a1410" stroke-width="5"/>'
               '<path d="M0 -90 L0 92" stroke="#1a1410" stroke-width="4" opacity="0.5"/>'
               '<path d="M-55 -40 Q-35 -25 -50 -5 Q-30 10 -48 35" stroke="#1a1410" stroke-width="4" fill="none" opacity="0.5"/>'
               '<path d="M55 -40 Q35 -25 50 -5 Q30 10 48 35" stroke="#1a1410" stroke-width="4" fill="none" opacity="0.5"/>')


def BRAIN(fill="#F2A9A0"):
    return BRAIN_SHAPE.format(fill=fill)


# ---------- S1: gancho ----------
scene("s1", CSS + """
    #s1-t { top:330px; font-size:92px; line-height:1.1; }
    #s1-k { top:1000px; font-size:50px; color:#E8E4DA; background:#D7263D; padding:8px 0; }
""", f"""
      {layers("s1", bedroom("s1-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 1800) rotate(-6) scale(1.1)">{teo("t1", "neutro", glow=True, level=None, tag=False)}</g>
        <g id="s1-phone" transform="translate(630 1620) rotate(14) scale(1.1)">{PHONE}</g>
      </svg>
      <div id="s1-t" class="big">1 HORA A MENOS<br><span class="red">DE SONO</span></div>
""", tint("s1", ["#1d3557", "#2E9BFF", "#1d3557"], 7) + """
    tl.fromTo("#s1-phone", { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1.1, duration: 0.4, ease: "back.out(2)" }, 0.2);
    tl.fromTo("#t1-glow", { scale: 1, opacity: 0.3, transformOrigin: "50% 50%" }, { scale: 1.6, opacity: 0.8, duration: 1.2, yoyo: true, repeat: 3, ease: "sine.inOut" }, 0.6);
    tl.to("#t1-x-neutro", { opacity: 0, duration: 0.1 }, @l1:17@);
    tl.fromTo(".t1-pw", { opacity: 0 }, { opacity: 1, duration: 0.1, immediateRender: false }, @l1:17@);
    tl.fromTo("#s1-k", { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.out" }, @l1:19@);
""")

# ---------- S2: melatonina travada ----------
scene("s2", CSS + """
    #s2-k { top:1020px; font-size:46px; font-weight:700; color:#E9C46A; }
""", f"""
      {layers("s2", bedroom("s2-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 980) scale(2.6)" >{BRAIN()}</g>
        <g id="s2-block" transform="translate(760 760) scale(1.3)">
          <rect x="-70" y="-50" width="140" height="100" rx="14" fill="#D7263D" stroke="#fff" stroke-width="5"/>
          <text x="0" y="12" font-family="Oswald, Osw" font-weight="700" font-size="44" text-anchor="middle" fill="#fff">ZZZ</text>
          <line x1="-80" y1="-60" x2="80" y2="60" stroke="#fff" stroke-width="8"/>
        </g>
      </svg>
      <div id="s2-k" class="big mono">MELATONINA TRAVADA</div>
""", tint("s2", ["#2E9BFF", "#1d3557"], 5.8) + """
    tl.fromTo("#s2-block", { opacity: 0, scale: 0.4, rotation: -20 }, { opacity: 1, scale: 1.3, rotation: 0, duration: 0.3, ease: "back.out(3)" }, @l2:9@);
    tl.fromTo("#s2-k", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l2:11@);
""")

# ---------- S3: rolando o feed, insônia ----------
scene("s3", CSS + """
    #s3-k { top:340px; font-size:76px; font-weight:700; color:#8FA3B0; }
""", f"""
      {layers("s3", bedroom("s3-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 1800) scale(1.1)">{teo("t3", "medo", glow=True, tag=False)}</g>
        <g transform="translate(540 1430) scale(1.2)">{PHONE}
          <g id="s3-feed"><rect x="-45" y="-100" width="90" height="16" rx="4" fill="#111318"/><rect x="-45" y="-70" width="90" height="16" rx="4" fill="#111318"/><rect x="-45" y="-40" width="90" height="16" rx="4" fill="#111318"/><rect x="-45" y="-10" width="90" height="16" rx="4" fill="#111318"/><rect x="-45" y="20" width="90" height="16" rx="4" fill="#111318"/><rect x="-45" y="50" width="90" height="16" rx="4" fill="#111318"/></g>
        </g>
      </svg>
      <div id="s3-k" class="big">SEM SONO.</div>
""", tint("s3", ["#1d3557", "#2E9BFF", "#1d3557"], 4.6) + """
    tl.fromTo("#s3-feed", { y: 60 }, { y: -200, duration: 1.1, ease: "none", repeat: 4 }, 0);
    tl.fromTo("#s3-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, @l3:9@);
""")

# ---------- S4: estudo de Harvard, +60% ----------
scene("s4", CSS + """
    #s4-k { top:330px; font-size:42px; color:#8FA3B0; }
    #s4-n { top:420px; font-size:220px; font-weight:700; color:#D7263D; line-height:1; }
    #s4-src { top:1020px; font-size:42px; font-weight:700; color:#E9C46A; }
""", f"""
      {layers("s4", bedroom("s4-bg"))}
      <div id="s4-k" class="big mono">ESTUDO · HARVARD</div>
      <div id="s4-n" class="big">+<span id="s4-num">0</span>%</div>
      <div id="s4-src" class="big">MAIS DEMORA PRA DORMIR</div>
""", """
    tl.fromTo("#s4-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.1);
    const n4 = { v: 0 };
    tl.fromTo(n4, { v: 0 }, { v: 60, duration: 1.2, ease: "power2.out",
      onUpdate: () => { document.getElementById("s4-num").textContent = Math.round(n4.v); } }, @l4:12@);
    tl.fromTo("#s4-src", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l4:16@);
""")

# ---------- S5: memória e humor ----------
scene("s5", CSS + """
""", f"""
      {layers("s5", bedroom("s5-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 1780) scale(1.1)">{teo("t5", "medo", glow=False, tag=False)}</g>
        <g id="s5-mem" transform="translate(300 800) scale(1.2)"><rect x="-90" y="-60" width="180" height="120" rx="16" fill="#111318" stroke="#D7263D" stroke-width="5"/><text x="0" y="14" font-family="Oswald, Osw" font-weight="700" font-size="40" text-anchor="middle" fill="#D7263D">MEMÓRIA</text></g>
        <g id="s5-hum" transform="translate(780 800) scale(1.2)"><rect x="-90" y="-60" width="180" height="120" rx="16" fill="#111318" stroke="#5CE1E6" stroke-width="5"/><text x="0" y="14" font-family="Oswald, Osw" font-weight="700" font-size="40" text-anchor="middle" fill="#5CE1E6">HUMOR</text></g>
      </svg>
""", tint("s5", ["#1d3557", "#3a0a12", "#1d3557"], 11.7) + """
    tl.fromTo("#s5-mem", { opacity: 0, x: -200 }, { opacity: 1, x: 0, duration: 0.4, ease: "power4.out" }, @l5:14@);
    tl.fromTo("#s5-hum", { opacity: 0, x: 200 }, { opacity: 1, x: 0, duration: 0.4, ease: "power4.out" }, @l5:17@);
    tl.fromTo(["#s5-mem", "#s5-hum"], { y: 0 }, { y: -14, duration: 0.6, yoyo: true, repeat: 5, ease: "sine.inOut", immediateRender: false }, @l5:18@);
""")

# ---------- S6: esquecer informações ----------
scene("s6", CSS + """
    #s6-k { top:340px; font-size:72px; font-weight:700; line-height:1.15; }
""", f"""
      {layers("s6", bedroom("s6-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g id="s6-brain" transform="translate(540 1000) scale(3.2)" >{BRAIN("#8FA3B0")}</g></svg>
      <div id="s6-k" class="big">MENOS DE 6H<br><span class="red">= MAIS ESQUECIMENTO</span></div>
""", tint("s6", ["#3a0a12", "#D7263D", "#3a0a12"], 6.4) + """
    tl.fromTo("#s6-brain", { opacity: 0.9 }, { opacity: 0.3, duration: 0.3, yoyo: true, repeat: 7, ease: "sine.inOut" }, 0.2);
    tl.fromTo("#s6-k", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l6:10@);
""")

# ---------- S7: ansiedade ----------
scene("s7", CSS + """
    #s7-k { top:1020px; font-size:72px; font-weight:700; color:#fff; -webkit-text-stroke:3px #D7263D; }
""", f"""
      {layers("s7", bedroom("s7-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 1800) scale(1.1)">{teo("t7", "medo", glow=False, tag=False)}</g>
        <g id="s7-bang" transform="translate(760 1560) scale(1)">
          <circle r="90" fill="#D7263D"/><text y="16" font-family="Oswald, Osw" font-weight="700" font-size="70" text-anchor="middle" fill="#fff">!</text>
        </g>
      </svg>
      <div id="s7-k" class="big">ANSIEDADE</div>
""", tint("s7", ["#1d3557", "#9b1b2b", "#3a0a12"], 6.8) + """
    tl.fromTo("#s7-bang", { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.18, ease: "back.out(3)" }, @l7:13@);
    tl.fromTo("#s7-bang", { x: 0 }, { x: 10, duration: 0.05, yoyo: true, repeat: 7, ease: "none", immediateRender: false }, @l7:13+0.2@);
    tl.fromTo("#s7-k", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.out" }, @l7:16@);
""")

# ---------- S8: sistema imunológico ----------
SHIELD = '<path d="M0 -90 L80 -60 Q80 40 0 90 Q-80 40 -80 -60 Z"/>'
scene("s8", CSS + """
    #s8-k { top:1020px; font-size:52px; font-weight:700; color:#E9C46A; }
""", f"""
      {layers("s8", bedroom("s8-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s8-shield" transform="translate(540 900) scale(2.6)" fill="#2A9D8F" stroke="#1a1410" stroke-width="4">{SHIELD}</g>
        <path id="s8-crack" d="M540 700 L560 800 L520 870 L560 980" stroke="#D7263D" stroke-width="10" fill="none" stroke-dasharray="320" stroke-dashoffset="320"/>
      </svg>
      <div id="s8-k" class="big mono">SISTEMA IMUNOLÓGICO FRACO</div>
""", tint("s8", ["#2A9D8F", "#1d6f8a"], 6.9) + """
    tl.fromTo("#s8-crack", { strokeDashoffset: 320 }, { strokeDashoffset: 0, duration: 0.5, ease: "power4.out" }, @l8:10@);
    tl.fromTo("#s8-shield", { x: 0 }, { x: 8, duration: 0.05, yoyo: true, repeat: 5, ease: "none", immediateRender: false }, @l8:10@);
    tl.fromTo("#s8-k", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l8:11@);
""")

# ---------- S9: boa notícia ----------
scene("s9", CSS + """
    #s9-k { top:330px; font-size:100px; font-weight:700; color:#2A9D8F; }
    #s9-h { top:980px; font-size:110px; font-weight:700; }
""", f"""
      {layers("s9", bedroom("s9-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}<g transform="translate(540 1800) scale(1.1)">{teo("t9", "decidido", glow=False, tag=False)}</g></svg>
      <div id="s9-k" class="big">BOA NOTÍCIA</div>
      <div id="s9-h" class="big">1H ANTES</div>
""", tint("s9", ["#1d3557", "#2A9D8F"], 4.5) + """
    tl.fromTo("#s9-k", { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.22, ease: "power4.out" }, @l9:1@);
    tl.fromTo("#s9-h", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.25, ease: "power4.out" }, @l9:9@);
""")

# ---------- S10: modo noturno ----------
scene("s10", CSS + """
""", f"""
      {layers("s10", bedroom("s10-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 1000) scale(1.5)">{PHONE}
          <g id="s10-dot" transform="translate(0 -170)"><circle r="16" fill="#5CE1E6"/></g>
          <g id="s10-toggle" transform="translate(-20 -170)"><rect x="-40" y="-16" width="80" height="32" rx="16" fill="#2A9D8F"/><circle id="s10-knob" cx="24" cy="0" r="13" fill="#fff"/></g>
        </g>
      </svg>
""", tint("s10", ["#2E9BFF", "#1d6f8a"], 5.4) + """
    tl.fromTo("#s10-knob", { cx: -24 }, { cx: 24, duration: 0.3, ease: "power2.inOut" }, @l10:9@);
    tl.to("#s10-toggle rect", { fill: "#2A9D8F" }, @l10:9@);
""")

# ---------- S11: celular fora do quarto ----------
scene("s11", CSS + """
    #s11-k { top:1000px; font-size:72px; font-weight:700; color:#5CE1E6; }
""", f"""
      {layers("s11", bedroom("s11-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g id="s11-plug" transform="translate(540 1680)"><rect x="-10" y="0" width="20" height="90" fill="#E9C46A"/><rect x="-26" y="-18" width="52" height="24" rx="4" fill="#E9C46A" stroke="#1a1410" stroke-width="3"/></g>
        <g id="s11-phone" transform="translate(540 1500) scale(1.3)">{PHONE}</g>
      </svg>
      <div id="s11-k" class="big">FORA DO QUARTO</div>
""", tint("s11", ["#1d3557", "#1d6f8a"], 5.1) + """
    tl.fromTo("#s11-phone", { opacity: 0 }, { opacity: 1, duration: 0.5, ease: "power2.out" }, @l11:8@);
    tl.fromTo("#s11-plug", { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "power2.out" }, @l11:9@);
    tl.fromTo("#s11-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, @l11:12@);
""")

# ---------- S12: livro, luz apagada ----------
scene("s12", CSS + """
""", f"""
      {layers("s12", bedroom("s12-bg"))}
      <svg class="fig" data-layout-ignore viewBox="0 0 1080 1920">{DEFS}
        <g transform="translate(540 1780) scale(1.1)">{teo("t12", "decidido", glow=False, tag=False)}</g>
        <g transform="translate(540 1500) scale(1.2)"><path d="M-80 -60 L0 -40 L80 -60 L80 60 L0 40 L-80 60 Z" fill="#E9C46A" stroke="#1a1410" stroke-width="5"/></g>
      </svg>
""", tint("s12", ["#1d3557", "#2a1f4a"], 4.8) + "")

# ---------- S13: a escolha ----------
scene("s13", CSS + """
    #s13-k { top:330px; font-size:40px; color:#8FA3B0; }
    #s13-t { top:395px; font-size:90px; font-weight:700; line-height:1.1; }
    .s13-card { position:absolute; left:130px; width:820px; height:260px; border:4px solid #E8E4DA; background:#111318; box-sizing:border-box; }
    #s13-A { top:530px; } #s13-B { top:820px; }
    .s13-let { position:absolute; left:0; top:0; width:170px; height:252px; background:#D7263D; color:#fff; font-size:170px; font-weight:700; text-align:center; line-height:252px; }
    .s13-txt { position:absolute; left:200px; top:46px; width:590px; }
    .s13-txt b { display:block; font-size:50px; line-height:1.1; }
    #s13-bar { position:absolute; left:130px; top:1100px; width:820px; height:8px; background:#D7263D; transform-origin:0 50%; }
""", f"""
      {layers("s13", bedroom("s13-bg"))}
      <div id="s13-k" class="center mono">VOCÊ SABIA? · VOCÊ DECIDE</div>
      <div id="s13-t" class="center">AMANHÃ, <span class="red">QUAL?</span></div>
      <div id="s13-A" class="s13-card"><div class="s13-let">A</div><div class="s13-txt"><b>CAFÉ TODO DIA</b></div></div>
      <div id="s13-B" class="s13-card"><div class="s13-let">B</div><div class="s13-txt"><b>JEJUM NO CORPO</b></div></div>
      <div id="s13-bar"></div>
""", tint("s13", ["#2a1f4a", "#D7263D", "#2E9BFF"], 7.8) + """
    tl.fromTo("#s13-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.1);
    tl.fromTo("#s13-t", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.15);
    tl.fromTo("#s13-A", { opacity: 0, x: -1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l13:3@);
    tl.fromTo("#s13-B", { opacity: 0, x: 1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l13:14@);
    tl.fromTo("#s13-A", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l14:0@);
    tl.fromTo("#s13-B", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l14:0+0.25@);
    tl.fromTo("#s13-bar", { scaleX: 0 }, { scaleX: 1, duration: 2.6, ease: "none" }, @l14:0+0.6@);
""")
_p = "compositions/s13.html"
_c = open(_p).read()
open(_p, "w").write(_c.replace('tl.to("#s13-cam", { opacity: 0, duration: 0.14, ease: "power2.in" }, D - 0.16);', ""))

G_EP = [
 ("l1", [("VOCÊ SABIA", "Você sabia"), ("QUE USAR O CELULAR", "que usar o celular"), ("ANTES DE DORMIR", "antes de dormir"), ("PODE ATRASAR SEU SONO", "pode atrasar seu sono"), ("EM ATÉ 1 HORA?", "em até uma hora?"), ("E NO FINAL,", "E no final,"), ("VOCÊ DECIDE", "você decide"), ("O PRÓXIMO TEMA.", "o próximo tema.")]),
 ("l2", [("A LUZ AZUL DA TELA", "A luz azul da tela"), ("ENGANA SEU CÉREBRO.", "engana seu cérebro."), ("ELA TRAVA A MELATONINA,", "Ela trava a melatonina,"), ("O HORMÔNIO QUE AVISA", "o hormônio que avisa"), ("QUE É HORA DE DORMIR.", "que é hora de dormir.")]),
 ("l3", [("POR ISSO VOCÊ FICA", "Por isso você fica"), ("ROLANDO O FEED,", "rolando o feed,"), ("SEM SONO,", "sem sono,"), ("MESMO CANSADO,", "mesmo cansado,"), ("ATÉ TARDE DA NOITE.", "até tarde da noite.")]),
 ("l4", [("UM ESTUDO DE HARVARD", "Um estudo de Harvard"), ("MOSTROU QUE QUEM USA", "mostrou que quem usa"), ("TELAS À NOITE", "telas à noite"), ("DEMORA ATÉ 60%", "demora até sessenta por cento"), ("MAIS PRA PEGAR NO SONO.", "mais pra pegar no sono.")]),
 ("l5", [("E NÃO PARA POR AÍ.", "E não para por aí."), ("DORMIR MAL", "Dormir mal"), ("POR CAUSA DO CELULAR", "por causa do celular"), ("TAMBÉM PREJUDICA", "também prejudica"), ("SUA MEMÓRIA E SEU HUMOR", "sua memória e seu humor"), ("NO DIA SEGUINTE.", "no dia seguinte.")]),
 ("l6", [("PESQUISADORES VIRAM", "Pesquisadores viram"), ("QUE QUEM DORME", "que quem dorme"), ("MENOS DE 6 HORAS", "menos de seis horas"), ("TEM MUITO MAIS CHANCE", "tem muito mais chance"), ("DE ESQUECER", "de esquecer"), ("INFORMAÇÕES IMPORTANTES.", "informações importantes.")]),
 ("l7", [("E ROLAR NOTÍCIA RUIM", "E rolar notícia ruim"), ("OU BRIGA NAS REDES", "ou briga nas redes"), ("ANTES DE DORMIR", "antes de dormir"), ("AUMENTA A ANSIEDADE,", "aumenta a ansiedade,"), ("E ISSO ROUBA", "e isso rouba"), ("AINDA MAIS O SEU SONO.", "ainda mais o seu sono.")]),
 ("l8", [("DORMIR POUCO", "Dormir pouco"), ("POR CAUSA DA TELA", "por causa da tela"), ("TAMBÉM BAGUNÇA", "também bagunça"), ("SEU SISTEMA IMUNOLÓGICO,", "seu sistema imunológico,"), ("DEIXANDO VOCÊ MAIS SUJEITO", "deixando você mais sujeito"), ("A FICAR DOENTE.", "a ficar doente.")]),
 ("l9", [("A BOA NOTÍCIA:", "A boa notícia:"), ("PARAR DE OLHAR A TELA", "parar de olhar a tela"), ("1 HORA ANTES DE DORMIR", "uma hora antes de dormir"), ("JÁ MUDA O JOGO.", "já muda o jogo.")]),
 ("l10", [("SE NÃO DER", "Se não der"), ("PRA LARGAR O CELULAR,", "pra largar o celular,"), ("PELO MENOS ATIVA", "pelo menos ativa"), ("O MODO NOTURNO,", "o modo noturno,"), ("QUE FILTRA BOA PARTE", "que filtra boa parte"), ("DA LUZ AZUL.", "da luz azul.")]),
 ("l11", [("UM TRUQUE SIMPLES", "Um truque simples"), ("AJUDA BASTANTE:", "ajuda bastante:"), ("DEIXA O CELULAR", "deixa o celular"), ("CARREGANDO FORA DO QUARTO,", "carregando fora do quarto,"), ("LONGE DA CAMA.", "longe da cama.")]),
 ("l12", [("TROCA A ÚLTIMA HORA", "Troca a última hora"), ("DO DIA POR UM LIVRO,", "do dia por um livro,"), ("OU SÓ A LUZ APAGADA.", "ou só a luz apagada."), ("SEU CÉREBRO AGRADECE.", "Seu cérebro agradece.")]),
 ("l13", [("AMANHÃ,", "Amanhã,"), ("VOCÊ DECIDE.", "você decide."), ("A: O QUE ACONTECE", "A: o que acontece"), ("SE VOCÊ BEBER CAFÉ", "se você beber café"), ("TODO DIA.", "todo dia."), ("OU B:", "Ou B:"), ("O QUE O JEJUM FAZ", "o que o jejum faz"), ("COM SEU CORPO.", "com seu corpo.")]),
 ("l14", [("COMENTA A OU B!", "Comenta A ou B.")]),
]
SFX_EP = [
    ("whoosh.mp3", WT("l1", 16), 0.4), ("impact-bass-2.mp3", WT("l1", 20), 0.5),
    ("glitch-2.mp3", WT("l2", 9), 0.3),
    ("whoosh-short.mp3", WT("l3", 9), 0.35),
    ("impact-bass-1.mp3", WT("l4", 12), 0.6),
    ("pop.mp3", WT("l5", 14), 0.45), ("pop.mp3", WT("l5", 17), 0.45),
    ("glitch-1.mp3", WT("l6", 10), 0.3),
    ("impact-bass-2.mp3", WT("l7", 13), 0.55),
    ("impact-bass-1.mp3", WT("l8", 10), 0.5),
    ("whoosh.mp3", slot["s9"][0], 0.4),
    ("pop.mp3", WT("l10", 9), 0.4),
    ("whoosh-short.mp3", WT("l11", 8), 0.4),
    ("whoosh-short.mp3", WT("l13", 2), 0.5), ("whoosh-short.mp3", WT("l13", 14), 0.5),
]
