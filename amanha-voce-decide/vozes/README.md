# Vozes para narração (Caian Studio)

## Voz padrão atual: **Chatterbox clonado** (escolhida pelo usuário em 21/11/2026)

Todo vídeo novo usa `chatterbox_voice.py`. É o motor **Chatterbox Multilingual TTS**
(Resemble AI, licença MIT, roda local) clonando o timbre de `referencia-voz-grave.wav`
(uma voz grave gerada com o Piper, livre de licença). O usuário testou 3 versões — a
voz fina original do Chatterbox, a mesma com o tom baixado, e essa clonada — e escolheu
a clonada como a mais natural e com o tom certo.

## Local e grátis (sempre disponíveis, rodam neste ambiente de nuvem)

| Motor | Script | Observação |
|---|---|---|
| **Chatterbox (clonado)** ⭐ padrão | `chatterbox_voice.py` | Ritmo/prosódia do Chatterbox Multilingual + timbre grave clonado de `referencia-voz-grave.wav`. Mais natural que os outros, mas mais lento: ~5x o tempo real sem GPU (um vídeo de 90s leva uns 8-9 min pra narrar). Marca d'água inaudível (PerTh) embutida em todo áudio gerado. |
| Piper (reserva, rápido) | `piper_voice.py` | Voz `pt_BR-faber-medium`. Quase instantâneo, mas soa mais "fininho"/robótico. Bom se precisar de um vídeo com urgência. |
| Kokoro (reserva) | `voice.py` (via `hyperframes tts --voice pm_alex --lang pt-br`) | Voz `pm_alex`. Usado antes do Piper. |

Nenhum dos motores locais devolve o tempo exato de cada palavra (como o ElevenLabs dava).
Todos estimam esse tempo pelo tamanho de cada palavra — funciona bem o bastante pra
sincronizar legenda, mas não é perfeito.

## Pago (créditos, melhor qualidade e timing exato por palavra)

| Serviço | Status em 21/11/2026 |
|---|---|
| **ElevenLabs** | Conectado, mas com **0 créditos** (quota de 10.000 esgotada). Precisa recarregar pra voltar a funcionar. |

## Ferramentas analisadas e não instaladas

- **skill-tts** (github.com/captjt/skill-tts) e **AgentVibes** (github.com/paulpreibisch/AgentVibes):
  são ferramentas pra o Claude Code *falar notificações* durante o trabalho (tipo "build concluído"),
  não pra narrar vídeos. Extraímos só a parte útil: o motor Piper e a voz pt_BR do AgentVibes.
  Instalar o resto delas criaria hooks de notificação que não servem pro Caian Studio.
- **XTTS-v2** (Coqui): descartado. Licença CPML (Coqui Public Model License) proíbe uso
  comercial, e o canal é comercial.

## Como usar num projeto novo

```bash
cp vozes/chatterbox_voice.py vozes/referencia-voz-grave.wav meu-projeto/
cd meu-projeto
python3 chatterbox_voice.py .          # padrão: Chatterbox clonado

# alternativas, se precisar de velocidade:
cp ../vozes/piper_voice.py .  && python3 piper_voice.py .           # Piper, rápido
cp ../vozes/voice.py ../vozes/timing.py . && python3 voice.py 1.1 && python3 timing.py 0.4  # Kokoro
```
