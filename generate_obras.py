import json

html = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <title>Obras - VGI</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: "#F2CA50",
                        "primary-fixed": "#FFE178",
                        secondary: "#D1C5B4",
                        background: "#0B0D11",
                        surface: "#0B0D11",
                        "surface-dim": "#11141A",
                        "surface-container-lowest": "#0B0D11",
                        "surface-container-low": "#11141A",
                        "surface-container": "#1A1D24",
                        "surface-container-high": "#232832",
                        "surface-container-highest": "#232832",
                        "on-surface": "#F1F3F5",
                        "on-surface-variant": "#9CA3AF",
                        "outline": "#9CA3AF",
                        "outline-variant": "rgba(255,255,255,0.08)"
                    },
                    fontFamily: {
                        "headline-lg": ['Syne', 'sans-serif'],
                        "headline-sm": ['Syne', 'sans-serif'],
                        "body-md": ['Inter', 'sans-serif'],
                        "body-sm": ['Inter', 'sans-serif'],
                        "label-caps": ['JetBrains Mono', 'monospace']
                    },
                    spacing: {
                        "gutter": "2rem",
                        "gutter-lg": "4rem",
                        "space-sm": "0.5rem",
                        "space-md": "1rem",
                        "space-lg": "2rem",
                        "space-xl": "4rem",
                        "space-2xl": "8rem"
                    }
                }
            }
        }
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
    <link href="https://fonts.googleapis.com" rel="preconnect">
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
    <style>
        body { margin: 0; padding: 0; overscroll-behavior: none; }
    </style>
</head>
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
        "num": "01",
        "header": "EDIFICACIONES",
        "title": "OBRAS DE EDIFICACIONES Y AFINES",
        "img": "./08-multifamiliar/primera-piedra/PRIMERA_PIEDRA_1.webp",
        "desc": "Ejecución integral de infraestructuras residenciales, comerciales e institucionales con los más altos estándares estructurales y arquitectónicos."
    },
    {
        "num": "02",
        "header": "INFRAESTRUCTURA VIAL",
        "title": "OBRAS VIALES, PUERTOS Y AFINES",
        "img": "./02-pistas/IMAGEN%209.webp",
        "desc": "Construcción y pavimentación de carreteras, vías urbanas e infraestructura portuaria garantizando conectividad y máxima resistencia."
    },
    {
        "num": "03",
        "header": "SANEAMIENTO",
        "title": "OBRAS DE SANEAMIENTO Y AFINES",
        "img": "./07-saneamiento/saneamiento_1.jpg",
        "desc": "Desarrollo de redes de agua potable, alcantarillado y plantas de tratamiento (PETAR) para mejorar la calidad de vida y el medio ambiente."
    },
    {
        "num": "04",
        "header": "ELECTROMECÁNICA",
        "title": "OBRAS ELECTROMECÁNICAS Y TELECOM.",
        "img": "./images/imagen-6.jpeg",
        "desc": "Instalaciones energéticas, montajes industriales y redes de telecomunicaciones ejecutadas con absoluta precisión técnica y seguridad."
    },
    {
        "num": "05",
        "header": "REPRESAS E IRRIGACIONES",
        "title": "OBRAS DE REPRESAS E IRRIGACIONES",
        "img": "./01-recreacion/IMAGEN%201.webp",
        "desc": "Proyectos hidráulicos de gran envergadura para el control, almacenamiento y distribución eficiente de recursos hídricos en el sector."
    }
]

for cat in categories:
    html += f"""
                    <div class="bg-surface-container border-t-2 border-t-primary border border-outline-variant flex flex-col group hover:border-primary/50 transition-colors shadow-lg">
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
