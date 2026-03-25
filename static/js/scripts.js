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

    // CALENDAR JS

    (function() {
    const monthYear = document.getElementById("month-year");
    const calendarDays = document.getElementById("calendar-days");
    const prevBtn = document.getElementById("prev");
    const nextBtn = document.getElementById("next");

    const dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    let currentDate = new Date();

    // Render the calendar
    function renderCalendar(date) {
        calendarDays.innerHTML = "";

        const year = date.getFullYear();
        const month = date.getMonth();

        // Display month and year
        monthYear.textContent = date.toLocaleString("default", { month: "long", year: "numeric" });

        // Add day names
        dayNames.forEach(day => {
            const dayElem = document.createElement("div");
            dayElem.textContent = day;
            dayElem.classList.add("day-name");
            calendarDays.appendChild(dayElem);
        });

        // First day of the month
        const firstDay = new Date(year, month, 1).getDay();
        // Number of days in the month
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        // Fill empty slots before first day
        for (let i = 0; i < firstDay; i++) {
            const empty = document.createElement("div");
            calendarDays.appendChild(empty);
        }

        // Fill days
        for (let day = 1; day <= daysInMonth; day++) {
            const dayElem = document.createElement("div");
            dayElem.textContent = day;
            dayElem.classList.add("day");

            // Highlight today
            const today = new Date();
            if (day === today.getDate() && month === today.getMonth() && year === today.getFullYear()) {
                dayElem.classList.add("today");
            }

            calendarDays.appendChild(dayElem);
        }
    }

    // Event listeners for navigation
    prevBtn.addEventListener("click", () => {
        currentDate.setMonth(currentDate.getMonth() - 1);
        renderCalendar(currentDate);
    });

    nextBtn.addEventListener("click", () => {
        currentDate.setMonth(currentDate.getMonth() + 1);
        renderCalendar(currentDate);
    });

    // Initial render
    renderCalendar(currentDate);
})();

});