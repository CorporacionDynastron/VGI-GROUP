import re

with open("index.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Make hero-img object-contain
html = re.sub(r'(<img class="w-full h-full )object-cover( transition-all duration-700"[^>]*id="hero-img")', r'\1object-contain\2', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
