import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Revert single quotes
    html = html.replace('["\'Barlow Condensed\'", "\'Bahnschrift Condensed\'", "sans-serif"]', '["Barlow Condensed", "Bahnschrift Condensed", "sans-serif"]')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Reverted single quotes in tailwind config")
