import re, glob

# Fixes for index.html (and other files where applicable)
for f in glob.glob('*.html'):
    html = open(f, encoding='utf-8').read()
    
    # Task 1: Fix logo line break
    # Current: <span class="font-body-sm text-body-sm text-white tracking-widest uppercase mt-1 font-semibold text-[10px]">TRAINING & CONSTRUCTION</span>
    # Or: <span class="font-body-sm text-body-sm text-white tracking-widest uppercase mt-1 font-semibold text-[10px]">TRAINING  & CONSTRUCTION</span>
    html = re.sub(r'(<span class="font-body-sm text-body-sm text-white tracking-widest uppercase mt-1 font-semibold text-\[10px\]">)TRAINING\s*&\s*CONSTRUCTION(</span>)', r'\1TRAINING <br> & CONSTRUCTION\2', html)

    # Task 2: Submenu font in OBRAS
    # Current: font-label-caps uppercase tracking-wide
    # Change to: font-headline-sm uppercase tracking-wider
    if 'OBRAS DE EDIFICACIONES' in html:
        # We replace `font-label-caps uppercase tracking-wide` with `font-headline-sm uppercase tracking-wider` for all submenus
        # Actually I can just target the anchor tags in the dropdowns.
        html = html.replace('text-sm font-label-caps uppercase tracking-wide border-b', 'text-[13px] font-headline-sm uppercase tracking-wider border-b')

    # Task 4: ISO logos size in footer
    # Current: <div class="bg-white p-1 rounded h-8 w-9 flex items-center justify-center shadow-sm">
    # Change to: <div class="bg-white p-1 rounded h-12 w-14 flex items-center justify-center shadow-sm">
    if 'sistemas homologados' in html.lower() or 'SISTEMAS HOMOLOGADOS' in html:
        html = html.replace('h-8 w-9', 'h-12 w-14')
        html = html.replace('h-8 w-12', 'h-12 w-20')
        html = html.replace('h-8 w-14', 'h-12 w-24')

    if f == 'index.html':
        # Task 3: Text below header, above banner
        # We need to insert: "Impulsando el crecimiento con obras de alto impacto"
        # Where? Below the header, maybe as a scrolling marquee or a small thin banner?
        # "<div class='w-full bg-primary text-on-primary font-headline-sm text-center py-2 uppercase tracking-widest text-sm'>Impulsando el crecimiento con obras de alto impacto</div>"
        # Insert right after </header>
        banner_html = """
    </header>
    <div class="w-full bg-primary text-on-primary font-headline-sm text-center py-2 uppercase tracking-widest text-xs md:text-sm font-bold shadow-md z-40 relative">
        Impulsando el crecimiento con obras de alto impacto
    </div>"""
        if "Impulsando el crecimiento con obras de alto impacto" not in html:
            html = html.replace('</header>', banner_html, 1)

        # Task 5: Gerencias de proyectos cards in index.html
        # Replace: ELABORACIÓN DE PROYECTOS with EJECUCION DE PROYECTOS PUBLICOS Y PRIVADOS
        # Replace: EJECUCIÓN DE OBRAS with EJECUCION DE OBRAS PUBLICAS Y PRIVADAS
        html = html.replace('>ELABORACIÓN DE PROYECTOS<', '>EJECUCION DE PROYECTOS PUBLICOS Y PRIVADOS<')
        html = html.replace('>ELABORACIN DE PROYECTOS<', '>EJECUCION DE PROYECTOS PUBLICOS Y PRIVADOS<')
        html = html.replace('>EJECUCIÓN DE OBRAS<', '>EJECUCION DE OBRAS PUBLICAS Y PRIVADAS<')
        html = html.replace('>EJECUCIN DE OBRAS<', '>EJECUCION DE OBRAS PUBLICAS Y PRIVADAS<')
        
        # Task 6: CONTACTANOS background
        # <div class="absolute inset-0 opacity-20" style="background-image: url('./images/imagen-5.jpeg'); background-size: cover; background-attachment: fixed; background-position: center; filter: grayscale(80%);"></div>
        # <div class="absolute inset-0 bg-gradient-to-r from-surface via-surface/90 to-surface/40"></div>
        html = re.sub(r'(url\(\'\./images/imagen-5\.jpeg\'\)[^;]*;[^;]*;[^;]*;)\s*filter:\s*grayscale\(80%\);', r'\1', html)
        html = re.sub(r'<div class="absolute inset-0 opacity-20"(.*imagen-5.*)></div>', r'<div class="absolute inset-0 opacity-50"\1></div>', html)
        html = re.sub(r'<div class="absolute inset-0 bg-gradient-to-r from-surface via-surface/90 to-surface/40"></div>', r'<div class="absolute inset-0 bg-gradient-to-r from-surface via-surface/70 to-surface/20"></div>', html)
        
        # Task 7 & 8: CUATRO ETAPAS background (imagen-6.jpeg)
        # <div class="absolute inset-0 opacity-40" style="background-image: url('./images/imagen-6.jpeg'); background-size: cover; background-attachment: fixed; background-position: center; "></div>
        # <div class="absolute inset-0 bg-gradient-to-b from-surface via-surface/80 to-surface"></div>
        html = re.sub(r'<div class="absolute inset-0 opacity-40"(.*imagen-6.*)></div>', r'<div class="absolute inset-0 opacity-80"\1></div>', html)
        html = re.sub(r'<div class="absolute inset-0 bg-gradient-to-b from-surface via-surface/80 to-surface"></div>', r'<div class="absolute inset-0 bg-gradient-to-b from-surface/80 via-surface/60 to-surface"></div>', html)
        

    open(f, 'w', encoding='utf-8').write(html)
