import os
import re

html_files = [f for f in os.listdir("C:\\Dynastron_Code\\VGI") if f.endswith(".html")]

for html_file in html_files:
    filepath = os.path.join("C:\\Dynastron_Code\\VGI", html_file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if "Parque Naciones Unidas" in html or "NACIONES UNIDAS" in html.upper():
        print(f"Found 'Naciones Unidas' in {html_file}")
        
    if "TRES DISCIPLINAS" in html.upper():
        print(f"Found 'TRES DISCIPLINAS' in {html_file}")
