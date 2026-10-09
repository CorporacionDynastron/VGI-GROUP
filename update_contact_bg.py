import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

contact_bg = """<section class="relative w-full py-space-2xl overflow-hidden" id="contacto-tecnico">
                <!-- Background Image -->
                <div class="absolute inset-0 opacity-20" style="background-image: url('./images/imagen-5.jpeg'); background-size: cover; background-attachment: fixed; background-position: center; filter: grayscale(80%);"></div>
                <div class="absolute inset-0 bg-gradient-to-r from-surface via-surface/90 to-surface/40"></div>
                
                <div class="max-w-7xl mx-auto px-gutter relative z-10">"""

html = html.replace('<section class="w-full bg-surface-container-lowest py-space-2xl" id="contacto-tecnico">\n                <div class="max-w-7xl mx-auto px-gutter">', contact_bg)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
