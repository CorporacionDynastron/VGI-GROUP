import os

# 1. Update nosotros.html
nosotros_path = r"C:\Dynastron_Code\VGI\nosotros.html"
with open(nosotros_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace just the values safely
html = html.replace("url('./images/IMAGEN%202.jpeg')", "url('./images/imagen-2.jpeg')")
html = html.replace("rgba(6,19,37,0.85) 0%, rgba(10,31,61,0.75) 55%, rgba(22,51,94,0.7)", "rgba(6,19,37,0.6) 0%, rgba(10,31,61,0.5) 55%, rgba(22,51,94,0.45)")

with open(nosotros_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update index.html hero image
index_path = r"C:\Dynastron_Code\VGI\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()

idx = idx.replace('./01-recreacion/IMAGEN%201.png', './images/imagen-1.jpeg')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx)

print("Safely replaced CSS and HTML.")
