document.addEventListener("DOMContentLoaded", function() {

    const adminMenu = document.querySelector(".admin-menu");

    if (adminMenu) {
        adminMenu.addEventListener("click", function() {
            document.querySelector(".dropdown").classList.toggle("active");
        });
    }

    // Toggle aside menu on mobile
    const hamburger = document.querySelector('.hamburger');
    const aside = document.querySelector('.aside');

    hamburger.addEventListener('click', () => {
      aside.classList.toggle('active');
    });

});