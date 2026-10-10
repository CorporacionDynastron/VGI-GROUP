import glob
import re

banner_html = """
    <div class="w-full bg-primary text-on-primary font-headline-sm text-center py-2 uppercase tracking-widest text-xs md:text-sm font-bold shadow-[0_4px_12px_rgba(0,0,0,0.3)] border-t border-primary/50 relative z-[60]">
        Impulsando el crecimiento con obras de alto impacto
    </div>
"""

def fix_active_nav(html, active_path):
    # Reset all to inactive
    # "Inicio"
    html = re.sub(r'class="[^"]*"(\s*data-path="inicio")', r'class="tracking-wide uppercase py-2 transition-colors text-on-surface-variant hover:text-on-surface flex items-center gap-1 cursor-pointer"\1', html)
    # "SERVICIOS"
    html = re.sub(r'class="[^"]*"(\s*data-path="servicios")', r'class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-on-surface-variant hover:text-on-surface"\1', html)
    # "OBRAS"
    html = re.sub(r'class="[^"]*"(\s*data-path="obras")', r'class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-on-surface-variant hover:text-on-surface"\1', html)
    # "NOSOTROS"
    html = re.sub(r'class="[^"]*"(\s*data-path="nosotros")', r'class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-on-surface-variant hover:text-on-surface"\1', html)
    
    # Set the active one
    if active_path == 'inicio':
        html = re.sub(r'class="[^"]*"(\s*data-path="inicio")', r'class="tracking-wide uppercase py-2 transition-colors text-primary border-b border-primary font-semibold"\1', html)
    elif active_path == 'servicios':
        html = re.sub(r'class="[^"]*"(\s*data-path="servicios")', r'class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-primary border-b border-primary font-semibold"\1', html)
    elif active_path == 'obras':
        html = re.sub(r'class="[^"]*"(\s*data-path="obras")', r'class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-primary border-b border-primary font-semibold"\1', html)
    elif active_path == 'nosotros':
        html = re.sub(r'class="[^"]*"(\s*data-path="nosotros")', r'class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-primary border-b border-primary font-semibold"\1', html)
        
    return html

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # 1. Move banner INSIDE header
    # Remove the old one outside the header
    old_banner_regex = r'</header>\s*<div class="w-full bg-primary[^>]*>\s*Impulsando el crecimiento con obras de alto impacto\s*</div>'
    html = re.sub(old_banner_regex, '</header>', html, flags=re.DOTALL)
    
    # Remove any existing banner inside the header just in case
    html = re.sub(r'<div class="w-full bg-primary[^>]*>\s*Impulsando el crecimiento con obras de alto impacto\s*</div>\s*</header>', '</header>', html, flags=re.DOTALL)
    
    # Add it exactly before </header>
    html = html.replace('</header>', banner_html + '\n</header>')
    
    # 2. Fix active navs
    if f == 'index.html':
        html = fix_active_nav(html, 'inicio')
    elif f == 'nosotros.html':
        html = fix_active_nav(html, 'nosotros')
    elif f == 'obras.html':
        html = fix_active_nav(html, 'obras')
    elif f in ('planos.html', 'capacitaciones.html'):
        html = fix_active_nav(html, 'servicios')
        
    # 3. Fix nosotros.html hero image
    if f == 'nosotros.html':
        # Replace the <img> tag with a background div
        old_hero_img_regex = r'<div class="absolute inset-0 w-full h-full">\s*<img src="\./images/imagen-6\.jpeg"[^>]*>\s*<div class="absolute inset-0 bg-gradient-to-b from-surface/10 via-surface/30 to-surface/90"></div>\s*</div>'
        
        new_hero_bg = """
    <div class="absolute inset-0 w-full h-full">
        <div class="absolute inset-0 opacity-80" style="background-image: url('./images/imagen-6.jpeg'); background-size: cover; background-position: center; background-repeat: no-repeat;"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-surface/10 via-surface/40 to-surface/90"></div>
    </div>
"""
        html = re.sub(old_hero_img_regex, new_hero_bg, html, flags=re.DOTALL)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)
