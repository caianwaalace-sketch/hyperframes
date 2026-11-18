# Série "Caian" — animações em bloquinhos, 60 s, 9:16

Histórias curtas em português, com narrador e diálogos, num mundo de bonecos de blocos
(estilo jogo de construção/obby). Personagem fixo: **Caian**.

> Estilo "bloquinho" inspirado em jogos de blocos, mas com personagens, nomes e visual próprios.
> Não usamos logo, nome, marca nem personagens de nenhum jogo existente.

## Pastas

```
series/caian/
├── README.md                 este arquivo
├── biblia/
│   ├── personagens.md        quem é quem: aparência, cores, jeito de falar, voz
│   └── estilo.md             regras visuais, de roteiro, de áudio e de formato
├── compartilhado/
│   ├── personagens/          bonecos 3D reutilizáveis (Caian, Lia, Kaio, Pedrita…)
│   ├── sfx/                  efeitos sonoros gratuitos (com créditos)
│   └── musica/               trilhas gratuitas (com licença anotada)
├── modelos/
│   └── roteiro-modelo.md     esqueleto de roteiro de 60 s
├── ferramentas/              scripts para gerar vozes e tempos das legendas
└── episodios/
    └── ep01-o-pet-de-50-moedas/
        ├── ROTEIRO.md        roteiro aprovado
        ├── index.html        (depois) composição HyperFrames do episódio
        ├── compositions/     (depois) uma cena por arquivo
        ├── assets/voice/     (depois) falas gravadas ou geradas, uma por arquivo
        └── renders/          (depois) MP4 final — não vai para o git
```

## Fluxo de cada episódio

1. Roteiro em `episodios/epXX/ROTEIRO.md` → aprovação.
2. Vozes: uma fala por arquivo (`assets/voice/<cena>-<personagem>.wav`).
3. Cenas animadas reutilizando os bonecos de `compartilhado/personagens/`.
4. Legendas sincronizadas com as falas.
5. Checagem (`hyperframes check`), revisão de quadros, render 1080×1920.

## Ferramentas (todas gratuitas)

| Etapa             | Ferramenta                                                                              | Custo         |
| ----------------- | --------------------------------------------------------------------------------------- | ------------- |
| Animação e render | HyperFrames + Three.js (3D)                                                             | grátis, local |
| Vozes             | sua gravação **ou** Kokoro (local) **ou** HeyGen plano grátis (3 min/mês, só com conta) | grátis        |
| Efeitos sonoros   | pacote incluso (Pixabay)                                                                | grátis        |
| Música            | só com sua autorização (catálogo HeyGen grátis com conta, ou faixa sua)                 | grátis        |

Nada pago é usado sem autorização explícita.
