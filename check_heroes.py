import re
with open(r"C:\Dynastron_Code\VGI\capacitaciones.html", 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'\.hero-[^\s{]*\s*\{[^}]*\}|\.hero\s*\{[^}]*\}', html)
if match: print("capacitaciones hero CSS:", match.group(0))

with open(r"C:\Dynastron_Code\VGI\obras.html", 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'\.hero-[^\s{]*\s*\{[^}]*\}', html)
if match: print("obras hero CSS:", match.group(0))
