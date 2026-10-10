import glob
import re

for f in glob.glob('*.html'):
    html = open(f, encoding='utf-8').read()
    
    # Fix double class attribute: class="..." aria-current="page" class="..."
    html = re.sub(r'class="([^"]*)"\s*aria-current="page"\s*class="([^"]*)"', r'aria-current="page" class="\1 \2"', html)
    
    # Make sure we don't have duplicated text-on-surface-variant vs text-primary
    html = html.replace('text-on-surface-variant hover:text-on-surface text-primary border-b', 'text-primary border-b')
    html = html.replace('text-primary border-b border-primary font-semibold text-on-surface-variant', 'text-primary border-b border-primary font-semibold')
    
    open(f, 'w', encoding='utf-8').write(html)
