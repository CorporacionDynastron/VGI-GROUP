import re

with open("obras.html", "r", encoding="utf-8") as f:
    html = f.read()

# Split into parts
parts = html.split('<div class="category-section">')

new_parts = [parts[0]]

for part in parts[1:]:
    if 'category-title' not in part:
        new_parts.append('<div class="category-section">' + part)
        continue
        
    title_match = re.search(r'<h3 class="category-title">(.*?)</h3>', part)
    if title_match:
        title = title_match.group(1).lower()
        if 'tratamiento' in title or 'hdpe' in title or 'multifamiliar' in title or 'recreacional' in title:
            # Skip this section entirely
            # BUT we need to preserve whatever comes after this section!
            # The section ends at the matching </div> for `<div class="category-section">`?
            pass
