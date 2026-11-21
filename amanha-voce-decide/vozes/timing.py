import json,subprocess,sys
gapd=float(sys.argv[1]) if len(sys.argv)>1 else 0.45
lines=[l.split('|',1) for l in open('lines.txt').read().splitlines() if l.strip()]
t=0.12;out=[];words={}
for k,txt in lines:
    al=json.load(open(f'.el/{k}.json'));ch=al['characters'];s=al['character_start_times_seconds'];e=al['character_end_times_seconds']
    dur=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"assets/voice-el/{k}.mp3"]))
    ws=[];cur=None
    for i,c in enumerate(ch):
        if c.isspace():
            if cur: ws.append(cur);cur=None
        elif cur is None: cur=[c,s[i],e[i]]
        else: cur[0]+=c;cur[2]=e[i]
    if cur: ws.append(cur)
    assert [w[0] for w in ws]==txt.split(),k
    words[k]=[[w[0],round(t+w[1],3),round(t+w[2],3)] for w in ws]
    out.append({"id":k,"start":round(t,3),"dur":round(dur,3)}); t+=dur+gapd
json.dump({"lines":out,"words":words},open('timing.json','w'),ensure_ascii=False)
print("fim",round(t-gapd,2))
for k,_ in lines: print(k," ".join(f"{i}:{w[0]}" for i,w in enumerate(words[k])))
