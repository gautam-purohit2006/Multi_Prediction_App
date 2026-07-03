const menu = document.getElementById("menu-btn");

const sidebar = document.querySelector(".sidebar");

if (menu) {

    menu.onclick = () => {

        sidebar.classList.toggle("show");

    }

}

const btn = document.querySelector(".predict-btn");

if (btn) {

    btn.onclick = () => {

        btn.innerHTML = "⏳ Predicting...";

    }

}