import re

def migrate_page(filename):
    with open("index.html", "r", encoding="utf-8", errors="ignore") as f:
        index_html = f.read()
    
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        page_html = f.read()

    # Extract new head and header from index.html
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
    
    # Make current page active
    path_name = filename.replace('.html', '')
    if path_name == 'obras':
        head_header = head_header.replace(
            'data-path="obras" href="obras.html">Obras</a>',
            'aria-current="page" class="tracking-wide uppercase py-2 transition-colors text-primary border-b border-primary font-semibold" data-path="obras" href="obras.html">Obras</a>'
        )
    # Extract new footer
    footer_match = re.search(r'(<footer.*)', index_html, re.DOTALL)
    if not footer_match:
        print("Could not find footer in index.html")
        return
    footer = footer_match.group(1)

    # Extract old content from page
    # The content is usually between </header> and <footer>, or <div class="nav-actions"> and <footer>
    content_match = re.search(r'(?:</header>|</nav>.*?</div>)(.*?)<footer', page_html, re.DOTALL | re.IGNORECASE)
    if not content_match:
        print(f"Could not extract content from {filename}")
        return
    
    old_content = content_match.group(1)
    
    # Since we are dropping the old head, we must preserve any inline styles or scripts the page had in its head?
    # No, we will try to let the old CSS class names survive, but they won't have the CSS definitions if they were in an external file.
    # Wait, the old CSS was in `<style>` blocks in the `<head>`!
    old_head_styles = re.findall(r'(<style.*?</style>)', page_html, re.DOTALL | re.IGNORECASE)
    style_blocks = "\n".join(old_head_styles)
    
    # Inject the old style blocks into the new head so the old layout doesn't completely break
    head_header = head_header.replace('</head>', f'{style_blocks}\n</head>')

    new_html = head_header + '\n<main class="w-full pt-20 bg-surface min-h-[calc(100vh-20rem)]">\n' + old_content + '\n</main>\n' + footer

    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Migrated {filename} to new design!")

migrate_page('obras.html')
migrate_page('capacitaciones.html')
migrate_page('planos.html')
