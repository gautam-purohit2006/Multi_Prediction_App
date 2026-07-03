// Sidebar

const menu = document.getElementById("menu-btn");

const sidebar = document.querySelector(".sidebar");

menu.addEventListener("click", () => {

    sidebar.classList.toggle("show");

});

// Active Menu

const items = document.querySelectorAll(".sidebar li");

items.forEach(item => {

    item.addEventListener("click", () => {

        items.forEach(i => i.classList.remove("active"));

        item.classList.add("active");

    });

});

// Button Animation

const btn = document.querySelector(".predict-btn");

btn.addEventListener("click", function () {

    btn.innerHTML = "⏳ Predicting...";

    btn.disabled = true;

    setTimeout(() => {

        btn.innerHTML = "✔ Prediction Complete";

        btn.disabled = false;

    }, 2000);

});

// Input Animation

const inputs = document.querySelectorAll("input,select");

inputs.forEach(input => {

    input.addEventListener("focus", () => {

        input.style.transform = "scale(1.02)";

    });

    input.addEventListener("blur", () => {

        input.style.transform = "scale(1)";

    });

});

// Fade on Scroll

const cards = document.querySelectorAll(".prediction-card,.result-card");

const observer = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.style.opacity = 1;

            entry.target.style.transform = "translateY(0)";

        }

    });

});

cards.forEach(card => {

    card.style.opacity = 0;

    card.style.transform = "translateY(40px)";

    card.style.transition = ".6s";

    observer.observe(card);

});