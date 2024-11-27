// Установка начальной темы в зависимости от cookies или настроек операционной системы
function getCookie(name) {
    const value = "; " + document.cookie;
    const parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
}

let savedTheme = getCookie("theme");
if (savedTheme === "dark" || (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches && !savedTheme)) {
    document.body.classList.add("dark-mode");
    document.getElementById("theme-toggle").innerText = "Дневной режим";
} else {
    document.getElementById("theme-toggle").innerText = "Ночной режим";
}

// Сохранение выбранной темы в cookies
document.getElementById("theme-toggle").addEventListener("click", function(e) {
    e.preventDefault();
    document.body.classList.toggle("dark-mode");
    if (document.body.classList.contains("dark-mode")) {
        document.getElementById("theme-toggle").innerText = "Дневной режим";
        document.cookie = "theme=dark; path=/; max-age=31536000"; // Сохранить тему в cookies на год
    } else {
        document.getElementById("theme-toggle").innerText = "Ночной режим";
        document.cookie = "theme=light; path=/; max-age=31536000"; // Сохранить тему в cookies на год
    }
});