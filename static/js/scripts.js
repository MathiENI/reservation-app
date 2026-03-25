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

        const monthYear = document.getElementById("month-year");
    const calendarDays = document.getElementById("calendar-days");
    const prevBtn = document.getElementById("prev");
    const nextBtn = document.getElementById("next");

    const reservationsData = JSON.parse(
        document.getElementById("reservations-data").textContent
    );

    let currentDate = new Date();

    function renderCalendar(date) {
        calendarDays.innerHTML = "";

        const year = date.getFullYear();
        const month = date.getMonth();

        monthYear.textContent = date.toLocaleString("fr-FR", {
            month: "long",
            year: "numeric"
        });

        const dayNames = ["L", "M", "M", "J", "V", "S", "D"];

        dayNames.forEach(day => {
            const el = document.createElement("div");
            el.textContent = day;
            el.classList.add("day-name");
            calendarDays.appendChild(el);
        });

        const firstDay = new Date(year, month, 1).getDay();
        const adjustedFirstDay = (firstDay === 0 ? 6 : firstDay - 1);

        const daysInMonth = new Date(year, month + 1, 0).getDate();

        for (let i = 0; i < adjustedFirstDay; i++) {
            calendarDays.appendChild(document.createElement("div"));
        }

        for (let day = 1; day <= daysInMonth; day++) {
            const dayElem = document.createElement("div");
            dayElem.textContent = day;
            dayElem.classList.add("day");

            const fullDate = new Date(year, month, day);

            // 🎯 highlight today
            const today = new Date();
            if (
                day === today.getDate() &&
                month === today.getMonth() &&
                year === today.getFullYear()
            ) {
                dayElem.classList.add("today");
            }

            // 🔥 click event
            dayElem.addEventListener("click", function () {
                showReservationsForDate(fullDate);
            });

            calendarDays.appendChild(dayElem);
        }
    }

    function showReservationsForDate(date) {
        const selectedDate = date.toISOString().split("T")[0];

        const filtered = reservationsData.filter(r =>
            r.start_datetime.startsWith(selectedDate)
        );

        displayReservations(filtered, selectedDate);
    }

    function displayReservations(reservations, date) {
        let container = document.getElementById("reservation-list");

        ul = document.createElement("ul");
        ul.classList = "card-section";
        li = document.createElement("li");
        li.classList = "card";

        container.appendChild(ul);
        ul.appendChild(li);

        li.innerHTML = `<h3>Réservations du ${date}</h3>`;

        if (reservations.length === 0) {
            li.innerHTML += "<p>Aucune réservation</p>";
            return;
        }

        reservations.forEach(r => {
            li.innerHTML += `
                <p>
                    📌 ${r.resource_name} <br>
                    ⏰ ${r.start_datetime.slice(11,16)} - ${r.end_datetime.slice(11,16)}
                </p>
            `;
        });
    }

    prevBtn.addEventListener("click", () => {
        currentDate.setMonth(currentDate.getMonth() - 1);
        renderCalendar(currentDate);
    });

    nextBtn.addEventListener("click", () => {
        currentDate.setMonth(currentDate.getMonth() + 1);
        renderCalendar(currentDate);
    });

    renderCalendar(currentDate);

});