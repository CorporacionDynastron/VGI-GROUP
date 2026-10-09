import re

with open("index.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Fix Nav Links (Header)
html = html.replace('href="#">Inicio</a>', 'href="index.html">Inicio</a>')
html = html.replace('href="#">Servicios</a>', 'href="#servicios">Servicios</a>')
html = html.replace('href="#obras-destacadas">Obras</a>', 'href="obras.html">Obras</a>')
html = html.replace('href="#">Nosotros</a>', 'href="nosotros.html">Nosotros</a>')

# Add id="servicios"
html = html.replace('<section class="w-full bg-surface py-space-2xl">', '<section id="servicios" class="w-full bg-surface py-space-2xl">')

# Fix other links in Footer
html = html.replace('href="#">Historia Corporativa</a>', 'href="nosotros.html">Historia Corporativa</a>')
html = html.replace('href="#">Equipo Técnico</a>', 'href="nosotros.html">Equipo Técnico</a>')
html = html.replace('href="#">Capacitaciones Especializadas</a>', 'href="capacitaciones.html">Capacitaciones Especializadas</a>')

# And in the Modal Javascript, if they click the CTA, we should redirect them based on ID
# id 1 -> planos.html, id 2 -> obras.html, id 3 -> capacitaciones.html
# Wait, let's see how the modal CTA is rendered.

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Fixed links!")
