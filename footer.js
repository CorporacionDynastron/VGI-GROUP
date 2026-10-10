const vgiFooterHTML = `
<footer
        class="w-full bg-surface-container-lowest border-t border-outline-variant/40 pt-space-2xl pb-space-lg text-on-surface-variant relative">
        <div class="max-w-7xl mx-auto px-gutter">
            <div
                class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-gutter-lg pb-space-2xl border-b border-outline-variant/20">
                <div class="lg:col-span-4 flex flex-col items-start">
                    <div class="flex items-center gap-space-md mb-space-md"><img alt="Logo VGI"
                            class="w-14 h-14 object-cover drop-shadow-[0_0_12px_rgba(242,202,80,0.3)]"
                            src="./WhatsApp%20Image%202026-07-09%20at%2010.41.46%20AM.png">
                        <div class="flex flex-col"><span class="font-headline-sm text-headline-md md:text-headline-lg text-primary tracking-wider uppercase leading-none font-bold text-lg md:text-xl drop-shadow-sm" style="text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">VAD GOD ING'S</span><span class="font-body-sm text-body-sm text-white tracking-widest uppercase mt-1 font-semibold text-[10px]">TRAINING <br> & CONSTRUCTION</span></div>
                    </div>
                    <p class="font-body-sm text-body-sm text-secondary leading-relaxed mb-space-lg max-w-sm">Ingeniería
                        civil, construcción y consultoría técnica orientada a la excelencia. Soluciones integrales con
                        los más altos estándares de calidad.</p>
                    <div class="flex flex-wrap gap-2 font-headline-sm text-sm font-bold tracking-wider text-primary">
                        <div class="flex items-center gap-2 flex-wrap">
                            <div class="bg-surface-container border border-outline-variant/30 p-2 flex items-center justify-center hover:border-primary/50 transition-all shadow-sm" title="ISO 9001:2015">
                                <div class="bg-white p-1 rounded flex items-center justify-center h-16 w-20">
                                    <img src="./CERTIFICACIONES/ISO%209001.png" alt="ISO 9001" class="h-full w-full object-contain">
                                </div>
                            </div>
                            <div class="bg-surface-container border border-outline-variant/30 p-2 flex items-center justify-center hover:border-primary/50 transition-all shadow-sm" title="ISO 14001:2015">
                                <div class="bg-white p-1 rounded flex items-center justify-center h-16 w-20">
                                    <img src="./CERTIFICACIONES/ISO%2014001.png" alt="ISO 14001" class="h-full w-full object-contain">
                                </div>
                            </div>
                            <div class="bg-surface-container border border-outline-variant/30 p-2 flex items-center justify-center hover:border-primary/50 transition-all shadow-sm" title="ISO 45001">
                                <div class="bg-white p-1 rounded flex items-center justify-center h-16 w-28">
                                    <img src="./CERTIFICACIONES/ISO%2045001.png" alt="ISO 45001" class="h-full w-full object-contain">
                                </div>
                            </div>
                            <div class="bg-surface-container border border-outline-variant/30 p-2 flex items-center justify-center hover:border-primary/50 transition-all shadow-sm" title="ISO 37001:2016">
                                <div class="bg-white p-1 rounded flex items-center justify-center h-16 w-20">
                                    <img src="./CERTIFICACIONES/ISO%2037001.png" alt="ISO 37001" class="h-full w-full object-contain">
                                </div>
                            </div>
                            <div class="bg-surface-container border border-outline-variant/30 p-2 flex items-center justify-center hover:border-primary/50 transition-all shadow-sm" title="ISO 27001">
                                <div class="bg-white p-1 rounded flex items-center justify-center h-16 w-28">
                                    <img src="./CERTIFICACIONES/ISO%2027001.png" alt="ISO 27001" class="h-full w-full object-contain">
                                </div>
                            </div>
                            <div class="bg-surface-container border border-outline-variant/30 p-2 flex items-center justify-center hover:border-primary/50 transition-all shadow-sm" title="Colegio de Ingenieros del Perú">
                                <div class="bg-white p-1 rounded flex items-center justify-center h-16 w-20">
                                    <img src="./CERTIFICACIONES/CIP.png" alt="CIP" class="h-full w-full object-contain">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="lg:col-span-2 flex flex-col">
                    <h3
                        class="font-label-caps text-label-caps text-primary uppercase tracking-widest mb-space-md pb-2 border-b border-outline-variant/20">
                        Empresa</h3>
                    <ul class="flex flex-col gap-2 font-body-sm text-body-sm">
                        <li class=""><div class="relative group">
                      <a class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-on-surface-variant hover:text-on-surface" data-path="servicios" href="index.html#servicios">SERVICIOS <span class="material-symbols-outlined text-sm">expand_more</span></a>
                      <div class="absolute left-0 top-full mt-0 hidden group-hover:flex flex-col bg-surface-container-high shadow-2xl border border-outline-variant/30 min-w-[320px] z-50">
                          <a href="planos.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">EJECUCION DE PROYECTOS PUBLICOS Y PRIVADOS</a>
                          <a href="obras.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">EJECUCION DE OBRAS PUBLICAS Y PRIVADAS</a>
                          <a href="capacitaciones.html" class="px-5 py-3 hover:bg-surface-container-highest hover:text-primary transition-colors text-[13px] font-headline-sm uppercase tracking-wider border-b border-outline-variant/10 flex items-center gap-2">CAPACITACIONES</a>
                      </div>
                  </div></li>
                        <li class=""><a class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-on-surface-variant hover:text-on-surface" data-path="obras"
                                href="#">Obras</a></li>
                        <li class=""><a class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-on-surface-variant hover:text-on-surface" data-path="nosotros"
                                href="nosotros.html">Nosotros</a></li>
                        <li class=""><a class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-on-surface-variant hover:text-on-surface" data-path="nosotros"
                                href="nosotros.html">Historia Corporativa</a></li>
                        <li class=""><a class="font-body-sm text-body-sm tracking-wide uppercase py-2 transition-colors flex items-center gap-1 cursor-pointer text-on-surface-variant hover:text-on-surface" data-path="nosotros"
                                href="nosotros.html">Equipo Técnico</a></li>
                    </ul>
                </div>
                <div class="lg:col-span-3 flex flex-col">
                    <h3
                        class="font-label-caps text-label-caps text-primary uppercase tracking-widest mb-space-md pb-2 border-b border-outline-variant/20">
                        Formación Técnica</h3>
                    <ul class="flex flex-col gap-2 font-body-sm text-body-sm">
                        <li class=""><a class="hover:text-primary transition-colors" data-path="formacion-tecnica"
                                href="capacitaciones.html">Capacitaciones Especializadas</a></li>
                        <li class=""><a class="hover:text-primary transition-colors" data-path="formacion-tecnica"
                                href="#">Certificaciones Profesionales</a></li>
                        <li class=""><a class="hover:text-primary transition-colors" data-path="formacion-tecnica"
                                href="#">Inscripciones y Convocatorias</a></li>
                        <li class=""><a
                                class="hover:text-primary transition-colors flex items-center gap-1.5 mt-2 text-on-surface"
                                data-path="libro-de-reclamaciones" href="#"><span
                                    class="material-symbols-outlined text-sm text-primary">menu_book</span>Libro de
                                Reclamaciones Virtual</a></li>
                    </ul>
                </div>
                <div class="lg:col-span-3 flex flex-col">
                    <h3
                        class="font-label-caps text-label-caps text-primary uppercase tracking-widest mb-space-md pb-2 border-b border-outline-variant/20">
                        Contacto Directo</h3>
                    <div class="flex flex-col gap-3 font-body-sm text-body-sm text-secondary">
                        <div class="flex items-start gap-2.5"><span
                                class="material-symbols-outlined text-primary text-base mt-0.5">mail</span><a
                                class="hover:text-primary transition-colors"
                                href="mailto:vadgi22@gmail.com">vadgi22@gmail.com</a></div>
                        <div class="flex items-start gap-2.5"><span
                                class="material-symbols-outlined text-primary text-base mt-0.5">call</span><a
                                class="hover:text-primary transition-colors" href="tel:+51984515818">+51 984 515 818</a>
                        </div>
                        <div class="flex items-start gap-2.5"><span
                                class="material-symbols-outlined text-primary text-base mt-0.5">schedule</span><span
                                class="">Lun - Sáb 9:00 am - 6:00 pm</span></div>
                        <div class="flex items-start gap-2.5"><span
                                class="material-symbols-outlined text-primary text-base mt-0.5">location_on</span><span
                                class="">Sede Principal de Operaciones, Perú</span></div>
                    </div>
                </div>
            </div>
            <div
                class="pt-space-lg flex flex-col md:flex-row items-center justify-between gap-space-md font-headline-sm text-sm font-bold tracking-wider text-outline">
                <div class="flex items-center gap-2 text-center md:text-left"><span class="">© VADGOD INGS. Todos los
                        derechos reservados.</span><span class="text-outline/40">|</span><span
                        class="text-primary-fixed-dim">POWERED BY DYNASTRON</span></div>
                <div class="flex items-center gap-space-lg"><a class="hover:text-on-surface transition-colors"
                        data-path="terminos-y-condiciones" href="#">Términos y Condiciones</a><a
                        class="hover:text-on-surface transition-colors" data-path="politicas-de-privacidad"
                        href="#">Políticas de Privacidad</a><a class="hover:text-on-surface transition-colors"
                        data-path="uso-de-cookies" href="#">Uso de Cookies</a></div>
            </div>
        </div>
    </footer>
`;
document.write(vgiFooterHTML);
