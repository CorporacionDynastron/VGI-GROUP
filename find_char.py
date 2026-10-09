import glob, re
for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
    if "slidesPer" in content:
        matches = re.findall(r'slidesPer\S+', content)
        print(f"{f}: {set(matches)}")
