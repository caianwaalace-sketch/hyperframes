#!/usr/bin/env python3
"""Narra um roteiro (lines.txt, formato id|texto) com o Piper (voz pt_BR-faber-medium, local e grátis).
Uso: python3 piper_voice.py [pasta-do-projeto]
Gera assets/voice-el/<id>.mp3 e timing.json (tempos estimados por caractere, igual ao fallback do Kokoro).
"""
import json
import subprocess
import sys
from pathlib import Path

MODEL = "/root/.cache/piper/pt_BR-faber-medium/pt_BR-faber-medium.onnx"
proj = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
voice_dir = proj / "assets" / "voice-el"
voice_dir.mkdir(parents=True, exist_ok=True)

lines = [l.split("|", 1) for l in (proj / "lines.txt").read_text().splitlines() if l.strip()]

for k, txt in lines:
    wav = voice_dir / f"{k}.wav"
    mp3 = voice_dir / f"{k}.mp3"
    subprocess.run(["piper", "--model", MODEL, "--output_file", str(wav)], input=txt, text=True, check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(wav), str(mp3)], check=True)
    wav.unlink()
    print(k, "ok")

# tempos estimados por tamanho de palavra (Piper não dá timestamp por palavra)
gap = 0.45
t = 0.15
out, words = [], {}
for k, txt in lines:
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(voice_dir / f"{k}.mp3")]))
    ws = txt.split()
    weights = [len(w.strip(",.:!?")) + 2 + (4 if w[-1] in ".:!?" else 2 if w[-1] == "," else 0) for w in ws]
    tot = sum(weights)
    c = t + 0.06
    span = dur - 0.1
    wl = []
    for w, wt in zip(ws, weights):
        ln = span * wt / tot
        wl.append([w, round(c, 3), round(c + ln * 0.85, 3)])
        c += ln
    words[k] = wl
    out.append({"id": k, "start": round(t, 3), "dur": round(dur, 3)})
    t += dur + gap

json.dump({"lines": out, "words": words}, open(proj / "timing.json", "w"), ensure_ascii=False)
print("fim", round(t, 2), "s")
