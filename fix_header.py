import glob, re

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        
    # CSS modifications
    content = re.sub(r'\.brand img\s*\{[^}]+\}', r'.brand img{ height:85px; width:auto; border-radius:var(--radius-s); flex-shrink:0; }', content)
    
    content = re.sub(r'\.brand-text\s*\{[^}]+\}', r'.brand-text{ font-family:var(--display); font-weight:800; font-size:42px; color:var(--ink); text-transform:uppercase; letter-spacing:0; line-height:1; }', content)
    
    content = re.sub(r'\.brand-text small\s*\{[^}]+\}', r'.brand-text small{ display:block; font-family:var(--mono); font-weight:700; font-size:12px; letter-spacing:.08em; color:var(--gold); margin-top:4px; text-transform:uppercase; }', content)
    
    content = re.sub(r'nav\.links > a\s*\{[^}]+\}', r'nav.links > a{ font-size:14px; font-weight:600; color:var(--ink); position:relative; padding:8px 0; text-transform:uppercase; letter-spacing:0.04em; }', content)
    content = re.sub(r'\.dropdown > a\s*\{[^}]+\}', r'.dropdown > a { font-size:14px; font-weight:600; color:var(--ink); position:relative; padding:8px 0; text-decoration:none; display:flex; align-items:center; text-transform:uppercase; letter-spacing:0.04em; }', content)
    
    # Add an active class CSS
    if '.nav.links > a.active' not in content:
        content = content.replace('nav.links > a:hover::after, nav.links .dropdown > a:hover::after{ width:100%; }', 'nav.links > a:hover::after, nav.links .dropdown > a:hover::after{ width:100%; }\nnav.links > a.active{ color:var(--gold); }\nnav.links > a.active::after{ width:100%; }')
        
    # Header HTML modifications (for nav brand)
    content = re.sub(
        r'<span class="brand-text">Grupo Vad God Ing\'s<small>[^<]*</small></span>',
        r'<span class="brand-text">VGI<small>Construcción y Capacitaciones</small></span>',
        content,
        flags=re.IGNORECASE
    )
    
    # Footer brand
    content = re.sub(
        r'<span class="brand-text">Grupo Vad God Ing\'s</span>',
        r'<span class="brand-text">VGI<small>Construcción y Capacitaciones</small></span>',
        content,
        flags=re.IGNORECASE
    )
    
    # Active class for current page
    if f == 'index.html':
        content = content.replace('<a href="index.html">Inicio</a>', '<a href="index.html" class="active">Inicio</a>')
    elif f == 'nosotros.html':
        content = content.replace('<a href="nosotros.html">', '<a href="nosotros.html" class="active">')

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Fixed header logo and text.")
