# Vozes para narração (Caian Studio)

## Voz padrão atual: **Piper** (escolhida pelo usuário em 21/11/2026)

Todo vídeo novo usa `piper_voice.py` com a voz `pt_BR-faber-medium`, a não ser que o
usuário peça outra coisa (ex.: recarregar o ElevenLabs e voltar pra ele).

## Local e grátis (sempre disponíveis, rodam neste ambiente de nuvem)

| Motor | Script | Voz usada | Observação |
|---|---|---|---|
| **Piper** ⭐ padrão | `piper_voice.py` | `pt_BR-faber-medium` | Voz nativa em português brasileiro, instalada em 21/11/2026. Modelo baixado de huggingface.co (único lugar onde existe), salvo no setup_script do ambiente pra sobreviver a reinícios. |
| Kokoro (reserva) | `voice.py` (via `hyperframes tts --voice pm_alex --lang pt-br`) | `pm_alex` (prefixo "p" = português) | Usado nos vídeos antes do Piper. Mantido como alternativa se o Piper falhar. |

Nenhum dos dois motores locais devolve o tempo exato de cada palavra (como o ElevenLabs dava).
`piper_voice.py` e a função `estimate_timing` em `voice.py`/`timing.py` estimam esse tempo pelo
tamanho de cada palavra — funciona bem o bastante pra sincronizar legenda, mas não é perfeito.

## Pago (créditos, melhor qualidade e timing exato por palavra)

| Serviço | Status em 21/11/2026 |
|---|---|
| **ElevenLabs** | Conectado, mas com **0 créditos** (quota de 10.000 esgotada). Precisa recarregar pra voltar a funcionar. |

## Ferramentas analisadas e não instaladas

- **skill-tts** (github.com/captjt/skill-tts) e **AgentVibes** (github.com/paulpreibisch/AgentVibes):
  são ferramentas pra o Claude Code *falar notificações* durante o trabalho (tipo "build concluído"),
  não pra narrar vídeos. Extraímos só a parte útil: o motor Piper e a voz pt_BR do AgentVibes.
  Instalar o resto delas criaria hooks de notificação que não servem pro Caian Studio.

## Como usar num projeto novo

```bash
cp vozes/voice.py vozes/timing.py vozes/piper_voice.py meu-projeto/
cd meu-projeto
# opção A: Kokoro (voz pm_alex)
python3 voice.py 1.1 && python3 timing.py 0.4
# opção B: Piper (voz pt_BR-faber-medium)
python3 piper_voice.py .
```
