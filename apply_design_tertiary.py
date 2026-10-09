import glob, re

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        
    # Modal Close button
    content = content.replace('background:rgba(255,255,255,0.9); color:var(--ivory);', 'background:var(--navy-light); color:var(--gold); border:1px solid var(--gold); border-radius:0px;')
    # Remove border-radius:50% on close button
    content = content.replace('border-radius:50%;', 'border-radius:0px;')
    
    # Stat card
    content = content.replace('background:rgba(6,19,37,0.4)', 'background:var(--paper)')
    
    # Replace white drop shadows from before if there are any that don't fit
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Applied tertiary DESIGN.md rules!")
