import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Elaboracion de Proyectos
html = re.sub(r'<button\s*class="(w-full py-3\.5 bg-surface-container-high[^"]*)"\s*onclick="openSpecModal\(1\)"><span[^>]*>VER DETALLES</span>.*?arrow_forward</span></button>', r'<a href="planos.html" class="\1"><span class="">VER DETALLES</span><span class="material-symbols-outlined text-sm">arrow_forward</span></a>', html, flags=re.DOTALL)

# Replace Ejecucion de Obras
html = re.sub(r'<button\s*class="(w-full py-3\.5 bg-surface-container-high[^"]*)"\s*onclick="openSpecModal\(2\)"><span[^>]*>VER DETALLES</span>.*?arrow_forward</span></button>', r'<a href="obras.html" class="\1"><span class="">VER DETALLES</span><span class="material-symbols-outlined text-sm">arrow_forward</span></a>', html, flags=re.DOTALL)

# Replace Capacitaciones
html = re.sub(r'<button\s*class="(w-full py-3\.5 bg-surface-container-high[^"]*)"\s*onclick="openSpecModal\(3\)"><span[^>]*>VER DETALLES</span>.*?arrow_forward</span></button>', r'<a href="capacitaciones.html" class="\1"><span class="">VER DETALLES</span><span class="material-symbols-outlined text-sm">arrow_forward</span></a>', html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
