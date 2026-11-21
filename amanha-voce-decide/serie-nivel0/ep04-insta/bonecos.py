"""Bonecos cartoon originais em SVG. Origem nos pés (0,0); altura ~300 unidades.

Partes animáveis (ids): {p}-armL, {p}-armR, {p}-legL, {p}-legR, {p}-head, {p}-eyes, {p}-fig.
"""

SKIN = "#F2C9A0"


def hat_svg(kind, color):
    if kind == "beanie":
        return (f'<path d="M-46 -268 Q-46 -318 0 -320 Q46 -318 46 -268 Z" fill="{color}"/>'
                f'<rect x="-50" y="-276" width="100" height="16" rx="8" fill="{color}" stroke="#00000033" stroke-width="3"/>'
                f'<circle cx="0" cy="-326" r="12" fill="#E8E4DA"/>')
    if kind == "fedora":
        return (f'<ellipse cx="0" cy="-282" rx="70" ry="12" fill="{color}"/>'
                f'<path d="M-40 -282 L-34 -326 Q0 -340 34 -326 L40 -282 Z" fill="{color}"/>'
                f'<rect x="-38" y="-296" width="76" height="9" fill="#111"/>')
    if kind == "nurse":
        return (f'<path d="M-40 -296 L-34 -326 L34 -326 L40 -296 Z" fill="#F4F4F0" stroke="#ccc" stroke-width="2"/>'
                f'<rect x="-5" y="-322" width="10" height="22" fill="#C1121F"/><rect x="-11" y="-316" width="22" height="10" fill="#C1121F"/>')
    if kind == "ushanka":
        return (f'<path d="M-50 -268 Q-50 -322 0 -324 Q50 -322 50 -268 Z" fill="{color}"/>'
                f'<rect x="-62" y="-282" width="20" height="62" rx="10" fill="{color}"/>'
                f'<rect x="42" y="-282" width="20" height="62" rx="10" fill="{color}"/>')
    return ""


def boneco(p, x, y, s=1.0, jacket="#3A6EA5", hat="beanie", hat_color="#C1121F",
           scarf="#E9C46A", pants="#2B2F3A", socks=False, worried=True, prop="", hand_prop="", hair=None, eyes_closed=False):
    feet = ("#E8E4DA" if socks else "#1a1a1a")
    brows = ('<path d="M-26 -276 L-8 -270" stroke="#3a2a20" stroke-width="5" stroke-linecap="round"/>'
             '<path d="M26 -276 L8 -270" stroke="#3a2a20" stroke-width="5" stroke-linecap="round"/>') if worried else ""
    mouth = ('<ellipse cx="0" cy="-232" rx="9" ry="7" fill="#3a2a20"/>' if worried
             else '<path d="M-10 -234 Q0 -228 10 -234" stroke="#3a2a20" stroke-width="4" fill="none"/>')
    hair_svg = (f'<path d="M-52 -262 Q-56 -318 0 -318 Q56 -318 52 -262 L56 -188 Q30 -176 34 -230 L-34 -230 Q-30 -176 -56 -188 Z" fill="{hair}"/>' if hair else "")
    eyes = ('<path d="M-24 -256 Q-16 -250 -8 -256" stroke="#1a1a1a" stroke-width="4" fill="none"/><path d="M8 -256 Q16 -250 24 -256" stroke="#1a1a1a" stroke-width="4" fill="none"/>'
            if eyes_closed else '<ellipse cx="-16" cy="-258" rx="6" ry="8" fill="#1a1a1a"/><ellipse cx="16" cy="-258" rx="6" ry="8" fill="#1a1a1a"/>')
    return f"""
<g transform="translate({x} {y}) scale({s})">
 <g id="{p}-fig">
  <ellipse cx="0" cy="4" rx="58" ry="10" fill="#000" opacity="0.35"/>
  <g id="{p}-legL"><rect x="-30" y="-112" width="24" height="108" rx="10" fill="{pants}"/><ellipse cx="-20" cy="-4" rx="20" ry="10" fill="{feet}"/></g>
  <g id="{p}-legR"><rect x="6" y="-112" width="24" height="108" rx="10" fill="{pants}"/><ellipse cx="20" cy="-4" rx="20" ry="10" fill="{feet}"/></g>
  <g id="{p}-armL"><rect x="-66" y="-200" width="24" height="96" rx="12" fill="{jacket}"/><circle cx="-54" cy="-102" r="13" fill="{SKIN}"/></g>
  <rect x="-48" y="-212" width="96" height="112" rx="34" fill="{jacket}"/>
  <path d="M-48 -160 L48 -160" stroke="#00000030" stroke-width="5"/>
  <path d="M-48 -130 L48 -130" stroke="#00000030" stroke-width="5"/>
  {prop}
  <g id="{p}-armR"><rect x="42" y="-200" width="24" height="96" rx="12" fill="{jacket}"/><circle cx="54" cy="-102" r="13" fill="{SKIN}"/>{hand_prop}</g>
  <rect x="-36" y="-222" width="72" height="22" rx="11" fill="{scarf}"/>
  <g id="{p}-head">
   {hair_svg}
   <circle cx="0" cy="-262" r="46" fill="{SKIN}"/>
   <g id="{p}-eyes">{eyes}</g>
   {brows}{mouth}
   <circle cx="-30" cy="-240" r="8" fill="#e8907a" opacity="0.5"/><circle cx="30" cy="-240" r="8" fill="#e8907a" opacity="0.5"/>
   {hat_svg(hat, hat_color)}
  </g>
 </g>
</g>"""
