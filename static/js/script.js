// Fade animation on cards

const cards = document.querySelectorAll(".model-card,.stat-card");

const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.style.opacity = "1";

            entry.target.style.transform = "translateY(0)";

        }

    });

});

cards.forEach(card => {

    card.style.opacity = "0";

    card.style.transform = "translateY(40px)";

    card.style.transition = ".6s";

    observer.observe(card);

});

// Hero icon rotation

const hero = document.querySelector(".hero-icon");

setInterval(() => {

    hero.style.transform = "rotate(360deg)";

    setTimeout(() => {

        hero.style.transform = "rotate(0deg)";

    }, 1000);

}, 5000);


// Hover Tilt Effect

document.querySelectorAll(".model-card").forEach(card => {

    card.addEventListener("mousemove", (e) => {

        const rect = card.getBoundingClientRect();

        const x = e.clientX - rect.left;

        const y = e.clientY - rect.top;

        const rotateY = ((x - rect.width / 2) / 12);

        const rotateX = ((rect.height / 2 - y) / 12);

        card.style.transform =
            `perspective(900px)
        rotateX(${rotateX}deg)
        rotateY(${rotateY}deg)
        translateY(-8px)`;

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = "perspective(900px) rotateX(0) rotateY(0)";

    });

});