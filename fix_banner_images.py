import glob

banner_html = """
    </header>
    <div class="w-full bg-primary text-on-primary font-headline-sm text-center py-2 uppercase tracking-widest text-xs md:text-sm font-bold shadow-md z-40 relative">
        Impulsando el crecimiento con obras de alto impacto
    </div>"""

for f in glob.glob('*.html'):
    html = open(f, encoding='utf-8').read()
    
    # 1. Add banner if missing
    if "Impulsando el crecimiento con obras de alto impacto" not in html:
        html = html.replace('</header>', banner_html, 1)
        
    # 2. Fix nosotros.html background
    if f == 'nosotros.html':
        html = html.replace('./04-primera-piedra/IMAGEN%202.jpeg', './images/imagen-6.jpeg')
        
    # 3. Fix obras.html background
    if f == 'obras.html':
        html = html.replace('./02-pistas/DJI_0461.webp', './02-pistas/IMAGEN%201.webp')
        html = html.replace('./02-pistas/DJI_0461.webp', './02-pistas/IMAGEN%201.webp') # just in case
        
    open(f, 'w', encoding='utf-8').write(html)
