import re

with open("nosotros.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the team section
team_data = [
    ("Ander Zeballos", "Sub Gerente O.P.", "Gerencia de Infraestructura"),
    ("Bryan López", "Monitor", "Obras Públicas"),
    ("Karen Gutierrez", "Sub Gerencia de Imagen O.P.P.", "Imagen Institucional"),
    ("Kiara Huaylla", "Sub Gerente de Logística O.P.P.", "Logística"),
    ("Estefani Diaz", "Sub Gerente de Diseño Arquitectónico", "Arquitectura"),
    ("Jairo Gutierrez", "Monitor", "Obras Públicas"),
    ("Ángela Arcos", "Especialista en Arquitectura", "Arquitectura"),
    ("Valentina Navarrete", "Monitor", "Obras Públicas"),
    ("Yanelly Alcahuaman", "Monitor", "Obras Públicas"),
    ("Betsy Calloapaza", "Especialista en Arquitectura", "Arquitectura"),
    ("Henrry Villagaray", "Monitor", "Obras Públicas")
]

cards_html = ""
for name, role, dept in team_data:
    cards_html += f"""
                <div class="bg-surface-container-low border border-outline-variant/20 shadow-xl overflow-hidden group relative p-space-lg flex flex-col md:flex-row items-center gap-6" data-aos="fade-up">
                    <div class="w-20 h-20 flex-shrink-0 flex items-center justify-center p-2 rounded-full border border-primary/20 bg-surface">
                        <img src="./images/test_logo.png" onerror="this.src='./test_logo.png'" alt="VGI Stamp" class="w-full h-full object-contain filter drop-shadow-md group-hover:scale-110 transition-all duration-300">
                    </div>
                    <div class="text-center md:text-left">
                        <h4 class="font-headline-sm text-[18px] text-white uppercase mb-1 font-semibold tracking-wide group-hover:text-primary transition-colors">{name}</h4>
                        <span class="font-technical-code text-xs text-secondary tracking-widest uppercase block mb-1">{role}</span>
                        <span class="font-label-caps text-[10px] text-outline tracking-widest uppercase bg-surface-container px-2 py-1 inline-block mt-2">{dept}</span>
                    </div>
                </div>"""

# Replace the grid container contents for the team
new_html = re.sub(r'(<section id="equipo"[^>]*>.*?<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-gutter-lg">)(.*?)(</section>)', r'\g<1>' + cards_html + r'\n            </div>\n        </div>\n    \g<3>', html, flags=re.DOTALL)

with open("nosotros.html", "w", encoding="utf-8") as f:
    f.write(new_html)
