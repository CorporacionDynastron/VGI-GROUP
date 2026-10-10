import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace JetBrains Mono with Bahnschrift Condensed
    # Look for "label-caps": ["JetBrains Mono"] and "technical-code": ["JetBrains Mono"]
    html = html.replace('["JetBrains Mono"]', '["Bahnschrift Condensed", "Bahnschrift", "sans-serif"]')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated tailwind fonts in all html files")
