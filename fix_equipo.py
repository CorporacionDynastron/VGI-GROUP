import os

nosotros_path = r"C:\Dynastron_Code\VGI\nosotros.html"
with open(nosotros_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_equipo = '<section id="equipo" style="padding:100px 0; background:var(--navy); color:#fff; overflow:hidden;">'
new_equipo = '<section id="equipo" style="padding:100px 0; background:linear-gradient(to bottom, rgba(6,19,37,0.92), rgba(6,19,37,0.85)), url(\'./images/imagen-1.jpeg\') center/cover fixed no-repeat; color:#fff; overflow:hidden; position: relative;">'

html = html.replace(old_equipo, new_equipo)

with open(nosotros_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated equipo background.")
