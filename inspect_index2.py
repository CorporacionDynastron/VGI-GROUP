import re
with open(r"C:\Dynastron_Code\VGI\index.html", "r", encoding="utf-8") as f:
    html = f.read()

grid_match = re.search(r'<div class="client-marks".*?</div>\s*</div>\s*(?=</section>|<div class="testimonials")', html, re.DOTALL)
if grid_match:
    print(grid_match.group(0))
