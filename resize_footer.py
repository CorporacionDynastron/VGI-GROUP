import re

with open('footer.js', 'r', encoding='utf-8') as f:
    js = f.read()

# I had replaced:
# h-12 w-14 -> h-24 w-28
# h-12 w-20 -> h-24 w-40

# Let's revert and make them slightly smaller than the huge ones, but bigger than the original 12.
# h-24 w-28 -> h-16 w-20
# h-24 w-40 -> h-16 w-28

js = js.replace('h-24 w-28', 'h-16 w-20')
js = js.replace('h-24 w-40', 'h-16 w-28')

with open('footer.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Footer ISOs resized")
