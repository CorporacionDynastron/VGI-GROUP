import os
import re

# 1. Fix Capacitaciones Hero
cap_path = r"C:\Dynastron_Code\VGI\capacitaciones.html"
with open(cap_path, 'r', encoding='utf-8') as f:
    cap_html = f.read()

# Replace inline style with background image
old_section = '<section class="hero-obras" style="background: var(--navy-deep); color: white; padding: 180px 0 80px; text-align: center;">'
new_section = '<section class="hero-obras" style="background: linear-gradient(to bottom, rgba(3,10,20,0.7), rgba(6,19,37,0.95)), url(\'./05-formacion/IMAGEN%201.jpeg\') center/cover no-repeat; color: white; padding: 180px 0 80px; text-align: center; position: relative;">'
cap_html = cap_html.replace(old_section, new_section)

with open(cap_path, 'w', encoding='utf-8') as f:
    f.write(cap_html)


# 2. Fix Certificaciones in index.html
index_path = r"C:\Dynastron_Code\VGI\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace the Certificaciones block
cert_regex = r'<h5[^>]*>Certificaciones de Calidad</h5>\s*<div class="client-marks">.*?</div>\s*</div>\s*</div>\s*</section>'

new_certs = """<h5 style="font-family:var(--display); font-size:16px; color:var(--navy); margin-bottom:15px; text-transform:uppercase; font-weight:700;">Certificaciones de Calidad</h5>
            <div class="client-marks">
                <div class="client-mark" title="Colegio de Ingenieros del Perú">
                    <img src="./storage/aliados/IUbbSY3xCcy6hNE5Xz17vDL5Z2Oj8CLN9fkKMD5r.png" alt="CIP">
                </div>
                <div class="client-mark" title="ISO 37001">
                    <img src="./CERTIFICACIONES/ISO%2037001.jpg" alt="ISO 37001">
                </div>
                <div class="client-mark" title="ISO 9001">
                    <img src="./images/certificaciones/what-is-iso-9001-compliance.webp" alt="ISO 9001">
                </div>
            </div>
        </div>
      </div>
    </div>
  </section>"""

index_html = re.sub(cert_regex, new_certs, index_html, flags=re.IGNORECASE | re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Updates applied successfully.")
