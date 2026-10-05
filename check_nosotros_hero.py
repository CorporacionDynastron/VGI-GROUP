with open(r"C:\Dynastron_Code\VGI\nosotros.html", 'r', encoding='utf-8') as f:
    html = f.read()
import re
match = re.search(r'\.hero[^}]*\{[^}]*\}', html)
if match: print("Hero CSS in nosotros.html:", match.group(0))

matches = re.findall(r'<img[^>]*>', html)
for m in matches: print(m)
