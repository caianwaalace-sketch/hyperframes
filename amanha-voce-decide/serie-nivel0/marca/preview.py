import teo
html = open('teo-frente-costas.html').read(); pre = html.split('<svg')[0]
svg = '<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0">' + teo.DEFS + '<rect width="1080" height="1920" fill="#15161b"/>'
open('teo-frente-costas.html', 'w').write(pre + svg
    + '<g transform="translate(290 1580) scale(1.05)">' + teo.teo("f", "neutro", level="0") + '</g>'
    + '<g transform="translate(800 1580) scale(1.05)">' + teo.teo_back("b") + '</g></svg>'
    + '<div class="t" style="top:80px;font-size:70px">TÉO · FRENTE E COSTAS</div>'
    + '<div class="t" style="top:1650px;font-size:44px;width:540px">FRENTE</div><div class="t" style="top:1650px;left:540px;font-size:44px;width:540px">COSTAS</div></body></html>')
open('teo-close.html', 'w').write(pre + svg
    + '<g transform="translate(540 3150) scale(3.6)">' + teo.teo("c", "neutro", tag=False) + '</g></svg>'
    + '<div class="t" style="top:80px;font-size:70px">TÉO · CLOSE</div></body></html>')
open('teo-close-costas.html', 'w').write(pre + svg
    + '<g transform="translate(540 3150) scale(3.6)">' + teo.teo_back("cb").replace(teo.nametag(-920), '') + '</g></svg>'
    + '<div class="t" style="top:80px;font-size:70px">TÉO · NAGÔ (COSTAS)</div></body></html>')
