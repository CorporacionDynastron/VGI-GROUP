import re
with open(r"C:\Dynastron_Code\VGI\nosotros.html", 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.finditer(r'<img[^>]*>', html)
for m in matches:
    img = m.group(0)
    if 'unsplash' in img or 'placeholder' in img:
        print(img)
