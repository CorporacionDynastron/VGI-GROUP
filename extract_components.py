import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Extract header
header_match = re.search(r'(<header.*?</header>)', html, re.DOTALL)
if header_match:
    header = header_match.group(1)
    # Make sure links point to the right place relative to root
    with open('header.html', 'w', encoding='utf-8') as f:
        f.write(header)

# Extract footer
footer_match = re.search(r'(<footer.*?</footer>)', html, re.DOTALL)
if footer_match:
    footer = footer_match.group(1)
    with open('footer.html', 'w', encoding='utf-8') as f:
        f.write(footer)

js_code = """
document.addEventListener("DOMContentLoaded", function() {
    // Inject Header
    const headerContainer = document.getElementById('header-container');
    if (headerContainer) {
        fetch('header.html')
            .then(response => response.text())
            .then(data => {
                headerContainer.innerHTML = data;
                // Active link logic
                const currentPath = window.location.pathname.split('/').pop() || 'index.html';
                const links = headerContainer.querySelectorAll('nav a[data-path]');
                links.forEach(link => {
                    const linkPath = link.getAttribute('href');
                    if (linkPath.includes(currentPath) || (currentPath === 'index.html' && link.getAttribute('data-path') === 'inicio')) {
                        link.classList.add('text-primary', 'border-b', 'border-primary', 'font-semibold');
                        link.setAttribute('aria-current', 'page');
                    } else {
                        link.classList.remove('text-primary', 'border-b', 'border-primary', 'font-semibold');
                        link.removeAttribute('aria-current');
                    }
                });
            });
    }

    // Inject Footer
    const footerContainer = document.getElementById('footer-container');
    if (footerContainer) {
        fetch('footer.html')
            .then(response => response.text())
            .then(data => {
                footerContainer.innerHTML = data;
            });
    }
});
"""

with open('components.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Created components!")
