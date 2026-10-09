import glob, re
for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Remove the massive inline style in index.html
    content = re.sub(
        r'style="height:70px; width:auto; filter: drop-shadow\([^"]+" onmouseover="[^"]+" onmouseout="[^"]+"',
        'style="height:70px; width:auto;"',
        content
    )
    content = re.sub(
        r'style="height:70px; width:auto; filter: drop-shadow[^"]+"',
        'style="height:70px; width:auto;"',
        content
    )
    
    # Replace the soft white glow CSS with a light colored drop shadow
    new_css = """
    /* Added to make the VGI logo pop with a light shadow */
    .brand img {
      filter: drop-shadow(3px 4px 6px rgba(230, 230, 230, 0.5)) drop-shadow(0px 2px 4px rgba(0,0,0,0.4)) !important;
      transition: filter 0.3s ease, transform 0.3s ease !important;
    }
    .brand:hover img {
      filter: drop-shadow(3px 4px 8px rgba(230, 230, 230, 0.7)) drop-shadow(0px 2px 6px rgba(0,0,0,0.6)) !important;
      transform: scale(1.03) !important;
    }
    """
    
    # We find the existing style block and replace it
    content = re.sub(
        r'/\* Added to make the VGI logo pop with a soft white glow \*/.*?transform: scale\(1\.03\) !important;\s*}',
        new_css.strip(),
        content,
        flags=re.DOTALL
    )
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)
