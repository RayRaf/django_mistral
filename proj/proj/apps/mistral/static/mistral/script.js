

// Функция для отправки формы и отображения ответа
async function submitPromptForm(e) {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);

    document.getElementById("loading").style.display = 'block';
    const response = await fetch(form.action, {
        method: form.method,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        },
        body: formData
    });
    document.getElementById("loading").style.display = 'none';

    const json = await response.json();
    document.getElementById("response").innerHTML = marked.parse(json.response);
    document.getElementById("download-button").style.display = 'block';
}

// Обработчик отправки формы
document.getElementById("prompt-form").onsubmit = submitPromptForm;

// Обработчик нажатия клавиши Enter для отправки формы
document.getElementById("prompt-form").addEventListener("keydown", function(e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        document.querySelector("button[type='submit']").click();
    }
});
