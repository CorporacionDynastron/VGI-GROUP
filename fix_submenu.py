import glob, re

for f in glob.glob('*.html'):
    html = open(f, encoding='utf-8').read()
    
    # Hero Slides images in index.html
    if f == 'index.html':
        html = html.replace("img: './Fotos Proyectos/05.webp'", "img: './09-recreacional/img_1.webp'")
        html = html.replace("img: './Fotos Proyectos/04.webp'", "img: './02-pistas/IMAGEN%201.webp'")
        html = html.replace("img: './Fotos Proyectos/02.webp'", "img: './03-mantenimiento/IMAGEN%201.webp'")

    # Submenus mapping
    html = re.sub(r'<a href="index\.html#servicios"([^>]*>EJECUCION DE PROYECTOS PUBLICOS Y PRIVADOS)</a>', r'<a href="planos.html"\1</a>', html)
    html = re.sub(r'<a href="index\.html#servicios"([^>]*>EJECUCION DE OBRAS PUBLICAS Y PRIVADAS)</a>', r'<a href="obras.html"\1</a>', html)
    
    html = re.sub(r'<a href="#"([^>]*>OBRAS DE EDIFICACIONES Y AFINES)</a>', r'<a href="obras.html#edificaciones"\1</a>', html)
    html = re.sub(r'<a href="#"([^>]*>OBRAS VIALES, PUERTOS Y AFINES)</a>', r'<a href="obras.html#viales"\1</a>', html)
    html = re.sub(r'<a href="#"([^>]*>OBRAS DE SANEAMIENTO Y AFINES)</a>', r'<a href="obras.html#saneamiento"\1</a>', html)
    html = re.sub(r'<a href="#"([^>]*>OBRAS ELECTROMECÁNICAS, ENERGÉTICAS, TELECOM. Y AFINES)</a>', r'<a href="obras.html"\1</a>', html)
    html = re.sub(r'<a href="#"([^>]*>OBRAS DE REPRESAS, IRRIGACIONES Y AFINES)</a>', r'<a href="obras.html"\1</a>', html)
    
    open(f, 'w', encoding='utf-8').write(html)
