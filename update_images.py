import re
import urllib.parse

# 1. New HTML for CERTIFICACIONES
cert_images = [
    {"file": "ISO 9001.png", "title": "ISO 9001:2015", "alt": "ISO 9001"},
    {"file": "ISO 14001.png", "title": "ISO 14001:2015", "alt": "ISO 14001"},
    {"file": "ISO 45001.png", "title": "ISO 45001", "alt": "ISO 45001"},
    {"file": "ISO 37001.png", "title": "ISO 37001:2016", "alt": "ISO 37001"},
    {"file": "ISO 27001.png", "title": "ISO 27001", "alt": "ISO 27001"},
    {"file": "CIP.png", "title": "Colegio de Ingenieros del Perú", "alt": "CIP"}
]

certs_html = '<div class="flex items-center gap-3 md:gap-space-md flex-wrap">\n'
for cert in cert_images:
    encoded_file = urllib.parse.quote(cert["file"])
    path = f"./CERTIFICACIONES/{encoded_file}"
    certs_html += f"""                                <div class="bg-surface-container border border-outline-variant/30 p-2 flex items-center justify-center hover:border-primary/50 transition-all shadow-sm" title="{cert['title']}">
                                    <div class="bg-white p-1 rounded flex items-center justify-center h-16 w-auto min-w-[4rem]">
                                        <img src="{path}" alt="{cert['alt']}" class="h-full w-auto object-contain">
                                    </div>
                                </div>\n"""
certs_html += '                            </div>'


# 2. New HTML for PATROCINADORES
patrocinadores_images = [
    "./PATROCINADORES%20Y%20MARCAS%20ALIADAS/ACEROS%20AREQUIPA.png",
    "./PATROCINADORES%20Y%20MARCAS%20ALIADAS/PAVCO.png",
    "./PATROCINADORES%20Y%20MARCAS%20ALIADAS/ROTOPLAS.webp",
    "./PATROCINADORES%20Y%20MARCAS%20ALIADAS/TREBOL.png",
    "./PATROCINADORES%20Y%20MARCAS%20ALIADAS/Nicoll.png",
    "./PATROCINADORES%20Y%20MARCAS%20ALIADAS/CATERPILLAR.png",
    "./images/patrocinadores/INDECO-transparent.webp",
    "./PATROCINADORES%20Y%20MARCAS%20ALIADAS/SIKA.webp",
    "./PATROCINADORES%20Y%20MARCAS%20ALIADAS/APU.png",
    "./PATROCINADORES%20Y%20MARCAS%20ALIADAS/CEMEX.png",
    "./PATROCINADORES%20Y%20MARCAS%20ALIADAS/CEMENTO%20SOL.png",
    "./PATROCINADORES%20Y%20MARCAS%20ALIADAS/LADRILLOS%20LARK.png"
]

patroc_html = '<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-space-md">\n'
for p_img in patrocinadores_images:
    # Use bg-white to ensure dark logos are visible
    patroc_html += f"""                                <div class="bg-white py-4 px-6 flex items-center justify-center transition-colors h-28 rounded border border-outline-variant/10 shadow-sm hover:shadow-md">
                                    <img src="{p_img}" alt="Marca Aliada" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm">
                                </div>\n"""
patroc_html += '                            </div>'


# Replace in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Certificaciones in index.html
html = re.sub(r'<div class="flex items-center gap-3 md:gap-space-md flex-wrap">\s*<div class="bg-surface-container.*?</div>\s*</div>\s*</div>', 
              certs_html + '\n                        </div>', html, flags=re.DOTALL)

# Replace Patrocinadores in index.html
html = re.sub(r'<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-space-md">.*?</div>\s*</div>\s*</div>\s*</section>', 
              patroc_html + '\n                        </div>\n                  </div>\n              </section>', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# Replace in footer.js
with open('footer.js', 'r', encoding='utf-8') as f:
    footer_js = f.read()

# Replace Certificaciones in footer.js
footer_js = re.sub(r'<div class="flex items-center gap-2 flex-wrap">\s*<div class="bg-surface-container.*?</div>\s*</div>\s*</div>\s*</div>', 
                   certs_html.replace('gap-3 md:gap-space-md', 'gap-2') + '\n                                </div>\n                            </div>', footer_js, flags=re.DOTALL)

with open('footer.js', 'w', encoding='utf-8') as f:
    f.write(footer_js)

print("Images replaced in index.html and footer.js")
