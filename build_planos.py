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
                <img src="./Fotos Proyectos/PROYECTO AMALFI- UNIFAMILIAR.webp" alt="Diseño Arquitectónico" class="w-full h-full object-cover opacity-50 brightness-110 object-center">
                <div class="absolute inset-0 bg-gradient-to-b from-surface/20 via-surface/60 to-surface"></div>
            </div>
            <div class="relative z-10 max-w-4xl mx-auto" data-aos="fade-up">
                <div class="font-technical-code text-technical-code text-primary uppercase tracking-widest mb-4">DEPARTAMENTO DE ARQUITECTURA</div>
                <h1 class="font-headline-xl text-headline-xl-mobile md:text-headline-xl text-white uppercase font-bold tracking-tight mb-space-md">DISEÑO Y PROYECTOS</h1>
                <p class="font-body-lg text-body-lg text-secondary max-w-2xl mx-auto leading-relaxed">
                    Visualizamos espacios con estética contemporánea y funcionalidad técnica. Cada diseño está respaldado por rigurosas memorias de cálculo, modelos 3D y cumplimiento de normativas vigentes, garantizando viabilidad técnica.
                </p>
            </div>
        </section>

        <!-- GALLERY SECTION -->
        <section class="py-space-2xl bg-surface">
            <div class="max-w-7xl mx-auto px-gutter">
                <div class="text-center mb-space-xl" data-aos="fade-up">
                    <h2 class="font-headline-lg text-headline-lg-mobile md:text-headline-lg text-white uppercase font-bold mb-space-md">PORTAFOLIO DE DISEÑOS</h2>
                    <div class="w-24 h-1 bg-primary mx-auto"></div>
                </div>

                <!-- Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
"""

projects = [
    {
        "name": "PROYECTO AMALFI",
        "tag": "UNIFAMILIAR",
        "images": [
            "PROYECTO AMALFI- UNIFAMILIAR.webp",
            "PROYECTO AMALFI- INTERIOR 1.webp",
            "PROYECTO AMALFI- INTERIOR 2.webp",
            "PROYECTO AMALFI- INTERIOR 3.webp"
        ]
    },
    {
        "name": "PROYECTO LITUANIA",
        "tag": "MULTIFAMILIAR",
        "images": [
            "PROYECTO LITUANIA-MULTIFAMILIAR.webp",
            "PROYECTO LITUANIA-IINTERIOR 1.webp",
            "PROYECTO LITUANIA-IINTERIOR 2.webp",
            "PROYECTO LITUANIA - INTERIOR 3.webp"
        ]
    },
    {
        "name": "PROYECTO MANHATAN",
        "tag": "MULTIFAMILIAR",
        "images": [
            "PROYECTO MANHATAN- MULTIFAMILIAR.webp",
            "PROYECTO MANHATAN - INTERIOR 1.webp",
            "PROYECTO MANHATAN - INTERIOR 2.webp"
        ]
    },
    {
        "name": "PROYECTO ALBORADA",
        "tag": "CASA DE CAMPO",
        "images": [
            "PROYECTO ALBORADA - CASA DE CAMPO.webp",
            "PROYECTO ALBORADA - INTERIOR 1.webp",
            "PROYECTO ALBORADA - INTERIOR 2.webp",
            "PROYECTO ALBORADA - INTERIOR 3.webp"
        ]
    },
    {
        "name": "PROYECTO OLIVO",
        "tag": "CASA DE CAMPO",
        "images": [
            "PROYECTO OLIVO - CASA DE CAMPO.webp",
            "PROYECTO OLIVO - INTERIOR 1.webp",
            "PROYECTO OLIVO - INTERIOR 2.webp",
            "PROYECTO OLIVO - INTERIOR 3.webp"
        ]
    }
]

for proj in projects:
    html += f"""
                    <div class="bg-surface-container-low border border-outline-variant/20 overflow-hidden flex flex-col group" data-aos="fade-up">
                        <div class="relative h-64 overflow-hidden cursor-pointer" onclick="openLightbox('./Fotos Proyectos/{proj['images'][0]}')">
                            <img src="./Fotos Proyectos/{proj['images'][0]}" alt="{proj['name']}" class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700">
                            <div class="absolute inset-0 bg-surface/30 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                                <span class="material-symbols-outlined text-white text-3xl">zoom_in</span>
                            </div>
                        </div>
                        <div class="p-6 flex-1 flex flex-col">
                            <div class="font-technical-code text-xs text-primary tracking-widest uppercase mb-2">{proj['tag']}</div>
                            <h3 class="font-headline-sm text-white uppercase font-bold mb-4">{proj['name']}</h3>
                            <div class="mt-auto grid grid-cols-3 gap-2">
"""
    for img in proj['images'][1:]:
        html += f"""
                                <div class="relative h-20 overflow-hidden border border-outline-variant/30 cursor-pointer hover:border-primary/50 transition-colors" onclick="openLightbox('./Fotos Proyectos/{img}')">
                                    <img src="./Fotos Proyectos/{img}" alt="Detalle" class="w-full h-full object-cover">
                                </div>
"""
    html += """
                            </div>
                        </div>
                    </div>
"""

html += f"""
                </div>
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

html = html.replace("<title>VAD GOD ING'S | Civil Engineering & Construction</title>", "<title>Diseño de Proyectos | VAD GOD ING'S</title>")
html = html.replace('text-primary font-bold', 'text-outline hover:text-white')

with open('planos.html', 'w', encoding='utf-8') as f:
    f.write(html)
