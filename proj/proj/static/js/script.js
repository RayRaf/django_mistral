// Установка начальной темы в зависимости от cookies или настроек операционной системы
function getCookie(name) {
    const value = "; " + document.cookie;
    const parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
}

let savedTheme = getCookie("theme");
let isDarkMode = savedTheme === "dark" || (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches && !savedTheme);
if (isDarkMode) {
    document.body.classList.add("dark-mode");
    document.getElementById("theme-toggle").innerHTML = '<i class="bi bi-brightness-high-fill"></i>';
} else {
    document.getElementById("theme-toggle").innerHTML = '<i class="bi bi-moon-fill"></i>';
}
updateBackground();

// Сохранение выбранной темы в cookies
document.getElementById("theme-toggle").addEventListener("click", function(e) {
    e.preventDefault();
    document.body.classList.toggle("dark-mode");
    if (document.body.classList.contains("dark-mode")) {
        document.getElementById("theme-toggle").innerHTML = '<i class="bi bi-brightness-high-fill"></i>';
        document.cookie = "theme=dark; path=/; max-age=31536000"; // Сохранить тему в cookies на год
        isDarkMode = true;
    } else {
        document.getElementById("theme-toggle").innerHTML = '<i class="bi bi-moon-fill"></i>';
        document.cookie = "theme=light; path=/; max-age=31536000"; // Сохранить тему в cookies на год
        isDarkMode = false;
    }
    updateBackground();
});

// Анимация абстрактного фона
const canvas = document.getElementById('animatedCanvas');
const ctx = canvas.getContext('2d');
let width = canvas.width = window.innerWidth;
let height = canvas.height = window.innerHeight;
let particles = [];
const particleCount = 150;

window.addEventListener('resize', function() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    particles = [];
    initParticles();
});

function updateBackground() {
    if (isDarkMode) {
        document.getElementById('background').style.background = 'black';
    } else {
        document.getElementById('background').style.background = 'white';
    }
}

function Particle() {
    this.x = Math.random() * width;
    this.y = Math.random() * height;
    this.vx = (Math.random() - 0.5) * 2;
    this.vy = (Math.random() - 0.5) * 2;
    this.size = Math.random() * 2 + 1;
    this.opacity = Math.random();
}

Particle.prototype.update = function() {
    this.x += this.vx;
    this.y += this.vy;

    if (this.x < 0 || this.x > width) {
        this.vx = -this.vx;
    }
    if (this.y < 0 || this.y > height) {
        this.vy = -this.vy;
    }
}

Particle.prototype.draw = function() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fillStyle = isDarkMode ? `rgba(255, 255, 255, ${this.opacity})` : `rgba(0, 0, 0, ${this.opacity})`;
    ctx.fill();
}

function initParticles() {
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }
}

function animate() {
    ctx.clearRect(0, 0, width, height);
    for (let i = 0; i < particles.length; i++) {
        particles[i].update();
        particles[i].draw();
    }
    requestAnimationFrame(animate);
}

initParticles();
animate();
