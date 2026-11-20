# "Você sabia?" #01: ficar sentado demais. Incluído por build.py.
GREEN = "#2A9D8F"
SIT = boneco("p1", 0, 0, 1.0, jacket="#3A6EA5", hat="none", scarf="#E9C46A", worried=True)
LEGS3 = boneco("p3", 0, 0, 1.0, jacket="#3A6EA5", hat="none", scarf="#E9C46A", worried=True)
WALK = boneco("p4", 0, 0, 1.0, jacket="#2A9D8F", hat="beanie", hat_color="#E9C46A", scarf="#E8E4DA", worried=False)
UP = boneco("p5", 0, 0, 1.0, jacket="#3A6EA5", hat="none", scarf="#E9C46A", worried=False)
INV = SHRUG = ""
CHAIR = '<rect x="-70" y="-120" width="150" height="18" rx="6" fill="#6b4f3a"/><rect x="60" y="-260" width="18" height="150" rx="6" fill="#6b4f3a"/><rect x="-62" y="-104" width="12" height="104" fill="#4a3628"/><rect x="58" y="-104" width="12" height="104" fill="#4a3628"/>'
SITJS = lambda p: f'''
    tl.fromTo("#{p}-legL", {{ rotation: -80, transformOrigin: "50% 0%" }}, {{ rotation: -80, duration: 0.01 }}, 0);
    tl.fromTo("#{p}-legR", {{ rotation: -80, transformOrigin: "50% 0%" }}, {{ rotation: -80, duration: 0.01 }}, 0);
    tl.fromTo("#{p}-fig", {{ y: 0 }}, {{ y: 0, duration: 0.01 }}, 0);'''

# ---------- S1: gancho ----------
scene("s1", """
    #s1-big { top:330px; font-size:130px; font-weight:700; line-height:0.95; }
    #s1-scene { position:absolute; left:140px; top:560px; width:520px; height:500px; }
    #s1-clock { position:absolute; left:680px; top:600px; width:260px; height:260px; }
    #s1-risk { position:absolute; left:640px; top:880px; width:340px; text-align:center; font-size:120px; font-weight:700; color:#D7263D; line-height:1; }
    #s1-riskk { position:absolute; left:640px; top:1000px; width:340px; text-align:center; font-size:30px; color:#8FA3B0; }
""", f"""
      <div id="s1-big" class="center">8 HORAS<br><span class="red">SENTADO</span></div>
      <svg id="s1-scene" data-layout-ignore viewBox="-260 -400 520 410">
        <rect x="-250" y="-190" width="230" height="16" fill="#8D99AE"/><rect x="-240" y="-174" width="12" height="174" fill="#5c6370"/>
        <rect x="-210" y="-260" width="130" height="80" rx="6" fill="#222" stroke="#8D99AE" stroke-width="5"/><rect x="-198" y="-250" width="106" height="60" fill="#3A6EA5" opacity="0.6"/>
        <g transform="translate(40 0)">{CHAIR}<g transform="translate(0 0)">{SIT}</g></g>
      </svg>
      <svg id="s1-clock" data-layout-ignore viewBox="-130 -130 260 260">
        <circle r="120" fill="#111318" stroke="#E8E4DA" stroke-width="8"/>
        <g id="s1-hand"><rect x="-5" y="-95" width="10" height="100" rx="5" fill="#D7263D"/></g>
        <circle r="10" fill="#E8E4DA"/>
      </svg>
      <div id="s1-risk">+60%</div>
      <div id="s1-riskk" class="mono">RISCO DE MORTE</div>
""", SITJS("p1") + """
    tl.fromTo("#s1-hand", { rotation: 0, transformOrigin: "50% 95%" }, { rotation: 1440, duration: 5, ease: "power1.inOut" }, 0);
    tl.fromTo("#p1-head", { rotation: 0, transformOrigin: "50% 100%" }, { rotation: 8, duration: 2, ease: "sine.inOut" }, 1.5);
    tl.fromTo("#s1-risk", { opacity: 0, scale: 1.8 }, { opacity: 1, scale: 1, duration: 0.22, ease: "power4.out" }, @l1:12@);
    tl.fromTo("#s1-riskk", { opacity: 0 }, { opacity: 1, duration: 0.3 }, @l1:14@);
""")

# ---------- S2: o estudo ----------
dots = "".join(f'<circle class="s2-d" cx="{30 + (i % 20) * 40}" cy="{30 + (i // 20) * 40}" r="13" fill="#E8E4DA"/>' for i in range(160))
scene("s2", """
    #s2-k { top:330px; font-size:40px; color:#8FA3B0; }
    #s2-n { top:390px; font-size:150px; font-weight:700; line-height:1; }
    #s2-sub { top:550px; font-size:48px; }
    #s2-grid { position:absolute; left:140px; top:640px; width:800px; height:320px; }
    #s2-src { top:985px; font-size:44px; font-weight:700; color:#E9C46A; }
""", f"""
      <div id="s2-k" class="center mono">ESTUDO</div>
      <div id="s2-n" class="center"><span id="s2-num">0</span></div>
      <div id="s2-sub" class="center">PESSOAS ANALISADAS</div>
      <svg id="s2-grid" data-layout-ignore viewBox="0 0 800 320">{dots}</svg>
      <div id="s2-src" class="center">THE LANCET · 2016</div>
""", """
    const n2 = { v: 0 };
    tl.fromTo(n2, { v: 0 }, { v: 1000000, duration: 1.6, ease: "power2.out",
      onUpdate: () => { document.getElementById("s2-num").textContent = "+" + Math.round(n2.v).toLocaleString("pt-BR"); } }, @l2:4@);
    tl.fromTo("#s2-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.05);
    tl.fromTo("#s2-sub", { opacity: 0 }, { opacity: 1, duration: 0.3 }, @l2:9@);
    tl.fromTo(".s2-d", { opacity: 0, scale: 0, transformOrigin: "50% 50%" }, { opacity: 0.85, scale: 1, duration: 0.12, stagger: 0.008, ease: "back.out(3)" }, @l2:4@);
    tl.fromTo("#s2-src", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l2:15@);
""")

# ---------- S3: o que acontece no corpo ----------
flow = "".join(f'<circle class="s3-f" cx="0" cy="0" r="7" fill="#D7263D"/>' for _ in range(6))
scene("s3", """
    #s3-k { top:330px; font-size:56px; font-weight:700; }
    #s3-body { position:absolute; left:180px; top:440px; width:420px; height:600px; }
    #s3-bat { position:absolute; left:680px; top:500px; width:200px; height:340px; }
    #s3-batk { position:absolute; left:640px; top:860px; width:280px; text-align:center; font-size:30px; color:#8FA3B0; }
""", f"""
      <div id="s3-k" class="center">PARADO POR HORAS…</div>
      <svg id="s3-body" data-layout-ignore viewBox="-210 -400 420 410">
        <g transform="translate(-20 0)">{CHAIR}{LEGS3}</g>
        <path id="s3-vein" d="M-40 -110 L-40 -20 L90 -20" stroke="#D7263D" stroke-width="4" fill="none" opacity="0.4"/>
        {flow}
      </svg>
      <svg id="s3-bat" data-layout-ignore viewBox="0 0 200 340">
        <rect x="70" y="0" width="60" height="24" rx="6" fill="#8D99AE"/>
        <rect x="10" y="20" width="180" height="310" rx="16" fill="none" stroke="#E8E4DA" stroke-width="8"/>
        <rect id="s3-lvl" x="26" y="36" width="148" height="278" rx="8" fill="{GREEN}"/>
      </svg>
      <div id="s3-batk" class="mono">ENERGIA GASTA</div>
""", SITJS("p3") + """
    tl.fromTo("#s3-k", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, 0.05);
    tl.fromTo("#s3-lvl", { scaleY: 1, transformOrigin: "50% 100%", fill: "#2A9D8F" }, { scaleY: 0.18, fill: "#D7263D", duration: 1.6, ease: "power2.inOut" }, @l3:5@);
    tl.fromTo(".s3-f", { x: -40, y: -110, opacity: 1 }, { keyframes: [{ x: -40, y: -20, duration: 0.6 }, { x: 90, y: -20, duration: 0.8 }], stagger: 0.35, repeat: 2, ease: "none" }, @l3:9@);
    tl.fromTo(".s3-f", { opacity: 1 }, { opacity: 0.5, duration: 1.5, immediateRender: false }, @l3:12@);
""")

# ---------- S4: a boa notícia ----------
scene("s4", """
    #s4-k { top:330px; font-size:90px; font-weight:700; color:#2A9D8F; }
    #s4-walk { position:absolute; left:120px; top:470px; width:360px; height:430px; }
    #s4-h { position:absolute; left:500px; top:500px; width:460px; text-align:center; font-size:140px; font-weight:700; line-height:1; }
    #s4-hk { position:absolute; left:500px; top:650px; width:460px; text-align:center; font-size:34px; color:#8FA3B0; }
    #s4-barbg { position:absolute; left:140px; top:960px; width:800px; height:44px; background:#22252b; border-radius:22px; }
    #s4-bar { position:absolute; left:140px; top:960px; width:800px; height:44px; background:#D7263D; border-radius:22px; transform-origin:0 50%; }
    #s4-bark { position:absolute; left:140px; top:910px; width:800px; font-size:30px; color:#8FA3B0; }
""", f"""
      <div id="s4-k" class="center">BOA NOTÍCIA</div>
      <svg id="s4-walk" data-layout-ignore viewBox="-180 -360 360 370">{WALK}</svg>
      <div id="s4-h">1H<span style="font-size:70px">/DIA</span></div>
      <div id="s4-hk" class="mono">CAMINHADA OU EXERCÍCIO</div>
      <div id="s4-bark" class="mono">RISCO</div>
      <div id="s4-barbg"></div><div id="s4-bar"></div>
""", """
    tl.fromTo("#s4-k", { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power4.out" }, @l4:3@);
    tl.fromTo("#s4-walk", { opacity: 0, x: -200 }, { opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }, @l4:5@);
    tl.fromTo("#p4-legL", { rotation: -25, transformOrigin: "50% 0%" }, { rotation: 25, duration: 0.3, yoyo: true, repeat: 11, ease: "sine.inOut" }, @l4:5@);
    tl.fromTo("#p4-legR", { rotation: 25, transformOrigin: "50% 0%" }, { rotation: -25, duration: 0.3, yoyo: true, repeat: 11, ease: "sine.inOut" }, @l4:5@);
    tl.fromTo("#p4-armL", { rotation: 25, transformOrigin: "50% 0%" }, { rotation: -25, duration: 0.3, yoyo: true, repeat: 11, ease: "sine.inOut" }, @l4:5@);
    tl.fromTo("#p4-armR", { rotation: -25, transformOrigin: "50% 0%" }, { rotation: 25, duration: 0.3, yoyo: true, repeat: 11, ease: "sine.inOut" }, @l4:5@);
    tl.fromTo("#s4-h", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l4:6@);
    tl.fromTo("#s4-hk", { opacity: 0 }, { opacity: 1, duration: 0.3 }, @l4:10@);
    tl.fromTo("#s4-bark", { opacity: 0 }, { opacity: 1, duration: 0.3 }, @l4:12@);
    tl.fromTo("#s4-barbg", { opacity: 0 }, { opacity: 1, duration: 0.3 }, @l4:12@);
    tl.fromTo("#s4-bar", { opacity: 0, scaleX: 1, backgroundColor: "#D7263D" }, { opacity: 1, duration: 0.3 }, @l4:12@);
    tl.to("#s4-bar", { scaleX: 0.08, backgroundColor: "#2A9D8F", duration: 1.0, ease: "power3.inOut" }, @l4:15@);
""")

# ---------- S5: levanta a cada 30 min ----------
scene("s5", """
    #s5-t { top:330px; font-size:150px; font-weight:700; line-height:1; font-family:'Space Mono',monospace; }
    #s5-k { top:500px; font-size:40px; color:#8FA3B0; }
    #s5-up { position:absolute; left:330px; top:580px; width:420px; height:420px; }
    #s5-go { top:1000px; font-size:76px; font-weight:700; color:#2A9D8F; }
""", f"""
      <div id="s5-t" class="center"><span id="s5-num">30:00</span></div>
      <div id="s5-k" class="center mono">A CADA 30 MIN SENTADO</div>
      <svg id="s5-up" data-layout-ignore viewBox="-210 -400 420 410"><g transform="translate(0 0)">{CHAIR}{UP}</g></svg>
      <div id="s5-go" class="center">LEVANTA 2–3 MIN</div>
""", SITJS("p5") + """
    const t5 = { v: 1800 };
    tl.fromTo(t5, { v: 1800 }, { v: 0, duration: 1.8, ease: "power1.in",
      onUpdate: () => { const s = Math.round(t5.v); document.getElementById("s5-num").textContent = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0"); } }, 0.1);
    tl.fromTo("#s5-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.2);
    tl.to("#p5-legL", { rotation: 0, duration: 0.3, ease: "back.out(2)" }, @l5:6@);
    tl.to("#p5-legR", { rotation: 0, duration: 0.3, ease: "back.out(2)" }, @l5:6@);
    tl.fromTo("#p5-fig", { y: 0 }, { y: -40, duration: 0.3, ease: "back.out(2)", immediateRender: false }, @l5:6@);
    tl.fromTo("#p5-armL", { rotation: 0, transformOrigin: "50% 0%" }, { rotation: 150, duration: 0.3, ease: "back.out(2)" }, @l5:6+0.2@);
    tl.fromTo("#p5-armR", { rotation: 0, transformOrigin: "50% 0%" }, { rotation: -150, duration: 0.3, ease: "back.out(2)" }, @l5:6+0.2@);
    tl.fromTo("#s5-go", { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.22, ease: "power4.out" }, @l5:8@);
""")

# ---------- S6: a pergunta ----------
scene("s6", """
    #s6-k { top:330px; font-size:40px; color:#8FA3B0; }
    #s6-t { top:395px; font-size:96px; font-weight:700; line-height:1; }
    .s6-card { position:absolute; left:130px; width:820px; height:260px; border:4px solid #E8E4DA; background:#111318; box-sizing:border-box; }
    #s6-A { top:510px; } #s6-B { top:800px; }
    .s6-let { position:absolute; left:0; top:0; width:170px; height:252px; background:#D7263D; color:#fff; font-size:170px; font-weight:700; text-align:center; line-height:252px; }
    .s6-txt { position:absolute; left:200px; top:40px; width:590px; }
    .s6-txt b { display:block; font-size:56px; line-height:1.05; }
    .s6-txt span { display:block; margin-top:14px; font-size:28px; color:#8FA3B0; }
    #s6-bar { position:absolute; left:130px; top:1080px; width:820px; height:8px; background:#D7263D; transform-origin:0 50%; }
""", """
      <div id="s6-k" class="center mono">VOCÊ SABIA? · VOCÊ DECIDE</div>
      <div id="s6-t" class="center">AMANHÃ, <span class="red">QUAL?</span></div>
      <div id="s6-A" class="s6-card"><div class="s6-let">A</div><div class="s6-txt"><b>DORMIR MENOS DE 6 HORAS</b><span class="mono">O QUE ACONTECE COM O CORPO</span></div></div>
      <div id="s6-B" class="s6-card"><div class="s6-let">B</div><div class="s6-txt"><b>CELULAR ANTES DE DORMIR</b><span class="mono">O QUE FAZ COM O CÉREBRO</span></div></div>
      <div id="s6-bar"></div>
""", """
    tl.fromTo("#s6-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.1);
    tl.fromTo("#s6-t", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.15);
    tl.fromTo("#s6-A", { opacity: 0, x: -1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l6:3@);
    tl.fromTo("#s6-B", { opacity: 0, x: 1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l6:15@);
    tl.fromTo("#s6-A", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l7:0@);
    tl.fromTo("#s6-B", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l7:0+0.25@);
    tl.fromTo("#s6-bar", { scaleX: 0 }, { scaleX: 1, duration: 2.6, ease: "none" }, @l7:0+0.8@);
""")
_p = "compositions/s6.html"
_c = open(_p).read()
open(_p, "w").write(_c.replace('tl.to("#s6-cam", { opacity: 0, duration: 0.14, ease: "power2.in" }, D - 0.16);', ""))

G_EP = [
 ("l1", [("VOCÊ SABIA", "Você sabia"), ("QUE FICAR SENTADO", "que ficar sentado"), ("MAIS DE 8 HORAS POR DIA", "mais de oito horas por dia"), ("PODE AUMENTAR", "pode aumentar"), ("SEU RISCO DE MORTE", "seu risco de morte"), ("EM QUASE 60%?", "em quase sessenta por cento?")]),
 ("l2", [("FOI O QUE MOSTROU", "Foi o que mostrou"), ("UM ESTUDO COM MAIS", "um estudo com mais"), ("DE 1 MILHÃO DE PESSOAS,", "de um milhão de pessoas,"), ("PUBLICADO NA REVISTA", "publicado na revista"), ("THE LANCET.", "The Lancet.")]),
 ("l3", [("PARADO POR HORAS,", "Parado por horas,"), ("O CORPO GASTA", "o corpo gasta"), ("MENOS ENERGIA", "menos energia"), ("E O SANGUE CIRCULA", "e o sangue circula"), ("MAIS DEVAGAR", "mais devagar"), ("NAS PERNAS.", "nas pernas.")]),
 ("l4", [("MAS TEM UMA", "Mas tem uma"), ("BOA NOTÍCIA:", "boa notícia:"), ("1 HORA POR DIA", "uma hora por dia"), ("DE CAMINHADA", "de caminhada"), ("OU EXERCÍCIO MODERADO", "ou exercício moderado"), ("PRATICAMENTE APAGA", "praticamente apaga"), ("ESSE RISCO.", "esse risco.")]),
 ("l5", [("E A CADA 30 MINUTOS", "E a cada trinta minutos"), ("SENTADO,", "sentado,"), ("LEVANTAR POR 2 OU 3 MINUTOS", "levantar por dois ou três minutos"), ("JÁ AJUDA.", "já ajuda.")]),
 ("l6", [("AMANHÃ,", "Amanhã,"), ("VOCÊ DECIDE.", "você decide."), ("A: DORMIR", "A: o que acontece se você dormir"), ("MENOS DE 6 HORAS.", "menos de seis horas."), ("OU B:", "Ou B:"), ("O CELULAR", "o que o celular"), ("ANTES DE DORMIR", "antes de dormir"), ("NO SEU CÉREBRO.", "faz com seu cérebro.")]),
 ("l7", [("COMENTA A OU B!", "Comenta A ou B.")]),
]
SFX_EP = [
    ("impact-bass-2.mp3", WT("l1", 12), 0.55),
    ("whoosh.mp3", slot["s2"][0], 0.45), ("pop.mp3", WT("l2", 15), 0.45),
    ("whoosh-short.mp3", slot["s3"][0], 0.5),
    ("whoosh.mp3", slot["s4"][0], 0.45), ("pop.mp3", WT("l4", 3), 0.5), ("impact-bass-1.mp3", WT("l4", 15), 0.45),
    ("whoosh-short.mp3", slot["s5"][0], 0.5), ("pop.mp3", WT("l5", 6), 0.5),
    ("whoosh-short.mp3", WT("l6", 3), 0.5), ("whoosh-short.mp3", WT("l6", 15), 0.5),
]
