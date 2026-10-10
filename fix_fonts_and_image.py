import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # 1. Replace the typewriter font globally
    # Replace "font-technical-code text-technical-code" -> "font-headline-sm text-sm font-bold tracking-wider"
    html = html.replace('font-technical-code text-technical-code', 'font-headline-sm text-sm font-bold tracking-wider')
    # Replace "text-technical-code font-technical-code" -> "font-headline-sm text-sm font-bold tracking-wider"
    html = html.replace('text-technical-code font-technical-code', 'font-headline-sm text-sm font-bold tracking-wider')

    # 2. Update Pavimentacion de Vias image
    if f == 'index.html':
        # Find the card for Pavimentacion de Vias and update its image
        # In the context of:
        # <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
        #     data-alt="Heavy roadway concrete paving..."
        #     src="./02-pistas/IMAGEN%2014.webp">
        # </div>
        # <div class="p-space-lg">
        # <h3 class="font-headline-sm text-headline-sm text-on-surface font-bold uppercase mb-2">Pavimentación de Vías</h3>
        
        # We can just replace the specific image IMAGEN 14 since it's the one currently used for this section.
        html = html.replace('./02-pistas/IMAGEN%2014.webp', './02-pistas/IMAGEN%209.webp')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)
