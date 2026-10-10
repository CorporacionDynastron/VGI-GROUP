import re

with open('footer.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace custom spacing with standard spacing
replacements = {
    'gap-gutter-lg': 'gap-10',
    'pb-space-2xl': 'pb-16',
    'pt-space-2xl': 'pt-16',
    'pb-space-lg': 'pb-8',
    'pt-space-lg': 'pt-8',
    'px-gutter': 'px-6',
    'mb-space-md': 'mb-4',
    'gap-space-md': 'gap-4',
    'gap-space-lg': 'gap-8',
    'mb-space-lg': 'mb-8'
}

for old, new in replacements.items():
    js = js.replace(old, new)

with open('footer.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Standardized spacing classes in footer.js")
