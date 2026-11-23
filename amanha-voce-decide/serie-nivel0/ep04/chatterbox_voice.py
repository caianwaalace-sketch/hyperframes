#!/usr/bin/env python3
"""Narra um roteiro (lines.txt, formato id|texto) com Chatterbox Multilingual TTS
(Resemble AI, MIT, roda local) clonando o timbre de referencia-voz-grave.wav
(gerada com Piper, livre de licença). É a voz padrão do Caian Studio desde 21/11/2026.

Uso: python3 chatterbox_voice.py [pasta-do-projeto]
Gera assets/voice-el/<id>.mp3 e timing.json. Pula a narração de uma linha se o
mp3 já existir (reaproveita áudio gerado antes, só recalcula o tempo das palavras).

O Chatterbox não devolve timestamp por palavra, então o tempo de cada palavra é
estimado pelo tamanho dela. Uma fala com mais de uma frase tem pausas reais entre
elas (o Chatterbox varia esse silêncio por frase); espalhar as palavras de forma
uniforme por cima dessas pausas fazia a legenda "andar" errado depois de cada
pausa (legenda fora do que estava sendo falado). Por isso a estimativa roda em
duas etapas: primeiro acha as pausas reais no áudio (silencedetect do ffmpeg),
depois distribui as palavras só dentro dos trechos com fala de verdade, pulando
as pausas em vez de atravessá-las.
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

REF = Path(__file__).parent / "referencia-voz-grave.wav"
proj = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
voice_dir = proj / "assets" / "voice-el"
voice_dir.mkdir(parents=True, exist_ok=True)

lines = [l.split("|", 1) for l in (proj / "lines.txt").read_text().splitlines() if l.strip()]

pending = [(k, txt) for k, txt in lines if not (voice_dir / f"{k}.mp3").exists()]
if pending:
    from chatterbox.mtl_tts import ChatterboxMultilingualTTS
    import torchaudio

    print("carregando modelo...")
    t0 = time.time()
    model = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
    print(f"modelo carregado em {time.time() - t0:.0f}s")

    for k, txt in pending:
        t1 = time.time()
        wav = model.generate(txt, language_id="pt", audio_prompt_path=str(REF), exaggeration=0.5, cfg_weight=0.5)
        wav_path = voice_dir / f"{k}.wav"
        torchaudio.save(str(wav_path), wav, model.sr)
        mp3_path = voice_dir / f"{k}.mp3"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(wav_path), str(mp3_path)], check=True)
        wav_path.unlink()
        print(k, f"{time.time() - t1:.0f}s")
else:
    print("áudio já existe pra todas as linhas, só recalculando timing.json")


def detect_silences(mp3_path, dur, thresh_db=-30, min_d=0.15):
    """Pausas reais na fala (ignora as bem no começo/fim do clipe)."""
    out = subprocess.run(
        ["ffmpeg", "-i", str(mp3_path), "-af", f"silencedetect=noise={thresh_db}dB:d={min_d}", "-f", "null", "-"],
        capture_output=True, text=True,
    ).stderr
    sils = []
    cur_start = None
    for line in out.splitlines():
        if "silence_start:" in line:
            cur_start = float(line.split("silence_start:")[1].split()[0])
        elif "silence_end:" in line and cur_start is not None:
            end = float(line.split("silence_end:")[1].split("|")[0])
            if cur_start > 0.05 and end < dur - 0.05:
                sils.append((cur_start, end))
            cur_start = None
    return sils


def word_times(txt, dur, mp3_path, pad_start=0.06, tail_margin=0.1):
    ws = txt.split()
    weights = [len(w.strip(",.:!?")) + 2 + (4 if w[-1] in ".:!?" else 2 if w[-1] == "," else 0) for w in ws]
    tot = sum(weights)
    sils = detect_silences(mp3_path, dur)
    # trechos de fala de verdade, entre as pausas detectadas
    segs = []
    prev = pad_start
    for s, e in sils:
        if s > prev:
            segs.append((prev, s))
        prev = max(prev, e)
    if dur - tail_margin > prev:
        segs.append((prev, dur - tail_margin))
    if not segs:
        segs = [(pad_start, dur - tail_margin)]
    total_speech = sum(e - s for s, e in segs)
    wl = []
    seg_idx = 0
    seg_start, seg_end = segs[0]
    cursor = seg_start
    for w, wt in zip(ws, weights):
        if cursor >= seg_end and seg_idx < len(segs) - 1:
            seg_idx += 1
            seg_start, seg_end = segs[seg_idx]
            cursor = seg_start
        start_t = cursor
        want = total_speech * wt / tot
        end_t = min(start_t + want, seg_end)
        cursor = end_t
        wl.append([w, round(start_t, 3), round(start_t + (end_t - start_t) * 0.85, 3)])
    return wl


gap = 0.45
t = 0.15
out, words = [], {}
for k, txt in lines:
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(voice_dir / f"{k}.mp3")]))
    wl = word_times(txt, dur, voice_dir / f"{k}.mp3")
    words[k] = [[w, round(a + t, 3), round(b + t, 3)] for w, a, b in wl]
    out.append({"id": k, "start": round(t, 3), "dur": round(dur, 3)})
    t += dur + gap

json.dump({"lines": out, "words": words}, open(proj / "timing.json", "w"), ensure_ascii=False)
print("fim", round(t, 2), "s")
