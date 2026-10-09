import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Make sure slides array has `headline`
slides_old = r"""const slides = \[
                    \{
                        img: "\./images/imagen-3\.jpeg",
                        title: "INFRAESTRUCTURA RECREATIVA",
                        tag: "FOLIO 04 / PROYECTO 2024",
                        desc: "Diseñamos y ejecutamos obras de ingeniería civil con precisión milimétrica\. Transformamos espacios públicos, losas deportivas y áreas recreativas garantizando máxima seguridad y cumplimiento estricto de plazos\."
                    \},
                    \{
                        img: "\./images/imagen-1\.jpeg",
                        title: "PAVIMENTACIÓN DE VÍAS",
                        tag: "FOLIO 08 / VIALIDAD MTC",
                        desc: "Ejecución de pistas y veredas de concreto de alta resistencia\. Movimiento de tierras, compactación y vaciado con maquinaria especializada bajo normativa técnica MTC\."
                    \},
                    \{
                        img: "\./images/imagen-2\.jpeg",
                        title: "MANTENIMIENTO ESTRUCTURAL",
                        tag: "FOLIO 12 / GESTIÓN CIV",
                        desc: "Servicios integrales de mantenimiento preventivo y correctivo en infraestructuras civiles\. Preservamos la integridad de las obras con soluciones técnicas precisas\."
                    \}
                \];"""

slides_new = """const slides = [
                    {
                        img: "./images/imagen-3.jpeg",
                        title: "INFRAESTRUCTURA RECREATIVA",
                        headline: "Espacios públicos de <span class='text-primary'>alto impacto.</span>",
                        desc: "Diseñamos y ejecutamos obras de ingeniería civil con precisión milimétrica. Transformamos espacios públicos, losas deportivas y áreas recreativas garantizando máxima seguridad y cumplimiento estricto de plazos."
                    },
                    {
                        img: "./images/imagen-1.jpeg",
                        title: "PAVIMENTACIÓN DE VÍAS",
                        headline: "Conectividad y <span class='text-primary'>resistencia.</span>",
                        desc: "Ejecución de pistas y veredas de concreto de alta resistencia. Movimiento de tierras, compactación y vaciado con maquinaria especializada bajo normativa técnica MTC."
                    },
                    {
                        img: "./images/imagen-2.jpeg",
                        title: "MANTENIMIENTO ESTRUCTURAL",
                        headline: "Preservamos la <span class='text-primary'>integridad.</span>",
                        desc: "Servicios integrales de mantenimiento preventivo y correctivo en infraestructuras civiles. Preservamos la integridad de las obras con soluciones técnicas precisas."
                    }
                ];"""

html = re.sub(r'const slides = \[.*?\];', slides_new, html, flags=re.DOTALL)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
