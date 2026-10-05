import re
with open(r"C:\Dynastron_Code\VGI\index.html", 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'h2\s*\{[^}]*\}', html)
if match: print("h2 global:", match.group(0))

match = re.search(r'\.section-head h2\s*\{[^}]*\}', html)
if match: print("section-head h2:", match.group(0))
