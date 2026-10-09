import re
import glob

new_logo = """<span class="font-headline-sm text-headline-md md:text-headline-lg text-primary tracking-wider uppercase leading-none font-bold text-xl md:text-2xl drop-shadow-sm" style="text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">VAD GOD ING'S</span><span class="font-body-sm text-body-sm text-white tracking-widest uppercase mt-1 font-semibold text-[10px]">TRAINING Y CONSTRUCTION</span>"""

files = glob.glob('*.html')

for filename in files:
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    html = re.sub(r'<span[^>]*>VGI</span>\s*<span[^>]*>CONSTRUCTION & TRAINING</span>', new_logo, html, flags=re.DOTALL)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Fixed logo")
