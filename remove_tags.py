import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Specifically target the spans with bg-surface-dim next to the titles in the cards
# Example: <span class="bg-surface-dim px-2.5 py-0.5 text-white font-bold uppercase border border-primary/30">FORMACIÓN</span>
pattern = r'<span\s+class="bg-surface-dim[^>]+>.*?</span>'
html = re.sub(pattern, '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Tags removed from index.html")
