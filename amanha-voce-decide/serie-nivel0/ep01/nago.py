"""Tranças nagô (cornrows) realistas para o Téo. Gera SVG em coordenadas do personagem."""
import math

HAIR = "#F4F4F0"; HAIR_MID = "#d9dbe0"; HAIR_DK = "#9a9ea8"; PART = "#5e3a26"


def qbez(p0, p1, p2, t):
    a = (1 - t) ** 2; b = 2 * (1 - t) * t; c = t * t
    return (a * p0[0] + b * p1[0] + c * p2[0], a * p0[1] + b * p1[1] + c * p2[1])


def cornrow(p0, p1, p2, w0=11.0, w1=7.0, step=9.0):
    """Uma trança: gomos alternados em V ao longo de uma curva quadrática."""
    # comprimento aproximado
    pts = [qbez(p0, p1, p2, i / 60) for i in range(61)]
    L = sum(math.dist(pts[i], pts[i + 1]) for i in range(60))
    n = max(4, int(L / step))
    out_shadow, out_parts = [], []
    for i in range(n + 1):
        t = i / n
        x, y = qbez(p0, p1, p2, t)
        x2, y2 = qbez(p0, p1, p2, min(1, t + 0.01))
        ang = math.degrees(math.atan2(y2 - y, x2 - x))
        w = w0 + (w1 - w0) * t
        side = 1 if i % 2 == 0 else -1
        # deslocamento perpendicular de cada gomo
        nx, ny = -math.sin(math.radians(ang)), math.cos(math.radians(ang))
        cx, cy = x + nx * side * w * 0.28, y + ny * side * w * 0.28
        rot = ang + side * 38
        out_shadow.append(f'<ellipse cx="{x:.1f}" cy="{y + 1.5:.1f}" rx="{w * 0.62:.1f}" ry="{w * 0.62:.1f}" fill="{HAIR_DK}"/>')
        out_parts.append(
            f'<g transform="translate({cx:.1f} {cy:.1f}) rotate({rot:.1f})">'
            f'<ellipse rx="{w * 0.62:.1f}" ry="{w * 0.36:.1f}" fill="{HAIR}" stroke="{HAIR_DK}" stroke-width="1.6"/>'
            f'<path d="M{-w * 0.4:.1f} {w * 0.08:.1f} Q0 {w * 0.26:.1f} {w * 0.4:.1f} {w * 0.08:.1f}" stroke="{HAIR_MID}" stroke-width="1.4" fill="none"/>'
            f'</g>')
    return "".join(out_shadow) + "".join(out_parts)


def parting(p0, p1, p2):
    return f'<path d="M{p0[0]} {p0[1]} Q{p1[0]} {p1[1]} {p2[0]} {p2[1]}" stroke="{PART}" stroke-width="2.4" fill="none" opacity="0.55"/>'


def nago_front():
    """Vista de frente: tranças finas saindo da linha do cabelo e subindo para o topo."""
    rows = []
    for x in (-56, -40, -24, -8, 8, 24, 40, 56):
        p0 = (x, -754 + (x / 56) ** 2 * 16)
        p1 = (x * 0.92, -786)
        p2 = (x * 0.62, -802)
        rows.append((p0, p1, p2))
    parts = "".join(
        f'<path d="M{(a[0][0] + b[0][0]) / 2:.1f} {(a[0][1] + b[0][1]) / 2:.1f} Q{(a[1][0] + b[1][0]) / 2:.1f} {(a[1][1] + b[1][1]) / 2:.1f} {(a[2][0] + b[2][0]) / 2:.1f} {(a[2][1] + b[2][1]) / 2:.1f}" stroke="{PART}" stroke-width="2" fill="none" opacity="0.45"/>'
        for a, b in zip(rows, rows[1:]))
    temples = cornrow((-72, -730), (-74, -752), (-66, -774), 7, 6, 6.5) + cornrow((72, -730), (74, -752), (66, -774), 7, 6, 6.5)
    return parts + temples + "".join(cornrow(*r, w0=8.5, w1=6.5, step=6.5) for r in rows)


def nago_back():
    """Vista de costas: tranças descendo do alto da cabeça até a nuca."""
    out = []
    for x in (-66, -44, -22, 0, 22, 44, 66):
        p0 = (x * 0.55, -796 + (x / 66) ** 2 * 8)
        p1 = (x * 1.05, -730)
        p2 = (x * 0.85, -640 + (x / 66) ** 2 * 30)
        out.append(cornrow(p0, p1, p2, 11, 8, 9))
        # pontinha da trança na nuca
        out.append(f'<ellipse cx="{p2[0]:.1f}" cy="{p2[1] + 8:.1f}" rx="5" ry="7" fill="{HAIR}" stroke="{HAIR_DK}" stroke-width="1.5"/>')
    return "".join(out)
