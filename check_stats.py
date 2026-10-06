import re
with open(r"C:\Dynastron_Code\VGI\index.html", 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<section class="stats".*?</section>', html, re.IGNORECASE | re.DOTALL)
if match:
    print(match.group(0))
