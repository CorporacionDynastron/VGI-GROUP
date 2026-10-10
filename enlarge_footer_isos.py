import re

with open('footer.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make the ISO containers bigger
# They look like: class="bg-white p-1 rounded h-12 w-14 ...
# and class="bg-white p-1 rounded h-12 w-20 ...

js = js.replace('h-12 w-14', 'h-24 w-28') # Double size
js = js.replace('h-12 w-20', 'h-24 w-40') # Double size

# The container of these ISO logos is `flex items-center gap-2 flex-wrap`. That's fine.

with open('footer.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Footer ISO logos enlarged.")
