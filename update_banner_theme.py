import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Change section background
# Original: <section class="w-full bg-surface-container-low py-space-md">
html = re.sub(
    r'<section class="w-full bg-surface-container-low py-space-md"(.*?>\s*<div class="max-w-7xl mx-auto px-gutter">\s*<div class="flex flex-wrap items-center justify-between gap-space-lg">)',
    r'<section class="w-full bg-white py-space-md"\1',
    html, flags=re.DOTALL
)

# 2. Change text color for "SISTEMAS HOMOLOGADOS:"
# Original: class="flex items-center gap-2 font-headline-sm text-sm font-bold tracking-wider text-outline uppercase"
html = html.replace(
    'class="flex items-center gap-2 font-headline-sm text-sm font-bold tracking-wider text-outline uppercase"',
    'class="flex items-center gap-2 font-headline-sm text-sm font-bold tracking-wider text-black uppercase"'
)

# 3. Change gradient fade edges
# Original: from-surface-container-low
html = html.replace(
    'from-surface-container-low to-transparent',
    'from-white to-transparent'
)

# 4. Remove dark background and borders from ISO containers
# Original: bg-surface-container border border-outline-variant/30 p-2 rounded flex items-center justify-center hover:border-primary/50 transition-all shadow-sm
html = html.replace(
    'bg-surface-container border border-outline-variant/30 p-2 rounded flex items-center justify-center hover:border-primary/50 transition-all shadow-sm',
    'p-2 rounded flex items-center justify-center hover:opacity-80 transition-all'
)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated SISTEMAS HOMOLOGADOS banner to white theme")
