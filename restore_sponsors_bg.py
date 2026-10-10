import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Restore bg-white for the Patrocinadores
html = html.replace('class="bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28"',
                    'class="bg-white py-4 px-6 flex items-center justify-center transition-colors h-28 rounded border border-outline-variant/10 shadow-sm hover:shadow-md"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Restored white background for sponsors")
