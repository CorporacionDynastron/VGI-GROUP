import re

with open("obras.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# 1. Increase image size
html = html.replace('grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));', 'grid-template-columns: repeat(auto-fill, minmax(450px, 1fr));')

# 2. Rename categories
html = html.replace('Infraestructura deportiva y recreativa', 'Infraestructura Recreativa')
html = html.replace('Pavimentacin de vas', 'Pavimentación de vías')
html = html.replace('Pavimentacin de vas', 'Pavimentación de vías')
html = html.replace('Mantenimiento de infraestructura', 'Mantenimiento')

# 3. Remove discarded categories: Planta de Tratamiento, Instalacion de tuberia HDPE, Vivienda Multifamiliar, Infraestructura Recreacional
def remove_category(category_name, text):
    # Regex to find <div class="category-section"> ... </div>
    # where the h3 inside contains the category_name
    # Since there are multiple category-sections, we find the exact one.
    pattern = r'<div class="category-section">\s*<h3 class="category-title">.*?'+category_name+r'.*?</h3>.*?</div>\s*(?=<div class="category-section"|</section>)'
    return re.sub(pattern, '', text, flags=re.DOTALL | re.IGNORECASE)

html = remove_category('Planta de Tratamiento', html)
html = remove_category('tuber.a HDPE', html)
html = remove_category('HDPE', html)
html = remove_category('Infraestructura Recreacional', html)
html = remove_category('Vivienda Multifamiliar', html)

with open("obras.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated obras.html!")
