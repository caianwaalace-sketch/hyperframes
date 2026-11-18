#!/usr/bin/env bash
# Gera uma fala por arquivo com Kokoro (local, grátis) e dá um timbre a cada personagem.
# Uso: HYPERFRAMES_PYTHON=<python com kokoro-onnx> ./ferramentas/gerar-vozes.sh <launcher plugin-cli.mjs>
set -euo pipefail
L="$1"; cd "$(dirname "$0")/.."
mkdir -p assets/voice .tmp-voice
while IFS=$'\t' read -r id who txt; do
  case "$who" in
    NAR)    v=pm_santa; sp=1.0;  pitch=1.00 ;;
    CAIAN)  v=pm_alex;  sp=1.08; pitch=1.00 ;;
    LIA)    v=pf_dora;  sp=1.05; pitch=1.00 ;;
    KAIO)   v=pm_alex;  sp=1.02; pitch=1.09 ;;
    JUCA)   v=pm_santa; sp=0.92; pitch=0.93 ;;
    TONHAO) v=pm_santa; sp=1.0;  pitch=0.84 ;;
  esac
  node "$L" tts "$txt" --voice "$v" --lang pt-br --speed "$sp" -o ".tmp-voice/$id.wav" >/dev/null </dev/null
  # muda o timbre sem mudar a duração; normaliza o pico
  ffmpeg -nostdin -y -loglevel error -i ".tmp-voice/$id.wav" \
    -af "asetrate=24000*${pitch},aresample=24000,atempo=1/${pitch},alimiter=limit=0.89" "assets/voice/$id.wav"
done < ferramentas/falas.tsv
rm -rf .tmp-voice
