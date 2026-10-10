import re

with open('header.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace EJECUCION DE OBRAS PUBLICAS Y PRIVADAS link inside SERVICIOS
js = js.replace('<a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">EJECUCION DE OBRAS PUBLICAS Y PRIVADAS</a>', 
                '<a href="ejecucion-obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">EJECUCION DE OBRAS PUBLICAS Y PRIVADAS</a>')

# Update active logic
active_logic_old = "else if (currentPath.includes('planos.html') || currentPath.includes('capacitaciones.html')) activeTarget = 'servicios';"
active_logic_new = "else if (currentPath.includes('planos.html') || currentPath.includes('capacitaciones.html') || currentPath.includes('ejecucion-obras.html')) activeTarget = 'servicios';"
js = js.replace(active_logic_old, active_logic_new)

with open('header.js', 'w', encoding='utf-8') as f:
    f.write(js)
