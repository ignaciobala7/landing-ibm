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
        rootMargin: '0px',
        threshold: 0.15 // Se activa cuando el 15% del elemento es visible
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
    // 4. SMOOTH SCROLL PARA BOTONES (Transición suave)
    // ==========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if(targetId === '#') return; // Ignorar si es solo #
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                
                // Si el menú móvil está abierto, lo cerramos
                if(mainNav && mainNav.classList.contains('active')) {
                    mainNav.classList.remove('active');
                }
                
                // Calculamos la posición considerando el alto del menú fijo
                const headerHeight = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerHeight;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });
            }
        });
    });
});
