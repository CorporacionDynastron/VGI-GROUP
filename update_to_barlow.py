import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Update Google Fonts link to include Barlow Condensed instead of JetBrains Mono
    html = html.replace('JetBrains+Mono:wght@400;500;600;700', 'Barlow+Condensed:wght@400;500;600;700')
    
    # 2. Update Tailwind config
    # Currently it is: ["Bahnschrift Condensed", "Bahnschrift", "sans-serif"]
    # We will replace it with: ["'Barlow Condensed'", "'Bahnschrift Condensed'", "sans-serif"]
    html = html.replace('["Bahnschrift Condensed", "Bahnschrift", "sans-serif"]', '["\'Barlow Condensed\'", "\'Bahnschrift Condensed\'", "sans-serif"]')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated fonts to Barlow Condensed (Bahnschrift alternative) with proper quotes")
