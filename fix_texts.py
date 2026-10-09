import glob, re

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        
    # Services sections
    content = content.replace('<h3>Planos &amp; diseño</h3>', '<h3>Elaboración de proyectos</h3>')
    content = content.replace('<h3>Planos & diseño</h3>', '<h3>Elaboración de proyectos</h3>')
    content = content.replace('<h3>Construcciones</h3>', '<h3>Ejecución de obras</h3>')
    
    # Expediente Técnico -> Gerencia de proyectos
    content = content.replace('Expediente técnico', 'Gerencia de proyectos')
    content = content.replace('Expediente tcnico', 'Gerencia de proyectos')
    content = content.replace('expediente técnico', 'gerencia de proyectos')
    content = content.replace('expediente tcnico', 'gerencia de proyectos')
    
    # First person plural translations and AI cleanup
    content = content.replace('"Entregaron la obra', '"Entregamos la obra')
    content = re.sub(r'<p class="test-who">[^<]+</p>', '', content) # Remove the testimonial author
    
    content = content.replace('Obra Culminada! Nueva Infraestructura Vial Entregada con los Más Altos Estándares', 'Infraestructura vial entregada con altos estándares de calidad')
    content = content.replace('Obra Culminada! Nueva Infraestructura Vial Entregada con los Ms Altos Estndares', 'Infraestructura vial entregada con altos estándares de calidad')
    
    # "Se entregó la obra" or similar?
    content = content.replace('Se entregó la obra', 'Entregamos la obra')
    content = content.replace('Se entreg la obra', 'Entregamos la obra')
    content = content.replace('Proyecto de infraestructura recreativa entregado exitosamente', 'Entregamos exitosamente el proyecto de infraestructura recreativa')
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Applied text changes.")
