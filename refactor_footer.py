import glob
import re

# Read index.html to extract the footer
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

footer_match = re.search(r'(<footer\b.*?>.*?</footer>)', html, flags=re.DOTALL | re.IGNORECASE)
if not footer_match:
    print("Could not find footer in index.html!")
    exit(1)

footer_html = footer_match.group(1)

# Escape the backticks just in case
footer_js_content = "const vgiFooterHTML = `\n" + footer_html.replace('`', '\\`') + "\n`;\ndocument.write(vgiFooterHTML);\n"

# Write footer.js
with open('footer.js', 'w', encoding='utf-8') as f:
    f.write(footer_js_content)

# Replace the footer block in all html files with <script src="footer.js"></script>
for file_path in glob.glob('*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_html = f.read()
    
    # Remove tags from the cards (PLANOS BIM, OBRA CIVIL, FORMACIÓN)
    # The tags match this pattern exactly:
    # <span class="bg-surface-dim px-2.5 py-0.5 text-white font-bold uppercase border border-primary/30">PLANOS BIM</span>
    # <span class="bg-surface-dim px-2.5 py-0.5 text-white font-bold uppercase border border-primary/30">OBRA CIVIL</span>
    # <span class="bg-surface-dim px-2.5 py-0.5 text-white font-bold uppercase border border-primary/30">FORMACIÓN</span>
    # Because of encoding issues, I will use a regex to strip them based on class
    file_html = re.sub(r'<span\s+class="bg-surface-dim px-2\.5 py-0\.5 text-white font-bold uppercase border border-primary/30">.*?</span>', '', file_html)
    # They could also have slightly different whitespace. Let's use a simpler regex
    file_html = re.sub(r'<span[^>]*class="[^"]*bg-surface-dim px-2\.5 py-0\.5[^"]*"[^>]*>.*?</span>', '', file_html)

    # Replace footer
    file_html = re.sub(r'<footer\b.*?>.*?</footer>', '<script src="footer.js"></script>', file_html, flags=re.DOTALL | re.IGNORECASE)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(file_html)

print("Footer refactored and tags removed.")
