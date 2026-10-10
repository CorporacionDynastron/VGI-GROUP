import os, re

for f in ['obras.html', 'planos.html']:
    html = open(f, encoding='utf-8').read()
    def url_encode(match):
        path = match.group(1)
        path = path.replace(' ', '%20')
        return f'src="{path}"'
    html = re.sub(r'src="([^"]+)"', url_encode, html)
    
    # also fix onclick openLightbox
    def encode_lightbox(match):
        path = match.group(1)
        path = path.replace(' ', '%20')
        return f"openLightbox('{path}')"
    html = re.sub(r"openLightbox\('([^']+)'\)", encode_lightbox, html)
    
    open(f, 'w', encoding='utf-8').write(html)
