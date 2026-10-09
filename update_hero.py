import re

with open("index.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Replace the heroSlides array definition and the switchHeroSlide function
old_script = """                const heroSlides = [
                    {
                        title: "INFRAESTRUCTURA <br><span class='text-primary underline decoration-primary/40 decoration-4 underline-offset-8'>RECREATIVA</span>",
                        desc: "Recuperacin de espacios pǧblicos. Ejecucin de losas deportivas, ǭreas verdes y zonas de recreacin con estrictos estǭndares de seguridad y durabilidad estructural.",
                        tag: "FOLIO 04 / PROYECTO 2024",
                        imgSrc: "./01-recreacion/IMAGEN%204.webp"
                    },
                    {
                        title: "PAVIMENTACI"N <br><span class='text-primary underline decoration-primary/40 decoration-4 underline-offset-8'>DE V?AS</span>",
                        desc: "Ejecucin de pistas y veredas de concreto de alta resistencia. Movimiento de tierras, compactacin y vaciado con maquinaria especializada bajo normativa tǸcnica MTC.",
                        tag: "FOLIO 08 / VIALIDAD MTC",
                        imgSrc: "./02-pistas/IMAGEN%201.webp"
                    },
                    {
                        title: "MANTENIMIENTO <br><span class='text-primary underline decoration-primary/40 decoration-4 underline-offset-8'>ESTRUCTURAL</span>",
                        desc: "Servicios integrales de mantenimiento preventivo y correctivo en infraestructuras civiles. Preservamos la integridad de las obras con soluciones tǸcnicas precisas.",
                        tag: "FOLIO 12 / GESTI"N CIV",
                        imgSrc: "./03-mantenimiento/IMAGEN%205.webp"
                    }
                ];

                function switchHeroSlide(index) {
                    const data = heroSlides[index];
                    document.getElementById('hero-title').innerHTML = data.title;
                    document.getElementById('hero-desc').innerText = data.desc;
                    document.getElementById('hero-tag').innerText = data.tag;

                    const imgEl = document.getElementById('hero-img');
                    imgEl.src = data.imgSrc;"""

# Wait, the unicode chars might cause match failure. Let's use regex.
pattern = r'const heroSlides = \[.*?function switchHeroSlide\(index\) \{.*?imgEl\.src = data\.imgSrc;'

new_script = """const heroSlides = [
                    {
                        title: "INFRAESTRUCTURA <br><span class='text-primary underline decoration-primary/40 decoration-4 underline-offset-8'>RECREATIVA</span>",
                        desc: "Recuperación de espacios públicos. Ejecución de losas deportivas, áreas verdes y zonas de recreación con estrictos estándares de seguridad y durabilidad estructural.",
                        tag: "FOLIO 04 / PROYECTO 2024",
                        images: [
                            "./images/imagen-3.jpeg", 
                            "./01-recreacion/IMAGEN%204.webp", 
                            "./01-recreacion/IMAGEN%208.webp", 
                            "./01-recreacion/IMAGEN%2012.webp"
                        ]
                    },
                    {
                        title: "PAVIMENTACIÓN <br><span class='text-primary underline decoration-primary/40 decoration-4 underline-offset-8'>DE VÍAS</span>",
                        desc: "Ejecución de pistas y veredas de concreto de alta resistencia. Movimiento de tierras, compactación y vaciado con maquinaria especializada bajo normativa técnica MTC.",
                        tag: "FOLIO 08 / VIALIDAD MTC",
                        images: [
                            "./02-pistas/IMAGEN%201.webp",
                            "./02-pistas/IMAGEN%205.webp",
                            "./02-pistas/IMAGEN%2010.webp"
                        ]
                    },
                    {
                        title: "MANTENIMIENTO <br><span class='text-primary underline decoration-primary/40 decoration-4 underline-offset-8'>ESTRUCTURAL</span>",
                        desc: "Servicios integrales de mantenimiento preventivo y correctivo en infraestructuras civiles. Preservamos la integridad de las obras con soluciones técnicas precisas.",
                        tag: "FOLIO 12 / GESTIÓN CIV",
                        images: [
                            "./03-mantenimiento/IMAGEN%201.webp",
                            "./03-mantenimiento/IMAGEN%205.webp",
                            "./03-mantenimiento/IMAGEN%209.webp"
                        ]
                    }
                ];

                let currentSlideIndex = 0;
                let currentImageIndex = 0;
                let imageInterval;

                function startImageRotation() {
                    clearInterval(imageInterval);
                    imageInterval = setInterval(() => {
                        const data = heroSlides[currentSlideIndex];
                        currentImageIndex = (currentImageIndex + 1) % data.images.length;
                        const imgEl = document.getElementById('hero-img');
                        imgEl.style.opacity = 0;
                        setTimeout(() => {
                            imgEl.src = data.images[currentImageIndex];
                            imgEl.style.opacity = 1;
                        }, 300);
                    }, 4000);
                }

                // Initial start
                setTimeout(startImageRotation, 1000);

                function switchHeroSlide(index) {
                    currentSlideIndex = index;
                    currentImageIndex = 0;
                    const data = heroSlides[index];
                    document.getElementById('hero-title').innerHTML = data.title;
                    document.getElementById('hero-desc').innerText = data.desc;
                    document.getElementById('hero-tag').innerText = data.tag;

                    const imgEl = document.getElementById('hero-img');
                    imgEl.style.opacity = 0;
                    setTimeout(() => {
                        imgEl.src = data.images[0];
                        imgEl.style.opacity = 1;
                    }, 300);
                    
                    startImageRotation();"""

html = re.sub(pattern, new_script, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated hero script!")
