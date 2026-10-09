import glob, re

root_css = """:root{
  --navy:        #0B0D11;
  --navy-deep:   #0B0D11;
  --navy-light:  #11141A;
  --gold:        #D4AF37;
  --gold-light:  #E5C158;
  --gold-burnish:#C59B27;
  --gold-sheen:  #F3E5AB;
  --paper:       #1A1D24;
  --concrete:    #11141A;
  --ink:         #FFFFFF;
  --steel:       #9CA3AF;
  --ivory:       #F1F3F5;
  --line:        rgba(255, 255, 255, 0.08);
  --line-soft:   rgba(212, 175, 55, 0.22);
  --ok:          #4caf7d;

  --display: "Syne", sans-serif;
  --body:    "Inter", sans-serif;
  --mono:    "JetBrains Mono", monospace;

  --ease: cubic-bezier(.16,1,.3,1);
  --radius-m: 0px;
  --radius-s: 0px;
}"""

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        
    # Replace root CSS
    content = re.sub(r':root\s*\{[^}]+\}', root_css, content)
    
    # Replace fonts
    content = re.sub(r'family=Oswald[^&]*&', r'family=Syne:wght@400;500;600;700;800&', content)
    
    # Replace hardcoded backgrounds
    content = content.replace('background:#fff;', 'background:var(--paper);')
    content = content.replace('background:#ffffff;', 'background:var(--paper);')
    
    # Replace hardcoded text colors that clash with dark mode
    content = content.replace('color:var(--navy-deep)', 'color:var(--ivory)')
    content = content.replace('color:var(--navy)', 'color:var(--ivory)')
    content = content.replace('color:var(--ink)', 'color:var(--ink)')
    
    # Add body defaults
    if 'body{' in content and 'background:var(--navy)' not in content:
        content = content.replace('body{', 'body{ background:var(--navy); color:var(--ivory);')
        
    # Remove some hardcoded border-radius
    content = re.sub(r'border-radius:\s*[0-9]+px', 'border-radius:0px', content)
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Applied Design.md palette!")
