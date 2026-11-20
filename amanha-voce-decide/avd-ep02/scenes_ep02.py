# Cenas do EP.02: O Homem de Somerton. Incluído por build.py (usa scene(), boneco(), slot, T).

BODY = boneco("b1", 0, 0, 1.0, jacket="#5c6370", hat="none", scarf="#2b2f3a", pants="#3a3f4a", worried=False, eyes_closed=True)
NURSE = boneco("n6", 0, 0, 1.0, jacket="#F4F4F0", hat="nurse", scarf="#C1121F", pants="#8D99AE", hair="#3b2a1a", worried=False)
SHRUG = boneco("h8", 0, 0, 1.0, jacket="#6A994E", hat="beanie", hat_color="#E9C46A", scarf="#3A6EA5")
INV = ""

# ---------- S1: a praia ----------
scene("s1", """
    #s1-big { top:330px; font-size:150px; font-weight:700; line-height:0.95; }
    #s1-tag { top:500px; font-size:32px; color:#8FA3B0; }
    #s1-beach { position:absolute; left:0; top:680px; width:1080px; height:420px; }
    #s1-doc { position:absolute; left:250px; top:575px; width:580px; white-space:nowrap; text-align:center; font-size:50px; font-weight:700; color:#D7263D; border:6px solid #D7263D; padding:4px 0; }
""", f"""
      <div id="s1-big" class="center">SEM NOME.</div>
      <div id="s1-tag" class="center mono">1948 · SOMERTON · AUSTRÁLIA</div>
      <svg id="s1-beach" data-layout-ignore viewBox="0 60 1080 460" preserveAspectRatio="xMidYMid slice">
        <rect x="0" y="120" width="1080" height="400" fill="#1b1d22"/>
        <path id="s1-wave1" d="M-200 150 Q-100 130 0 150 T200 150 T400 150 T600 150 T800 150 T1000 150 T1200 150 T1400 150" stroke="#3A6EA5" stroke-width="6" fill="none" opacity="0.7"/>
        <path id="s1-wave2" d="M-200 190 Q-100 170 0 190 T200 190 T400 190 T600 190 T800 190 T1000 190 T1200 190 T1400 190" stroke="#3A6EA5" stroke-width="4" fill="none" opacity="0.45"/>
        <rect x="0" y="230" width="1080" height="290" fill="#3b3428"/>
        <rect x="620" y="250" width="460" height="150" fill="#4a4a50"/>
        <path d="M620 290 L1080 290 M620 330 L1080 330 M620 370 L1080 370" stroke="#3a3a40" stroke-width="4"/>
        <g transform="translate(700 430) rotate(-90) scale(0.95)">{BODY}</g>
      </svg>
      <div id="s1-doc" class="mono">SEM DOCUMENTOS</div>
""", """
    tl.fromTo("#s1-wave1", { x: 0 }, { x: -200, duration: D, ease: "none" }, 0);
    tl.fromTo("#s1-wave2", { x: -100 }, { x: 100, duration: D, ease: "none" }, 0);
    tl.fromTo("#s1-tag", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.4, ease: "power4.out" }, 0.4);
    tl.fromTo("#s1-big", { scale: 1 }, { scale: 1.06, duration: 0.18, yoyo: true, repeat: 1, ease: "power2.out" }, @l1:10@);
    tl.fromTo("#s1-doc", { opacity: 0, scale: 2, rotation: -12 }, { opacity: 1, scale: 1, rotation: -6, duration: 0.16, ease: "power4.in" }, @l1:18@);
""")

# ---------- S2: etiquetas cortadas ----------
scene("s2", """
    #s2-t1 { top:335px; font-size:48px; font-weight:700; color:#8FA3B0; }
    #s2-shirt { position:absolute; left:240px; top:430px; width:600px; height:520px; }
    #s2-t2 { top:960px; font-size:96px; font-weight:700; color:#D7263D; }
""", """
      <div id="s2-t1" class="center mono">ETIQUETAS DAS ROUPAS</div>
      <svg id="s2-shirt" data-layout-ignore viewBox="0 0 600 520">
        <path d="M180 40 L240 20 Q300 60 360 20 L420 40 L560 120 L510 220 L450 190 L450 500 L150 500 L150 190 L90 220 L40 120 Z" fill="#5c6370" stroke="#E8E4DA" stroke-width="5"/>
        <path d="M240 20 Q300 90 360 20" fill="none" stroke="#E8E4DA" stroke-width="5"/>
        <g id="s2-tag"><rect x="262" y="70" width="76" height="50" fill="#E8E4DA"/><text x="300" y="102" font-family="Space Mono" font-size="16" text-anchor="middle" fill="#111">MARCA</text></g>
        <path id="s2-cut" d="M240 66 L360 66" stroke="#D7263D" stroke-width="5" stroke-dasharray="10 8"/>
      </svg>
      <div id="s2-t2" class="center">CORTADAS</div>
""", """
    tl.fromTo("#s2-t1", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.1);
    tl.fromTo("#s2-shirt", { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "power4.out" }, 0.15);
    tl.fromTo("#s2-cut", { opacity: 0 }, { opacity: 1, duration: 0.2 }, @l2:5@);
    tl.fromTo("#s2-tag", { y: 0, rotation: 0, opacity: 1, transformOrigin: "50% 0%" }, { y: 380, rotation: 40, opacity: 0, duration: 0.9, ease: "power2.in" }, @l2:7@);
    tl.fromTo("#s2-t2", { opacity: 0, scale: 1.5 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.out" }, @l2:7@);
""")

# ---------- S3: veneno? ----------
scene("s3", """
    #s3-bottle { position:absolute; left:390px; top:340px; width:300px; height:460px; }
    #s3-x { position:absolute; left:340px; top:380px; width:400px; height:400px; }
    #s3-t { top:850px; font-size:92px; font-weight:700; line-height:1.05; }
""", """
      <svg id="s3-bottle" data-layout-ignore viewBox="0 0 300 460">
        <rect x="120" y="10" width="60" height="50" rx="6" fill="#8D99AE"/>
        <path d="M110 60 L190 60 L190 120 Q270 160 270 240 L270 430 Q270 450 250 450 L50 450 Q30 450 30 430 L30 240 Q30 160 110 120 Z" fill="#7B2CBF" opacity="0.85"/>
        <rect x="60" y="250" width="180" height="120" rx="8" fill="#E8E4DA"/>
        <text x="150" y="330" font-family="Oswald" font-weight="700" font-size="80" text-anchor="middle" fill="#7B2CBF">?</text>
      </svg>
      <svg id="s3-x" data-layout-ignore viewBox="0 0 400 400">
        <path id="s3-x1" d="M40 40 L360 360" stroke="#D7263D" stroke-width="22" stroke-linecap="round" stroke-dasharray="460" stroke-dashoffset="460"/>
        <path id="s3-x2" d="M360 40 L40 360" stroke="#D7263D" stroke-width="22" stroke-linecap="round" stroke-dasharray="460" stroke-dashoffset="460"/>
      </svg>
      <div id="s3-t" class="center">VENENO?<br><span class="red">NENHUM.</span></div>
""", """
    tl.fromTo("#s3-bottle", { opacity: 0, y: 80, rotation: -8 }, { opacity: 1, y: 0, rotation: 0, duration: 0.5, ease: "back.out(2)" }, 0.1);
    tl.fromTo("#s3-t", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l3:4@);
    tl.fromTo("#s3-x1", { strokeDashoffset: 460 }, { strokeDashoffset: 0, duration: 0.18, ease: "power4.out" }, @l3:6@);
    tl.fromTo("#s3-x2", { strokeDashoffset: 460 }, { strokeDashoffset: 0, duration: 0.18, ease: "power4.out" }, @l3:6+0.12@);
""")

# ---------- S4: Tamám Shud ----------
scene("s4", """
    #s4-k { top:330px; font-size:40px; color:#8FA3B0; }
    #s4-paper { position:absolute; left:140px; top:470px; width:800px; height:260px; background:#e6dcc3; border-radius:6px; transform-origin:50% 50%; box-shadow:0 20px 50px rgba(0,0,0,0.6); }
    #s4-words { position:absolute; left:140px; top:530px; width:800px; text-align:center; font-family:'Playfair Display',serif; font-style:italic; font-size:120px; color:#1a1a1a; }
    #s4-mean { top:800px; font-size:84px; font-weight:700; }
""", """
      <div id="s4-k" class="center mono">BOLSO SECRETO DA CALÇA</div>
      <div id="s4-paper"></div>
      <div id="s4-words">Tamám Shud</div>
      <div id="s4-mean" class="center">= <span class="red">"ESTÁ TERMINADO"</span></div>
""", """
    tl.fromTo("#s4-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.1);
    tl.fromTo("#s4-paper", { scaleX: 0.06, opacity: 0 }, { scaleX: 1, opacity: 1, duration: 0.6, ease: "power3.inOut" }, @l4:7-0.3@);
    tl.fromTo("#s4-words", { opacity: 0, scale: 1.25 }, { opacity: 1, scale: 1, duration: 0.6, ease: "power3.out" }, @l4:9@);
    tl.fromTo("#s4-mean", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l4:13@);
""")

# ---------- S5: o livro e o código ----------
CODE = ["WRGOABABD", "MLIAOI", "WTBIMPANETP", "MLIABOAIAQC", "ITTMTSAMSTGAB"]
code_html = "".join(f'<div class="s5-c" id="s5-c{i}">{c}</div>' for i, c in enumerate(CODE))
scene("s5", """
    #s5-book { position:absolute; left:170px; top:375px; width:740px; height:660px; background:#2a2118; border:5px solid #b08d57; border-radius:10px; box-sizing:border-box; }
    #s5-title { position:absolute; left:0; width:730px; top:30px; text-align:center; font-family:'Space Mono',monospace; font-size:30px; color:#b08d57; letter-spacing:0.2em; }
    #s5-codebox { position:absolute; left:60px; top:110px; width:610px; }
    .s5-c { font-family:'Space Mono',monospace; font-size:52px; letter-spacing:0.12em; color:#E8E4DA; margin-bottom:14px; }
    #s5-stamp { position:absolute; left:230px; top:905px; width:620px; text-align:center; font-size:74px; font-weight:700; color:#D7263D; border:8px solid #D7263D; }
""", f"""
      <div id="s5-book"><div id="s5-title">LIVRO DE POEMAS · CÓDIGO</div><div id="s5-codebox">{code_html}</div></div>
      <div id="s5-stamp">NÃO DECIFRADO</div>
""", """
    tl.fromTo("#s5-book", { opacity: 0, y: 100, rotation: 4 }, { opacity: 1, y: 0, rotation: 0, duration: 0.55, ease: "power4.out" }, 0.1);
    tl.fromTo(".s5-c", { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: 0.15, stagger: 0.28, ease: "power3.out" }, @l5:15@);
    tl.fromTo("#s5-stamp", { opacity: 0, scale: 2.2, rotation: -14 }, { opacity: 0.95, scale: 1, rotation: -7, duration: 0.16, ease: "power4.in" }, @l5:21@);
""")

# ---------- S6: a enfermeira ----------
scene("s6", """
    #s6-card { position:absolute; left:130px; top:400px; width:480px; height:200px; background:#d9d2c0; color:#1a1a1a; padding:30px; box-sizing:border-box; }
    #s6-card .mono { font-size:26px; color:#444; }
    #s6-card b { display:block; font-family:'Space Mono',monospace; font-size:52px; margin-top:20px; }
    #s6-nurse { position:absolute; left:620px; top:350px; width:330px; height:380px; }
    #s6-t1 { top:740px; font-size:56px; color:#8FA3B0; }
    #s6-t2 { top:830px; font-size:120px; font-weight:700; line-height:1; }
""", f"""
      <div id="s6-card"><div class="mono">TELEFONE NO LIVRO</div><b>☎ ████-████</b></div>
      <svg id="s6-nurse" data-layout-ignore viewBox="-150 -345 300 345">{NURSE}</svg>
      <div id="s6-t1" class="center mono">A ENFERMEIRA JUROU:</div>
      <div id="s6-t2" class="center">"<span class="red">NUNCA VI</span>"</div>
""", """
    tl.fromTo("#s6-card", { opacity: 0, x: -200, rotation: -6 }, { opacity: 1, x: 0, rotation: -2, duration: 0.45, ease: "power4.out" }, @l6:5@);
    tl.fromTo("#s6-nurse", { opacity: 0, y: 80 }, { opacity: 1, y: 0, duration: 0.4, ease: "power4.out" }, @l6:8@);
    tl.fromTo("#s6-t1", { opacity: 0 }, { opacity: 1, duration: 0.3 }, @l6:15@);
    tl.fromTo("#n6-head", { rotation: -14, transformOrigin: "50% 100%" }, { rotation: 14, duration: 0.16, yoyo: true, repeat: 5, ease: "sine.inOut" }, @l6:15@);
    tl.fromTo("#s6-t2", { opacity: 0, scale: 1.5 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.out" }, @l6:17@);
""")

# ---------- S7: DNA ----------
rungs = "".join(f'<line class="s7-r" x1="{60 + i*36}" y1="80" x2="{60 + i*36}" y2="220" stroke="#8FA3B0" stroke-width="5"/>' for i in range(22))
scene("s7", """
    #s7-y { top:330px; font-size:150px; font-weight:700; color:#8FA3B0; line-height:1; }
    #s7-dna { position:absolute; left:110px; top:510px; width:860px; height:300px; }
    #s7-k { top:820px; font-size:40px; color:#8FA3B0; }
    #s7-name { top:870px; font-size:150px; font-weight:700; line-height:1; color:#E9C46A; }
""", f"""
      <div id="s7-y" class="center">2022 · DNA</div>
      <svg id="s7-dna" data-layout-ignore viewBox="0 0 860 300">
        <g id="s7-helix">{rungs}
          <path d="M40 150 Q130 20 220 150 T400 150 T580 150 T760 150 T940 150" stroke="#D7263D" stroke-width="10" fill="none"/>
          <path d="M40 150 Q130 280 220 150 T400 150 T580 150 T760 150 T940 150" stroke="#3A6EA5" stroke-width="10" fill="none"/>
        </g>
      </svg>
      <div id="s7-k" class="center mono">O NOME DELE ERA</div>
      <div id="s7-name" class="center">CARL WEBB</div>
""", """
    tl.fromTo("#s7-y", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.05);
    tl.fromTo("#s7-dna", { opacity: 0, scaleX: 0.2 }, { opacity: 1, scaleX: 1, duration: 0.7, ease: "power3.out" }, @l7:8@);
    tl.fromTo("#s7-helix", { x: 0 }, { x: -180, duration: 4, ease: "none" }, @l7:8@);
    tl.fromTo("#s7-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, @l7:11@);
    tl.fromTo("#s7-name", { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, duration: 0.22, ease: "power4.out" }, @l7:15@);
""")

# ---------- S8: ninguém sabe ----------
scene("s8", """
    #s8-q1 { top:330px; font-size:96px; font-weight:700; }
    #s8-q2 { top:460px; font-size:96px; font-weight:700; color:#D7263D; }
    #s8-shrug { position:absolute; left:400px; top:640px; width:280px; height:360px; }
""", f"""
      <div id="s8-q1" class="center">POR QUE MORREU?</div>
      <div id="s8-q2" class="center">O QUE DIZ O CÓDIGO?</div>
      <svg id="s8-shrug" data-layout-ignore viewBox="-140 -345 280 350">{SHRUG}</svg>
""", """
    tl.fromTo("#s8-q1", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, 0.05);
    tl.fromTo("#s8-q2", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }, @l8:5@);
    tl.fromTo("#s8-shrug", { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, @l8:5@);
    tl.fromTo("#h8-armL", { rotation: 0, transformOrigin: "50% 0%" }, { rotation: 120, duration: 0.25, ease: "back.out(2)" }, @l8:11@);
    tl.fromTo("#h8-armR", { rotation: 0, transformOrigin: "50% 0%" }, { rotation: -120, duration: 0.25, ease: "back.out(2)" }, @l8:11@);
    tl.fromTo("#h8-head", { rotation: 0, transformOrigin: "50% 100%" }, { rotation: -10, duration: 0.3, ease: "power2.out" }, @l8:11+0.05@);
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
    #s9-bar { position:absolute; left:130px; top:1080px; width:820px; height:8px; background:#D7263D; transform-origin:0 50%; }
""", """
      <div id="s9-k" class="center mono">EPISÓDIO 03 · VOCÊ DECIDE</div>
      <div id="s9-t" class="center">AMANHÃ, <span class="red">QUAL?</span></div>
      <div id="s9-A" class="s9-card"><div class="s9-let">A</div><div class="s9-txt"><b>ELISA LAM E O HOTEL CECIL</b><span class="mono">LOS ANGELES · 2013</span></div></div>
      <div id="s9-B" class="s9-card"><div class="s9-let">B</div><div class="s9-txt"><b>A MULHER DE ISDAL</b><span class="mono">NORUEGA · 1970</span></div></div>
      <div id="s9-bar"></div>
""", """
    tl.fromTo("#s9-k", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.1);
    tl.fromTo("#s9-t", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }, 0.15);
    tl.fromTo("#s9-A", { opacity: 0, x: -1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l9:3@);
    tl.fromTo("#s9-B", { opacity: 0, x: 1000 }, { opacity: 1, x: 0, duration: 0.45, ease: "power4.out" }, @l9:13@);
    tl.fromTo("#s9-A", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l10:0@);
    tl.fromTo("#s9-B", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 7, ease: "sine.inOut", immediateRender: false }, @l10:0+0.25@);
    tl.fromTo("#s9-bar", { scaleX: 0 }, { scaleX: 1, duration: 3, ease: "none" }, @l10:0+1.2@);
""")
p = "compositions/s9.html"
_c = open(p).read()
open(p, "w").write(_c.replace('tl.to("#s9-cam", { opacity: 0, duration: 0.14, ease: "power2.in" }, D - 0.16);', ""))
