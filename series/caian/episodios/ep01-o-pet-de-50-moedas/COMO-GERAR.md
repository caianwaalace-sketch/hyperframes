# Como gerar o Ep. 01 de novo

Tudo grátis e local. Rodar dentro desta pasta.

1. **Vozes** (só se mudar uma fala em `ferramentas/falas.tsv`):
   `HYPERFRAMES_PYTHON=<python com kokoro-onnx> ./ferramentas/gerar-vozes.sh <launcher>`
   Para usar gravações reais: salve cada fala como `assets/voice/<id>.wav` (ids em `falas.tsv`)
   e pule este passo.
2. **Volume das bocas:** `python3 -I ferramentas/envelopes.py .`
3. **Tempos, legendas e áudio:** `node ferramentas/montar.mjs`
   (os horários de cada fala e dos efeitos ficam no topo desse arquivo).
4. **Checar e ver quadros:** `npx hyperframes check` e `npx hyperframes snapshot --at 5,20,40`
5. **Render:** `npx hyperframes render --output renders/caian-ep01.mp4`

Os bonecos vêm de `compartilhado/personagens/blocos.js` (copiado para `assets/lib/blocos.js`).
Se mudar o boneco lá, copie de novo para cá.
