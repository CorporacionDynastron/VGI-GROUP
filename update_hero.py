import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# I will replace the hero section
hero_pattern = r'<main.*?</main>' # Wait, no, we just want to replace the first section.
hero_pattern = r'<!-- HERO SECTION -->.*?<!-- NOSOTROS BRIEFING -->'
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
                        Diseñamos y construimos <span class="text-primary">el futuro.</span>
                    </h1>
                    <p class="font-body-lg text-body-lg text-secondary leading-relaxed mb-space-xl max-w-2xl" id="hero-desc">
                        Diseñamos y ejecutamos obras de ingeniería civil con precisión milimétrica. Transformamos espacios públicos, garantizando máxima seguridad.
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
        <!-- NOSOTROS BRIEFING -->"""

html = re.sub(r'<!-- HERO SECTION -->.*?<!-- NOSOTROS BRIEFING -->', new_hero, html, flags=re.DOTALL)

# Update the javascript for hero slide
js_replace = r'const imgEl = document\.getElementById\(\'hero-img\'\);.*?tagEl\.innerText = slide\.tag;'
new_js = """const imgEl = document.getElementById('hero-bg');
                    const titleEl = document.getElementById('hero-title');
                    const headlineEl = document.getElementById('hero-headline');
                    const descEl = document.getElementById('hero-desc');

                    imgEl.style.opacity = 0;
                    setTimeout(() => {
                        imgEl.src = slide.img;
                        titleEl.innerText = slide.title;
                        headlineEl.innerHTML = slide.headline || slide.title;
                        descEl.innerText = slide.desc;
                        imgEl.style.opacity = 1;
                    }, 500);

                    // Update dots
                    document.querySelectorAll('.hero-dot').forEach((dot, idx) => {
                        if(idx === index) {
                            dot.className = "hero-dot w-3 h-3 bg-primary rounded-full transition-all duration-300 shadow-[0_0_10px_rgba(212,175,55,0.5)]";
                        } else {
                            dot.className = "hero-dot w-2 h-2 bg-outline-variant rounded-full hover:bg-primary/50 transition-all duration-300";
                        }
                    });"""
html = re.sub(js_replace, new_js, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
