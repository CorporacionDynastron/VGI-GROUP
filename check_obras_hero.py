import re
with open(r"C:\Dynastron_Code\VGI\obras.html", 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<section class="hero[^>]*>.*?</h1>', html, re.IGNORECASE | re.DOTALL)
if match:
    print(repr(match.group(0)))
