import re

with open("nosotros.html", "r", encoding="utf-8") as f:
    html = f.read()

# The grid starts at <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
# and ends right before </div>\s*</section>

team_data = [
    ("Ander Zeballos", "Sub Gerente O.P.", "Gerencia de Infraestructura"),
    ("Bryan López", "Monitor", "Obras Públicas"),
    ("Karen Gutierrez", "Sub Gerencia de Imagen", "O.P.P."),
    ("Kiara Huaylla", "Sub Gerente de Logística", "O.P.P."),
    ("Estefani Diaz", "Sub Gerente de Diseño", "Arquitectónico"),
    ("Jairo Gutierrez", "Monitor", "Obras Públicas"),
    ("Ángela Arcos", "Especialista en Arquitectura", "Arquitectura"),
    ("Valentina Navarrete", "Monitor", "Obras Públicas"),
    ("Yanelly Alcahuaman", "Monitor", "Obras Públicas"),
    ("Betsy Calloapaza", "Especialista en Arquitectura", "Arquitectura"),
    ("Henrry Villagaray", "Monitor", "Obras Públicas")
]

cards_html = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
for name, role, dept in team_data:
    cards_html += f"""
                    <div class="group bg-surface-container-high border border-outline-variant/20 p-8 hover:bg-surface-container-highest hover:border-primary/50 transition-all duration-300 flex items-center justify-between" data-aos="fade-up">
                        <div>
                            <h4 class="font-headline-sm text-[16px] text-on-surface uppercase font-bold mb-1 group-hover:text-primary transition-colors">{name}</h4>
                            <p class="font-technical-code text-[11px] text-secondary tracking-widest leading-relaxed mb-2">{role}</p>
                            <span class="bg-surface-container px-2 py-1 text-[9px] font-label-caps text-outline tracking-widest uppercase">{dept}</span>
                        </div>
                        <img src="./test_logo.png" alt="VGI Sello" class="h-12 w-auto opacity-80 group-hover:opacity-100 group-hover:scale-110 transition-all duration-500 drop-shadow-lg">
                    </div>"""
cards_html += '\n                </div>'

new_html = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">.*?</div>\s*</div>\s*</section>', cards_html + '\n            </div>\n        </section>', html, flags=re.DOTALL)

with open("nosotros.html", "w", encoding="utf-8") as f:
    f.write(new_html)
