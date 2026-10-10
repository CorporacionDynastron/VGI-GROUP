import glob
import re

# In index.html, find the Explora Nuestras Obras and Solicitar Cotizacion buttons and increase their text size.
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Explora button
html = re.sub(
    r'(Explora nuestras obras <span class="material-symbols-outlined)',
    r'\1', # Not changing the text here
    html
)
html = html.replace(
    'class="inline-flex items-center justify-center bg-primary text-on-primary font-label-caps text-label-caps uppercase px-8 py-4',
    'class="inline-flex items-center justify-center bg-primary text-on-primary font-label-caps text-[13px] uppercase px-8 py-4'
)

# Solicitar button
html = html.replace(
    'class="inline-flex items-center justify-center bg-surface-container-high text-on-surface font-label-caps text-label-caps uppercase px-8 py-4 tracking-wider border border-outline-variant/30 hover:border-primary/50 transition-all duration-300">\n                            <span class="material-symbols-outlined text-sm text-primary mr-2">description</span> Solicitar Cotización',
    'class="inline-flex items-center justify-center bg-surface-container-high text-on-surface font-label-caps text-[13px] uppercase px-8 py-4 tracking-wider border border-outline-variant/30 hover:border-primary/50 transition-all duration-300">\n                            <span class="material-symbols-outlined text-sm text-primary mr-2">description</span> Solicitar Cotización'
)

# There's an encoding issue with "Solicitar Cotizacin" if using powershell. Let's just replace the class string directly.
html = html.replace(
    'class="inline-flex items-center justify-center bg-surface-container-high text-on-surface font-label-caps text-label-caps uppercase px-8 py-4',
    'class="inline-flex items-center justify-center bg-surface-container-high text-on-surface font-label-caps text-[13px] uppercase px-8 py-4'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated button text size in index.html")

# In header.js
with open('header.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace(
    'class="inline-flex items-center justify-center bg-primary-container text-on-primary-container font-label-caps text-label-caps uppercase px-6 py-3.5',
    'class="inline-flex items-center justify-center bg-primary-container text-on-primary-container font-label-caps text-[13px] uppercase px-6 py-3.5'
)

with open('header.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated button text size in header.js")
