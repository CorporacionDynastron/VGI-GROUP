import re
import urllib.parse

cert_images = [
    {"file": "ISO 9001.png", "title": "ISO 9001:2015", "alt": "ISO 9001"},
    {"file": "ISO 14001.png", "title": "ISO 14001:2015", "alt": "ISO 14001"},
    {"file": "ISO 45001.png", "title": "ISO 45001", "alt": "ISO 45001"},
    {"file": "ISO 37001.png", "title": "ISO 37001:2016", "alt": "ISO 37001"},
    {"file": "ISO 27001.png", "title": "ISO 27001", "alt": "ISO 27001"},
    {"file": "CIP.png", "title": "Colegio de Ingenieros del Perú", "alt": "CIP"}
]

certs_html_footer = '<div class="flex items-center gap-2 flex-wrap">\n'
for cert in cert_images:
    encoded_file = urllib.parse.quote(cert["file"])
    path = f"./CERTIFICACIONES/{encoded_file}"
    certs_html_footer += f"""                            <div class="bg-surface-container border border-outline-variant/30 p-2 flex items-center justify-center hover:border-primary/50 transition-all shadow-sm" title="{cert['title']}">
                                <div class="bg-white p-1 rounded flex items-center justify-center h-16 w-auto min-w-[4rem]">
                                    <img src="{path}" alt="{cert['alt']}" class="h-full w-auto object-contain">
                                </div>
                            </div>\n"""
certs_html_footer += '                        </div>'

with open('footer.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Finding the certifications block in footer
# It starts with <div class="flex items-center gap-2 flex-wrap">
# And ends before <div class="lg:col-span-2 flex flex-col">
pattern = r'<div class="flex items-center gap-2 flex-wrap">.*?</div>\s*</div>'

new_js = re.sub(pattern, certs_html_footer, js, flags=re.DOTALL)

with open('footer.js', 'w', encoding='utf-8') as f:
    f.write(new_js)

print("footer.js updated!")
