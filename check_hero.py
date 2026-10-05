import re
with open(r"C:\Dynastron_Code\VGI\nosotros.html", 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'\.hero\s*\{[^}]*\}', html)
if match:
    print(match.group(0))
