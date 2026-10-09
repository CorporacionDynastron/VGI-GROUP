with open("obras.html", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

new_lines = []
skip = False

for line in lines:
    if '<div class="category-section">' in line:
        pass
    
    if '<h3 class="category-title">' in line:
        title = line.lower()
        if 'tratamiento' in title or 'hdpe' in title or 'multifamiliar' in title or 'recreacional' in title:
            skip = True
            # We need to remove the previous line if it was <div class="category-section">
            if '<div class="category-section">' in new_lines[-1]:
                new_lines.pop()
            continue
        
        # Rename valid categories
        if 'deportiva' in title:
            line = '            <h3 class="category-title">Infraestructura Recreativa</h3>\n'
        elif 'pavimentac' in title or 'va' in title or 'vía' in title:
            line = '            <h3 class="category-title">Pavimentación de vías</h3>\n'
        elif 'mantenimiento' in title:
            line = '            <h3 class="category-title">Mantenimiento</h3>\n'

    if skip:
        # Check if this is the end of the category section
        # In this HTML, each category section ends before the next <div class="category-section">
        # or before </section>
        if '<div class="category-section">' in line:
            skip = False
            new_lines.append(line)
        elif '</section>' in line:
            skip = False
            new_lines.append(line)
        continue

    new_lines.append(line)

html = "".join(new_lines)
html = html.replace('minmax(320px', 'minmax(450px')

with open("obras.html", "w", encoding="utf-8") as f:
    f.write(html)
