import re
import urllib.parse

# 1. New HTML for CERTIFICACIONES WITHOUT white background
cert_images = [
    {"file": "ISO 9001.png", "title": "ISO 9001:2015", "alt": "ISO 9001", "w_class": "w-20"},
    {"file": "ISO 14001.png", "title": "ISO 14001:2015", "alt": "ISO 14001", "w_class": "w-20"},
    {"file": "ISO 45001.png", "title": "ISO 45001", "alt": "ISO 45001", "w_class": "w-28"},
    {"file": "ISO 37001.png", "title": "ISO 37001:2016", "alt": "ISO 37001", "w_class": "w-20"},
    {"file": "ISO 27001.png", "title": "ISO 27001", "alt": "ISO 27001", "w_class": "w-28"},
    {"file": "CIP.png", "title": "Colegio de Ingenieros del Perú", "alt": "CIP", "w_class": "w-20"}
]

# For the footer (no carousel, just no white background)
certs_html_footer = '<div class="flex items-center gap-2 flex-wrap">\n'
for cert in cert_images:
    encoded_file = urllib.parse.quote(cert["file"])
    path = f"./CERTIFICACIONES/{encoded_file}"
    certs_html_footer += f"""                            <div class="bg-surface-container border border-outline-variant/30 p-2 rounded flex items-center justify-center hover:border-primary/50 transition-all shadow-sm h-20 {cert['w_class']}" title="{cert['title']}">
                                <img src="{path}" alt="{cert['alt']}" class="h-full w-full object-contain">
                            </div>\n"""
certs_html_footer += '                        </div>'

# For index.html (with infinite carousel)
# We need an overflow-hidden container, and a scrolling inner container with duplicated items.
certs_html_index = '<div class="overflow-hidden w-full max-w-[calc(100vw-2rem)] lg:max-w-[700px] relative">\n'
certs_html_index += '    <!-- Gradient fade edges -->\n'
certs_html_index += '    <div class="absolute inset-y-0 left-0 w-12 bg-gradient-to-r from-surface-container-low to-transparent z-10 pointer-events-none"></div>\n'
certs_html_index += '    <div class="absolute inset-y-0 right-0 w-12 bg-gradient-to-l from-surface-container-low to-transparent z-10 pointer-events-none"></div>\n'
certs_html_index += '    <div class="flex animate-marquee hover:[animation-play-state:paused]">\n'
# We duplicate the items array so it scrolls seamlessly
for loop in range(2):
    for cert in cert_images:
        encoded_file = urllib.parse.quote(cert["file"])
        path = f"./CERTIFICACIONES/{encoded_file}"
        certs_html_index += f"""        <div class="flex-shrink-0 bg-surface-container border border-outline-variant/30 p-2 rounded flex items-center justify-center hover:border-primary/50 transition-all shadow-sm h-20 {cert['w_class']} mx-2" title="{cert['title']}">
            <img src="{path}" alt="{cert['alt']}" class="h-full w-full object-contain">
        </div>\n"""
certs_html_index += '    </div>\n'
certs_html_index += '</div>'


# Replace in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Certificaciones in index.html
html = re.sub(r'<div class="flex items-center gap-3 md:gap-space-md flex-wrap">\s*<div class="bg-surface-container.*?</div>\s*</div>\s*</div>\s*</div>', 
              certs_html_index, html, flags=re.DOTALL)

# Let's add the marquee animation CSS if it's not there
marquee_css = """
        @keyframes marquee {
            0% { transform: translateX(0%); }
            100% { transform: translateX(-50%); }
        }
        .animate-marquee {
            display: flex;
            width: max-content;
            animation: marquee 20s linear infinite;
        }
"""
if 'animate-marquee' not in html:
    html = html.replace('</style>', marquee_css + '\n    </style>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Let's add the marquee CSS to obras.html as well just in case, but obras doesn't have the banner.

# Replace in footer.js
with open('footer.js', 'r', encoding='utf-8') as f:
    footer_js = f.read()

footer_js = re.sub(r'<div class="flex items-center gap-2 flex-wrap">\s*<div class="bg-surface-container.*?</div>\s*</div>\s*</div>\s*</div>', 
                   certs_html_footer, footer_js, flags=re.DOTALL)

with open('footer.js', 'w', encoding='utf-8') as f:
    f.write(footer_js)

print("Images fixed without white backgrounds, and slider added!")
