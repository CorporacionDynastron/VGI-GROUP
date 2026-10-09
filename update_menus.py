import re
import glob

# The new dropdowns text:
servicios_dropdown = """<div class="relative group">
                      <a class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer" data-path="servicios" href="index.html#servicios">SERVICIOS <span class="material-symbols-outlined text-sm">expand_more</span></a>
                      <div class="absolute left-0 top-full mt-0 hidden group-hover:flex flex-col bg-surface-container-high shadow-2xl border border-outline-variant/30 min-w-[320px] z-50">
                          <a href="index.html#servicios" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">EJECUCION DE PROYECTOS PUBLICOS Y PRIVADOS</a>
                          <a href="index.html#servicios" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">EJECUCION DE OBRAS PUBLICAS Y PRIVADAS</a>
                          <a href="capacitaciones.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">CAPACITACIONES</a>
                      </div>
                  </div>"""

obras_dropdown = """<div class="relative group">
                      <a class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer" data-path="obras" href="obras.html">OBRAS <span class="material-symbols-outlined text-sm">expand_more</span></a>
                      <div class="absolute left-0 top-full mt-0 hidden group-hover:flex flex-col bg-surface-container-high shadow-2xl border border-outline-variant/30 min-w-[320px] z-50">
                          <a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">OBRAS DE EDIFICACIONES Y AFINES</a>
                          <a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">OBRAS VIALES, PUERTOS Y AFINES</a>
                          <a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">OBRAS DE SANEAMIENTO Y AFINES</a>
                          <a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">OBRAS ELECTROMECÁNICAS, ENERGÉTICAS, TELECOM. Y AFINES</a>
                          <a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">OBRAS DE REPRESAS, IRRIGACIONES Y AFINES</a>
                      </div>
                  </div>"""

files = glob.glob('*.html')

for filename in files:
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    # 1. Update Servicios Dropdown
    # It starts with <div class="relative group"> and ends with </div>\s*</div> right before <a class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface tracking-wide uppercase py-2 transition-colors"\n                    data-path="obras" href="obras.html">Obras</a>
    # Actually, we can just replace the whole block by looking for the anchor with data-path="servicios"
    html = re.sub(r'<div class="relative group">\s*<a[^>]*data-path="servicios".*?<div class="absolute.*?</div>\s*</div>', servicios_dropdown, html, flags=re.DOTALL)
    
    # 2. Update Obras Dropdown
    # We look for the anchor that links to obras.html (in the main header nav).
    html = re.sub(r'<a\s+class="[^"]*"\s*(?:aria-current="page"\s*)?data-path="obras" href="obras.html">Obras</a>', obras_dropdown, html, flags=re.DOTALL | re.IGNORECASE)

    # 3. Footer Links for Servicios
    footer_servicios = """<a href="index.html#servicios" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">EJECUCION DE PROYECTOS PUBLICOS Y PRIVADOS</a>
                          <a href="index.html#servicios" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">EJECUCION DE OBRAS PUBLICAS Y PRIVADAS</a>
                          <a href="capacitaciones.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">CAPACITACIONES</a>"""
    html = re.sub(r'<div class="absolute left-0 top-full mt-0 hidden group-hover:flex flex-col bg-surface-container-high shadow-2xl border border-outline-variant/30 min-w-\[320px\] z-50">.*?(?=</div>\s*</div></li>\s*<li class=""><a class="hover:text-primary transition-colors"\s*data-path="obras")', '<div class="absolute left-0 top-full mt-0 hidden group-hover:flex flex-col bg-surface-container-high shadow-2xl border border-outline-variant/30 min-w-[320px] z-50">\n' + footer_servicios + '\n                      ', html, flags=re.DOTALL)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Updated menus")
