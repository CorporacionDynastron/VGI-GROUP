import os

head = open('head_template.txt', encoding='utf-8').read()
header = open('header_template.txt', encoding='utf-8').read()
footer = open('footer_template.txt', encoding='utf-8').read()

html = f"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
{head}
<body class="bg-surface text-on-surface font-body-md antialiased selection:bg-primary/30 selection:text-primary">
    {header}
    
    <main class="w-full flex flex-col pt-[100px]">
        <!-- HERO SECTION -->
        <section class="relative w-full h-[60vh] min-h-[400px] flex flex-col items-center justify-center text-center px-gutter overflow-hidden border-b border-outline-variant/20">
            <div class="absolute inset-0 z-0">
                <img src="./02-pistas/DJI_0461.webp" alt="Obras Ejecutadas" class="w-full h-full object-cover opacity-50 brightness-110 object-center">
                <div class="absolute inset-0 bg-gradient-to-b from-surface/20 via-surface/60 to-surface"></div>
            </div>
            <div class="relative z-10 max-w-4xl mx-auto" data-aos="fade-up">
                <div class="font-technical-code text-technical-code text-primary uppercase tracking-widest mb-4">PORTAFOLIO DE EJECUCIÓN</div>
                <h1 class="font-headline-xl text-headline-xl-mobile md:text-headline-xl text-white uppercase font-bold tracking-tight mb-space-md">OBRAS ENTREGADAS</h1>
                <p class="font-body-lg text-body-lg text-secondary max-w-2xl mx-auto leading-relaxed">
                    Mostramos únicamente proyectos 100% concluidos que reflejan nuestra capacidad técnica, cumplimiento de normativas y rigor en la construcción civil y urbana.
                </p>
            </div>
        </section>

        <!-- WORKS SECTION -->
        <section class="py-space-2xl bg-surface">
            <div class="max-w-7xl mx-auto px-gutter">
"""

categories = [
    {
        "id": "edificaciones",
        "title": "EDIFICACIONES Y AFINES",
        "folders": ["08-multifamiliar", "06-planta"]
    },
    {
        "id": "viales",
        "title": "VIALES, PUERTOS Y AFINES",
        "folders": ["02-pistas"]
    },
    {
        "id": "saneamiento",
        "title": "SANEAMIENTO Y AFINES",
        "folders": ["07-saneamiento"]
    },
    {
        "id": "recreativa",
        "title": "INFRAESTRUCTURA RECREATIVA",
        "folders": ["01-recreacion", "09-recreacional"]
    },
    {
        "id": "mantenimiento",
        "title": "MANTENIMIENTO DE INFRAESTRUCTURA",
        "folders": ["03-mantenimiento"]
    }
]

import glob

for cat in categories:
    html += f"""
                <div id="{cat['id']}" class="mb-space-2xl scroll-mt-[120px]" data-aos="fade-up">
                    <div class="mb-space-xl border-b-2 border-primary/30 pb-4">
                        <h2 class="font-headline-lg text-3xl md:text-4xl text-primary uppercase font-bold">{cat['title']}</h2>
                    </div>
                    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
"""
    count = 0
    for folder in cat['folders']:
        if os.path.exists(folder):
            images = []
            for ext in ('*.webp', '*.jpg', '*.jpeg', '*.png'):
                images.extend(glob.glob(os.path.join(folder, ext)))
                images.extend(glob.glob(os.path.join(folder, "**", ext), recursive=True))
            
            # Sort images to have deterministic output
            images = sorted(list(set(images)))
            
            for img in images:
                count += 1
                img_web = img.replace('\\', '/')
                html += f"""
                        <div class="group relative overflow-hidden border border-outline-variant/20 cursor-pointer h-64" onclick="openLightbox('./{img_web}')">
                            <img src="./{img_web}" alt="Obra" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700">
                            <div class="absolute inset-0 bg-surface/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                                <span class="material-symbols-outlined text-white text-3xl">zoom_in</span>
                            </div>
                        </div>"""
    
    if count == 0:
         html += f"""
                        <div class="col-span-full py-12 text-center text-outline font-technical-code">
                            [ ACTUALIZANDO PORTAFOLIO FOTOGRÁFICO DE OBRAS CONCLUIDAS ]
                        </div>"""
         
    html += """
                    </div>
                </div>
"""

html += f"""
            </div>
        </section>
    </main>
    
    {footer}

    <!-- Lightbox Modal -->
    <div id="lightbox" class="fixed inset-0 z-[200] bg-surface/95 hidden flex-col items-center justify-center p-4 backdrop-blur-md opacity-0 transition-opacity duration-300">
        <button onclick="closeLightbox()" class="absolute top-6 right-6 text-white hover:text-primary transition-colors z-10">
            <span class="material-symbols-outlined text-4xl">close</span>
        </button>
        <img id="lightbox-img" src="" alt="Zoomed Image" class="max-w-full max-h-[85vh] object-contain border border-outline-variant/30 shadow-2xl transform scale-95 transition-transform duration-300">
    </div>

    <!-- Scripts -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({{ once: true, offset: 50, duration: 800 }});
        
        // Lightbox logic
        const lightbox = document.getElementById('lightbox');
        const lightboxImg = document.getElementById('lightbox-img');
        
        window.openLightbox = function(src) {{
            lightboxImg.src = src;
            lightbox.classList.remove('hidden');
            setTimeout(() => {{
                lightbox.classList.remove('opacity-0');
                lightboxImg.classList.remove('scale-95');
                lightboxImg.classList.add('scale-100');
            }}, 10);
        }};
        
        window.closeLightbox = function() {{
            lightbox.classList.add('opacity-0');
            lightboxImg.classList.remove('scale-100');
            lightboxImg.classList.add('scale-95');
            setTimeout(() => {{
                lightbox.classList.add('hidden');
                lightboxImg.src = '';
            }}, 300);
        }};
        
        document.addEventListener('keydown', e => {{
            if(e.key === 'Escape' && !lightbox.classList.contains('hidden')) closeLightbox();
        }});
        lightbox.addEventListener('click', e => {{
            if(e.target === lightbox) closeLightbox();
        }});
    </script>
</body>
</html>
"""

html = html.replace("<title>VAD GOD ING'S | Civil Engineering & Construction</title>", "<title>Obras Entregadas | VAD GOD ING'S</title>")
html = html.replace('text-primary font-bold', 'text-outline hover:text-white')

with open('obras.html', 'w', encoding='utf-8') as f:
    f.write(html)
