import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace bg-white with bg-surface-container-high for the Patrocinadores
html = html.replace('bg-white py-4 px-6 flex items-center justify-center transition-colors h-28 rounded border border-outline-variant/10 shadow-sm hover:shadow-md',
                    'bg-surface-container-high py-4 px-6 flex items-center justify-center transition-colors h-28')

# The user also wanted to make sure they are somewhat visible if they have dark tones.
# Let's add hover:brightness-125 or just keep it as is.
# The previous class was `h-16 md:h-20 w-auto object-contain drop-shadow-sm` on the img.
# I'll just change the container background.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Removed white background from sponsors")
