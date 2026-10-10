import re

with open('header.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace font-headline-sm with font-label-caps in the dropdown links
# <a href="obras.html#edificaciones" class="... font-headline-sm ...">
js = re.sub(
    r'(<a href="obras\.html#\w+" class="[^"]*?)font-headline-sm([^"]*?">)',
    r'\1font-label-caps\2',
    js
)

with open('header.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated header.js dropdown fonts")
