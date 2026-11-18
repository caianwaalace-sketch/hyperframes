"""Lê assets/voice/*.wav e escreve assets/lib/falas.js com o volume de cada fala a 30 quadros/s
(para a boca dos bonecos) e a duração. Uso: python3 -I ferramentas/envelopes.py <pasta do episódio>"""
import json, math, subprocess, sys, struct, pathlib
root = pathlib.Path(sys.argv[1])
out = {}
for wav in sorted((root / "assets/voice").glob("*.wav")):
    raw = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", str(wav), "-ac", "1", "-ar", "24000",
                          "-f", "s16le", "-"], capture_output=True, check=True).stdout
    n = len(raw) // 2
    s = struct.unpack(f"<{n}h", raw[: n * 2])
    hop = 800  # 24000 / 30
    env = []
    for i in range(0, n, hop):
        seg = s[i:i + hop]
        env.append(math.sqrt(sum(x * x for x in seg) / max(1, len(seg))) / 32768)
    peak = max(env) or 1
    out[wav.stem] = {"dur": round(n / 24000, 3), "env": [round(min(1, v / peak), 2) for v in env]}
js = "window.FALAS = " + json.dumps(out, separators=(",", ":")) + ";\n"
(root / "assets/lib/falas.js").write_text(js)
print(len(out), "falas")
