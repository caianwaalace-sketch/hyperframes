#!/usr/bin/env python3
"""Narra um roteiro (lines.txt, formato id|texto) com Chatterbox Multilingual TTS
(Resemble AI, MIT, roda local) clonando o timbre de referencia-voz-grave.wav
(gerada com Piper, livre de licença). É a voz padrão do Caian Studio desde 21/11/2026.

Uso: python3 chatterbox_voice.py [pasta-do-projeto]
Gera assets/voice-el/<id>.mp3 e timing.json (tempos estimados por caractere,
porque o Chatterbox, como os outros motores locais, não devolve timestamp por palavra).
"""
import json
import subprocess
import sys
import time
from pathlib import Path

REF = Path(__file__).parent / "referencia-voz-grave.wav"
proj = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
voice_dir = proj / "assets" / "voice-el"
voice_dir.mkdir(parents=True, exist_ok=True)

lines = [l.split("|", 1) for l in (proj / "lines.txt").read_text().splitlines() if l.strip()]

from chatterbox.mtl_tts import ChatterboxMultilingualTTS
import torchaudio

print("carregando modelo...")
t0 = time.time()
model = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
print(f"modelo carregado em {time.time() - t0:.0f}s")

for k, txt in lines:
    t1 = time.time()
    wav = model.generate(txt, language_id="pt", audio_prompt_path=str(REF), exaggeration=0.5, cfg_weight=0.5)
    wav_path = voice_dir / f"{k}.wav"
    torchaudio.save(str(wav_path), wav, model.sr)
    mp3_path = voice_dir / f"{k}.mp3"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(wav_path), str(mp3_path)], check=True)
    wav_path.unlink()
    print(k, f"{time.time() - t1:.0f}s")

# tempos estimados por tamanho de palavra (Chatterbox não dá timestamp por palavra)
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
