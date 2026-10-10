import json
import re

# 1. Read index.html to extract its complete <head> block
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

head_match = re.search(r'(<head>.*?</head>)', index_html, flags=re.DOTALL | re.IGNORECASE)
if not head_match:
    print("Could not find <head> in index.html!")
    exit(1)
index_head = head_match.group(1)

# Modify title
index_head = re.sub(r'<title>.*?</title>', '<title>Obras - VGI</title>', index_head)

html = f"""<!DOCTYPE html>
<html lang="es" class="dark scroll-smooth">
{index_head}
<body class="bg-background font-body-md text-on-surface antialiased min-h-screen">
    
    <script src="header.js"></script>

    <main class="w-full pt-0 bg-surface min-h-[calc(100vh-20rem)] flex flex-col">
        <!-- HERO -->
        <section class="relative w-full h-[40vh] min-h-[300px] flex flex-col items-center justify-center overflow-hidden border-b border-outline-variant">
            <div class="absolute inset-0 z-0 bg-surface-dim">
                <img src="./02-pistas/IMAGEN%201.webp" alt="Obras Ejecutadas" class="w-full h-full object-cover opacity-20 object-center filter grayscale">
                <div class="absolute inset-0 bg-gradient-to-b from-surface/40 via-surface/80 to-surface"></div>
            </div>
            
            <div class="max-w-7xl mx-auto px-gutter relative z-10 w-full flex flex-col items-center text-center mt-20">
                <div class="flex items-center gap-2 mb-4">
                    <div class="h-px w-8 bg-primary"></div>
                    <span class="font-label-caps text-primary tracking-widest uppercase text-sm font-bold">PORTAFOLIO</span>
                    <div class="h-px w-8 bg-primary"></div>
                </div>
                <h1 class="font-headline-lg text-4xl md:text-5xl text-white uppercase tracking-tight font-bold drop-shadow-lg mb-4">
                    NUESTRAS <span class="text-primary">OBRAS</span>
                </h1>
                <p class="font-body-md text-on-surface-variant text-lg max-w-2xl mx-auto">
                    Clasificación general de obras y proyectos de infraestructura.
                </p>
            </div>
        </section>

        <!-- WORKS GRID SECTION -->
        <section class="w-full bg-surface py-space-xl relative border-t border-outline-variant">
            <div class="max-w-7xl mx-auto px-gutter">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-gutter">
"""

categories = [
    {
        "id": "edificaciones",
        "num": "01",
        "header": "EDIFICACIONES",
        "title": "OBRAS DE EDIFICACIONES Y AFINES",
        "img": "./08-multifamiliar/primera-piedra/PRIMERA_PIEDRA_1.webp",
        "desc": "Ejecución integral de infraestructuras residenciales, comerciales e institucionales con los más altos estándares estructurales y arquitectónicos."
    },
    {
        "id": "viales",
        "num": "02",
        "header": "INFRAESTRUCTURA VIAL",
        "title": "OBRAS VIALES, PUERTOS Y AFINES",
        "img": "./02-pistas/IMAGEN%209.webp",
        "desc": "Construcción y pavimentación de carreteras, vías urbanas e infraestructura portuaria garantizando conectividad y máxima resistencia."
    },
    {
        "id": "saneamiento",
        "num": "03",
        "header": "SANEAMIENTO",
        "title": "OBRAS DE SANEAMIENTO Y AFINES",
        "img": "./07-saneamiento/saneamiento_1.jpg",
        "desc": "Desarrollo de redes de agua potable, alcantarillado y plantas de tratamiento (PETAR) para mejorar la calidad de vida y el medio ambiente."
    },
    {
        "id": "electromecanicas",
        "num": "04",
        "header": "ELECTROMECÁNICA",
        "title": "OBRAS ELECTROMECÁNICAS Y TELECOM.",
        "img": "./images/imagen-6.jpeg",
        "desc": "Instalaciones energéticas, montajes industriales y redes de telecomunicaciones ejecutadas con absoluta precisión técnica y seguridad."
    },
    {
        "id": "represas",
        "num": "05",
        "header": "REPRESAS E IRRIGACIONES",
        "title": "OBRAS DE REPRESAS E IRRIGACIONES",
        "img": "./01-recreacion/IMAGEN%201.webp",
        "desc": "Proyectos hidráulicos de gran envergadura para el control, almacenamiento y distribución eficiente de recursos hídricos en el sector."
    }
]

for cat in categories:
    html += f"""
                    <div id="{cat['id']}" class="scroll-mt-[150px] bg-surface-container border-t-2 border-t-primary border border-outline-variant flex flex-col group hover:border-primary/50 transition-colors shadow-lg">
                        <div class="p-space-md bg-surface-container-high flex items-center justify-between font-label-caps text-xs font-bold tracking-widest text-outline">
                            <span class="text-primary font-bold tracking-wider">{cat['num']}. {cat['header']}</span>
                        </div>
                        <div class="relative h-56 w-full overflow-hidden bg-surface-dim">
                            <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="{cat['header']}" src="{cat['img']}">
                        </div>
                        <div class="p-space-lg flex-1 flex flex-col">
                            <h3 class="font-headline-sm text-xl text-white uppercase font-bold mb-space-sm leading-tight">
                                {cat['title']}
                            </h3>
                            <p class="font-body-sm text-on-surface-variant leading-relaxed mt-2">
                                {cat['desc']}
                            </p>
                        </div>
                    </div>
"""

html += """
                </div>
            </div>
        </section>
    </main>

    <script src="footer.js"></script>
</body>
</html>
"""

with open('obras.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("obras.html generated perfectly!")

# 2. Update header.js to point to those IDs!
with open('header.js', 'r', encoding='utf-8') as f:
    header_js = f.read()

# Replace general 'obras.html' links with specific ones.
# Because the string matches exactly, I'll just use string replacement.
header_js = header_js.replace('<a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS DE EDIFICACIONES Y AFINES</a>', 
                              '<a href="obras.html#edificaciones" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS DE EDIFICACIONES Y AFINES</a>')

header_js = header_js.replace('<a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS VIALES, PUERTOS Y AFINES</a>', 
                              '<a href="obras.html#viales" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS VIALES, PUERTOS Y AFINES</a>')

header_js = header_js.replace('<a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS DE SANEAMIENTO Y AFINES</a>', 
                              '<a href="obras.html#saneamiento" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS DE SANEAMIENTO Y AFINES</a>')

header_js = header_js.replace('<a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS ELECTROMEC?NICAS, ENERG%TICAS, TELECOM. Y AFINES</a>', 
                              '<a href="obras.html#electromecanicas" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS ELECTROMECÁNICAS, ENERGÉTICAS, TELECOM. Y AFINES</a>')

header_js = header_js.replace('OBRAS ELECTROMECNICAS, ENERGTICAS, TELECOM. Y AFINES', 'OBRAS ELECTROMECÁNICAS, ENERGÉTICAS, TELECOM. Y AFINES') # Catch any encoding issues from previous regex

header_js = header_js.replace('<a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS DE REPRESAS, IRRIGACIONES Y AFINES</a>', 
                              '<a href="obras.html#represas" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS DE REPRESAS, IRRIGACIONES Y AFINES</a>')

# Just to be sure the electromechanics link works if the exact string replacement failed due to encoding:
header_js = re.sub(r'<a href="obras\.html"[^>]*>OBRAS ELECTROMEC[^<]*</a>', 
                   r'<a href="obras.html#electromecanicas" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS ELECTROMECÁNICAS, ENERGÉTICAS, TELECOM. Y AFINES</a>', 
                   header_js)

with open('header.js', 'w', encoding='utf-8') as f:
    f.write(header_js)
print("header.js submenu links updated!")

