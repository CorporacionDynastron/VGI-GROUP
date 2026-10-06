import os
import re

index_path = r"C:\Dynastron_Code\VGI\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the first slide image with imagen-3.jpeg
html = html.replace('./01-recreacion/IMAGEN%201.png', './images/imagen-3.jpeg')

# Add the brutal CSS animations
css_animations = """
<style>
  /* BRUTAL ANIMATIONS FOR HERO SLIDER */
  @keyframes brutalZoom {
    0% { transform: scale(1.05); opacity: 0; }
    5% { opacity: 0.4; }
    100% { transform: scale(1.15); opacity: 0.4; }
  }
  @keyframes brutalSlideUp {
    0% { transform: translateY(60px); opacity: 0; filter: blur(4px); }
    100% { transform: translateY(0); opacity: 1; filter: blur(0); }
  }
  @keyframes brutalFadeIn {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
  }
  
  .swiper-slide img {
    opacity: 0 !important; /* Hide by default until active */
  }
  
  .swiper-slide-active img {
    animation: brutalZoom 10s ease-out forwards !important;
  }
  .swiper-slide-active h1 {
    animation: brutalSlideUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  }
  .swiper-slide-active p.lede {
    animation: brutalSlideUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.3s forwards;
    opacity: 0;
  }
  .swiper-slide-active .hero-actions {
    animation: brutalFadeIn 1s ease-out 0.6s forwards;
    opacity: 0;
  }
</style>
"""

# Insert the CSS right before </head>
html = html.replace('</head>', css_animations + '\n</head>')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected imagen-3.jpeg and brutal animations.")
