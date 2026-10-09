import re

with open("index.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# 1. Project 3 needs to be fixed FIRST so we don't overwrite it later
html = html.replace(
    'src="./01-recreacion/IMAGEN%203.webp">\n                                <div\n                                    class="absolute top-3 left-3 bg-primary',
    'src="./03-mantenimiento/IMAGEN%202.webp">\n                                <div\n                                    class="absolute top-3 left-3 bg-primary'
)

# 2. Project 1
html = html.replace(
    'src="./05-formacion/IMG-20240409-WA0016.jpg">\n                                <div',
    'src="./01-recreacion/IMAGEN%203.webp">\n                                <div'
)

# 3. Project 2
html = html.replace(
    'src="./05-formacion/ponencia/IMAG_3.jpeg">\n                                <div',
    'src="./02-pistas/IMAGEN%2014.webp">\n                                <div'
)

# Patrocinadores
trebol_img = '<img src="./images/patrocinadores/TREBOL.png" alt="Trebol" class="h-10 object-contain">'
html = html.replace('TREBOL GRIFER?AS', trebol_img)
html = html.replace('TREBOL GRIFERÍAS', trebol_img) # Just in case

# Let's add extra ones to the grid
caterpillar_img = '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors"><img src="./images/patrocinadores/caterpillar-transparent.webp" alt="Caterpillar" class="h-10 object-contain"></div>'
indeco_img = '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors"><img src="./images/patrocinadores/INDECO-transparent.webp" alt="Indeco" class="h-10 object-contain"></div>'
sika_img = '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors"><img src="./images/patrocinadores/sika-transparent.webp" alt="Sika" class="h-10 object-contain"></div>'

# Change grid cols from 5 to 4 so it wraps nicely (8 items = 2 rows of 4)
html = html.replace('grid-cols-2 sm:grid-cols-3 md:grid-cols-5', 'grid-cols-2 sm:grid-cols-3 md:grid-cols-4')

grid_end = 'NICOLL SISTEMAS\n                              </div>'
new_grid_items = f'NICOLL SISTEMAS\n                              </div>\n                              {caterpillar_img}\n                              {indeco_img}\n                              {sika_img}'
html = html.replace(grid_end, new_grid_items)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Fixed images and added patrocinadores!")
