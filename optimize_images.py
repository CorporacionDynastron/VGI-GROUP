import os
import glob
from PIL import Image
import re

directories = [
    r"C:\Dynastron_Code\VGI\01-recreacion",
    r"C:\Dynastron_Code\VGI\02-pistas",
    r"C:\Dynastron_Code\VGI\03-mantenimiento",
    r"C:\Dynastron_Code\VGI\04-primera-piedra",
    r"C:\Dynastron_Code\VGI\05-formacion",
    r"C:\Dynastron_Code\VGI\Fotos Proyectos",
    r"C:\Dynastron_Code\VGI\storage\obras"
]

total_saved = 0

def optimize_image(filepath):
    global total_saved
    try:
        size_before = os.path.getsize(filepath)
        if size_before < 200 * 1024:  # skip if already small (<200KB)
            return None
            
        with Image.open(filepath) as img:
            # Convert to RGB if PNG with transparency to save space or if it's RGBA
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Resize if too large
            max_width = 1200
            if img.width > max_width:
                ratio = max_width / img.width
                new_h = int(img.height * ratio)
                img = img.resize((max_width, new_h), Image.Resampling.LANCZOS)
            
            new_path = os.path.splitext(filepath)[0] + '.webp'
            img.save(new_path, 'webp', quality=75)
            
        # Delete original
        os.remove(filepath)
        size_after = os.path.getsize(new_path)
        total_saved += (size_before - size_after)
        return os.path.basename(filepath), os.path.basename(new_path)
    except Exception as e:
        print(f"Error optimizing {filepath}: {e}")
        return None

html_files = glob.glob(r"C:\Dynastron_Code\VGI\*.html")
replacements = []

for d in directories:
    if not os.path.exists(d): continue
    for ext in ['*.png', '*.jpg', '*.jpeg']:
        for f in glob.glob(os.path.join(d, ext)):
            result = optimize_image(f)
            if result:
                old_name, new_name = result
                # Need to consider URL encoded names too
                old_encoded = old_name.replace(' ', '%20')
                new_encoded = new_name.replace(' ', '%20')
                replacements.append((old_name, new_name))
                replacements.append((old_encoded, new_encoded))

# Update HTML files
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        html = f.read()
    
    modified = False
    for old_val, new_val in replacements:
        if old_val in html:
            html = html.replace(old_val, new_val)
            modified = True
            
    if modified:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(html)

print(f"Optimization complete. Saved {total_saved / (1024*1024):.2f} MB.")
