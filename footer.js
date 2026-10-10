const vgiFooterHTML = `
<footer class="w-full bg-surface-container-lowest border-t border-outline-variant/40 pt-16 pb-8 text-on-surface-variant relative">
    <div class="max-w-7xl mx-auto px-6">

        <!-- Fila 1: Marca + Certificaciones -->
        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-10 pb-12 border-b border-outline-variant/20">
            <div class="flex flex-col items-start max-w-md">
                <div class="flex items-center gap-4 mb-4">
                    <img alt="Logo VGI" class="w-14 h-14 object-cover drop-shadow-[0_0_12px_rgba(242,202,80,0.3)]" src="./WhatsApp%20Image%202026-07-09%20at%2010.41.46%20AM.png">
                    <div class="flex flex-col">
                        <span class="font-headline-sm text-primary tracking-wider uppercase leading-none font-bold text-lg md:text-xl drop-shadow-sm" style="text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">VAD GOD ING'S</span>
                        <span class="font-body-sm text-white tracking-widest uppercase mt-1 font-semibold text-[10px]">TRAINING <br> &amp; CONSTRUCTION</span>
                    </div>
                </div>
                <p class="font-body-sm text-body-sm text-secondary leading-relaxed">Ingeniería civil, construcción y consultoría técnica orientada a la excelencia. Soluciones integrales con los más altos estándares de calidad.</p>
            </div>
            <div class="flex flex-wrap items-center gap-3 lg:justify-end">
                <div class="bg-surface-container border border-outline-variant/30 p-2 rounded flex items-center justify-center hover:border-primary/50 transition-all shadow-sm h-20 w-20" title="ISO 9001:2015"><img src="./CERTIFICACIONES/ISO%209001.png" alt="ISO 9001" class="h-full w-full object-contain"></div>
                <div class="bg-surface-container border border-outline-variant/30 p-2 rounded flex items-center justify-center hover:border-primary/50 transition-all shadow-sm h-20 w-20" title="ISO 14001:2015"><img src="./CERTIFICACIONES/ISO%2014001.png" alt="ISO 14001" class="h-full w-full object-contain"></div>
                <div class="bg-surface-container border border-outline-variant/30 p-2 rounded flex items-center justify-center hover:border-primary/50 transition-all shadow-sm h-20 w-28" title="ISO 45001"><img src="./CERTIFICACIONES/ISO%2045001.png" alt="ISO 45001" class="h-full w-full object-contain"></div>
                <div class="bg-surface-container border border-outline-variant/30 p-2 rounded flex items-center justify-center hover:border-primary/50 transition-all shadow-sm h-20 w-20" title="ISO 37001:2016"><img src="./CERTIFICACIONES/ISO%2037001.png" alt="ISO 37001" class="h-full w-full object-contain"></div>
                <div class="bg-surface-container border border-outline-variant/30 p-2 rounded flex items-center justify-center hover:border-primary/50 transition-all shadow-sm h-20 w-28" title="ISO 27001"><img src="./CERTIFICACIONES/ISO%2027001.png" alt="ISO 27001" class="h-full w-full object-contain"></div>
                <div class="bg-surface-container border border-outline-variant/30 p-2 rounded flex items-center justify-center hover:border-primary/50 transition-all shadow-sm h-20 w-20" title="Colegio de Ingenieros del Perú"><img src="./CERTIFICACIONES/CIP.png" alt="CIP" class="h-full w-full object-contain"></div>
            </div>
        </div>

        <!-- Fila 2: Columnas de enlaces -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 py-12 border-b border-outline-variant/20">

            <div class="flex flex-col">
                <h3 class="font-label-caps text-label-caps text-primary uppercase tracking-widest mb-4 pb-2 border-b border-outline-variant/20">Servicios</h3>
                <ul class="flex flex-col gap-3 font-body-sm text-body-sm">
                    <li><a class="hover:text-primary transition-colors" href="planos.html">Ejecución de Proyectos Públicos y Privados</a></li>
                    <li><a class="hover:text-primary transition-colors" href="obras.html">Ejecución de Obras Públicas y Privadas</a></li>
                    <li><a class="hover:text-primary transition-colors" href="capacitaciones.html">Capacitaciones</a></li>
                </ul>
            </div>

            <div class="flex flex-col">
                <h3 class="font-label-caps text-label-caps text-primary uppercase tracking-widest mb-4 pb-2 border-b border-outline-variant/20">Empresa</h3>
                <ul class="flex flex-col gap-3 font-body-sm text-body-sm">
                    <li><a class="hover:text-primary transition-colors" href="obras.html">Obras</a></li>
                    <li><a class="hover:text-primary transition-colors" href="nosotros.html">Nosotros</a></li>
                    <li><a class="hover:text-primary transition-colors" href="nosotros.html">Historia Corporativa</a></li>
                    <li><a class="hover:text-primary transition-colors" href="nosotros.html">Equipo Técnico</a></li>
                </ul>
            </div>

            <div class="flex flex-col">
                <h3 class="font-label-caps text-label-caps text-primary uppercase tracking-widest mb-4 pb-2 border-b border-outline-variant/20">Formación Técnica</h3>
                <ul class="flex flex-col gap-3 font-body-sm text-body-sm">
                    <li><a class="hover:text-primary transition-colors" href="capacitaciones.html">Capacitaciones Especializadas</a></li>
                    <li><a class="hover:text-primary transition-colors" href="#">Certificaciones Profesionales</a></li>
                    <li><a class="hover:text-primary transition-colors" href="#">Inscripciones y Convocatorias</a></li>
                    <li><a class="hover:text-primary transition-colors inline-flex items-center gap-1.5 text-on-surface font-semibold" href="#"><span class="material-symbols-outlined text-sm text-primary">menu_book</span>Libro de Reclamaciones Virtual</a></li>
                </ul>
            </div>

            <div class="flex flex-col">
                <h3 class="font-label-caps text-label-caps text-primary uppercase tracking-widest mb-4 pb-2 border-b border-outline-variant/20">Contacto Directo</h3>
                <ul class="flex flex-col gap-3 font-body-sm text-body-sm text-secondary">
                    <li class="flex items-start gap-2.5"><span class="material-symbols-outlined text-primary text-base mt-0.5">mail</span><a class="hover:text-primary transition-colors break-all" href="mailto:vadgi22@gmail.com">vadgi22@gmail.com</a></li>
                    <li class="flex items-start gap-2.5"><span class="material-symbols-outlined text-primary text-base mt-0.5">call</span><a class="hover:text-primary transition-colors" href="tel:+51984515818">+51 984 515 818</a></li>
                    <li class="flex items-start gap-2.5"><span class="material-symbols-outlined text-primary text-base mt-0.5">schedule</span><span>Lun - Sáb 9:00 am - 6:00 pm</span></li>
                    <li class="flex items-start gap-2.5"><span class="material-symbols-outlined text-primary text-base mt-0.5">location_on</span><span>Sede Principal de Operaciones, Perú</span></li>
                </ul>
            </div>
        </div>

        <!-- Fila 3: Copyright + legales -->
        <div class="pt-8 flex flex-col md:flex-row items-center justify-between gap-4 font-headline-sm text-sm font-bold tracking-wider text-outline">
            <div class="flex flex-wrap items-center justify-center md:justify-start gap-2 text-center md:text-left">
                <span>© VADGOD INGS. Todos los derechos reservados.</span>
                <span class="text-outline/40">|</span>
                <span class="text-primary-fixed-dim">POWERED BY DYNASTRON</span>
            </div>
            <div class="flex flex-wrap items-center justify-center gap-x-8 gap-y-2">
                <a class="hover:text-on-surface transition-colors" href="#">Términos y Condiciones</a>
                <a class="hover:text-on-surface transition-colors" href="#">Políticas de Privacidad</a>
                <a class="hover:text-on-surface transition-colors" href="#">Uso de Cookies</a>
            </div>
        </div>
    </div>
</footer>
`;
document.write(vgiFooterHTML);
