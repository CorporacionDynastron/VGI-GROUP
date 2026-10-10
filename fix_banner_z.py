import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # Remove relative z-40 from banner
    html = html.replace(
        ' border-primary/50 relative z-40">',
        ' border-primary/50 relative z-0">'
    )
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)
