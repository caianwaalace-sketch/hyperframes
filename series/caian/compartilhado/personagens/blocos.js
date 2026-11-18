/* Biblioteca de bonecos de blocos da série Caian (Three.js r147, global THREE).
 * Tudo é função do tempo: nada de relógio, nada de Math.random (usa PRNG com semente).
 * Uso numa cena:  const W = Blocos.mundo(canvas); const caian = Blocos.personagem("caian"); W.scene.add(caian.root);
 *                 caian.pose({...}); caian.rosto("feliz", "aberta"); W.render(camera)
 */
(function () {
  const T = THREE;
  const B = {};
  B.LARG = 1080;
  B.ALT = 1920;

  // ---------- utilidades ----------
  B.prng = function (seed) {
    let a = seed >>> 0;
    return function () {
      a = (a + 0x6d2b79f5) >>> 0;
      let t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  };
  B.clamp = (x, a, b) => Math.max(a, Math.min(b, x));
  B.suave = (x) => {
    x = B.clamp(x, 0, 1);
    return x * x * (3 - 2 * x);
  };
  B.lerp = (a, b, k) => a + (b - a) * k;
  // chaves [[t, valor], ...]; valor número ou array; interpolação suave entre chaves
  B.kf = function (t, keys, ease = B.suave) {
    if (t <= keys[0][0]) return keys[0][1];
    for (let i = 1; i < keys.length; i++) {
      if (t <= keys[i][0]) {
        const [t0, v0] = keys[i - 1];
        const [t1, v1] = keys[i];
        const k = ease((t - t0) / Math.max(1e-6, t1 - t0));
        return Array.isArray(v0) ? v0.map((v, j) => B.lerp(v, v1[j], k)) : B.lerp(v0, v1, k);
      }
    }
    return keys[keys.length - 1][1];
  };
  // estado discreto: [[t, "estado"], ...]
  B.estado = function (t, keys) {
    let s = keys[0][1];
    for (const [k, v] of keys) if (t >= k) s = v;
    return s;
  };

  // volume da fala (0..1) no tempo t, para a boca
  B.volume = function (falas, quem, t) {
    let v = 0;
    for (const f of falas) {
      if (f.quem !== quem) continue;
      const d = window.FALAS[f.id];
      const lt = t - f.ini;
      if (lt < 0 || lt > d.dur) continue;
      const i = lt * 30;
      const i0 = Math.floor(i);
      const a = d.env[i0] || 0;
      const b = d.env[i0 + 1] || 0;
      v = Math.max(v, a + (b - a) * (i - i0));
    }
    return v;
  };
  B.bocaDaFala = function (vol, base) {
    if (vol > 0.42) return "aberta";
    if (vol > 0.12) return "meia";
    return base;
  };

  // ---------- mundo ----------
  B.mundo = function (canvas, opts = {}) {
    const renderer = new T.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true });
    renderer.setPixelRatio(1);
    renderer.setSize(B.LARG, B.ALT, false);
    renderer.outputEncoding = T.sRGBEncoding;
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = T.PCFSoftShadowMap;
    const scene = new T.Scene();
    scene.background = new T.Color(opts.ceu || 0x8fd3ff);
    if (opts.neblina) scene.fog = new T.Fog(opts.ceu || 0x8fd3ff, opts.neblina[0], opts.neblina[1]);
    const hemi = new T.HemisphereLight(0xffffff, 0x8a7a60, opts.hemi ?? 0.75);
    scene.add(hemi);
    const sol = new T.DirectionalLight(0xfff2dc, opts.sol ?? 0.85);
    sol.position.set(8, 18, 12);
    sol.castShadow = true;
    sol.shadow.mapSize.set(1024, 1024);
    const sc = opts.sombra || 16;
    Object.assign(sol.shadow.camera, {
      left: -sc,
      right: sc,
      top: sc,
      bottom: -sc,
      near: 1,
      far: 60,
    });
    sol.shadow.bias = -0.0008;
    scene.add(sol);
    scene.add(sol.target);
    const camera = new T.PerspectiveCamera(opts.fov || 38, B.LARG / B.ALT, 0.1, 400);
    return {
      renderer,
      scene,
      camera,
      sol,
      hemi,
      // camera: posição e alvo [x,y,z]
      camara(pos, alvo, fov) {
        camera.position.set(pos[0], pos[1], pos[2]);
        if (fov && camera.fov !== fov) {
          camera.fov = fov;
          camera.updateProjectionMatrix();
        }
        camera.lookAt(alvo[0], alvo[1], alvo[2]);
      },
      render() {
        renderer.render(scene, camera);
      },
    };
  };

  // ---------- materiais e peças ----------
  const matCache = {};
  B.mat = function (cor, extra) {
    const k = cor + JSON.stringify(extra || {});
    if (!matCache[k])
      matCache[k] = new T.MeshLambertMaterial(Object.assign({ color: cor }, extra || {}));
    return matCache[k];
  };
  B.bloco = function (w, h, d, cor, r = 0.12) {
    const g = T.RoundedBoxGeometry
      ? new T.RoundedBoxGeometry(w, h, d, 2, Math.min(r, w / 2.2, h / 2.2, d / 2.2))
      : new T.BoxGeometry(w, h, d);
    const m = new T.Mesh(g, typeof cor === "object" ? cor : B.mat(cor));
    m.castShadow = true;
    m.receiveShadow = true;
    return m;
  };
  function canvasTex(w, h, draw) {
    const c = document.createElement("canvas");
    c.width = w;
    c.height = h;
    const ctx = c.getContext("2d");
    draw(ctx, w, h);
    const tex = new T.CanvasTexture(c);
    tex.encoding = T.sRGBEncoding;
    tex.anisotropy = 4;
    return tex;
  }
  B.canvasTex = canvasTex;
  function plano(w, h, tex, z) {
    const m = new T.Mesh(
      new T.PlaneGeometry(w, h),
      new T.MeshLambertMaterial({ map: tex, transparent: true, alphaTest: 0.05 }),
    );
    m.position.z = z;
    return m;
  }
  B.plano = plano;
  B.placa = function (texto, opts = {}) {
    const w = opts.w || 6,
      h = opts.h || 2;
    const tex = canvasTex(1024, Math.round((1024 * h) / w), (ctx, cw, ch) => {
      ctx.fillStyle = opts.fundo || "#3b2414";
      ctx.fillRect(0, 0, cw, ch);
      ctx.strokeStyle = opts.borda || "#ffd23f";
      ctx.lineWidth = 18;
      ctx.strokeRect(9, 9, cw - 18, ch - 18);
      ctx.fillStyle = opts.cor || "#ffffff";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      const linhas = texto.split("\n");
      let fs = opts.fs || Math.min(140, (ch * 0.7) / linhas.length);
      ctx.font = `900 ${fs}px Montserrat, sans-serif`;
      while (fs > 12 && Math.max(...linhas.map((l) => ctx.measureText(l).width)) > cw * 0.88) {
        fs -= 4;
        ctx.font = `900 ${fs}px Montserrat, sans-serif`;
      }
      linhas.forEach((l, i) =>
        ctx.fillText(l, cw / 2, ch / 2 + (i - (linhas.length - 1) / 2) * fs * 1.1),
      );
    });
    const g = new T.Group();
    const face = new T.Mesh(new T.PlaneGeometry(w, h), new T.MeshLambertMaterial({ map: tex }));
    face.position.z = 0.16;
    g.add(face);
    const tabua = B.bloco(w + 0.2, h + 0.2, 0.3, 0x5a3a22, 0.06);
    g.add(tabua);
    return g;
  };

  // ---------- rostos ----------
  const ROSTOS = {
    caian: { sobr: "fina", estrela: true },
    lia: { oculos: "#1b1b1b", sobr: "media" },
    kaio: { sobr: "metida" },
    tonhao: { sobr: "preocupada" },
    juca: { bigode: "#f4f4f4", oculos: "#5a3a22", sobr: "branca" },
    pedrita: { pedra: true },
  };
  const rostoCache = {};
  function desenhaRosto(ctx, w, quem, olhos, boca) {
    const f = ROSTOS[quem];
    const s = w / 256;
    ctx.save();
    ctx.scale(s, s);
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    const ink = "#151515";
    const eyeY = f.pedra ? 120 : 104;
    const ex = f.pedra ? 62 : 52;
    // olhos
    for (const side of [-1, 1]) {
      const x = 128 + side * ex;
      ctx.fillStyle = ink;
      ctx.strokeStyle = ink;
      if (olhos === "fechado") {
        ctx.lineWidth = 7;
        ctx.beginPath();
        ctx.moveTo(x - 14, eyeY);
        ctx.lineTo(x + 14, eyeY);
        ctx.stroke();
      } else if (olhos === "feliz") {
        ctx.lineWidth = 8;
        ctx.beginPath();
        ctx.arc(x, eyeY + 6, 14, Math.PI * 1.1, Math.PI * 1.9);
        ctx.stroke();
      } else {
        const big = olhos === "arregalado" ? 1.45 : 1;
        const ry = (f.pedra ? 18 : 17) * big;
        const rx = (f.pedra ? 13 : 10) * big;
        ctx.beginPath();
        ctx.ellipse(x, eyeY, rx, ry, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#ffffff";
        ctx.beginPath();
        ctx.arc(x + rx * 0.3, eyeY - ry * 0.4, 3.6 * big, 0, Math.PI * 2);
        ctx.fill();
      }
      // sobrancelhas
      if (!f.pedra) {
        ctx.strokeStyle = f.sobr === "branca" ? "#e8e8e8" : ink;
        ctx.lineWidth = f.sobr === "fina" ? 5 : 7;
        ctx.beginPath();
        let lift = olhos === "arregalado" ? -10 : 0;
        if (f.sobr === "preocupada") {
          ctx.moveTo(x - side * 18, eyeY - 30 + lift);
          ctx.lineTo(x + side * 14, eyeY - 40 + lift);
        } else if (f.sobr === "metida") {
          ctx.moveTo(x - 16, eyeY - 30 + (side > 0 ? -8 : 2) + lift);
          ctx.lineTo(x + 16, eyeY - 34 + (side > 0 ? -8 : 2) + lift);
        } else {
          ctx.moveTo(x - 17, eyeY - 30 + lift);
          ctx.quadraticCurveTo(x, eyeY - 40 + lift, x + 17, eyeY - 32 + lift);
        }
        ctx.stroke();
      }
    }
    if (f.oculos) {
      ctx.strokeStyle = f.oculos;
      ctx.lineWidth = 6;
      for (const side of [-1, 1]) {
        ctx.beginPath();
        ctx.arc(128 + side * ex, eyeY, 27, 0, Math.PI * 2);
        ctx.stroke();
      }
      ctx.beginPath();
      ctx.moveTo(128 - ex + 27, eyeY);
      ctx.lineTo(128 + ex - 27, eyeY);
      ctx.stroke();
    }
    // boca
    const my = f.pedra ? 180 : 172;
    ctx.fillStyle = ink;
    ctx.strokeStyle = ink;
    ctx.lineWidth = 7;
    if (boca === "sorriso") {
      // sorriso largo de lado, com dentes (como o avatar do Caian)
      ctx.beginPath();
      ctx.moveTo(84, my - 10);
      ctx.quadraticCurveTo(128, my + 4, 182, my - 22);
      ctx.quadraticCurveTo(160, my + 36, 120, my + 34);
      ctx.quadraticCurveTo(92, my + 30, 84, my - 10);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.beginPath();
      ctx.moveTo(92, my - 6);
      ctx.quadraticCurveTo(128, my + 6, 174, my - 16);
      ctx.lineTo(170, my - 2);
      ctx.quadraticCurveTo(128, my + 16, 96, my + 6);
      ctx.fill();
    } else if (boca === "aberta" || boca === "meia") {
      const h = boca === "aberta" ? 30 : 16;
      ctx.beginPath();
      ctx.ellipse(130, my, 30, h, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.fillRect(108, my - h + 2, 44, Math.min(9, h * 0.45));
      if (boca === "aberta") {
        ctx.fillStyle = "#d9445a";
        ctx.beginPath();
        ctx.ellipse(130, my + h * 0.55, 16, 8, 0, 0, Math.PI * 2);
        ctx.fill();
      }
    } else if (boca === "o") {
      ctx.beginPath();
      ctx.ellipse(128, my + 4, 13, 17, 0, 0, Math.PI * 2);
      ctx.fill();
    } else if (boca === "triste") {
      ctx.beginPath();
      ctx.arc(128, my + 24, 26, Math.PI * 1.15, Math.PI * 1.85);
      ctx.stroke();
    } else if (boca === "reta") {
      ctx.beginPath();
      ctx.moveTo(104, my + 2);
      ctx.lineTo(152, my + 2);
      ctx.stroke();
    } else {
      // "leve": sorriso pequeno
      ctx.beginPath();
      ctx.arc(128, my - 16, 26, Math.PI * 0.2, Math.PI * 0.8);
      ctx.stroke();
    }
    if (f.bigode) {
      ctx.fillStyle = f.bigode;
      ctx.strokeStyle = "#9a9a9a";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(78, my - 12);
      ctx.quadraticCurveTo(100, my - 40, 128, my - 22);
      ctx.quadraticCurveTo(156, my - 40, 178, my - 12);
      ctx.quadraticCurveTo(150, my - 18, 128, my - 10);
      ctx.quadraticCurveTo(106, my - 18, 78, my - 12);
      ctx.fill();
      ctx.stroke();
    }
    ctx.restore();
  }
  function desenhaEstrela(ctx, w, k) {
    if (!k) return;
    const s = w / 256;
    const x = 196 * s,
      y = 168 * s,
      r = (16 + 10 * k) * s;
    ctx.fillStyle = "#ffffff";
    ctx.strokeStyle = "#1a1a1a";
    ctx.lineWidth = 3 * s;
    ctx.beginPath();
    for (let i = 0; i < 8; i++) {
      const a = (Math.PI / 4) * i - Math.PI / 2;
      const rr = i % 2 ? r * 0.28 : r;
      ctx.lineTo(x + Math.cos(a) * rr, y + Math.sin(a) * rr);
    }
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
  }
  function rostoMat(quem, olhos, boca, estrela) {
    const k = `${quem}|${olhos}|${boca}|${estrela}`;
    if (!rostoCache[k]) {
      const tex = canvasTex(256, 256, (ctx, w) => {
        desenhaRosto(ctx, w, quem, olhos, boca);
        if (ROSTOS[quem].estrela) desenhaEstrela(ctx, w, estrela);
      });
      rostoCache[k] = new T.MeshLambertMaterial({ map: tex, transparent: true, alphaTest: 0.05 });
    }
    return rostoCache[k];
  }

  // ---------- texturas de roupa ----------
  function texCamiseta(texto, cor, corTexto) {
    return canvasTex(512, 512, (ctx, w, h) => {
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = corTexto;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      let fs = 96;
      ctx.font = `900 ${fs}px Montserrat, sans-serif`;
      while (ctx.measureText(texto).width > w * 0.9 && fs > 20) {
        fs -= 2;
        ctx.font = `900 ${fs}px Montserrat, sans-serif`;
      }
      ctx.fillText(texto, w / 2, h * 0.42);
    });
  }
  function texTatuagem(seed) {
    const rnd = B.prng(seed);
    return canvasTex(128, 256, (ctx, w, h) => {
      ctx.clearRect(0, 0, w, h);
      ctx.strokeStyle = "rgba(25,22,22,0.85)";
      ctx.lineCap = "round";
      for (let i = 0; i < 26; i++) {
        ctx.lineWidth = 2 + rnd() * 4;
        ctx.beginPath();
        const x = rnd() * w,
          y = 30 + rnd() * (h - 40);
        ctx.moveTo(x, y);
        ctx.bezierCurveTo(
          x + (rnd() - 0.5) * 60,
          y + (rnd() - 0.5) * 50,
          x + (rnd() - 0.5) * 60,
          y + (rnd() - 0.5) * 50,
          x + (rnd() - 0.5) * 40,
          y + (rnd() - 0.5) * 40,
        );
        ctx.stroke();
      }
      ctx.fillStyle = "rgba(25,22,22,0.85)";
      ctx.beginPath();
      ctx.arc(w * 0.5, h * 0.55, 16, 0, Math.PI * 2);
      ctx.fill();
    });
  }

  // ---------- personagens ----------
  const SPECS = {
    caian: {
      pele: 0xe8c4a0,
      tronco: 0x161616,
      braco: "pele",
      manga: 0x161616,
      perna: 0x141414,
      tenis: 0x1a1a1a,
      sola: 0xffffff,
      cabelo: 0x3b2a20,
      estampa: "@caianwaalacee",
      corrente: 0xd4af37,
      tatuagem: true,
      pulseira: 0xd4af37,
      correntinha: 0xc8ccd2,
      escala: 1,
    },
    lia: {
      pele: 0x6b4128,
      tronco: 0x2ec4b6,
      braco: 0x2ec4b6,
      perna: 0x2b2d42,
      tenis: 0xffffff,
      sola: 0xdddddd,
      cabelo: 0x7b2cbf,
      cacheado: true,
      escala: 0.94,
    },
    kaio: {
      pele: 0xf3d5c0,
      tronco: 0xf2f2f2,
      braco: 0xf2f2f2,
      perna: 0xc9ced6,
      tenis: 0xc9ced6,
      sola: 0xffffff,
      cabelo: 0xf5d76e,
      topete: true,
      bone: 0xb8bec8,
      escala: 1,
    },
    tonhao: {
      pele: 0xb07a4f,
      tronco: 0xd62828,
      braco: "pele",
      perna: 0x3a3a3a,
      tenis: 0x222222,
      sola: 0xffffff,
      cabelo: 0x1d1d1d,
      bandana: 0x1f6bff,
      escala: 1.45,
    },
    juca: {
      pele: 0xf0c8a8,
      tronco: 0x6b4423,
      braco: 0xd9d4c7,
      perna: 0x5a5a5a,
      tenis: 0x3b2a20,
      sola: 0x2a1d14,
      cabelo: 0xeeeeee,
      careca: true,
      avental: 0x8b5a2b,
      escala: 0.95,
    },
  };

  B.personagem = function (quem) {
    const sp = SPECS[quem];
    const root = new T.Group();
    const corpo = new T.Group(); // quadril
    corpo.position.y = 2;
    root.add(corpo);
    const peleCor = sp.pele;
    const tronco = B.bloco(2, 2, 1, sp.tronco, 0.14);
    tronco.position.y = 1;
    corpo.add(tronco);
    if (sp.avental) {
      const av = B.bloco(1.7, 2.6, 0.12, sp.avental, 0.04);
      av.position.set(0, 0.7, 0.52);
      corpo.add(av);
    }
    if (sp.estampa) {
      const tex = texCamiseta(sp.estampa, sp.tronco, "#ffffff");
      const f = plano(1.9, 1.9, tex, 0.515);
      f.position.y = 1;
      corpo.add(f);
      const b = plano(1.9, 1.9, tex, -0.515);
      b.rotation.y = Math.PI;
      b.position.y = 1;
      corpo.add(b);
    }
    if (sp.corrente) {
      const c = new T.Mesh(
        new T.TorusGeometry(0.62, 0.09, 6, 18),
        B.mat(sp.corrente, { emissive: 0x3a2a00 }),
      );
      c.rotation.x = Math.PI / 2.6;
      c.position.set(0, 1.78, 0.18);
      c.castShadow = true;
      corpo.add(c);
    }
    if (sp.correntinha) {
      const c = new T.Mesh(new T.TorusGeometry(0.32, 0.035, 5, 14, Math.PI), B.mat(sp.correntinha));
      c.rotation.z = Math.PI;
      c.position.set(-0.75, -0.25, 0.53);
      corpo.add(c);
    }
    // cabeça
    const cabecaPiv = new T.Group();
    cabecaPiv.position.y = 2;
    corpo.add(cabecaPiv);
    const cab = B.bloco(1.25, 1.25, 1.25, peleCor, 0.3);
    cab.position.y = 0.66;
    cabecaPiv.add(cab);
    const rosto = new T.Mesh(new T.PlaneGeometry(1.15, 1.15), rostoMat(quem, "normal", "leve", 0));
    rosto.position.set(0, 0.66, 0.632);
    cabecaPiv.add(rosto);
    // cabelo
    const hair = (w, h, d, x, y, z, rx = 0, rz = 0) => {
      const m = B.bloco(w, h, d, sp.cabelo, 0.1);
      m.position.set(x, y, z);
      m.rotation.set(rx, 0, rz);
      cabecaPiv.add(m);
      return m;
    };
    if (quem === "caian") {
      hair(1.36, 0.34, 1.36, 0, 1.36, -0.02);
      hair(0.7, 0.36, 1.2, 0.3, 1.58, 0.05, 0, -0.25);
      hair(0.62, 0.3, 1.1, -0.28, 1.56, -0.05, 0, 0.3);
      hair(1.36, 0.8, 0.22, 0, 1.0, -0.6);
      hair(0.2, 0.62, 1.1, -0.66, 1.08, -0.05);
      hair(0.2, 0.62, 1.1, 0.66, 1.08, -0.05);
      hair(0.6, 0.28, 0.3, 0.32, 1.25, 0.6, 0.3, -0.35);
    } else if (sp.cacheado) {
      const rnd = B.prng(7);
      for (let i = 0; i < 16; i++) {
        const a = (i / 16) * Math.PI * 2;
        const m = B.bloco(0.5, 0.5, 0.5, sp.cabelo, 0.2);
        m.position.set(Math.cos(a) * 0.72, 1.2 + rnd() * 0.35, Math.sin(a) * 0.72 - 0.05);
        if (m.position.z > 0.5) m.position.y += 0.15;
        cabecaPiv.add(m);
      }
      hair(1.4, 0.5, 1.4, 0, 1.46, 0);
    } else if (sp.topete) {
      hair(1.34, 0.26, 1.34, 0, 1.36, 0);
      hair(0.9, 0.5, 0.6, 0.1, 1.6, 0.45, -0.4, -0.1);
    } else if (sp.careca) {
      hair(0.18, 0.4, 0.9, -0.66, 0.9, -0.1);
      hair(0.18, 0.4, 0.9, 0.66, 0.9, -0.1);
      hair(1.3, 0.4, 0.2, 0, 0.9, -0.62);
    } else {
      hair(1.32, 0.24, 1.32, 0, 1.36, 0);
    }
    let bone = null;
    if (sp.bone) {
      bone = new T.Group();
      const top = B.bloco(1.42, 0.38, 1.42, sp.bone, 0.15);
      const aba = B.bloco(1.2, 0.1, 0.8, sp.bone, 0.04);
      aba.position.set(0, -0.12, 0.9);
      bone.add(top, aba);
      bone.position.y = 1.5;
      cabecaPiv.add(bone);
    }
    if (sp.bandana) {
      const bd = B.bloco(1.32, 0.26, 1.32, sp.bandana, 0.08);
      bd.position.y = 1.12;
      cabecaPiv.add(bd);
    }
    // braços e pernas
    const membro = (x, y, cor, manga, isLeg) => {
      const piv = new T.Group();
      piv.position.set(x, y, 0);
      corpo.add(piv);
      const corM = cor === "pele" ? peleCor : cor;
      const m = B.bloco(0.96, 2, 1, corM, 0.16);
      m.position.y = -1;
      piv.add(m);
      if (manga && cor === "pele") {
        const mg = B.bloco(1.02, 0.7, 1.06, manga, 0.12);
        mg.position.y = -0.32;
        piv.add(mg);
      }
      if (isLeg) {
        const t = B.bloco(1.0, 0.55, 1.06, sp.tenis, 0.12);
        t.position.set(0, -1.72, 0.02);
        piv.add(t);
        const s = B.bloco(1.04, 0.16, 1.2, sp.sola, 0.05);
        s.position.set(0, -1.94, 0.06);
        piv.add(s);
      }
      return piv;
    };
    const bracoE = membro(-1.5, 1.95, sp.braco, sp.manga, false);
    const bracoD = membro(1.5, 1.95, sp.braco, sp.manga, false);
    const pernaE = membro(-0.5, 0, sp.perna, null, true);
    const pernaD = membro(0.5, 0, sp.perna, null, true);
    if (sp.tatuagem) {
      for (const [piv, seed] of [
        [bracoE, 3],
        [bracoD, 5],
      ]) {
        const tex = texTatuagem(seed);
        const f = plano(0.8, 1.3, tex, 0.505);
        f.position.y = -1.25;
        piv.add(f);
        const lado = plano(0.8, 1.3, tex, 0);
        lado.rotation.y = piv === bracoE ? -Math.PI / 2 : Math.PI / 2;
        lado.position.set(piv === bracoE ? -0.485 : 0.485, -1.25, 0);
        piv.add(lado);
      }
    }
    if (sp.pulseira) {
      const p = new T.Mesh(
        new T.TorusGeometry(0.55, 0.07, 5, 14),
        B.mat(sp.pulseira, { emissive: 0x3a2a00 }),
      );
      p.rotation.x = Math.PI / 2;
      p.position.y = -1.7;
      bracoE.add(p);
    }
    root.scale.setScalar(sp.escala);

    const P = {
      quem,
      root,
      corpo,
      cabeca: cabecaPiv,
      bracoE,
      bracoD,
      pernaE,
      pernaD,
      bone,
      rostoMesh: rosto,
      // pose: ângulos em radianos; andar: fase (s) para o ciclo de passos
      pose(o = {}) {
        const fase = o.andar ?? null;
        let sw = 0,
          bob = 0;
        if (fase !== null) {
          sw = Math.sin(fase * Math.PI * 2) * (o.passo ?? 0.7);
          bob = Math.abs(Math.cos(fase * Math.PI * 2)) * 0.12;
        }
        pernaE.rotation.x = sw + (o.pernaE || 0);
        pernaD.rotation.x = -sw + (o.pernaD || 0);
        bracoE.rotation.set(-sw * 0.8 + (o.bracoE?.[0] || 0), 0, o.bracoE?.[2] || 0);
        bracoD.rotation.set(sw * 0.8 + (o.bracoD?.[0] || 0), 0, o.bracoD?.[2] || 0);
        corpo.position.y = 2 + bob + (o.y || 0);
        corpo.rotation.set(o.inclina || 0, 0, o.lado || 0);
        cabecaPiv.rotation.set(o.cabX || 0, o.cabY || 0, o.cabZ || 0);
      },
      rosto(olhos, boca, estrela = 0) {
        rosto.material = rostoMat(quem, olhos, boca, Math.round(estrela * 4) / 4);
      },
    };
    return P;
  };

  // piscar natural, determinístico: devolve true quando os olhos devem estar fechados
  B.piscando = function (t, seed) {
    const rnd = B.prng(seed);
    let at = 0.6 + rnd() * 1.5;
    while (at < t + 1) {
      if (t >= at && t < at + 0.12) return true;
      at += 2.2 + rnd() * 2.6;
    }
    return false;
  };

  // ---------- Pedrita, dragão, ovo ----------
  B.pedrita = function () {
    const root = new T.Group();
    const corpo = new T.Group();
    root.add(corpo);
    const m = new T.MeshLambertMaterial({ color: 0x8d8d93 });
    const pedra = B.bloco(1.2, 1.0, 1.1, m, 0.3);
    pedra.position.y = 0.5;
    corpo.add(pedra);
    const rnd = B.prng(11);
    for (let i = 0; i < 5; i++) {
      const s = B.bloco(0.3 + rnd() * 0.2, 0.2, 0.3, 0x737378, 0.08);
      s.position.set((rnd() - 0.5) * 0.9, 0.96, (rnd() - 0.5) * 0.8);
      corpo.add(s);
    }
    const rosto = new T.Mesh(
      new T.PlaneGeometry(1.0, 1.0),
      rostoMat("pedrita", "normal", "leve", 0),
    );
    rosto.position.set(0, 0.52, 0.565);
    corpo.add(rosto);
    return {
      root,
      corpo,
      material: m,
      rostoMesh: rosto,
      rosto(olhos, boca) {
        rosto.material = rostoMat("pedrita", olhos, boca, 0);
      },
    };
  };

  B.dragao = function () {
    const root = new T.Group();
    const vermelho = 0xe63946,
      barriga = 0xffb703;
    const corpo = B.bloco(1.4, 1.1, 2.2, vermelho, 0.3);
    root.add(corpo);
    const bar = B.bloco(1.0, 0.5, 1.6, barriga, 0.2);
    bar.position.set(0, -0.35, 0.1);
    root.add(bar);
    const cab = new T.Group();
    cab.position.set(0, 0.7, 1.3);
    root.add(cab);
    const c = B.bloco(1.1, 0.9, 1.1, vermelho, 0.25);
    cab.add(c);
    const foc = B.bloco(0.8, 0.5, 0.7, vermelho, 0.15);
    foc.position.set(0, -0.15, 0.7);
    cab.add(foc);
    const boca = B.bloco(0.78, 0.18, 0.66, 0x3a0a0a, 0.05);
    boca.position.set(0, -0.42, 0.68);
    cab.add(boca);
    for (const s of [-1, 1]) {
      const o = B.bloco(0.18, 0.22, 0.05, 0xffffff, 0.04);
      o.position.set(s * 0.3, 0.12, 0.56);
      cab.add(o);
      const pu = B.bloco(0.1, 0.14, 0.05, 0x111111, 0.02);
      pu.position.set(s * 0.3, 0.1, 0.59);
      cab.add(pu);
      const ch = B.bloco(0.14, 0.4, 0.14, 0xfff1c1, 0.05);
      ch.position.set(s * 0.35, 0.6, -0.2);
      ch.rotation.x = -0.4;
      cab.add(ch);
    }
    const asaE = new T.Group();
    const asaD = new T.Group();
    asaE.position.set(-0.6, 0.4, 0);
    asaD.position.set(0.6, 0.4, 0);
    const a1 = B.bloco(1.8, 0.1, 1.2, 0xff7b7b, 0.04);
    a1.position.x = -0.9;
    asaE.add(a1);
    const a2 = B.bloco(1.8, 0.1, 1.2, 0xff7b7b, 0.04);
    a2.position.x = 0.9;
    asaD.add(a2);
    root.add(asaE, asaD);
    const cauda = B.bloco(0.4, 0.4, 1.6, vermelho, 0.15);
    cauda.position.set(0, 0, -1.7);
    cauda.rotation.x = 0.3;
    root.add(cauda);
    return {
      root,
      cabeca: cab,
      boca,
      bater(t) {
        const a = Math.sin(t * Math.PI * 2 * 3) * 0.7;
        asaE.rotation.z = a;
        asaD.rotation.z = -a;
      },
      morder(k) {
        boca.position.y = -0.42 - k * 0.25;
      },
    };
  };

  B.ovo = function (cor = 0xbfbfbf) {
    const root = new T.Group();
    const m = new T.MeshLambertMaterial({ color: cor });
    const g = new T.SphereGeometry(0.8, 18, 14);
    const metadeCima = new T.Mesh(
      new T.SphereGeometry(0.8, 18, 10, 0, Math.PI * 2, 0, Math.PI / 2),
      m,
    );
    const metadeBaixo = new T.Mesh(
      new T.SphereGeometry(0.8, 18, 10, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2),
      m,
    );
    for (const h of [metadeCima, metadeBaixo]) {
      h.scale.set(1, 1.3, 1);
      h.castShadow = true;
      h.receiveShadow = true;
    }
    const cima = new T.Group();
    cima.add(metadeCima);
    const baixo = new T.Group();
    baixo.add(metadeBaixo);
    root.add(cima, baixo);
    // manchinhas de poeira
    const rnd = B.prng(5);
    for (let i = 0; i < 6; i++) {
      const s = new T.Mesh(new T.SphereGeometry(0.12, 6, 5), B.mat(0x9a9a9a));
      const a = rnd() * Math.PI * 2,
        y = (rnd() - 0.3) * 0.8;
      s.position.set(Math.cos(a) * 0.74, y, Math.sin(a) * 0.74);
      (y > 0 ? cima : baixo).add(s);
    }
    g.dispose();
    root.position.y = 1.04;
    return { root, cima, baixo, material: m };
  };

  // ---------- cenário ----------
  B.chao = function (w, d, cor, cor2, tam = 2) {
    const tex = canvasTex(256, 256, (ctx, cw) => {
      ctx.fillStyle = cor;
      ctx.fillRect(0, 0, cw, cw);
      ctx.strokeStyle = cor2;
      ctx.lineWidth = 6;
      ctx.strokeRect(0, 0, cw, cw);
    });
    tex.wrapS = tex.wrapT = T.RepeatWrapping;
    tex.repeat.set(w / tam, d / tam);
    const m = new T.Mesh(new T.PlaneGeometry(w, d), new T.MeshLambertMaterial({ map: tex }));
    m.rotation.x = -Math.PI / 2;
    m.receiveShadow = true;
    return m;
  };

  // ---------- câmera por planos ----------
  // planos: [{a, b, de:[px,py,pz, ax,ay,az], para:[...], fov}] — a câmera vai de "de" a "para" dentro do plano
  B.planos = function (W, t, planos) {
    let p = planos[0];
    for (const q of planos) if (t >= q.a) p = q;
    const k = Math.sin((Math.PI / 2) * B.clamp((t - p.a) / Math.max(0.01, p.b - p.a), 0, 1));
    const para = p.para || p.de;
    const v = p.de.map((x, i) =>
      B.lerp(x, para[i], p.linear ? B.clamp((t - p.a) / (p.b - p.a), 0, 1) : k),
    );
    W.camara([v[0], v[1], v[2]], [v[3], v[4], v[5]], p.fov || 38);
    return p;
  };
  // vira o personagem para olhar um ponto (x, z) do chão
  B.olhar = function (obj, x, z) {
    obj.rotation.y = Math.atan2(x - obj.position.x, z - obj.position.z);
  };

  window.Blocos = B;
})();
