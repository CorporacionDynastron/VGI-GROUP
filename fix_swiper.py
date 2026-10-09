import glob, re
for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
    
    new_content = re.sub(r'slidesPer.iew', 'slidesPerView', content)
    if new_content != content:
        with open(f, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Fixed in {f}")
