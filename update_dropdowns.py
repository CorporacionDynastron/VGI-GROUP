import re
import glob

files = glob.glob('*.html')

for filename in files:
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    # Dropdown has exact text: Consultoría en obras de...
    # We will replace "Consultoría en " with "" ignoring case, BUT only inside the dropdown!
    # Wait, the user said: "lo que se ve en la imagen todo eso es en obra y borra en todos lo que dice "CONSULTORIA EN ""
    html = re.sub(r'(?i)Consultor.a en ', '', html)
    html = html.replace('Consultoría en ', '')
    html = html.replace('CONSULTORIA EN ', '')
    
    # Capitalize the first letter of the remaining text
    # e.g. "obras de edificaciones" -> "Obras de edificaciones"
    html = html.replace('obras de edificaciones', 'Obras de edificaciones')
    html = html.replace('obras viales', 'Obras viales')
    html = html.replace('obras de saneamiento', 'Obras de saneamiento')
    html = html.replace('obras electromec', 'Obras electromec')
    html = html.replace('obras de represas', 'Obras de represas')
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Removed CONSULTORIA EN from all files.")
