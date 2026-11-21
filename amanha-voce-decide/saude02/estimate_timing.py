import json, subprocess

lines = [l.split("|", 1) for l in open("lines.txt").read().splitlines() if l.strip()]
gap = {}
t = 0.15
out = []
words = {}
for k, txt in lines:
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"assets/voice-el/{k}.mp3"]))
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
    t += dur + gap.get(k, 0.55)

json.dump({"lines": out, "words": words}, open("timing.json", "w"), ensure_ascii=False)
print("fim", round(t, 2))
for k, _ in lines:
    print(k, " ".join(f"{i}:{w[0]}" for i, w in enumerate(words[k])))
