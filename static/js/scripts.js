document.addEventListener("DOMContentLoaded", function() {

    const hamburger = document.querySelector(".hamburger");
    const nav = document.querySelector("nav");

    if (hamburger && nav) {
        hamburger.addEventListener("click", function() {
            nav.classList.toggle("active-nav");
        });
    }

    const links = document.querySelectorAll("nav a");

    links.forEach(link => {
        link.addEventListener("click", () => {
            nav.classList.remove("active-nav");
        });
    });

});