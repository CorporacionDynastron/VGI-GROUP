import glob, re

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        
    content = content.replace('style="height:70px; width:auto;"', '')
    content = content.replace('style="height:65px; width:auto; border-radius:0px;"', '')
    content = content.replace('style="height:52px; width:auto;"', '')

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Removed inline logo styles.")
