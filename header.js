
const vgiHeaderHTML = `
<header
        class="relative z-50 w-full bg-surface/100 backdrop-blur-xl border-b border-outline-variant/30 shadow-none">
        <div class="py-2 max-w-7xl mx-auto px-gutter flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="relative flex items-center justify-center"><img alt="Logo VGI"
                        class="w-20 h-20 object-cover drop-shadow-[0_0_16px_rgba(242,202,80,0.35)]"
                        src="./WhatsApp%20Image%202026-07-09%20at%2010.41.46%20AM.png">
                    <div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 bg-primary"></div>
                </div>
                <div class="flex flex-col justify-center"><span class="font-headline-sm text-headline-md md:text-headline-lg text-primary tracking-wider uppercase leading-none font-bold text-lg md:text-xl drop-shadow-sm" style="text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">VAD GOD ING'S</span><span class="font-body-sm text-body-sm text-white tracking-widest uppercase mt-1 font-semibold text-[10px]">TRAINING <br> & CONSTRUCTION</span></div>
            </div>
            <nav class="hidden xl:flex items-center gap-space-lg h-full"
                data-active-classes="text-primary border-b border-primary font-semibold"><a aria-current="page"
                    class="tracking-wide uppercase py-2 transition-colors text-primary border-b border-primary font-semibold"
                    data-path="inicio" href="index.html">Inicio</a><div class="relative group">
                      <a class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-on-surface-variant hover:text-on-surface" data-path="servicios" href="index.html#servicios">SERVICIOS <span class="material-symbols-outlined text-sm">expand_more</span></a>
                      <div class="absolute left-0 top-full mt-0 hidden group-hover:flex flex-col bg-surface-container-high shadow-2xl border border-outline-variant/30 min-w-[320px] z-50">
                          <a href="planos.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">EJECUCION DE PROYECTOS PUBLICOS Y PRIVADOS</a>
                          <a href="ejecucion-obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">EJECUCION DE OBRAS PUBLICAS Y PRIVADAS</a>
                          <a href="capacitaciones.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">CAPACITACIONES</a>
                      </div>
                  </div><div class="relative group">
                      <a class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-on-surface-variant hover:text-on-surface" data-path="obras" href="obras.html">OBRAS <span class="material-symbols-outlined text-sm">expand_more</span></a>
                      <div class="absolute left-0 top-full mt-0 hidden group-hover:flex flex-col bg-surface-container-high shadow-2xl border border-outline-variant/30 min-w-[320px] z-50">
                          <a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS DE EDIFICACIONES Y AFINES</a>
                          <a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS VIALES, PUERTOS Y AFINES</a>
                          <a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS DE SANEAMIENTO Y AFINES</a>
                          <a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS ELECTROMECÁNICAS, ENERGÉTICAS, TELECOM. Y AFINES</a>
                          <a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">OBRAS DE REPRESAS, IRRIGACIONES Y AFINES</a>
                      </div>
                  </div><div class="relative group">
                      <a class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-on-surface-variant hover:text-on-surface" data-path="nosotros" href="nosotros.html">NOSOTROS <span class="material-symbols-outlined text-sm">expand_more</span></a>
                      <div class="absolute left-0 top-full mt-0 hidden group-hover:flex flex-col bg-surface-container-high shadow-2xl border border-outline-variant/30 min-w-[200px] z-50">
                          <a href="nosotros.html#historia" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-primary">history_edu</span> Nuestra historia</a>
                          <a href="nosotros.html#mision" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-primary">visibility</span> Misión y visión</a>
                          <a href="nosotros.html#equipo" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-sm font-label-caps uppercase tracking-wide flex items-center gap-2"><span class="material-symbols-outlined text-[16px] text-primary">groups</span> El equipo</a>
                      </div>
                  </div><a
                    class="font-body-sm text-body-sm text-on-surface-variant hover:text-on-surface tracking-wide uppercase py-2 transition-colors"
                    data-path="contacto" href="#contacto-tecnico">Contacto</a></nav>
            <div class="flex items-center gap-space-md"><a
                    class="inline-flex items-center justify-center bg-primary-container text-on-primary-container font-label-caps text-label-caps uppercase px-6 py-3.5 tracking-wider hover:bg-primary transition-all duration-200 shadow-[0_0_16px_rgba(212,175,55,0.25)] border-t border-primary"
                    data-path="contacto" href="#contacto-tecnico"><span
                        class="material-symbols-outlined text-sm mr-2">engineering</span>Solicitar cotización</a></div>
        </div>
    
    
    <div class="w-full bg-primary text-on-primary font-headline-sm text-center py-2 uppercase tracking-widest text-xs md:text-sm font-bold shadow-[0_4px_12px_rgba(0,0,0,0.3)] border-t border-primary/50">
        Impulsando el crecimiento con obras de alto impacto
    </div>

</header>
`;

document.write(vgiHeaderHTML);

// Script to set the active nav link based on the current URL
window.addEventListener('DOMContentLoaded', () => {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    let activeTarget = '';
    
    if (currentPath.includes('index.html') || currentPath === '') activeTarget = 'inicio';
    else if (currentPath.includes('obras.html')) activeTarget = 'obras';
    else if (currentPath.includes('nosotros.html')) activeTarget = 'nosotros';
    else if (currentPath.includes('planos.html') || currentPath.includes('capacitaciones.html') || currentPath.includes('ejecucion-obras.html')) activeTarget = 'servicios';
    
    if (activeTarget) {
        const links = document.querySelectorAll('header nav a');
        links.forEach(link => {
            if (link.getAttribute('data-path') === activeTarget) {
                // Remove inactive classes
                link.classList.remove('text-on-surface-variant', 'hover:text-on-surface');
                // Add active classes
                link.classList.add('text-primary', 'border-b', 'border-primary', 'font-semibold');
            } else {
                // Ensure inactive styling for the rest
                link.classList.remove('text-primary', 'border-b', 'border-primary', 'font-semibold');
                link.classList.add('text-on-surface-variant', 'hover:text-on-surface');
            }
        });
    }
});
