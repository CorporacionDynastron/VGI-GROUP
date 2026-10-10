import re
import urllib.parse

# 1. New HTML for CERTIFICACIONES
cert_images = [
    {"file": "ISO 9001.png", "title": "ISO 9001:2015", "alt": "ISO 9001", "w_class": "w-20"},
    {"file": "ISO 14001.png", "title": "ISO 14001:2015", "alt": "ISO 14001", "w_class": "w-20"},
    {"file": "ISO 45001.png", "title": "ISO 45001", "alt": "ISO 45001", "w_class": "w-28"},
    {"file": "ISO 37001.png", "title": "ISO 37001:2016", "alt": "ISO 37001", "w_class": "w-20"},
    {"file": "ISO 27001.png", "title": "ISO 27001", "alt": "ISO 27001", "w_class": "w-28"},
    {"file": "CIP.png", "title": "Colegio de Ingenieros del Perú", "alt": "CIP", "w_class": "w-20"}
]

# For index.html
certs_html = '<div class="flex items-center gap-3 md:gap-space-md flex-wrap">\n'
for cert in cert_images:
    encoded_file = urllib.parse.quote(cert["file"])
    path = f"./CERTIFICACIONES/{encoded_file}"
    certs_html += f"""                                <div class="bg-surface-container border border-outline-variant/30 p-2 flex items-center justify-center hover:border-primary/50 transition-all shadow-sm" title="{cert['title']}">
                                    <div class="bg-white p-1 rounded flex items-center justify-center h-16 {cert['w_class']}">
                                        <img src="{path}" alt="{cert['alt']}" class="h-full w-full object-contain">
                                    </div>
                                </div>\n"""
certs_html += '                            </div>'

# For footer.js
certs_html_footer = '<div class="flex items-center gap-2 flex-wrap">\n'
for cert in cert_images:
    encoded_file = urllib.parse.quote(cert["file"])
    path = f"./CERTIFICACIONES/{encoded_file}"
    certs_html_footer += f"""                            <div class="bg-surface-container border border-outline-variant/30 p-2 flex items-center justify-center hover:border-primary/50 transition-all shadow-sm" title="{cert['title']}">
                                <div class="bg-white p-1 rounded flex items-center justify-center h-16 {cert['w_class']}">
                                    <img src="{path}" alt="{cert['alt']}" class="h-full w-full object-contain">
                                </div>
                            </div>\n"""
certs_html_footer += '                        </div>'

# Replace in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Certificaciones in index.html
html = re.sub(r'<div class="flex items-center gap-3 md:gap-space-md flex-wrap">\s*<div class="bg-surface-container.*?</div>\s*</div>\s*</div>\s*</div>', 
              certs_html + '\n                        </div>', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# Replace in footer.js
with open('footer.js', 'r', encoding='utf-8') as f:
    footer_js = f.read()

footer_js = re.sub(r'<div class="flex items-center gap-2 flex-wrap">\s*<div class="bg-surface-container.*?</div>\s*</div>\s*</div>\s*</div>', 
                   certs_html_footer + '\n                    </div>', footer_js, flags=re.DOTALL)

with open('footer.js', 'w', encoding='utf-8') as f:
    f.write(footer_js)

print("Images fixed!")
