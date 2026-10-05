import re
with open(r"C:\Dynastron_Code\VGI\index.html", 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'.{0,150}imagen-1.jpeg.{0,150}', html, re.IGNORECASE | re.DOTALL)
if match:
    print(repr(match.group(0)))
