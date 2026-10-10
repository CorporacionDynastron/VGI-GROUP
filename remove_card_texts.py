import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<span class="text-primary font-bold tracking-wider">02\.\s+INFRAESTRUCTURA\s+CIVIL</span>', '<span class="text-primary font-bold tracking-wider"></span>', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
