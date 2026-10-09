import re

with open("index.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

caterpillar_img = '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors"><img src="./images/patrocinadores/caterpillar-transparent.webp" alt="Caterpillar" class="h-10 object-contain"></div>'
indeco_img = '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors"><img src="./images/patrocinadores/INDECO-transparent.webp" alt="Indeco" class="h-10 object-contain"></div>'
sika_img = '<div class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors"><img src="./images/patrocinadores/sika-transparent.webp" alt="Sika" class="h-10 object-contain"></div>'

pattern = r'(NICOLL SISTEMAS\s*</div>)'
replacement = r'\1\n                              ' + caterpillar_img + '\n                              ' + indeco_img + '\n                              ' + sika_img

html = re.sub(pattern, replacement, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Added missing sponsors!")
