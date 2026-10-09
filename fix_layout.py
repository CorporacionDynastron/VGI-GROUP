import glob, re

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        
    # Append --container and --gutter back into :root
    if '--container:' not in content:
        content = content.replace(':root{', ':root{\n  --container: 1280px;\n  --gutter: clamp(20px, 4vw, 48px);')
    if '--ease:' not in content:
        content = content.replace(':root{', ':root{\n  --ease: cubic-bezier(.16,1,.3,1);')
        
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Restored layout variables to :root!")
