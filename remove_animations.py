import re
with open(r"C:\Dynastron_Code\VGI\index.html", 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the brutal animations style block
html = re.sub(r'<style>\s*/\* BRUTAL ANIMATIONS FOR HERO SLIDER \*/.*?</style>', '', html, flags=re.IGNORECASE | re.DOTALL)

with open(r"C:\Dynastron_Code\VGI\index.html", 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed broken animations.")
