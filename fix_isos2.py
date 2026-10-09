import glob, re

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        
    # Restore fallback-text properly for ISOS
    content = re.sub(r'\.alianza-item\s+\.fallback-text\s*\{[^}]+\}', r'.alianza-item .fallback-text{ font-family:var(--display); font-size:24px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; color:#000000; display:block; }', content)
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Applied ISO fallback-text fix!")
