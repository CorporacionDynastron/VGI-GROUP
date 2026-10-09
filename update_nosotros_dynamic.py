import re

with open("nosotros.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# 1. Update Hero Section
# Find the hero section, which is the first <section ... py-space-2xl>
# It contains 'Construyendo el futuro'
hero_match = re.search(r'(<section[^>]*>.*?Construyendo el futuro.*?)</section>', html, re.DOTALL)
if hero_match:
    old_hero = hero_match.group(1) + "</section>"
    new_hero = """
<section class="relative w-full h-[60vh] min-h-[500px] flex items-center justify-center overflow-hidden border-b border-outline-variant/20">
    <!-- Background Image Zaha Hadid Style -->
    <div class="absolute inset-0 w-full h-full">
        <img src="./04-primera-piedra/IMAGEN 2.jpeg" alt="Hero Nosotros" class="w-full h-full object-cover object-top opacity-30 mix-blend-luminosity filter blur-[2px] transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-surface/20 via-surface/80 to-surface"></div>
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,rgba(17,19,23,0.8)_100%)]"></div>
    </div>
    <div class="relative z-10 max-w-4xl mx-auto px-gutter text-center" data-aos="fade-up">
        <h1 class="font-headline-xl text-headline-xl-mobile md:text-headline-xl text-white uppercase tracking-tight font-bold mb-space-md drop-shadow-2xl">Construyendo el futuro<br><span class="text-primary">con excelencia</span></h1>
        <p class="font-body-md text-body-md text-secondary leading-relaxed mb-space-md text-lg text-white/80 max-w-2xl mx-auto">
            Conoce nuestra trayectoria, nuestros valores y el equipo de profesionales que hace posible cada proyecto.
        </p>
    </div>
</section>
"""
    html = html.replace(old_hero, new_hero)

# 2. Add 'Nuestra historia' section
# The user wants an 'Nuestra historia' section.
# Currently, `nosotros.html` has a <section id="historia">. Let's see if we can style it dynamically.
historia_match = re.search(r'<section id="historia"[^>]*>.*?(<div[^>]*>.*?</div>.*?)</section>', html, re.DOTALL)
if historia_match:
    old_historia = historia_match.group(0)
    # The old historia just has "TRABAJANDO EN LA CONSTRUCCION DESDE EL 2018"
    new_historia = old_historia.replace(
        '<section id="historia" class="w-full bg-surface py-space-2xl">',
        '<section id="historia" class="relative w-full bg-surface py-space-2xl overflow-hidden">'
    )
    # Add a subtle architectural background to historia
    bg_historia = """
    <div class="absolute inset-0 w-full h-full pointer-events-none opacity-[0.03]">
        <img src="./Fotos Proyectos/PROYECTO ALBORADA - INTERIOR 1.webp" class="w-full h-full object-cover grayscale mix-blend-screen">
    </div>
    """
    new_historia = new_historia.replace('<div class="max-w-7xl', bg_historia + '<div class="relative z-10 max-w-7xl')
    html = html.replace(old_historia, new_historia)

# 3. Enhance Misión, Visión, Objetivo with subtle backgrounds
mision_match = re.search(r'<div id="mision"[^>]*>.*?</div>\s*</div>\s*</section>', html, re.DOTALL)
if mision_match:
    old_mision = mision_match.group(0)
    
    # Let's target the individual cards which are <div data-aos="fade-up"...>
    # There are 3 of them.
    # We will replace them.
    
    # We'll just write a quick replacer for the cards.
    def card_replacer(m):
        content = m.group(1)
        # Find which card it is
        bg_img = "./Fotos Proyectos/PROYECTO LITUANIA - INTERIOR 3.webp"
        if "Misin" in content or "Misión" in content:
            bg_img = "./Fotos Proyectos/PROYECTO AMALFI- INTERIOR 1.webp"
        elif "Visin" in content or "Visión" in content:
            bg_img = "./Fotos Proyectos/PROYECTO OLIVO - INTERIOR 1.webp"
            
        return f"""<div class="relative bg-surface-container-low border border-outline-variant/10 shadow-2xl overflow-hidden group p-space-xl rounded-xl transition-all hover:-translate-y-2 hover:shadow-primary/5" data-aos="fade-up">
            <!-- Dynamic background -->
            <div class="absolute inset-0 w-full h-full opacity-5 group-hover:opacity-[0.08] transition-opacity duration-700">
                <img src="{bg_img}" class="w-full h-full object-cover filter grayscale mix-blend-screen transform group-hover:scale-105 transition-transform duration-1000">
                <div class="absolute inset-0 bg-gradient-to-t from-surface-container-low via-transparent to-transparent"></div>
            </div>
            <div class="relative z-10">
                {content}
            </div>
        </div>"""
    
    new_mision = re.sub(r'<div data-aos="fade-up"[^>]*>(.*?)</div>\s*(?=</div|<div data-aos)', card_replacer, old_mision, flags=re.DOTALL)
    
    html = html.replace(old_mision, new_mision)

# 4. Remove Team Photos, replace with VGI logo as "sello"
team_match = re.search(r'<section id="equipo"[^>]*>.*?</section>', html, re.DOTALL)
if team_match:
    old_team = team_match.group(0)
    
    def team_replacer(m):
        # m.group(0) is the team card
        # We need to replace the <img> with a VGI logo stamp layout
        # and keep the name/role
        # Actually, let's just strip the <img> and inject the logo next to the name
        
        card = m.group(0)
        # Extract name and role
        name_match = re.search(r'<h4[^>]*>(.*?)</h4>', card)
        role_match = re.search(r'<span[^>]*>(.*?)</span>', card)
        
        if not name_match or not role_match:
            return card
            
        name = name_match.group(1)
        role = role_match.group(1)
        
        return f"""
        <div class="bg-surface-container-low border border-outline-variant/20 shadow-xl overflow-hidden group relative p-space-lg flex items-center gap-6" data-aos="fade-up">
            <div class="w-16 h-16 flex-shrink-0 border border-primary/30 rounded-full flex items-center justify-center bg-surface p-2 shadow-inner">
                <img src="./test_logo.png" alt="VGI Stamp" class="w-full h-full object-contain filter grayscale opacity-70 group-hover:grayscale-0 group-hover:opacity-100 transition-all duration-300">
            </div>
            <div>
                <h4 class="font-headline-sm text-[18px] text-white uppercase mb-1 font-semibold tracking-wide group-hover:text-primary transition-colors">{name}</h4>
                <span class="font-technical-code text-xs text-secondary tracking-widest uppercase">{role}</span>
            </div>
        </div>
        """
    
    new_team = re.sub(r'<div class="bg-surface-container-low border border-outline-variant/20 shadow-xl overflow-hidden group">.*?</div>\s*</div>', team_replacer, old_team, flags=re.DOTALL)
    html = html.replace(old_team, new_team)

with open("nosotros.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated nosotros.html with dynamic styling!")
