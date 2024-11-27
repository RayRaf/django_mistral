function analyzeImage() {
    const formData = new FormData();
    const imageFile = document.getElementById('image').files[0];
    formData.append('image', imageFile);

    document.getElementById('result').innerText = 'Анализ документа...';

    fetch('/pixtral/analyze_image/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
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