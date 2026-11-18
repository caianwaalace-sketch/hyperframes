// Monta os tempos do episódio: lê ferramentas/falas.tsv + assets/lib/falas.js e escreve
//  - assets/lib/ep01.js      (falas com horário de início, usado pelas cenas para mexer a boca)
//  - compositions/legendas.html (legendas coloridas por personagem)
//  - os <audio> de falas e efeitos dentro de index.html (entre os marcadores AUDIO)
// Uso: node ferramentas/montar.mjs   (rodar dentro da pasta do episódio)
import fs from "node:fs";

const INI = {
  n01: 0.3,
  j01: 3.7,
  c01: 7.75,
  l01: 9.5,
  t01: 12.0,
  c02: 15.1,
  l02: 17.0,
  k01: 19.3,
  c03: 23.35,
  n02: 25.9,
  n03: 30.6,
  k02: 33.0,
  k03: 35.1,
  t02: 37.35,
  c04: 39.7,
  l03: 41.6,
  c05: 43.5,
  k04: 47.6,
  c06: 49.8,
  c07: 51.6,
  c08: 53.65,
  c09: 57.5,
  c10: 59.1,
};
const CENAS = { loja: [0, 25.7], desafio: [25.7, 51.4], final: [51.4, 61.6] };
const TOTAL = 61.6;
// efeitos sonoros: [arquivo, início, volume]
const SFX = [
  ["ping.mp3", 4.0, 0.35],
  ["pop.mp3", 4.4, 0.35],
  ["ping.mp3", 4.8, 0.35],
  ["sparkle.mp3", 7.85, 0.3],
  ["click.mp3", 13.0, 0.6],
  ["click.mp3", 13.6, 0.6],
  ["pop.mp3", 14.2, 0.5],
  ["sparkle.mp3", 17.0, 0.25],
  ["whoosh.mp3", 19.25, 0.35],
  ["pop.mp3", 25.15, 0.45],
  ["whoosh-short.mp3", 25.6, 0.3],
  ["pop.mp3", 27.95, 0.4],
  ["pop.mp3", 29.3, 0.4],
  ["whoosh-cinematic.mp3", 30.4, 0.3],
  ["whoosh.mp3", 34.8, 0.4],
  ["whoosh-short.mp3", 37.6, 0.35],
  ["impact-bass-1.mp3", 40.1, 0.45],
  ["sparkle.mp3", 42.1, 0.35],
  ["whoosh-short.mp3", 45.0, 0.4],
  ["impact-bass-2.mp3", 47.3, 0.35],
  ["chime.mp3", 47.35, 0.35],
  ["sparkle.mp3", 51.0, 0.25],
  ["pop.mp3", 53.7, 0.45],
  ["pop.mp3", 57.55, 0.45],
  ["chime.mp3", 59.1, 0.3],
];
const COR = {
  NAR: "#ffffff",
  CAIAN: "#ffcf3f",
  LIA: "#5ee6d8",
  KAIO: "#d9dee6",
  TONHAO: "#ff6b5e",
  JUCA: "#f2b880",
};

const falasTsv = fs
  .readFileSync("ferramentas/falas.tsv", "utf8")
  .trim()
  .split("\n")
  .map((l) => l.split("\t"));
const FALAS = JSON.parse(
  fs
    .readFileSync("assets/lib/falas.js", "utf8")
    .replace(/^window\.FALAS = /, "")
    .replace(/;\s*$/, ""),
);
const r3 = (n) => Math.round(n * 1000) / 1000;

const falas = falasTsv.map(([id, quem, texto]) => ({
  id,
  quem,
  texto,
  ini: INI[id],
  dur: FALAS[id].dur,
}));
for (const f of falas) if (f.ini === undefined) throw new Error("sem horário: " + f.id);

// tempo das palavras: trechos de fala (pelo volume) + peso por vogais
function palavras(f) {
  const env = FALAS[f.id].env;
  const on = env.map((v) => v > 0.06);
  let a = on.indexOf(true),
    b = on.lastIndexOf(true);
  if (a < 0) {
    a = 0;
    b = env.length - 1;
  }
  const s0 = a / 30,
    s1 = (b + 1) / 30;
  const ws = f.texto.split(/\s+/);
  const w8 = (w) => Math.max(1, (w.match(/[aeiouáéíóúâêôãõà]/gi) || []).length) + 0.3;
  const tot = ws.reduce((x, w) => x + w8(w), 0);
  let t = s0;
  return ws.map((w) => {
    const d = ((s1 - s0) * w8(w)) / tot;
    const o = { w, s: r3(f.ini + t), e: r3(f.ini + t + d) };
    t += d;
    return o;
  });
}

// grupos de legenda: até 3 palavras, quebra em pontuação
const grupos = [];
for (const f of falas) {
  const ps = palavras(f);
  let g = [];
  const flush = () => {
    if (g.length) grupos.push({ quem: f.quem, ws: g });
    g = [];
  };
  ps.forEach((p) => {
    g.push(p);
    if (/[.,:?!…]$/.test(p.w) || g.length === 3) flush();
  });
  flush();
}
grupos.forEach((g, i) => {
  g.s = r3(Math.max(0.15, g.ws[0].s - 0.05));
  const prox = grupos[i + 1];
  g.e = r3(g.ws[g.ws.length - 1].e + 0.3);
  if (prox) g.e = Math.min(g.e, r3(Math.max(0.15, prox.ws[0].s - 0.05) - 0.02));
});

const legendas = `<template>
  <style>
    #root { position:absolute; inset:0; }
    .lg { position:absolute; left:40px; width:1000px; top:1110px; text-align:center; font-family:"Montserrat", sans-serif; font-weight:900;
      -webkit-text-stroke:12px #111; paint-order:stroke fill; line-height:1.06; overflow:visible; text-transform:uppercase; }
    .lg span { display:inline-block; margin:0 .17em; }
  </style>
  <div id="root" data-composition-id="legendas" data-width="1080" data-height="1920">
${grupos
  .map((g, i) => {
    const txt = g.ws.map((p) => p.w).join(" ");
    const fs = Math.min(86, Math.floor(960 / (txt.length * 0.8)));
    return `    <div id="lg-${i}" class="lg clip" data-start="${g.s}" data-duration="${r3(g.e - g.s)}" data-track-index="0" style="font-size:${fs}px; color:${COR[g.quem]}">${g.ws.map((p, j) => `<span id="lg-${i}-${j}">${p.w}</span>`).join("")}</div>`;
  })
  .join("\n")}
  </div>
  <script>
    const tl = gsap.timeline({ paused: true });
    ${JSON.stringify(grupos.map((g) => g.s))}.forEach((s, i) => {
      tl.fromTo("#lg-" + i + " span", { y: 26, scale: 0.7 }, { y: 0, scale: 1, duration: 0.12, ease: "back.out(2.4)", stagger: 0.05, immediateRender: false }, s);
    });
    window.__timelines["legendas"] = tl;
  </script>
</template>
`;
fs.writeFileSync("compositions/legendas.html", legendas);

fs.writeFileSync(
  "assets/lib/ep01.js",
  "window.EP = " +
    JSON.stringify({
      falas: falas.map(({ id, quem, ini, dur }) => ({ id, quem, ini, dur })),
      cenas: CENAS,
      total: TOTAL,
    }) +
    ";\n",
);

// áudio no index
const vozes = falas.map(
  (f) =>
    `      <audio id="voz-${f.id}" class="clip" src="assets/voice/${f.id}.wav" data-start="${f.ini}" data-duration="${f.dur}" data-track-index="5" data-volume="1"></audio>`,
);
const SFXDUR = JSON.parse(fs.readFileSync("ferramentas/sfx-duracoes.json", "utf8"));
const lanes = [];
const efeitos = SFX.map(([f, t, v], i) => {
  const d = Math.min(SFXDUR[f], r3(TOTAL - t));
  let lane = 0;
  while ((lanes[lane] ?? -1) > t) lane++;
  lanes[lane] = t + d;
  return `      <audio id="sfx-${i}" class="clip" src="assets/sfx/${f}" data-start="${t}" data-duration="${d}" data-track-index="${6 + lane}" data-volume="${v}"></audio>`;
});
const hosts = Object.entries(CENAS).map(
  ([id, [a, b]]) =>
    `      <div id="${id}" data-composition-id="${id}" data-composition-src="compositions/${id}.html" data-start="${a}" data-duration="${r3(b - a)}" data-track-index="1" data-track-kind="graphics" data-width="1080" data-height="1920"></div>`,
);
let index = fs.readFileSync("index.html", "utf8");
index = index.replace(
  /<!-- CENAS -->[\s\S]*<!-- \/CENAS -->/,
  `<!-- CENAS -->\n${hosts.join("\n")}\n      <div id="legendas" data-composition-id="legendas" data-composition-src="compositions/legendas.html" data-start="0" data-duration="${TOTAL}" data-track-index="2" data-track-kind="captions" data-width="1080" data-height="1920"></div>\n      <!-- /CENAS -->`,
);
index = index.replace(
  /<!-- AUDIO -->[\s\S]*<!-- \/AUDIO -->/,
  `<!-- AUDIO -->\n${vozes.join("\n")}\n${efeitos.join("\n")}\n      <!-- /AUDIO -->`,
);
index = index.replace(
  /data-composition-id="main" data-start="0" data-duration="[0-9.]+"/,
  `data-composition-id="main" data-start="0" data-duration="${TOTAL}"`,
);
fs.writeFileSync("index.html", index);
console.log(
  "falas",
  falas.length,
  "legendas",
  grupos.length,
  "efeitos",
  SFX.length,
  "total",
  TOTAL,
);
