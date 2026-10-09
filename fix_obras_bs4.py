import re
from bs4 import BeautifulSoup

def process_obras():
    with open("obras.html", "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Remove category sections we don't want
    sections = soup.find_all('div', class_='category-section')
    for section in sections:
        title = section.find('h3', class_='category-title')
        if title:
            t = title.text.strip().lower()
            if 'tratamiento' in t or 'hdpe' in t or 'multifamiliar' in t or 'recreacional' in t:
                section.decompose()
            elif 'deportiva' in t:
                title.string = 'Infraestructura Recreativa'
            elif 'pavimentac' in t or 'va' in t or 'vía' in t:
                title.string = 'Pavimentación de vías'
            elif 'mantenimiento' in t:
                title.string = 'Mantenimiento'

    # Change grid columns
    style = soup.find('style')
    if style and style.string:
        style.string = style.string.replace('minmax(320px', 'minmax(450px')
        
    with open("obras.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
        
process_obras()
