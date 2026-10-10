import os, re

pages = {'capacitaciones.html': 'CAPACITACIONES', 'planos.html': 'SERVICIOS', 'obras.html': 'OBRAS', 'index.html': 'INICIO', 'nosotros.html': 'NOSOTROS'}
for page, active_text in pages.items():
    if not os.path.exists(page): continue
    html = open(page, encoding='utf-8').read()
    
    # Remove active state from simple links
    html = re.sub(r'class="font-headline-sm text-primary uppercase font-bold tracking-wider hover:text-primary transition-colors text-sm border-b-2 border-primary pb-1"', r'class="font-headline-sm text-outline uppercase font-bold tracking-wider hover:text-white transition-colors text-sm"', html)
    # Remove active state from dropdown buttons
    html = re.sub(r'class="font-headline-sm text-primary uppercase font-bold tracking-wider flex items-center gap-1 hover:text-primary transition-colors text-sm border-b-2 border-primary pb-1"', r'class="font-headline-sm text-outline uppercase font-bold tracking-wider flex items-center gap-1 hover:text-white transition-colors text-sm"', html)

    # Set active for simple links
    html = re.sub(f'<a href="[^"]*" class="font-headline-sm text-outline uppercase font-bold tracking-wider hover:text-white transition-colors text-sm">{active_text}</a>', f'<a href="{page}" class="font-headline-sm text-primary uppercase font-bold tracking-wider hover:text-primary transition-colors text-sm border-b-2 border-primary pb-1">{active_text}</a>', html)
    
    # Set active for dropdown buttons
    html = re.sub(f'<button class="font-headline-sm text-outline uppercase font-bold tracking-wider flex items-center gap-1 hover:text-white transition-colors text-sm">\\s*{active_text}\\s*<span', f'<button class="font-headline-sm text-primary uppercase font-bold tracking-wider flex items-center gap-1 hover:text-primary transition-colors text-sm border-b-2 border-primary pb-1">{active_text} <span', html)

    open(page, 'w', encoding='utf-8').write(html)
