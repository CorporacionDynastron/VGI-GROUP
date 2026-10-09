import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

bg_html = """<!-- METODOLOGIA: DE LA IDEA A LA ENTREGA, EN CUATRO ETAPAS -->
            <section id="servicios" class="relative w-full bg-surface py-space-2xl overflow-hidden">
                <!-- Background Image -->
                <div class="absolute inset-0 opacity-10" style="background-image: url('./images/imagen-6.jpeg'); background-size: cover; background-attachment: fixed; background-position: center; filter: grayscale(100%);"></div>
                <div class="absolute inset-0 bg-gradient-to-b from-surface via-surface/95 to-surface"></div>
                
                <div class="max-w-7xl mx-auto px-gutter relative z-10">"""

html = re.sub(r'<!-- METODOLOG.A: DE LA IDEA A LA ENTREGA, EN CUATRO ETAPAS -->\s*<section id="servicios" class="w-full bg-surface py-space-2xl">\s*<div class="max-w-7xl mx-auto px-gutter">', bg_html, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
