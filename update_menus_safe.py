import re
import glob

# The new dropdowns text:
servicios_header_content = """<a class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer" data-path="servicios" href="index.html#servicios">SERVICIOS <span class="material-symbols-outlined text-sm">expand_more</span></a>
                      <div class="absolute left-0 top-full mt-0 hidden group-hover:flex flex-col bg-surface-container-high shadow-2xl border border-outline-variant/30 min-w-[320px] z-50">
                          <a href="index.html#servicios" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">EJECUCION DE PROYECTOS PUBLICOS Y PRIVADOS</a>
                          <a href="index.html#servicios" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">EJECUCION DE OBRAS PUBLICAS Y PRIVADAS</a>
                          <a href="capacitaciones.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">CAPACITACIONES</a>
                      </div>"""

obras_header_dropdown = """<div class="relative group">
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

    # 1. Update Servicios Dropdown in Header
    html = re.sub(r'<a[^>]*data-path="servicios"[^>]*>.*?</div>', servicios_header_content, html, count=1, flags=re.DOTALL)
    
    # 2. Update Servicios in Footer
    html = re.sub(r'<a[^>]*data-path="servicios"[^>]*>.*?</div>', servicios_header_content, html, flags=re.DOTALL)
    
    # 3. Update Obras in Header
    html = re.sub(r'<a[^>]*data-path="obras"\s*href="obras\.html">Obras</a>', obras_header_dropdown, html, count=1, flags=re.DOTALL | re.IGNORECASE)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Updated menus properly")
