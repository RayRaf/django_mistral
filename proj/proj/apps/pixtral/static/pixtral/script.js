function analyzeImage() {
    const formData = new FormData();
    const imageFile = document.getElementById('image').files[0];
    if (!imageFile) {
        document.getElementById('result').innerText = 'Please select an image or PDF file.';
        return;
    }
    formData.append('image', imageFile);

    // Добавляем скрытое поле prompt в formData
    const prompt = document.getElementById('prompt').value;
    formData.append('prompt', prompt);

    document.getElementById('result').innerText = 'Анализ документа...';

    fetch('/pixtral/analyze_image/', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                throw new Error(data.error || 'Network response was not ok');
            });
        }
        return response.json();
    })
    .then(data => {
        if (data.result) {
            document.getElementById('result').innerText = data.result;
        } else {
            document.getElementById('result').innerText = 'Error: ' + (data.error || 'Unknown error');
        }
    })
    .catch(error => {
        document.getElementById('result').innerText = 'Error: ' + error;
    });
}

