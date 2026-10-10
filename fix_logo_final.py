import re
import glob

# Current logo pattern in 9c36dae for index.html, and 82c0644 for the rest
# <span class="font-headline-sm text-headline-md md:text-headline-lg text-primary tracking-wider uppercase leading-none font-bold text-xl md:text-2xl drop-shadow-sm" style="text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">VAD GOD ING'S</span>
# <span class="font-body-sm text-body-sm text-white tracking-widest uppercase mt-1 font-semibold text-[10px]">TRAINING Y CONSTRUCTION</span>

# Wait, in index.html, because I reverted it to 9c36dae, the logo might be VGI again! Let's check!
# If it's VGI, I need a regex that matches either VGI or VAD GOD ING'S

new_logo = """<span class="font-headline-sm text-headline-md md:text-headline-lg text-primary tracking-wider uppercase leading-none font-bold text-lg md:text-xl drop-shadow-sm" style="text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">VAD GOD ING'S</span><span class="font-body-sm text-body-sm text-white tracking-widest uppercase mt-1 font-semibold text-[10px]">TRAINING & CONSTRUCTION</span>"""

files = glob.glob('*.html')

for filename in files:
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    # Generic replace for any VAD GOD ING'S or VGI with CONSTRUCTION
    html = re.sub(r'<span class="font-headline-sm[^>]*>(?:VGI|VAD GOD ING\'S)</span>\s*<span class="font-[^>]*>TRAINING [Y&] CONSTRUCTION.*?</span>', new_logo, html, flags=re.DOTALL)
    html = re.sub(r'<span class="font-headline-sm[^>]*>(?:VGI|VAD GOD ING\'S)</span>\s*<span class="font-[^>]*>CONSTRUCTION & TRAINING.*?</span>', new_logo, html, flags=re.DOTALL)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Fixed logo")
