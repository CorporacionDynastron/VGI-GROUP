import glob, re

new_css = """
    /* Added to make the VGI logo pop with a light shadow */
    .brand img {
      filter: drop-shadow(4px 6px 12px rgba(255, 255, 255, 0.7)) drop-shadow(0px 4px 8px rgba(0,0,0,0.5)) !important;
      transition: filter 0.3s ease, transform 0.3s ease !important;
    }
    .brand:hover img {
      filter: drop-shadow(4px 6px 16px rgba(255, 255, 255, 0.9)) drop-shadow(0px 4px 12px rgba(0,0,0,0.7)) !important;
      transform: scale(1.03) !important;
    }
"""

for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
    
    # Fix the capacitaciones typo
    content = content.replace("capacitaciónes", "capacitaciones")
    content = content.replace("capacitacines", "capacitaciones")
    # There's also some places where it was capacitacines
    content = content.replace("capacitacines", "capacitaciones")
    
    # Fix the shadow
    content = re.sub(
        r'/\* Added to make the VGI logo pop with a light shadow \*/.*?transform: scale\(1\.03\) !important;\s*}',
        new_css.strip(),
        content,
        flags=re.DOTALL
    )
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)
