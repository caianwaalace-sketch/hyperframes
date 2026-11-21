"""Lia: menina de capuz vermelho, nível 500. Mesmo estilo do Téo. Pés em (0,0)."""
OUT = "#1a1410"


def lia(p="lia", expr="neutro", level="500", arm_out=False):
    EY = {
        "neutro": '<ellipse cx="-30" cy="-690" rx="13" ry="15" fill="#fff" stroke="#1a1410" stroke-width="4"/><ellipse cx="30" cy="-690" rx="13" ry="15" fill="#fff" stroke="#1a1410" stroke-width="4"/><circle cx="-28" cy="-688" r="7" fill="#3b7a3a"/><circle cx="32" cy="-688" r="7" fill="#3b7a3a"/><circle cx="-26" cy="-692" r="2.5" fill="#fff"/><circle cx="34" cy="-692" r="2.5" fill="#fff"/>',
        "medo": '<ellipse cx="-30" cy="-692" rx="15" ry="19" fill="#fff" stroke="#1a1410" stroke-width="4"/><ellipse cx="30" cy="-692" rx="15" ry="19" fill="#fff" stroke="#1a1410" stroke-width="4"/><circle cx="-30" cy="-690" r="4" fill="#3b7a3a"/><circle cx="30" cy="-690" r="4" fill="#3b7a3a"/>',
    }
    BR = {"neutro": '<path d="M-46 -716 L-14 -712" /><path d="M14 -712 L46 -716" />',
          "medo": '<path d="M-46 -726 Q-30 -736 -14 -728" /><path d="M14 -728 Q30 -736 46 -726" />'}
    MO = {"neutro": '<path d="M-12 -634 L12 -636" stroke="#3a1f12" stroke-width="5" stroke-linecap="round"/>',
          "medo": '<ellipse cx="0" cy="-634" rx="9" ry="11" fill="#3a1f12"/>'}
    faces = "".join(f'<g id="{p}-x-{k}" opacity="{1 if k == expr else 0}">{EY[k]}<g stroke="#1c1410" stroke-width="6" fill="none" stroke-linecap="round">{BR[k]}</g>{MO[k]}</g>' for k in EY)
    arm = ('<g id="{p}-armR"><path d="M70 -540 Q150 -540 220 -520 L222 -488 Q150 -500 70 -500 Z" fill="#9b1b2b" stroke="#1a1410" stroke-width="5"/><circle cx="234" cy="-504" r="20" fill="#e3b48c" stroke="#1a1410" stroke-width="5"/></g>'
           if arm_out else '<g id="{p}-armR"><path d="M70 -540 Q96 -460 92 -370 L62 -366 Q60 -450 48 -520 Z" fill="#9b1b2b" stroke="#1a1410" stroke-width="5"/><circle cx="78" cy="-352" r="20" fill="#e3b48c" stroke="#1a1410" stroke-width="5"/></g>').replace("{p}", p)
    return f'''
<g id="{p}">
 <ellipse cx="0" cy="6" rx="120" ry="16" fill="#000" opacity="0.3"/>
 <path d="M-40 -300 L-14 -300 L-16 -60 L-42 -60 Z" fill="#2b2b36" stroke="{OUT}" stroke-width="5"/>
 <path d="M14 -300 L40 -300 L42 -60 L16 -60 Z" fill="#2b2b36" stroke="{OUT}" stroke-width="5"/>
 <path d="M-54 -90 L-8 -90 L-8 4 L-70 4 Q-78 -6 -60 -20 Z" fill="#3b2a1e" stroke="{OUT}" stroke-width="5"/>
 <path d="M8 -90 L54 -90 L60 -20 Q78 -6 70 4 L8 4 Z" fill="#3b2a1e" stroke="{OUT}" stroke-width="5"/>
 <path d="M-110 -250 Q-80 -560 0 -600 Q80 -560 110 -250 Q0 -220 -110 -250 Z" fill="#b51d31" stroke="{OUT}" stroke-width="5"/>
 <path d="M-110 -250 Q-80 -560 -30 -592 Q-70 -480 -70 -248 Z" fill="#000" opacity="0.18"/>
 <path d="M-60 -560 Q0 -590 60 -560 L56 -300 Q0 -290 -56 -300 Z" fill="#2f2a3a" stroke="{OUT}" stroke-width="4"/>
 <path d="M-70 -540 Q-96 -460 -92 -370 L-62 -366 Q-60 -450 -48 -520 Z" fill="#9b1b2b" stroke="{OUT}" stroke-width="5"/>
 <circle cx="-78" cy="-352" r="20" fill="#e3b48c" stroke="{OUT}" stroke-width="5"/>
 {arm}
 <g id="{p}-head">
  <path d="M-96 -640 Q-100 -800 0 -812 Q100 -800 96 -640 Q90 -590 60 -575 L-60 -575 Q-90 -590 -96 -640 Z" fill="#b51d31" stroke="{OUT}" stroke-width="5"/>
  <path d="M-66 -700 Q-70 -610 0 -598 Q70 -610 66 -700 Q60 -770 0 -772 Q-60 -770 -66 -700 Z" fill="#e3b48c" stroke="{OUT}" stroke-width="5"/>
  <path d="M-66 -716 Q-30 -770 30 -760 Q60 -750 66 -716 Q40 -740 -10 -736 Q-50 -732 -66 -716 Z" fill="#2a1a12"/>
  {faces}
  <path d="M-2 -676 Q-8 -654 2 -652" stroke="#a5704f" stroke-width="4" fill="none" stroke-linecap="round"/>
 </g>
 <g id="{p}-lvl"><rect x="-80" y="-930" width="160" height="84" rx="16" fill="#111318" stroke="#E9C46A" stroke-width="5"/>
  <text x="0" y="-870" font-family="Oswald, Osw" font-weight="700" font-size="60" text-anchor="middle" fill="#E9C46A">{level}</text></g>
</g>'''
