import re

with open("NuevaPlantillaVGI.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Logo
html = re.sub(r'src="https://lh3.googleusercontent.com/aida/[^"]+"', 'src="./WhatsApp%20Image%202026-07-09%20at%2010.41.46%20AM.png"', html)

# Replace ISOs
# 9001
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuBs3RaVs[^"]+"', 'src="./storage/aliados/fvKaovpp4p243ZJGkNfqN83l58BVEFS0TtlDmzGb-transparent.webp"', html)
# 14001
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuB0asNuf[^"]+"', 'src="./storage/aliados/zEyex57sHhCsE7CaJ0HKFFfJctKOFXFJ28E6HFUe-transparent.webp"', html)
# 45001
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuAWBv9RL[^"]+"', 'src="./storage/aliados/NOVsTFA7NHgob7VYxW0tebRRr52GCNbqBie1Dx2i-transparent.webp"', html)
# 37001
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuB_KI1wI[^"]+"', 'src="./storage/aliados/Zlx9PTNbfzQnLo5gGgzXrPj3DrHB1Ksu0GuTLS9N-transparent.webp"', html)
# CIP
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuCKe4XUI[^"]+"', 'src="./storage/aliados/rVe1f7nhZHb2CaJWpPnSWbWVJNM5tUAdSuh129Xt-transparent.webp"', html)

# Blocks Images
# Block 1 Planos
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuBJbqwOm[^"]+"', 'src="./Fotos%20Proyectos/PROYECTO%20ALBORADA%20-%20CASA%20DE%20CAMPO.webp"', html)
# Block 2 Ejecucion
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuDEFt58p[^"]+"', 'src="./02-pistas/IMAGEN%201.webp"', html)
# Block 3 Formacion
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuAdbkbvY[^"]+"', 'src="./05-formacion/ponencia/IMAG_2.jpeg"', html)

# Formacion Images
# Recreacional / Formacion 1 (Seguridad y normativa)
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuCnew6Su[^"]+"', 'src="./05-formacion/IMG-20240409-WA0016.jpg"', html)
# Formacion 2
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuBI7x62Z[^"]+"', 'src="./05-formacion/ponencia/IMAG_3.jpeg"', html)

# Obras Destacadas
# Obra 1
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuBvIt8y6[^"]+"', 'src="./01-recreacion/IMAGEN%203.webp"', html)
# Obra 2
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuAlkXygP[^"]+"', 'src="./02-pistas/IMAGEN%2014.webp"', html)
# Obra 3
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuAedFLkc[^"]+"', 'src="./03-mantenimiento/IMAGEN%202.webp"', html)
# Obra 4
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuB69W4Lg[^"]+"', 'src="./storage/obras/LQbDN2fYWVkgnx5zsFM2oIF2A1T3156X5BnszIHu.webp"', html)


# Initial Hero Image
html = re.sub(r'src="https://lh3.googleusercontent.com/aida-public/AB6AXuBT7_wk-[^"]+"', 'src="./01-recreacion/IMAGEN%204.webp"', html)

# Fix Javascript for Hero Slider
js_old = """imgPrompt: "High-contrast modern civil engineering playground and athletic complex under dramatic twilight sky with warm stadium spotlights, crisp geometric concrete walkways, fresh lush turf, perimeter steel safety fence, architectural photography, hyper-realistic, dark graphite and gold ambience."
                    },
                    {
                        title: "PAVIMENTACIÓN <br><span class='text-primary underline decoration-primary/40 decoration-4 underline-offset-8'>DE VÍAS</span>",
                        desc: "Ejecución de pistas y veredas de concreto de alta resistencia. Movimiento de tierras, compactación y vaciado con maquinaria especializada bajo normativa técnica MTC.",
                        tag: "FOLIO 08 / VIALIDAD MTC",
                        imgPrompt: "Heavy civil roadwork paving machinery applying high strength concrete pavement on major urban boulevard in Peru, surveying equipment in foreground, deep golden sunset hour, industrial precision."
                    },
                    {
                        title: "MANTENIMIENTO <br><span class='text-primary underline decoration-primary/40 decoration-4 underline-offset-8'>ESTRUCTURAL</span>",
                        desc: "Servicios integrales de mantenimiento preventivo y correctivo en infraestructuras civiles. Preservamos la integridad de las obras con soluciones técnicas precisas.",
                        tag: "FOLIO 12 / GESTIÓN CIV",
                        imgPrompt: "Indoor sports arena steel arched truss rehabilitation and maintenance, civil engineers inspecting structural joints and safety roofing, industrial high-end lighting."
                    }
                ];

                function switchHeroSlide(index) {
                    const data = heroSlides[index];
                    document.getElementById('hero-title').innerHTML = data.title;
                    document.getElementById('hero-desc').innerText = data.desc;
                    document.getElementById('hero-tag').innerText = data.tag;

                    const imgEl = document.getElementById('hero-img');
                    imgEl.setAttribute('data-alt', data.imgPrompt);"""

js_new = """imgSrc: "./01-recreacion/IMAGEN%204.webp"
                    },
                    {
                        title: "PAVIMENTACIÓN <br><span class='text-primary underline decoration-primary/40 decoration-4 underline-offset-8'>DE VÍAS</span>",
                        desc: "Ejecución de pistas y veredas de concreto de alta resistencia. Movimiento de tierras, compactación y vaciado con maquinaria especializada bajo normativa técnica MTC.",
                        tag: "FOLIO 08 / VIALIDAD MTC",
                        imgSrc: "./02-pistas/IMAGEN%201.webp"
                    },
                    {
                        title: "MANTENIMIENTO <br><span class='text-primary underline decoration-primary/40 decoration-4 underline-offset-8'>ESTRUCTURAL</span>",
                        desc: "Servicios integrales de mantenimiento preventivo y correctivo en infraestructuras civiles. Preservamos la integridad de las obras con soluciones técnicas precisas.",
                        tag: "FOLIO 12 / GESTIÓN CIV",
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

# Replace ASCII weird chars if any
html = html.replace("PAVIMENTACI\"N", "PAVIMENTACIÓN").replace("V?AS", "VÍAS")

# Do the JS replacement using regex or simple replace
# Because there might be weird characters in the desc, let's use regex
html = re.sub(r'imgPrompt:\s*"High-contrast[^"]+"[\s\S]+?imgEl\.setAttribute\(\'data-alt\',\s*data\.imgPrompt\);', js_new, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Applied NuevaPlantillaVGI.html to index.html with real images!")
