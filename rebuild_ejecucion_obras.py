import glob
import re
import urllib.parse

sections_data = [
    ("PLANTA DE TRATAMIENTO DE AGUAS RESIDUALES", "07-saneamiento", "petar"),
    ("INFRAESTRUCTURA MULTIFAMILIAR", "08-multifamiliar", "multifamiliar"),
    ("MANTENIMIENTO DE INFRAESTRUCTURA", "03-mantenimiento", "mantenimiento")
]

gallery_html = ""

for title, folder, id_name in sections_data:
    gallery_html += f"""
                <div id="{id_name}" class="mb-space-2xl scroll-mt-[120px]" data-aos="fade-up">
                    <div class="mb-space-xl border-b-2 border-primary/30 pb-4">
                        <h2 class="font-headline-lg text-3xl md:text-4xl text-primary uppercase font-bold">{title}</h2>
                    </div>
                    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
"""
    valid_ext = ('.webp', '.jpg', '.jpeg', '.png')
    images = []
    for ext in valid_ext:
        images.extend(glob.glob(f"{folder}/**/*{ext}", recursive=True))
        images.extend(glob.glob(f"{folder}/*{ext}", recursive=True))
    
    images = list(set(images))
    images.sort()
    
    for img in images:
        web_path = "./" + img.replace('\\', '/')
        parts = web_path.split('/')
        encoded_parts = [urllib.parse.quote(p) for p in parts]
        web_path_encoded = '/'.join(encoded_parts).replace('%2E', '.')
        
        gallery_html += f"""
                        <div class="group relative overflow-hidden border border-outline-variant/20 cursor-pointer h-64" onclick="openLightbox('{web_path_encoded}')">
                            <img src="{web_path_encoded}" alt="Obra" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700">
                        </div>"""
    gallery_html += "\n                    </div>\n                </div>\n"

with open('ejecucion-obras.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace content inside <section class="py-space-2xl bg-surface"> <div class="max-w-7xl mx-auto px-gutter">
# Up to the closing </div></section>
pattern = r'(<!-- WORKS SECTION -->\s*<section class="py-space-2xl bg-surface">\s*<div class="max-w-7xl mx-auto px-gutter">).*?(</div>\s*</section>)'

new_html = re.sub(pattern, rf'\1\n{gallery_html}\n\2', html, flags=re.DOTALL)

with open('ejecucion-obras.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("ejecucion-obras.html rebuilt successfully!")
