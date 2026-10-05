import re
with open(r"C:\Dynastron_Code\VGI\index.html", 'r', encoding='utf-8') as f:
    html = f.read()

# Look for image tags in index.html to find a good replacement spot
matches = re.finditer(r'<img[^>]*>', html)
for m in matches:
    img_tag = m.group(0)
    if 'storage' in img_tag or 'images' in img_tag or 'Fotos' in img_tag:
        print(img_tag)
