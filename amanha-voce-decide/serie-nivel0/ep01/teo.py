# Personagem fixo "Téo" (SVG). Origem: pés em (0,0), altura ~860.
from nago import nago_front, nago_back
OUT="#1a1410"
def teo(p="teo", expr="neutro", glow=True, level=None, level_color="#D7263D", tag=True):
    EY = {
     "neutro": '<ellipse cx="-34" cy="-700" rx="15" ry="17" fill="#fff" stroke="{o}" stroke-width="4"/><ellipse cx="34" cy="-700" rx="15" ry="17" fill="#fff" stroke="{o}" stroke-width="4"/><circle cx="-31" cy="-697" r="9" fill="#2E9BFF"/><circle cx="37" cy="-697" r="9" fill="#2E9BFF"/><circle cx="-31" cy="-697" r="4" fill="#0b1a2e"/><circle cx="37" cy="-697" r="4" fill="#0b1a2e"/><circle cx="-28" cy="-701" r="3" fill="#fff"/><circle cx="40" cy="-701" r="3" fill="#fff"/>',
     "medo": '<ellipse cx="-34" cy="-702" rx="17" ry="21" fill="#fff" stroke="{o}" stroke-width="4"/><ellipse cx="34" cy="-702" rx="17" ry="21" fill="#fff" stroke="{o}" stroke-width="4"/><circle cx="-34" cy="-700" r="6" fill="#2E9BFF"/><circle cx="34" cy="-700" r="6" fill="#2E9BFF"/><circle cx="-34" cy="-700" r="2.5" fill="#0b1a2e"/><circle cx="34" cy="-700" r="2.5" fill="#0b1a2e"/>',
     "decidido": '<path d="M-50 -704 Q-34 -712 -18 -704 L-18 -696 Q-34 -690 -50 -696 Z" fill="#fff" stroke="{o}" stroke-width="4"/><path d="M18 -704 Q34 -712 50 -704 L50 -696 Q34 -690 18 -696 Z" fill="#fff" stroke="{o}" stroke-width="4"/><circle cx="-32" cy="-700" r="7" fill="#2E9BFF"/><circle cx="36" cy="-700" r="7" fill="#2E9BFF"/><circle cx="-32" cy="-700" r="3" fill="#0b1a2e"/><circle cx="36" cy="-700" r="3" fill="#0b1a2e"/>',
    }
    BR = {"neutro":'<path d="M-52 -728 Q-34 -738 -16 -730" /><path d="M16 -730 Q34 -738 52 -728" />',
             "medo":'<path d="M-52 -738 Q-36 -750 -18 -742" /><path d="M18 -742 Q36 -750 52 -738" />',
             "decidido":'<path d="M-54 -726 L-16 -716" /><path d="M16 -716 L54 -726" />'}
    MO = {"neutro":'<path d="M-14 -640 Q0 -634 14 -640" stroke="#3a1f12" stroke-width="5" fill="none" stroke-linecap="round"/>',
             "medo":'<ellipse cx="0" cy="-638" rx="12" ry="15" fill="#3a1f12"/>',
             "decidido":'<path d="M-16 -638 L16 -642" stroke="#3a1f12" stroke-width="5" fill="none" stroke-linecap="round"/>'}
    faces = "".join(f'<g id="{p}-x-{k}" opacity="{1 if k == expr else 0}"><g id="{p}-eyes-{k}">{EY[k].replace("{o}", OUT)}</g><g stroke="#1c1410" stroke-width="7" fill="none" stroke-linecap="round">{BR[k]}</g>{MO[k]}</g>' for k in EY)
    tagsvg = nametag(-1010 if level is not None else -920) if tag else ""
    lvl = (f'<g id="{p}-lvl"><rect x="-70" y="-930" width="140" height="84" rx="16" fill="#111318" stroke="{level_color}" stroke-width="5"/><text id="{p}-lvlt" x="0" y="-870" font-family="Oswald, Osw" font-weight="700" font-size="60" text-anchor="middle" fill="{level_color}">{level}</text></g>' if level is not None else "")
    scalp = nago_front()
    glove = ('<g id="%s-glow"><circle cx="0" cy="0" r="52" fill="#5CE1E6" opacity="0.35" filter="url(#blur18)"/></g>' % p if glow else "") + \
            f'<path d="M-24 -22 Q-30 18 -6 26 Q22 30 26 6 L22 -26 Z" fill="#5CE1E6" stroke="{OUT}" stroke-width="4"/><path d="M-14 -8 L12 -10 M-12 6 L14 4" stroke="#1e8a96" stroke-width="4"/>'
    return f'''
<g id="{p}">
 <ellipse cx="0" cy="6" rx="130" ry="18" fill="#000" opacity="0.3"/>
 <g id="{p}-legL"><path d="M-62 -330 L-18 -330 L-22 -60 L-66 -60 Z" fill="#2f3542" stroke="{OUT}" stroke-width="5"/>
   <path d="M-76 -110 L-14 -110 L-12 -8 Q-12 4 -26 4 L-96 4 Q-110 4 -104 -12 L-80 -30 Z" fill="#5b3a26" stroke="{OUT}" stroke-width="5"/>
   <path d="M-76 -80 L-14 -80" stroke="#D7263D" stroke-width="7"/></g>
 <g id="{p}-legR"><path d="M18 -330 L62 -330 L66 -60 L22 -60 Z" fill="#2f3542" stroke="{OUT}" stroke-width="5"/>
   <path d="M14 -110 L76 -110 L80 -30 L104 -12 Q110 4 96 4 L26 4 Q12 4 12 -8 Z" fill="#5b3a26" stroke="{OUT}" stroke-width="5"/>
   <path d="M14 -80 L76 -80" stroke="#D7263D" stroke-width="7"/></g>
 <g id="{p}-armL"><path d="M-92 -560 Q-112 -515 -118 -466 L-84 -462 Q-80 -510 -60 -540 Z" fill="{POLO}" stroke="{OUT}" stroke-width="5"/>
   <path d="M-118 -466 L-84 -462" stroke="#E8E4DA" stroke-width="5"/>
   <path d="M-116 -462 Q-124 -420 -122 -360 L-88 -356 Q-86 -420 -86 -460 Z" fill="#8D5B3E" stroke="{OUT}" stroke-width="5"/>
   <circle cx="-106" cy="-342" r="22" fill="#8D5B3E" stroke="{OUT}" stroke-width="5"/></g>
 <path d="M-96 -570 Q0 -606 96 -570 L82 -320 Q0 -300 -82 -320 Z" fill="{POLO}" stroke="{OUT}" stroke-width="5"/>
 <path d="M-96 -570 Q-74 -480 -82 -320 L-66 -322 Q-60 -470 -76 -562 Z" fill="#000" opacity="0.18"/>
 <rect x="-11" y="-588" width="22" height="86" rx="4" fill="{POLO}" stroke="{OUT}" stroke-width="4"/>
 <circle cx="0" cy="-562" r="5" fill="#E8E4DA"/><circle cx="0" cy="-530" r="5" fill="#E8E4DA"/>
 <path d="M-44 -600 L-6 -592 L-24 -548 Z" fill="{POLO}" stroke="#E8E4DA" stroke-width="5" stroke-linejoin="round"/>
 <path d="M44 -600 L6 -592 L24 -548 Z" fill="{POLO}" stroke="#E8E4DA" stroke-width="5" stroke-linejoin="round"/>
 <g transform="translate(46 -500)"><circle r="13" fill="#5CE1E6" stroke="{OUT}" stroke-width="3"/><text x="0" y="6" font-family="Oswald, Osw" font-weight="700" font-size="16" text-anchor="middle" fill="#0b1a2e">0</text></g>
 <path d="M-84 -336 L84 -336" stroke="#5b3a26" stroke-width="16"/><rect x="-14" y="-346" width="28" height="22" fill="#c9a227" stroke="{OUT}" stroke-width="3"/>
 <g id="{p}-armR"><path d="M92 -560 Q112 -515 118 -466 L84 -462 Q80 -510 60 -540 Z" fill="{POLO}" stroke="{OUT}" stroke-width="5"/>
   <path d="M118 -466 L84 -462" stroke="#E8E4DA" stroke-width="5"/>
   <path d="M116 -462 Q124 -420 122 -360 L88 -356 Q86 -420 86 -460 Z" fill="#8D5B3E" stroke="{OUT}" stroke-width="5"/>
   <g transform="translate(106 -336)">{glove}</g></g>
 <g id="{p}-head">
  <path d="M-30 -610 L30 -610 L26 -568 L-26 -568 Z" fill="#7a4d33" stroke="{OUT}" stroke-width="5"/>
  <ellipse cx="-80" cy="-690" rx="14" ry="20" fill="#7a4d33" stroke="{OUT}" stroke-width="5"/>
  <ellipse cx="80" cy="-690" rx="14" ry="20" fill="#7a4d33" stroke="{OUT}" stroke-width="5"/>
  <path d="M-78 -720 Q-80 -620 0 -606 Q80 -620 78 -720 Q70 -790 0 -792 Q-70 -790 -78 -720 Z" fill="#8D5B3E" stroke="{OUT}" stroke-width="5"/>
  {scalp}
  {faces}
  <path d="M-4 -690 Q-10 -664 2 -662" stroke="#5e3a26" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M-58 -660 L-44 -656 M44 -656 L58 -660" stroke="#6e4229" stroke-width="3" opacity="0.6"/>
 </g>
 {lvl}
 <g id="{p}-tag">{tagsvg}</g>
</g>'''
POLO = "#1d3557"
HAIR = "#F4F4F0"; HAIR_L = "#b9bcc4"


def braid(x, y0, n, dx=0):
    return "".join(f'<ellipse cx="{x + dx*i:.1f}" cy="{y0 + i*15}" rx="7.5" ry="10" fill="{HAIR}" stroke="{HAIR_L}" stroke-width="2.5"/>' for i in range(n))


def braids(side=True):
    xs = [(-94, -735, 13, -0.6), (-82, -760, 15, -0.4), (94, -735, 13, 0.6), (82, -760, 15, 0.4), (-66, -780, 16, -0.3), (66, -780, 16, 0.3)]
    return "".join(braid(x, y, n, d) for x, y, n, d in xs)


SCALP = ('<path d="M-80 -712 Q-84 -800 0 -812 Q84 -800 80 -712 Q60 -760 0 -764 Q-60 -760 -80 -712 Z" fill="#F4F4F0" stroke="#1a1410" stroke-width="4"/>'
         + "".join(f'<path d="M{x*0.8:.0f} -796 Q{x:.0f} -776 {x*1.15:.0f} -758" stroke="#b9bcc4" stroke-width="3" fill="none" stroke-linecap="round"/>' for x in (-44, -22, 0, 22, 44)))


def nametag(y):
    return (f'<rect x="-150" y="{y}" width="300" height="50" rx="25" fill="#111318" fill-opacity="0.85" stroke="#E8E4DA" stroke-width="3"/>'
            f'<text x="0" y="{y + 36}" font-family="Oswald, Osw" font-weight="700" font-size="30" text-anchor="middle" fill="#E8E4DA">@amanha<tspan fill="#5CE1E6">voce</tspan><tspan fill="#D7263D">decide</tspan></text>')


DEFS='<defs><filter id="blur18" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="18"/></filter></defs>'




def teo_back(p="teob"):
    """Téo de costas: polo, tranças brancas caindo nas costas, @ em cima da cabeça."""
    return f'''
<g id="{p}">
 <ellipse cx="0" cy="6" rx="130" ry="18" fill="#000" opacity="0.3"/>
 <g><path d="M-62 -330 L-18 -330 L-22 -60 L-66 -60 Z" fill="#2f3542" stroke="{OUT}" stroke-width="5"/>
   <path d="M-76 -110 L-14 -110 L-14 4 L-80 4 Z" fill="#5b3a26" stroke="{OUT}" stroke-width="5"/><path d="M-76 -80 L-14 -80" stroke="#D7263D" stroke-width="7"/></g>
 <g><path d="M18 -330 L62 -330 L66 -60 L22 -60 Z" fill="#2f3542" stroke="{OUT}" stroke-width="5"/>
   <path d="M14 -110 L76 -110 L80 4 L14 4 Z" fill="#5b3a26" stroke="{OUT}" stroke-width="5"/><path d="M14 -80 L76 -80" stroke="#D7263D" stroke-width="7"/></g>
 <path d="M-92 -560 Q-112 -515 -118 -466 L-84 -462 Q-80 -510 -60 -540 Z" fill="{POLO}" stroke="{OUT}" stroke-width="5"/>
 <path d="M-116 -462 Q-124 -420 -122 -360 L-88 -356 Q-86 -420 -86 -460 Z" fill="#8D5B3E" stroke="{OUT}" stroke-width="5"/><circle cx="-106" cy="-342" r="22" fill="#8D5B3E" stroke="{OUT}" stroke-width="5"/>
 <path d="M92 -560 Q112 -515 118 -466 L84 -462 Q80 -510 60 -540 Z" fill="{POLO}" stroke="{OUT}" stroke-width="5"/>
 <path d="M116 -462 Q124 -420 122 -360 L88 -356 Q86 -420 86 -460 Z" fill="#8D5B3E" stroke="{OUT}" stroke-width="5"/>
 <g transform="translate(106 -336)"><path d="M-24 -22 Q-30 18 -6 26 Q22 30 26 6 L22 -26 Z" fill="#5CE1E6" stroke="{OUT}" stroke-width="4"/></g>
 <path d="M-96 -570 Q0 -606 96 -570 L82 -320 Q0 -300 -82 -320 Z" fill="{POLO}" stroke="{OUT}" stroke-width="5"/>
 <path d="M-60 -596 Q0 -612 60 -596 L56 -578 Q0 -590 -56 -578 Z" fill="{POLO}" stroke="#E8E4DA" stroke-width="5"/>
 <path d="M-84 -336 L84 -336" stroke="#5b3a26" stroke-width="16"/>
 <path d="M-30 -610 L30 -610 L26 -580 L-26 -580 Z" fill="#7a4d33" stroke="{OUT}" stroke-width="5"/>
 <ellipse cx="-80" cy="-690" rx="14" ry="20" fill="#7a4d33" stroke="{OUT}" stroke-width="5"/><ellipse cx="80" cy="-690" rx="14" ry="20" fill="#7a4d33" stroke="{OUT}" stroke-width="5"/>
 <path d="M-78 -720 Q-80 -620 0 -606 Q80 -620 78 -720 Q70 -790 0 -792 Q-70 -790 -78 -720 Z" fill="#8D5B3E" stroke="{OUT}" stroke-width="5"/>
 {nago_back()}
 <g id="{p}-tag">{nametag(-920)}</g>
</g>'''
