import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

new_slides = """        <!-- Obra 4 -->
        <div class="swiper-slide">
          <article class="noticia-card" onclick="openHojaModal('modal-obra-destacada-4')" style="cursor:pointer;">
            <div class="noticia-img"><img src="./07-saneamiento/saneamiento_1.jpg" alt="Saneamiento"></div>
            <div class="noticia-info">
              <span class="noticia-date">Saneamiento y Agua</span>
              <h4 class="noticia-title">Obras de Saneamiento</h4>
              <p class="noticia-desc">Instalación y mantenimiento de redes de saneamiento y tuberías HDPE.</p>
              <a href="javascript:void(0)" class="noticia-link">Ver detalles <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
            </div>
          </article>
        </div>

        <!-- Obra 5 -->
        <div class="swiper-slide">
          <article class="noticia-card" onclick="openHojaModal('modal-obra-destacada-5')" style="cursor:pointer;">
            <div class="noticia-img"><img src="./08-multifamiliar/primera-piedra/PRIMERA_PIEDRA_1.webp" alt="Vivienda Multifamiliar"></div>
            <div class="noticia-info">
              <span class="noticia-date">Edificaciones</span>
              <h4 class="noticia-title">Vivienda Multifamiliar</h4>
              <p class="noticia-desc">Desarrollo integral de proyectos de vivienda multifamiliar, desde la primera piedra hasta la entrega.</p>
              <a href="javascript:void(0)" class="noticia-link">Ver detalles <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
            </div>
          </article>
        </div>
"""

# Replace
content = re.sub(
    r'(<!-- Obra 3 -->.*?</article>\s*</div>)',
    r'\1\n\n' + new_slides,
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
