import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # Replace h-24 with h-40 for ISO logos
    html = html.replace('class="h-24 w-auto object-contain filter grayscale', 'class="h-40 w-auto object-contain filter grayscale')
    # Also I should probably remove the grayscale if they want it to "note better", but they only asked to make it bigger. Let's keep grayscale but make it bigger.

    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)

print("ISO sizes updated!")
