import glob, re

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        
    # Buttons
    content = re.sub(r'\.btn-gold\s*\{[^}]+\}', r'.btn-gold{ background:var(--gold); color:var(--navy-deep); font-family:var(--mono); padding:16px 28px; border-radius:0px; font-weight:700; }', content)
    content = re.sub(r'\.btn-gold:hover\s*\{[^}]+\}', r'.btn-gold:hover{ background:var(--gold-light); transform:translateY(-2px); box-shadow:0 0 16px rgba(212, 175, 55, 0.3); color:var(--navy-deep); }', content)
    
    # Secondary Button
    content = re.sub(r'\.btn-ghost\s*\{[^}]+\}', r'.btn-ghost{ background:var(--paper); border:1px solid rgba(212, 175, 55, 0.4); color:var(--ivory); font-family:var(--mono); padding:16px 28px; border-radius:0px; }', content)
    content = re.sub(r'\.btn-ghost:hover\s*\{[^}]+\}', r'.btn-ghost:hover{ border-color:var(--gold); color:var(--gold-sheen); transform:translateY(-2px); box-shadow:0 0 16px rgba(212, 175, 55, 0.3); }', content)
    
    # Cards
    # Project & Service Cards: Framed by 1px solid rgba(255, 255, 255, 0.08)
    content = re.sub(r'border:\s*1px solid var\(--line\)', r'border:1px solid rgba(255, 255, 255, 0.08)', content)
    
    # Text Inputs
    # Dark graphite fill (#11141A), bottom border 1px solid rgba(255, 255, 255, 0.16)
    content = re.sub(r'\.form-group input,\s*\.form-group textarea\s*\{[^}]+\}', r'.form-group input, .form-group textarea { background:var(--concrete); border:none; border-bottom:1px solid rgba(255, 255, 255, 0.16); color:var(--ivory); border-radius:0px; }', content)
    content = re.sub(r'\.form-group input:focus,\s*\.form-group textarea:focus\s*\{[^}]+\}', r'.form-group input:focus, .form-group textarea:focus { border-bottom:2px solid var(--gold); box-shadow:0 10px 10px -10px rgba(212, 175, 55, 0.2); outline:none; }', content)
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Applied secondary DESIGN.md rules!")
