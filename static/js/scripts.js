document.addEventListener("DOMContentLoaded", function() {

    const adminMenu = document.querySelector(".admin-menu");

    if (adminMenu) {
        adminMenu.addEventListener("click", function() {
            document.querySelector(".dropdown").classList.toggle("active");
        });
    }

});