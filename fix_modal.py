import re

with open("index.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Add ctaLink to dossiers
html = html.replace('ctaText: "Solicitar Planos"', 'ctaText: "Solicitar Planos",\n                        ctaLink: "planos.html"')
html = html.replace('ctaText: "Cotizar Construcción"', 'ctaText: "Cotizar Construcción",\n                        ctaLink: "obras.html"')
html = html.replace('ctaText: "Cotizar Construccin"', 'ctaText: "Cotizar Construcción",\n                        ctaLink: "obras.html"')
html = html.replace('ctaText: "Inscribirse en Cursos"', 'ctaText: "Inscribirse en Cursos",\n                        ctaLink: "capacitaciones.html"')

# Update JS to set href
js_to_replace = "document.getElementById('modal-cta').innerText = data.ctaText;"
js_new = "document.getElementById('modal-cta').innerText = data.ctaText;\n                    document.getElementById('modal-cta').href = data.ctaLink;"
html = html.replace(js_to_replace, js_new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated modal CTAs!")
