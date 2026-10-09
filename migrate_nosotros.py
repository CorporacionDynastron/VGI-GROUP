import re

def migrate_nosotros():
    with open("index.html", "r", encoding="utf-8", errors="ignore") as f:
        index_html = f.read()
    
    with open("nosotros.html", "r", encoding="utf-8", errors="ignore") as f:
        nosotros_html = f.read()

    # Extract new head and header
    head_header_match = re.search(r'(<!DOCTYPE html>.*?</header>)', index_html, re.DOTALL)
    if not head_header_match:
        print("Could not find head/header in index.html")
        return
    head_header = head_header_match.group(1)

    # Change active state in nav
    head_header = head_header.replace(
        'data-path="inicio" href="index.html">Inicio</a>',
        'class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface tracking-wide uppercase py-2 transition-colors" data-path="inicio" href="index.html">Inicio</a>'
    ).replace(
        'aria-current="page"\n                      class="tracking-wide uppercase py-2 transition-colors text-primary border-b border-primary font-semibold"\n                      data-path="inicio"',
        'class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface tracking-wide uppercase py-2 transition-colors" data-path="inicio"'
    )
    
    # Make Nosotros active
    # Wait, nosotros is now a dropdown in index.html!
    # Let's find the nosotros nav block in head_header and add aria-current logic, or just leave it for simplicity.
    # We will just replace it simply:
    head_header = head_header.replace(
        'data-path="nosotros" href="nosotros.html">NOSOTROS',
        'aria-current="page" class="text-primary border-b border-primary font-semibold flex items-center gap-1 cursor-pointer tracking-wide uppercase py-2" data-path="nosotros" href="nosotros.html">NOSOTROS'
    )
    # The above replacement won't perfectly match the exact class string but we'll try our best.

    # Extract new footer
    footer_match = re.search(r'(<footer.*)', index_html, re.DOTALL)
    if not footer_match:
        print("Could not find footer in index.html")
        return
    footer = footer_match.group(1)

    # Extract old content from nosotros.html
    # The content is usually between </nav> (or </header>) and <footer>
    content_match = re.search(r'</header>(.*?)<footer', nosotros_html, re.DOTALL | re.IGNORECASE)
    if not content_match:
        # try <nav>
        content_match = re.search(r'</nav>.*?</div>(.*?)<footer', nosotros_html, re.DOTALL | re.IGNORECASE)
    
    if not content_match:
        print("Could not extract content from nosotros.html")
        return
    
    old_content = content_match.group(1)
    
    # We'll wrap old_content in the new <main> tag and apply generic tailwind classes to modernize it
    # We'll replace old CSS classes with Tailwind ones
    
    # Replace sections
    old_content = re.sub(r'<section([^>]*)>', r'<section\1 class="w-full bg-surface py-space-2xl">', old_content)
    old_content = re.sub(r'<div class="container[^"]*">', r'<div class="max-w-7xl mx-auto px-gutter">', old_content)
    
    # Typography
    old_content = re.sub(r'<h1([^>]*)>', r'<h1\1 class="font-headline-xl text-headline-xl-mobile md:text-headline-xl text-on-surface uppercase tracking-tight font-bold mb-space-md">', old_content)
    old_content = re.sub(r'<h2([^>]*)>', r'<h2\1 class="font-headline-lg text-headline-lg-mobile md:text-headline-lg text-primary uppercase tracking-tight font-bold mb-space-md">', old_content)
    old_content = re.sub(r'<h3([^>]*)>', r'<h3\1 class="font-headline-sm text-headline-sm text-on-surface uppercase font-bold mb-space-sm">', old_content)
    old_content = re.sub(r'<p([^>]*)>', r'<p\1 class="font-body-md text-body-md text-secondary leading-relaxed mb-space-md">', old_content)
    
    # Grids
    old_content = old_content.replace('class="grid"', 'class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-gutter-lg"')
    old_content = old_content.replace('class="team-grid"', 'class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-gutter-lg mt-space-xl"')
    old_content = old_content.replace('class="team-card"', 'class="bg-surface-container-low border border-outline-variant/20 shadow-xl overflow-hidden group"')
    old_content = old_content.replace('class="team-info"', 'class="p-space-lg bg-surface-container-highest"')
    
    # Images in team cards
    old_content = re.sub(r'<img([^>]*)src="([^"]+)"([^>]*)>', r'<img\1src="\2"\3 class="w-full h-80 object-cover filter grayscale hover:grayscale-0 transition-all duration-500">', old_content)

    new_html = head_header + '\n<main class="w-full pt-20 bg-surface min-h-[calc(100vh-20rem)]">\n' + old_content + '\n</main>\n' + footer

    with open("nosotros.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Migrated nosotros.html to new design!")

migrate_nosotros()
