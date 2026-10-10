import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # Change banner z-index from 60 to 40
    html = html.replace(
        'relative z-[60]">',
        'relative z-40">'
    )
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)
