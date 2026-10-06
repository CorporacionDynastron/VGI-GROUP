import re

index_path = r"C:\Dynastron_Code\VGI\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix NaN bug in JS
# Replace `counter.removeAttribute('data-count');` with a safe class toggle or just remove it and add a check.
html = html.replace("counter.removeAttribute('data-count');", "/* counter.removeAttribute('data-count'); */ counter.classList.add('done');")
html = html.replace("const target = +counter.getAttribute('data-count');", "if(counter.classList.contains('done')) return; const target = +counter.getAttribute('data-count');")

# 2. Add background image to Stats section
# The stats section might look like: <section class="stats" style="...">
# We will inject the background image into it.
stats_regex = r'(<section class="stats" style=")([^"]*)(")'
def inject_bg(match):
    style = match.group(2)
    new_style = "background: linear-gradient(to bottom, rgba(6,19,37,0.92), rgba(6,19,37,0.85)), url('./images/imagen-3.jpeg') center/cover fixed no-repeat; " + style
    return match.group(1) + new_style + match.group(3)

html = re.sub(stats_regex, inject_bg, html, flags=re.IGNORECASE)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed NaN bug and added background to stats.")
