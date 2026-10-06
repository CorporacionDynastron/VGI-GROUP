import os
import re

# Fix index.html
index_path = r"C:\Dynastron_Code\VGI\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Restore landing page hero image
html = html.replace('./images/imagen-1.jpeg', './01-recreacion/IMAGEN%201.png')

# Fix Card 3
html = html.replace('./05-formacion/imagen-1.jpeg', './05-formacion/IMAGEN%201.jpeg')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Restored landing hero and fixed card 3.")
