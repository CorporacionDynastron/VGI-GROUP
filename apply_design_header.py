import glob, re

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        
    # Header scrolled
    content = content.replace('rgba(6,19,37,.94)', 'rgba(26,29,36,.94)')
    content = content.replace('rgba(6,19,37,.92)', 'rgba(26,29,36,.94)')
    
    # Text colors in .dropdown-menu
    content = content.replace('color:rgba(250,248,244,.5)', 'color:var(--steel)')
    content = content.replace('color:rgba(250,248,244,.7)', 'color:var(--ivory)')
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Applied header design rules!")
