import os
import re

# 1. Update index.html
index_path = r"C:\Dynastron_Code\VGI\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix text replacements
html = html.replace('Parque Naciones Unidas', 'Proyecto Recreacional')
html = html.replace('PARQUE NACIONES UNIDAS', 'PROYECTO RECREACIONAL')
html = html.replace('<h2>Tres disciplinas, un mismo estándar.</h2>', '<h2 style="font-family: var(--body); font-weight: 700; line-height: 1.25; letter-spacing: -1px; text-transform: none;">Tres disciplinas, un mismo estándar.</h2>')

new_sponsors = """
                <div class="client-mark" title="Nicoll">
                    <img src="./images/Patrocinadores%20y%20marcas%20aliados/NICOLL.png" alt="NICOLL">
                </div>
                <div class="client-mark" title="Pavco">
                    <img src="./images/Patrocinadores%20y%20marcas%20aliados/pavco.png" alt="PAVCO">
                </div>
                <div class="client-mark" title="Rotoplas">
                    <img src="./images/Patrocinadores%20y%20marcas%20aliados/ROTOPLAS.svg" alt="ROTOPLAS">
                </div>
                <div class="client-mark" title="Cemento Apu">
                    <img src="./images/Patrocinadores%20y%20marcas%20aliados/CEMENTO%20APU.png" alt="CEMENTO APU">
                </div>
                <div class="client-mark" title="Cemex">
                    <img src="./images/Patrocinadores%20y%20marcas%20aliados/CEMEX.jpg" alt="CEMEX">
                </div>
                <div class="client-mark" title="Ladrillos Lark">
                    <img src="./images/Patrocinadores%20y%20marcas%20aliados/LADRILLOS%20LARK.png" alt="LADRILLOS LARK">
                </div>"""

new_certs = """
                <div class="client-mark" title="ISO 9001">
                    <img src="./images/certificaciones/what-is-iso-9001-compliance.webp" alt="ISO 9001">
                </div>"""

# Insert new sponsors
if "Ladrillos Gonzaga" in html and "LADRILLOS LARK" not in html:
    html = re.sub(r'(<div class="client-mark" title="Ladrillos Gonzaga">\s*<img[^>]*>\s*</div>)', r'\1' + new_sponsors, html, flags=re.IGNORECASE)

# Insert new certifications
if "ISO 37001" in html and "ISO 9001" not in html:
    html = re.sub(r'(<div class="client-mark" title="ISO 37001">\s*<img[^>]*>\s*</div>)', r'\1' + new_certs, html, flags=re.IGNORECASE)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update obras.html
obras_path = r"C:\Dynastron_Code\VGI\obras.html"
with open(obras_path, 'r', encoding='utf-8') as f:
    obras_html = f.read()

old_css = ".hero-obras { background: var(--navy-deep); color: white; padding: 180px 0 80px; text-align: center; }"
new_css_obras = ".hero-obras { background: linear-gradient(to bottom, rgba(3,10,20,0.65), rgba(6,19,37,0.95)), url('./02-pistas/IMAGEN%201.png') center/cover no-repeat; color: white; padding: 180px 0 80px; text-align: center; position: relative; }"

if old_css in obras_html:
    obras_html = obras_html.replace(old_css, new_css_obras)
    with open(obras_path, 'w', encoding='utf-8') as f:
        f.write(obras_html)


# 3. Update capacitaciones.html
cap_path = r"C:\Dynastron_Code\VGI\capacitaciones.html"
with open(cap_path, 'r', encoding='utf-8') as f:
    cap_html = f.read()

new_css_cap = ".hero-obras { background: linear-gradient(to bottom, rgba(3,10,20,0.65), rgba(6,19,37,0.95)), url('./05-formacion/IMAGEN%201.jpeg') center/cover no-repeat; color: white; padding: 180px 0 80px; text-align: center; position: relative; }"

if old_css in cap_html:
    cap_html = cap_html.replace(old_css, new_css_cap)
    with open(cap_path, 'w', encoding='utf-8') as f:
        f.write(cap_html)

print("Updates applied successfully.")
