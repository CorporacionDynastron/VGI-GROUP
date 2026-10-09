import re

def update_html(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # 1. Update text to CONSTRUCTION & TRAINING
    html = html.replace('CONSTRUCCI&Oacute;N Y CAPACITACIONES', 'CONSTRUCTION & TRAINING')
    html = html.replace('CONSTRUCCI\xc3\x93N Y CAPACITACIONES', 'CONSTRUCTION & TRAINING')
    html = html.replace('CONSTRUCCIÓN Y CAPACITACIONES', 'CONSTRUCTION & TRAINING')

    # 2. Update primary color to #FFCC00 in Tailwind Config
    html = re.sub(r'primary: \[.*?\]', "primary: ['#FFCC00']", html)
    # The tailwind config might have primary: '#D4AF37'
    html = re.sub(r"primary:\s*['\"]#D4AF37['\"]", "primary: '#FFCC00'", html)

    # 3. Add NOSOTROS Submenu
    old_nosotros_nav = r'<a\s*class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface tracking-wide uppercase py-2 transition-colors"\s*data-path="nosotros" href="nosotros.html">Nosotros</a>'
    
    new_nosotros_nav = """<div class="relative group">
                      <a class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer" data-path="nosotros" href="nosotros.html">NOSOTROS <span class="material-symbols-outlined text-sm">expand_more</span></a>
                      <div class="absolute left-0 top-full mt-0 hidden group-hover:flex flex-col bg-surface-container-high shadow-2xl border border-outline-variant/30 min-w-[200px] z-50">
                          <a href="nosotros.html#historia" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-primary">history_edu</span> Nuestra historia</a>
                          <a href="nosotros.html#mision" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-primary">visibility</span> Misión y visión</a>
                          <a href="nosotros.html#equipo" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-primary">groups</span> El equipo</a>
                      </div>
                  </div>"""
    
    html = re.sub(old_nosotros_nav, new_nosotros_nav, html)

    # 4. Change specific hex instances of #d4af37 or #D4AF37 to #FFCC00 in HTML styles
    html = re.sub(r'#d4af37', '#FFCC00', html, flags=re.IGNORECASE)
    # But wait, we shouldn't replace it in paths or scripts if it's there.
    # It's mostly in Tailwind config anyway.

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {filename}")

update_html('index.html')
# We will do nosotros.html separately as we have to fully port it.
