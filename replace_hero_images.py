import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the initial img src
html = html.replace('src="./09-recreacional/img_1.webp"', 'src="./images/imagen-3.jpeg"')

# 2. Update the heroSlides array
html = html.replace('img: "./09-recreacional/img_1.webp"', 'img: "./images/imagen-3.jpeg"')
html = html.replace('img: "./02-pistas/IMAGEN%201.webp"', 'img: "./images/imagen-4.jpeg"')
html = html.replace('img: "./03-mantenimiento/IMAGEN%201.webp"', 'img: "./images/imagen-1.jpeg"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero images replaced")
