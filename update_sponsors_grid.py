import re

with open("index.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Generate the new grid HTML
blocks = [
    # Aceros Arequipa (Text, since no image was provided)
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center font-technical-code text-technical-code font-bold tracking-widest text-on-surface hover:text-primary transition-colors h-24">ACEROS AREQUIPA</div>',
    
    # PAVCO
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-24"><img src="./images/Patrocinadores%20y%20marcas%20aliados/pavco-transparent.webp" alt="Pavco" class="h-16 md:h-20 object-contain drop-shadow-sm filter brightness-0 invert opacity-80 hover:opacity-100 hover:filter-none transition-all"></div>',
    
    # ROTOPLAS
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-24"><img src="./images/Patrocinadores%20y%20marcas%20aliados/ROTOPLAS.svg" alt="Rotoplas" class="h-16 md:h-20 object-contain drop-shadow-sm filter brightness-0 invert opacity-80 hover:opacity-100 hover:filter-none transition-all"></div>',
    
    # TREBOL
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-24"><img src="./images/patrocinadores/TREBOL.png" alt="Trebol" class="h-16 md:h-20 object-contain drop-shadow-sm filter brightness-0 invert opacity-80 hover:opacity-100 hover:filter-none transition-all"></div>',
    
    # NICOLL
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-24"><img src="./images/Patrocinadores%20y%20marcas%20aliados/NICOLL-transparent.webp" alt="Nicoll" class="h-16 md:h-20 object-contain drop-shadow-sm filter brightness-0 invert opacity-80 hover:opacity-100 hover:filter-none transition-all"></div>',
    
    # CATERPILLAR
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-24"><img src="./images/patrocinadores/caterpillar-transparent.webp" alt="Caterpillar" class="h-16 md:h-20 object-contain drop-shadow-sm filter brightness-0 invert opacity-80 hover:opacity-100 hover:filter-none transition-all"></div>',
    
    # INDECO
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-24"><img src="./images/patrocinadores/INDECO-transparent.webp" alt="Indeco" class="h-16 md:h-20 object-contain drop-shadow-sm filter brightness-0 invert opacity-80 hover:opacity-100 hover:filter-none transition-all"></div>',
    
    # SIKA
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-24"><img src="./images/patrocinadores/sika-transparent.webp" alt="Sika" class="h-16 md:h-20 object-contain drop-shadow-sm filter brightness-0 invert opacity-80 hover:opacity-100 hover:filter-none transition-all"></div>',
    
    # CEMENTO APU
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-24"><img src="./images/Patrocinadores%20y%20marcas%20aliados/CEMENTO%20APU-transparent.webp" alt="Cemento APU" class="h-16 md:h-20 object-contain drop-shadow-sm filter brightness-0 invert opacity-80 hover:opacity-100 hover:filter-none transition-all"></div>',
    
    # CEMEX
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-24"><img src="./images/Patrocinadores%20y%20marcas%20aliados/CEMEX-transparent.webp" alt="Cemex" class="h-16 md:h-20 object-contain drop-shadow-sm filter brightness-0 invert opacity-80 hover:opacity-100 hover:filter-none transition-all"></div>',
    
    # CEMENTO SOL
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-24"><img src="./images/Patrocinadores%20y%20marcas%20aliados/CEMNTO%20SOL-transparent.webp" alt="Cemento Sol" class="h-16 md:h-20 object-contain drop-shadow-sm filter brightness-0 invert opacity-80 hover:opacity-100 hover:filter-none transition-all"></div>',
    
    # LADRILLOS LARK
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-24"><img src="./images/Patrocinadores%20y%20marcas%20aliados/LADRILLOS%20LARK-transparent.webp" alt="Ladrillos Lark" class="h-16 md:h-20 object-contain drop-shadow-sm filter brightness-0 invert opacity-80 hover:opacity-100 hover:filter-none transition-all"></div>',
]

# Wait, adding `filter brightness-0 invert opacity-80 hover:opacity-100 hover:filter-none` is a really nice trick 
# to make all logos look unified (white/grey) until hovered, where they show their original colors. This fits the dark theme perfectly!
# Let's remove this if they want exactly the original colors, but wait, the screenshot they shared showed the original colors (Trebol was red, CAT was yellow/white, INDECO was orange/white).
# Okay, I will NOT use the grayscale filter because the user explicitly shared a screenshot with colored logos.
# Let's re-define blocks without filters.

blocks_no_filter = [
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center font-technical-code text-technical-code font-bold tracking-widest text-on-surface hover:text-primary transition-colors h-28">ACEROS AREQUIPA</div>',
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28"><img src="./images/Patrocinadores%20y%20marcas%20aliados/pavco-transparent.webp" alt="Pavco" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm"></div>',
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28"><img src="./images/Patrocinadores%20y%20marcas%20aliados/ROTOPLAS.svg" alt="Rotoplas" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm"></div>',
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28"><img src="./images/patrocinadores/TREBOL.png" alt="Trebol" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm"></div>',
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28"><img src="./images/Patrocinadores%20y%20marcas%20aliados/NICOLL-transparent.webp" alt="Nicoll" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm"></div>',
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28"><img src="./images/patrocinadores/caterpillar-transparent.webp" alt="Caterpillar" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm"></div>',
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28"><img src="./images/patrocinadores/INDECO-transparent.webp" alt="Indeco" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm"></div>',
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28"><img src="./images/patrocinadores/sika-transparent.webp" alt="Sika" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm"></div>',
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28"><img src="./images/Patrocinadores%20y%20marcas%20aliados/CEMENTO%20APU-transparent.webp" alt="Cemento APU" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm"></div>',
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28"><img src="./images/Patrocinadores%20y%20marcas%20aliados/CEMEX-transparent.webp" alt="Cemex" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm"></div>',
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28"><img src="./images/Patrocinadores%20y%20marcas%20aliados/CEMNTO%20SOL-transparent.webp" alt="Cemento Sol" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm"></div>',
    '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28"><img src="./images/Patrocinadores%20y%20marcas%20aliados/LADRILLOS%20LARK-transparent.webp" alt="Ladrillos Lark" class="h-16 md:h-20 w-auto object-contain drop-shadow-sm"></div>',
]

grid_content = "\\n".join(blocks_no_filter)
grid_html = f'<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-space-md">\n{grid_content}\n                          </div>'

# Now we need to replace the entire <div class="grid ...">...</div> in that section.
pattern = r'<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-space-md">.*?</div>\s*</div>\s*</div>\s*</section>'

# Let's do a more precise replacement using the title above it
split_marker = '<span class="font-technical-code text-technical-code text-outline">INSUMOS\n                                  CERTIFICADOS</span>\n                          </div>'
if split_marker not in html:
    # Try one-liner
    split_marker = '<span class="font-technical-code text-technical-code text-outline">INSUMOS CERTIFICADOS</span></div>'

# Let's just use regex to replace everything after INSUMOS CERTIFICADOS</span></div> to the end of the section
# But wait, there are newlines.
regex_pattern = r'(INSUMOS\s*CERTIFICADOS</span>\s*</div>\s*)<div class="grid.*?</div>\s*(</div>\s*</div>\s*</section>)'

match = re.search(r'(INSUMOS\s*CERTIFICADOS</span>\s*</div>\s*)<div class="grid.*?(</div>\s*</div>\s*</section>)', html, re.DOTALL)
if match:
    new_html = html[:match.start(1)] + match.group(1) + grid_html + '\n                      ' + match.group(2) + html[match.end(2):]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Successfully replaced Patrocinadores grid!")
else:
    print("Regex match failed.")
