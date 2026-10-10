import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_hero = """<!-- HERO SECTION -->
        <section class="relative w-full h-[80vh] min-h-[600px] flex items-center overflow-hidden">
            <!-- Background Image Slider -->
            <div class="absolute inset-0 z-0 bg-surface-dim">
                <img id="hero-bg" src="./images/imagen-3.jpeg" alt="Construccion Civil" 
                     class="w-full h-full object-cover filter brightness-75 transition-opacity duration-1000 ease-in-out">
                <div class="absolute inset-0 bg-gradient-to-r from-surface via-surface/80 to-transparent"></div>
                <div class="absolute inset-0 bg-gradient-to-t from-surface via-transparent to-transparent"></div>
            </div>

            <div class="max-w-7xl mx-auto px-gutter relative z-10 w-full flex flex-col justify-center pt-20">
                <div class="max-w-3xl" data-aos="fade-up">
                    <div class="flex items-center gap-2 text-primary font-technical-code text-technical-code uppercase mb-4">
                        <span class="material-symbols-outlined text-sm">engineering</span>
                        <span id="hero-title">INFRAESTRUCTURA RECREATIVA</span>
                    </div>
                    <h1 class="font-headline-xl text-headline-xl-mobile md:text-headline-xl text-white uppercase tracking-tight font-bold mb-space-md" id="hero-headline">
                        Espacios públicos de <span class="text-primary">alto impacto.</span>
                    </h1>
                    <p class="font-body-lg text-body-lg text-secondary leading-relaxed mb-space-xl max-w-2xl" id="hero-desc">
                        Diseñamos y ejecutamos obras de ingeniería civil con precisión milimétrica. Transformamos espacios públicos, losas deportivas y áreas recreativas garantizando máxima seguridad y cumplimiento estricto de plazos.
                    </p>
                    
                    <div class="flex flex-wrap items-center gap-4">
                        <a href="obras.html"
                            class="inline-flex items-center justify-center bg-primary text-on-primary font-label-caps text-label-caps uppercase px-8 py-4 tracking-wider hover:bg-surface-tint transition-all duration-300 shadow-[0_0_24px_rgba(212,175,55,0.4)]">
                            Explora nuestras obras <span class="material-symbols-outlined text-sm ml-2">arrow_forward</span>
                        </a>
                        <a href="#contacto-tecnico"
                            class="inline-flex items-center justify-center bg-surface-container-high text-on-surface font-label-caps text-label-caps uppercase px-8 py-4 tracking-wider border border-outline-variant/30 hover:border-primary/50 transition-all duration-300">
                            <span class="material-symbols-outlined text-sm text-primary mr-2">description</span> Solicitar Cotización
                        </a>
                    </div>
                </div>
                
                <!-- Slide Controls -->
                <div class="flex items-center gap-2 mt-12" data-aos="fade-up" data-aos-delay="200">
                    <button onclick="switchHeroSlide(0)" class="hero-dot w-3 h-3 bg-primary rounded-full transition-all duration-300 shadow-[0_0_10px_rgba(212,175,55,0.5)]"></button>
                    <button onclick="switchHeroSlide(1)" class="hero-dot w-2 h-2 bg-outline-variant rounded-full hover:bg-primary/50 transition-all duration-300"></button>
                    <button onclick="switchHeroSlide(2)" class="hero-dot w-2 h-2 bg-outline-variant rounded-full hover:bg-primary/50 transition-all duration-300"></button>
                </div>
            </div>
        </section>
        <!-- BANNER: CERTIFICACIONES DE CALIDAD Y CONFIANZA -->"""

# Perform replacement
html = re.sub(r'<!-- HERO SECTION WITH TOPOGRAPHIC BLUEPRINT & DUAL SLIDER -->.*?<!-- BANNER: CERTIFICACIONES DE CALIDAD Y CONFIANZA -->', new_hero, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
