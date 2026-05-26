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
});
