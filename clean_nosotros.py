import re

with open("nosotros.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Strip all style="..."
html = re.sub(r' style="[^"]*"', '', html)

# Fix some remaining layout issues that used inline styles
# Let's see if there's any `<section class="nosotros-hero">`
html = html.replace('class="nosotros-hero"', 'class="w-full bg-surface-container-lowest py-space-2xl"')
html = html.replace('<div class="max-w-7xl mx-auto px-gutter" data-aos="fade-up">', '<div class="max-w-4xl mx-auto px-gutter text-center" data-aos="fade-up">')

with open("nosotros.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Stripped inline styles!")
