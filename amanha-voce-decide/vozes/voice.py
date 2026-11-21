import json,base64,subprocess,urllib.request,sys
speed=float(sys.argv[1]) if len(sys.argv)>1 else 1.1
lines=[l.split('|',1) for l in open('lines.txt').read().splitlines() if l.strip()]
for i,(k,txt) in enumerate(lines):
    body={"text":txt,"model_id":"eleven_multilingual_v2","language_code":"pt",
      "voice_settings":{"stability":0.4,"similarity_boost":0.8,"style":0.4,"use_speaker_boost":True,"speed":speed},
      "previous_text":lines[i-1][1] if i else "","next_text":lines[i+1][1] if i+1<len(lines) else ""}
    req=urllib.request.Request("https://api.elevenlabs.io/v1/text-to-speech/nPczCjzI2devNBz1zQrb/with-timestamps?output_format=mp3_44100_128",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"},method="POST")
    d=json.load(urllib.request.urlopen(req))
    open(f"assets/voice-el/{k}.mp3","wb").write(base64.b64decode(d["audio_base64"]))
    json.dump(d["alignment"],open(f".el/{k}.json","w"),ensure_ascii=False)
