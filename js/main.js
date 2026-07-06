/**
 * Instituto Bíblico Mediterráneo - Main JS
 * Archivo preparado para animaciones interactivas al hacer scroll.
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log("Sistema inicializado: Animaciones de Scroll listas.");
    
    // ==========================================
    // 1. SCROLL ANIMATIONS (Intersection Observer)
    // ==========================================
    
    // Seleccionamos todos los elementos con la clase 'scroll-animate'
    const animatedElements = document.querySelectorAll('.scroll-animate');
    
    // Configuramos el observador
    const observerOptions = {
        root: null, // usa el viewport del navegador
        rootMargin: '0px 0px -50px 0px',
        threshold: 0 // Se activa apenas 1 píxel es visible, asegurando que dispare siempre en mobile
    };
    
    const scrollObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Añade la clase 'show' que dispara la animación CSS
                entry.target.classList.add('show');
                // Dejamos de observar una vez que ya apareció
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Aplicamos el observador a cada elemento
    animatedElements.forEach(el => {
        scrollObserver.observe(el);
    });

    // Efectos de scroll removidos a pedido de mantener el header estático.

    // ==========================================
    // 3. MENÚ MÓVIL (HAMBURGUESA)
    // ==========================================
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const mainNav = document.querySelector('.main-nav');
    
    if(menuBtn) {
        menuBtn.addEventListener('click', () => {
            mainNav.classList.toggle('active');
        });
    }

    // ==========================================
    // 4. NAVEGACIÓN CON TRANSICIÓN DE PÁGINA
    // ==========================================
    const transitionOverlay = document.getElementById('page-transition');

    function navigateTo(targetId) {
        const targetElement = document.querySelector(targetId);
        if (!targetElement || !transitionOverlay) return;

        // Cierra el menú móvil si está abierto
        if (mainNav && mainNav.classList.contains('active')) {
            mainNav.classList.remove('active');
        }

        // 1. Fade IN del overlay (cubre la pantalla)
        transitionOverlay.classList.add('fade-in');

        setTimeout(() => {
            // 2. Scroll instantáneo a la sección destino
            const headerHeight = 80;
            const offsetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
            window.scrollTo({ top: offsetPosition, behavior: 'instant' });

            // 3. Fade OUT del overlay (revela la nueva sección)
            setTimeout(() => {
                transitionOverlay.classList.remove('fade-in');
            }, 60);
        }, 340);
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (!targetId || targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (!targetElement) return;

            e.preventDefault();
            navigateTo(targetId);
        });
    });
});
