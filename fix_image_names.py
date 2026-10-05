import os
import re

# Rename files
img_dir = r"C:\Dynastron_Code\VGI\images"
img1_old = os.path.join(img_dir, "IMAGEN 1.jpeg")
img2_old = os.path.join(img_dir, "IMAGEN 2.jpeg")
img1_new = os.path.join(img_dir, "imagen-1.jpeg")
img2_new = os.path.join(img_dir, "imagen-2.jpeg")

if os.path.exists(img1_old): os.rename(img1_old, img1_new)
if os.path.exists(img2_old): os.rename(img2_old, img2_new)

# Update index.html
index_path = r"C:\Dynastron_Code\VGI\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("IMAGEN%201.jpeg", "imagen-1.jpeg")
html = html.replace("IMAGEN 1.jpeg", "imagen-1.jpeg")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)


# Update nosotros.html
nosotros_path = r"C:\Dynastron_Code\VGI\nosotros.html"
with open(nosotros_path, 'r', encoding='utf-8') as f:
    nosotros_html = f.read()

nosotros_html = nosotros_html.replace("IMAGEN%202.jpeg", "imagen-2.jpeg")
nosotros_html = nosotros_html.replace("IMAGEN 2.jpeg", "imagen-2.jpeg")
# ALSO make sure the overlay isn't too dark!
# Old: linear-gradient(180deg, rgba(6,19,37,0.85) 0%, rgba(10,31,61,0.75) 55%, rgba(22,51,94,0.7) 100%)
# Let's make it more transparent so the image actually shows through
new_gradient = "linear-gradient(180deg, rgba(6,19,37,0.6) 0%, rgba(10,31,61,0.5) 55%, rgba(22,51,94,0.45) 100%)"
nosotros_html = re.sub(r'linear-gradient\(180deg,[^)]+\)', new_gradient, nosotros_html)

with open(nosotros_path, 'w', encoding='utf-8') as f:
    f.write(nosotros_html)

print("Renamed and updated HTML successfully.")
