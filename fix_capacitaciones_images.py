import os, glob

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
                <img src="./05-formacion/ponencias/img_1.webp" alt="Formación Técnica" class="w-full h-full object-cover opacity-50 brightness-110">
                <div class="absolute inset-0 bg-gradient-to-b from-surface/20 via-surface/60 to-surface"></div>
            </div>
            <div class="relative z-10 max-w-4xl mx-auto" data-aos="fade-up">
                <div class="font-technical-code text-technical-code text-primary uppercase tracking-widest mb-4">INSTITUTO VADGOD</div>
                <h1 class="font-headline-xl text-headline-xl-mobile md:text-headline-xl text-white uppercase font-bold tracking-tight mb-space-md">FORMACIÓN TÉCNICA</h1>
                <p class="font-body-lg text-body-lg text-secondary max-w-2xl mx-auto leading-relaxed">
                    Compartimos nuestra experiencia directamente desde el campo. Dictamos programas de formación especializados para ingenieros civiles, arquitectos, maestros de obra y operarios, asegurando que el mercado mantenga estándares de alta calidad.
                </p>
            </div>
        </section>

        <!-- GALLERY SECTION -->
        <section class="py-space-2xl bg-surface">
            <div class="max-w-7xl mx-auto px-gutter">
                <div class="text-center mb-space-xl" data-aos="fade-up">
                    <h2 class="font-headline-lg text-headline-lg-mobile md:text-headline-lg text-white uppercase font-bold mb-space-md">GALERÍA DE FORMACIÓN</h2>
                    <div class="w-24 h-1 bg-primary mx-auto"></div>
                </div>
                
                <!-- Filters -->
                <div class="flex flex-wrap justify-center gap-4 mb-space-xl" data-aos="fade-up" data-aos-delay="100">
                    <button class="filter-btn active px-6 py-2 bg-primary text-on-primary font-technical-code uppercase text-sm font-bold border border-primary transition-colors" data-filter="all">TODOS</button>
                    <button class="filter-btn px-6 py-2 bg-surface-container-high text-outline hover:text-white font-technical-code uppercase text-sm border border-outline-variant/30 transition-colors" data-filter="ponencias">PONENCIAS</button>
                    <button class="filter-btn px-6 py-2 bg-surface-container-high text-outline hover:text-white font-technical-code uppercase text-sm border border-outline-variant/30 transition-colors" data-filter="capacitaciones">CAPACITACIONES</button>
                    <button class="filter-btn px-6 py-2 bg-surface-container-high text-outline hover:text-white font-technical-code uppercase text-sm border border-outline-variant/30 transition-colors" data-filter="laboratorio">LABORATORIO</button>
                    <button class="filter-btn px-6 py-2 bg-surface-container-high text-outline hover:text-white font-technical-code uppercase text-sm border border-outline-variant/30 transition-colors" data-filter="catedra">CÁTEDRA</button>
                    <button class="filter-btn px-6 py-2 bg-surface-container-high text-outline hover:text-white font-technical-code uppercase text-sm border border-outline-variant/30 transition-colors" data-filter="campo">FORMACIÓN PRÁCTICA</button>
                </div>

                <!-- Grid -->
                <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4" id="gallery-grid">
"""

categories = ['ponencias', 'capacitaciones', 'laboratorio', 'catedra', 'campo']

for cat in categories:
    folder = f'05-formacion/{cat}'
    if os.path.exists(folder):
        images = []
        for ext in ('*.webp', '*.jpg', '*.jpeg', '*.png'):
            images.extend(glob.glob(os.path.join(folder, ext)))
        
        images = sorted(list(set(images)))
        
        for img in images:
            img_web = img.replace('\\', '/').replace(' ', '%20')
            html += f"""
                    <div class="gallery-item cursor-pointer overflow-hidden group border border-outline-variant/20 transition-all duration-300 relative" data-category="{cat}" onclick="openLightbox('./{img_web}')" data-aos="fade-up">
                        <img src="./{img_web}" alt="{cat}" class="w-full h-64 object-cover transform group-hover:scale-105 transition-transform duration-500 filter grayscale(20%) group-hover:grayscale-0">
                        <div class="absolute inset-0 bg-surface/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                            <span class="material-symbols-outlined text-primary text-4xl">zoom_in</span>
                        </div>
                        <div class="absolute bottom-0 left-0 right-0 bg-surface-container-highest/90 p-2 transform translate-y-full group-hover:translate-y-0 transition-transform duration-300">
                            <span class="font-technical-code text-xs text-primary uppercase block text-center">{cat}</span>
                        </div>
                    </div>"""

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
        <div id="lightbox-caption" class="mt-4 font-technical-code text-primary uppercase tracking-widest text-sm"></div>
    </div>

    <!-- Scripts -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({{ once: true, offset: 50, duration: 800 }});
        
        // Filter logic
        document.querySelectorAll('.filter-btn').forEach(btn => {{
            btn.addEventListener('click', function() {{
                // Update buttons
                document.querySelectorAll('.filter-btn').forEach(b => {{
                    b.classList.remove('active', 'bg-primary', 'text-on-primary', 'border-primary');
                    b.classList.add('bg-surface-container-high', 'text-outline', 'border-outline-variant/30');
                }});
                this.classList.add('active', 'bg-primary', 'text-on-primary', 'border-primary');
                this.classList.remove('bg-surface-container-high', 'text-outline', 'border-outline-variant/30');
                
                const filter = this.getAttribute('data-filter');
                const items = document.querySelectorAll('.gallery-item');
                
                items.forEach(item => {{
                    if(filter === 'all' || item.getAttribute('data-category') === filter) {{
                        item.style.display = 'block';
                        setTimeout(() => item.style.opacity = '1', 50);
                    }} else {{
                        item.style.opacity = '0';
                        setTimeout(() => item.style.display = 'none', 300);
                    }}
                }});
            }});
        }});
        
        // Lightbox logic
        const lightbox = document.getElementById('lightbox');
        const lightboxImg = document.getElementById('lightbox-img');
        const lightboxCaption = document.getElementById('lightbox-caption');
        
        window.openLightbox = function(src) {{
            lightboxImg.src = src;
            lightbox.classList.remove('hidden');
            setTimeout(() => {{
                lightbox.classList.remove('opacity-0');
                lightboxImg.classList.remove('scale-95');
                lightboxImg.classList.add('scale-100');
            }}, 10);
            
            const parts = src.split('/');
            if(parts.length > 2) {{
                lightboxCaption.innerText = "VADGOD INGS | " + parts[parts.length-2].toUpperCase();
            }}
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

html = html.replace("<title>VAD GOD ING'S | Civil Engineering & Construction</title>", "<title>Formación Técnica | VAD GOD ING'S</title>")
html = html.replace('text-primary font-bold', 'text-outline hover:text-white')

with open('capacitaciones.html', 'w', encoding='utf-8') as f:
    f.write(html)
