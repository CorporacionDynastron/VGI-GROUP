import re
with open(r"C:\Dynastron_Code\VGI\index.html", 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.finditer(r'<div class="hoja-body">.*?</div>', html, re.IGNORECASE | re.DOTALL)
for m in matches:
    print(m.group(0)[:200])
