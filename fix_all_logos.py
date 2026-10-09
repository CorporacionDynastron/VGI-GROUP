import os
import glob
import re

base_dir = r"C:\Dynastron_Code\VGI"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

css_to_add = """
  <style>
    /* Added to make the VGI logo pop with a soft white glow */
    .brand img {
      filter: drop-shadow(0px 4px 15px rgba(255, 255, 255, 0.4)) drop-shadow(0px 2px 4px rgba(0,0,0,0.6)) !important;
      transition: filter 0.3s ease, transform 0.3s ease !important;
    }
    .brand:hover img {
      filter: drop-shadow(0px 4px 20px rgba(255, 255, 255, 0.6)) drop-shadow(0px 2px 6px rgba(0,0,0,0.8)) !important;
      transform: scale(1.03) !important;
    }
  </style>
"""

old_style_regex = re.compile(r'<style>\s*/\* Added to make the VGI logo pop with a white border/glow \*/.*?</style>', re.DOTALL)

for path in html_files:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    # 1. Replace or Inject CSS
    if old_style_regex.search(html):
        html = old_style_regex.sub(css_to_add.strip(), html)
    elif "/* Added to make the VGI logo pop with a soft white glow */" not in html:
        html = html.replace("</head>", css_to_add + "\n</head>")

    # 2. Fix encoding issues (especially for planos.html which was skipped)
    html = re.sub(r'Ingenier.a', 'Ingeniería', html)
    html = re.sub(r'Ingeniera', 'Ingeniería', html)
    html = re.sub(r'construcci.n', 'construcción', html)
    html = re.sub(r'construccin', 'construcción', html)
    html = re.sub(r'Ǹxito', 'éxito', html)
    html = re.sub(r'tǸcnic', 'técnic', html)
    html = re.sub(r'capacitaci.n', 'capacitación', html)
    html = re.sub(r'capacitacin', 'capacitación', html)
    html = re.sub(r'mǭxima', 'máxima', html)
    html = re.sub(r'mǭs', 'más', html)
    html = re.sub(r'estǭndares', 'estándares', html)
    html = re.sub(r'informaci.n', 'información', html)
    html = re.sub(r'Ejecuci.n', 'Ejecución', html)
    html = re.sub(r's.mbolo', 'símbolo', html)
    html = re.sub(r'arquitect.nico', 'arquitectónico', html)
    html = re.sub(r'consultor.a', 'consultoría', html)
    html = re.sub(r'Per.', 'Perú', html)
    html = re.sub(r'p.blico', 'público', html)
    html = re.sub(r'Ing.s', "Ing's", html)
    html = html.replace('Ingeniera civil', 'Ingeniería civil')
    html = html.replace('construccin', 'construcción')

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Updated all HTML files with soft glow and encoding fixes.")
