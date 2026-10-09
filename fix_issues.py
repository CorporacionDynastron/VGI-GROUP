import re
import glob

# 1. Fix Logo in all files
logo_pattern = r'<div class="flex flex-col">\s*<span class="font-headline-lg[^>]*>.*?</span>\s*<span class="font-label-caps[^>]*>.*?</span>\s*</div>'

new_logo = """<div class="flex flex-col">
                    <span class="font-headline-lg text-xl md:text-2xl text-primary font-bold leading-none tracking-tight" style="text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">VAD GOD ING'S</span>
                    <span class="font-body-sm text-[12px] md:text-[14px] text-white tracking-widest uppercase mt-1">TRAINING Y CONSTRUCTION</span>
                </div>"""

# 2. Fix Obras Category Titles in obras.html
# We will add Tailwind classes to the category titles if they don't have them, or just replace the inline styles.

files = glob.glob('*.html')

for filename in files:
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    # Apply logo fix
    # Since my regex might be too strict, let's use a simpler one.
    html = re.sub(r'<div class="flex flex-col">\s*<span class="font-headline-lg[^>]*>VGI</span>\s*<span class="font-label-caps[^>]*>CONSTRUCTION & TRAINING</span>\s*</div>', new_logo, html, flags=re.DOTALL)
    
    # Alternatively, just replace the exact text if it exists
    html = re.sub(r'<span class="font-headline-lg text-headline-lg-mobile md:text-headline-lg text-white font-bold leading-none tracking-tight">VGI</span>\s*<span class="font-label-caps[^>]*>CONSTRUCTION & TRAINING</span>', r'<span class="font-headline-lg text-xl md:text-2xl text-primary font-bold leading-none tracking-tight" style="text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">VAD GOD ING\'S</span>\n                    <span class="font-body-sm text-[12px] md:text-[14px] text-white tracking-widest uppercase mt-1">TRAINING Y CONSTRUCTION</span>', html, flags=re.DOTALL)


    if filename == 'nosotros.html':
        # Fix space in image path for nosotros hero
        html = html.replace('IMAGEN 2.jpeg', 'IMAGEN%202.jpeg')
        # Increase visibility further
        html = html.replace('brightness-75 opacity-40', 'brightness-100 opacity-60')
        html = html.replace('via-surface/60 to-transparent', 'via-surface/30 to-transparent')

    if filename == 'index.html':
        # Make the folio image object-cover and full height
        html = html.replace('<img src="./images/imagen-6.jpeg"', '<img src="./images/imagen-6.jpeg"')
        # The user said "La imagen del banner princiapl del index debe salir en seccion compelta no cuadrado"
        # It could be the slider:
        html = html.replace('object-contain', 'object-cover')
        # Or the folio card image in index.html (currently it's class="w-full h-auto" maybe?)
        # Let's find the image inside the folio card.
        html = re.sub(r'(<img src="\./images/imagen-1\.jpeg" alt="Proyecto VGI" class="w-full) h-auto( object-cover)', r'\1 h-full\2', html)
        
    if filename == 'obras.html':
        # Fix the category titles: "Las letras de las obras de las organizaciones no se ve bien"
        # They currently have `<h3 class="category-title">Mantenimiento</h3>`
        # In the old CSS: .category-title { font-family: var(--display); font-size: 32px; color: var(--navy); margin-bottom: 40px; border-bottom: 2px solid var(--gold); padding-bottom: 15px; text-transform: uppercase; }
        # Since I dropped the old CSS variables, it looks bad! I need to style them with Tailwind.
        html = re.sub(r'<h3 class="category-title">(.*?)</h3>', r'<h3 class="font-headline-md text-3xl text-primary uppercase font-bold mb-8 pb-4 border-b-2 border-primary/30">\1</h3>', html)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Fixed issues")
