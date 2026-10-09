
document.addEventListener("DOMContentLoaded", function() {
    // Inject Header
    const headerContainer = document.getElementById('header-container');
    if (headerContainer) {
        fetch('header.html')
            .then(response => response.text())
            .then(data => {
                headerContainer.innerHTML = data;
                // Active link logic
                const currentPath = window.location.pathname.split('/').pop() || 'index.html';
                const links = headerContainer.querySelectorAll('nav a[data-path]');
                links.forEach(link => {
                    const linkPath = link.getAttribute('href');
                    if (linkPath.includes(currentPath) || (currentPath === 'index.html' && link.getAttribute('data-path') === 'inicio')) {
                        link.classList.add('text-primary', 'border-b', 'border-primary', 'font-semibold');
                        link.setAttribute('aria-current', 'page');
                    } else {
                        link.classList.remove('text-primary', 'border-b', 'border-primary', 'font-semibold');
                        link.removeAttribute('aria-current');
                    }
                });
            });
    }

    // Inject Footer
    const footerContainer = document.getElementById('footer-container');
    if (footerContainer) {
        fetch('footer.html')
            .then(response => response.text())
            .then(data => {
                footerContainer.innerHTML = data;
            });
    }
});
