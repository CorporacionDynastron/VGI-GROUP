import os

# Update index.html
index_path = r"C:\Dynastron_Code\VGI\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_unsplash = "https://images.unsplash.com/photo-1541888081622-19e34e5db8d3?q=80&w=800&auto=format&fit=crop"
new_image_1 = "./images/IMAGEN%201.jpeg"
html = html.replace(old_unsplash, new_image_1)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)


# Update nosotros.html
nosotros_path = r"C:\Dynastron_Code\VGI\nosotros.html"
with open(nosotros_path, 'r', encoding='utf-8') as f:
    nosotros_html = f.read()

old_shutter = "https://blogs.ucontinental.edu.pe/wp-content/uploads/2022/06/shutterstock_1681631557-696x464.jpg"
new_image_2 = "./images/IMAGEN%202.jpeg"
nosotros_html = nosotros_html.replace(old_shutter, new_image_2)

with open(nosotros_path, 'w', encoding='utf-8') as f:
    f.write(nosotros_html)

print("Images replaced successfully.")
