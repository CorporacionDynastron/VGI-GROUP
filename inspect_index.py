import re

with open(r"C:\Dynastron_Code\VGI\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove ACEROS from alianzas-set (ISO track)
iso_aceros_regex = r'<div class="alianza-item">\s*<img src="./storage/aliados/B2n8FligcJ4lRvHA18tVng60HSENL2yKFHbjNIus\.webp" alt="ACEROS">\s*<span class="fallback-text">ACEROS</span>\s*</div>'
html = re.sub(iso_aceros_regex, '', html, flags=re.IGNORECASE)

# Let's inspect the Patrocinadores grid
# We want to remove ONE Aceros Arequipa from Patrocinadores
print("HTML for Patrocinadores before:")
grid_match = re.search(r'<div class="client-marks".*?</div>\s*</div>\s*</div>', html, re.DOTALL)
if grid_match:
    print(grid_match.group(0)[:1000])

