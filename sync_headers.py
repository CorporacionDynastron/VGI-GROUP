import re
import glob

def update_all_html():
    files = glob.glob('*.html')
    # Use index.html as the source of truth for the navbar
    with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
        index_html = f.read()
    
    # Extract the header block from index.html
    header_match = re.search(r'(<header.*?</header>)', index_html, re.DOTALL)
    if not header_match:
        print("Could not find header in index.html")
        return
    
    master_header = header_match.group(1)
    
    for filename in files:
        if filename == 'index.html' or filename == 'NuevaPlantillaVGI.html':
            continue
            
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
            
        # Replace header
        html = re.sub(r'<header.*?</header>', master_header, html, flags=re.DOTALL)
        
        # We also need to fix the active state for the specific page.
        # master_header currently has `aria-current="page"` and `text-primary border-b border-primary` on Inicio.
        # Let's strip the active state from all items first in the HTML.
        
        # 1. Strip from Inicio
        html = html.replace('aria-current="page"\n                      class="tracking-wide uppercase py-2 transition-colors text-primary border-b border-primary font-semibold"', 'class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface tracking-wide uppercase py-2 transition-colors"')
        
        # 2. Add to current page based on filename
        path = filename.replace('.html', '')
        if path == 'nosotros':
            html = html.replace('data-path="nosotros" href="nosotros.html">NOSOTROS', 'aria-current="page" class="text-primary border-b border-primary font-semibold flex items-center gap-1 cursor-pointer tracking-wide uppercase py-2" data-path="nosotros" href="nosotros.html">NOSOTROS')
        elif path == 'obras':
            html = html.replace('class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface tracking-wide uppercase py-2 transition-colors"\n                      data-path="obras"', 'aria-current="page"\n                      class="tracking-wide uppercase py-2 transition-colors text-primary border-b border-primary font-semibold"\n                      data-path="obras"')
        elif path == 'planos' or path == 'capacitaciones':
            # They belong to servicios dropdown in some designs, or we just leave them without active navbar state
            pass

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated header in {filename}")

update_all_html()
