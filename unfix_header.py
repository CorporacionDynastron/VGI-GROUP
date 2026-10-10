import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # 1. Un-fix header
    html = html.replace('fixed top-0 left-0 right-0 z-50 bg-surface/90', 'relative z-50 w-full bg-surface/100')
    html = html.replace('shadow-[0_1px_8px_rgba(0,0,0,0.4)]', 'shadow-none') # maybe remove shadow since it's not floating anymore
    
    # 2. Fix main padding
    html = html.replace('pt-20', 'pt-0')
    html = html.replace('pt-[100px]', 'pt-0')
    
    # 3. Nosotros.html background image filter
    if f == 'nosotros.html':
        html = html.replace(
            '<div class="absolute inset-0 opacity-80" style="background-image: url(\'./images/imagen-6.jpeg\'); background-size: cover; background-position: center; background-repeat: no-repeat;"></div>',
            '<div class="absolute inset-0 opacity-40" style="background-image: url(\'./images/imagen-6.jpeg\'); background-size: cover; background-position: center; background-repeat: no-repeat; filter: grayscale(90%);"></div>'
        )
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)
