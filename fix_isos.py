import glob, re

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        
    # Fix the text that became dark because it used var(--paper) for text color
    content = content.replace('color:var(--paper)', 'color:var(--ink)')
    
    # Fix the Alianzas (ISOs) bar background to be white and text to be black
    # Currently it has: .alianzas{ background:var(--paper);
    content = re.sub(r'\.alianzas\s*\{[^}]+\}', r'.alianzas{ background:#ffffff; border-top:1px solid rgba(10,31,61,.1); padding:36px 0; overflow:hidden; }', content)
    
    # Text in alianzas was previously made --ivory. Change it to black.
    content = re.sub(r'\.alianza-item\s+\.fallback-text\s*\{[^}]+\}', r'.alianza-item .fallback-text{ display:block; text-align:center; font-family:var(--mono); font-size:12px; color:#000000; margin-top:8px; opacity:0; transition:opacity .3s ease; }', content)
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Applied ISOS fixes and --paper text fixes!")
