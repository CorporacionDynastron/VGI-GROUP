import glob
import re

# Read the header from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the header block
header_match = re.search(r'<header.*?</header>', html, re.DOTALL)
if not header_match:
    print("Could not find header in index.html")
    exit(1)

header_html = header_match.group(0)

# FIX THE Z-INDEX BUG in the extracted header
# Remove "relative z-0" from the yellow banner so it's strictly static and falls behind dropdowns
header_html = header_html.replace(' relative z-0">', '">')
header_html = header_html.replace(' relative z-40">', '">')

# Create the JavaScript component
# We use document.write so it executes synchronously and doesn't suffer from CORS on file:// protocol
js_content = """
const vgiHeaderHTML = `
""" + header_html.replace('`', '\\`') + """
`;

document.write(vgiHeaderHTML);

// Script to set the active nav link based on the current URL
window.addEventListener('DOMContentLoaded', () => {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    let activeTarget = '';
    
    if (currentPath.includes('index.html') || currentPath === '') activeTarget = 'inicio';
    else if (currentPath.includes('obras.html')) activeTarget = 'obras';
    else if (currentPath.includes('nosotros.html')) activeTarget = 'nosotros';
    else if (currentPath.includes('planos.html') || currentPath.includes('capacitaciones.html')) activeTarget = 'servicios';
    
    if (activeTarget) {
        const links = document.querySelectorAll('header nav a');
        links.forEach(link => {
            if (link.getAttribute('data-path') === activeTarget) {
                // Remove inactive classes
                link.classList.remove('text-on-surface-variant', 'hover:text-on-surface');
                // Add active classes
                link.classList.add('text-primary', 'border-b', 'border-primary', 'font-semibold');
            } else {
                // Ensure inactive styling for the rest
                link.classList.remove('text-primary', 'border-b', 'border-primary', 'font-semibold');
                link.classList.add('text-on-surface-variant', 'hover:text-on-surface');
            }
        });
    }
});
"""

with open('header.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Now, strip the header out of ALL html files and replace it with <script src="header.js"></script>
for file_name in glob.glob('*.html'):
    with open(file_name, 'r', encoding='utf-8') as f:
        file_html = f.read()
    
    # Replace the header block
    new_html = re.sub(r'<header.*?</header>', '<script src="header.js"></script>', file_html, flags=re.DOTALL)
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(new_html)

print("Refactored to use header.js across all files.")
