import re
with open(r"C:\Dynastron_Code\VGI\nosotros.html", 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<section[^>]*>.*?NUESTROS ESPECIALISTAS.*?</section>', html, re.IGNORECASE | re.DOTALL)
if match:
    print(match.group(0)[:500])
