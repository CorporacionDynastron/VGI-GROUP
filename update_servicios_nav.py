import re
import glob

def update_servicios_nav():
    files = glob.glob('*.html')
    
    old_servicios_nav = r'<a[^>]*data-path="servicios"[^>]*>Servicios</a>'
    
    new_servicios_nav = """<div class="relative group">
                      <a class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer" data-path="servicios" href="index.html#servicios">SERVICIOS <span class="material-symbols-outlined text-sm">expand_more</span></a>
                      <div class="absolute left-0 top-full mt-0 hidden group-hover:flex flex-col bg-surface-container-high shadow-2xl border border-outline-variant/30 min-w-[320px] z-50">
                          <a href="index.html#servicios" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">Consultoría en obras de edificaciones y afines</a>
                          <a href="index.html#servicios" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">Consultoría en obras viales, puertos y afines</a>
                          <a href="index.html#servicios" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">Consultoría en obras de saneamiento y afines</a>
                          <a href="index.html#servicios" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide border-b border-outline-variant/10 flex items-center gap-2">Consultoría en obras electromecánicas, energéticas, telecom. y afines</a>
                          <a href="index.html#servicios" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide flex items-center gap-2">Consultoría en obras de represas, irrigaciones y afines</a>
                      </div>
                  </div>"""
                  
    for filename in files:
        if filename == 'NuevaPlantillaVGI.html':
            continue
            
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
            
        html = re.sub(old_servicios_nav, new_servicios_nav, html)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated SERVICIOS nav in {filename}")

update_servicios_nav()
