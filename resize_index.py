import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to find the SISTEMAS HOMOLOGADOS section and replace the sizes there.
# The section starts with <span class="">SISTEMAS HOMOLOGADOS:</span>
# Let's extract the section or just replace globally because they might only appear in this banner and the footer.
# Wait, the footer is already extracted to footer.js! So any h-12 w-14 in index.html is likely the banner.

html = html.replace('h-12 w-14', 'h-16 w-20')
html = html.replace('h-12 w-20', 'h-16 w-28')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Index.html ISOs resized")
