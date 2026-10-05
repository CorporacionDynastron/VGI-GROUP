import re
with open(r"C:\Dynastron_Code\VGI\nosotros.html", 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the broken hero CSS
# Current broken background:
#   radial-gradient(ellipse at 75% 18%, rgba(201,162,39,.15), transparent 45%),
#   linear-gradient(180deg, rgba(6,19,37,0.6) 0%, rgba(10,31,61,0.5) 55%, rgba(22,51,94,0.45) 100%) 0%, rgba(10,31,61,0.75) 55%, rgba(22,51,94,0.7) 100%),
#   url('./images/imagen-2.jpeg') center/cover no-repeat;

correct_bg = """background:
    radial-gradient(ellipse at 75% 18%, rgba(201,162,39,.15), transparent 45%),
    linear-gradient(180deg, rgba(6,19,37,0.6) 0%, rgba(10,31,61,0.55) 55%, rgba(22,51,94,0.5) 100%),
    url('./images/imagen-2.jpeg') center/cover no-repeat;"""

html = re.sub(r'background:\s*radial-gradient.*?\);', correct_bg, html, flags=re.IGNORECASE | re.DOTALL)

with open(r"C:\Dynastron_Code\VGI\nosotros.html", 'w', encoding='utf-8') as f:
    f.write(html)
