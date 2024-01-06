document.addEventListener('DOMContentLoaded', function () {
    const fileUpload = document.getElementById('file-upload');
    const predictButton = document.getElementById('predict-button');
    const selectedImage = document.getElementById('selected-image');
    const predictionMessage = document.getElementById('prediction-message');

    // Event listener for file input change
    fileUpload.addEventListener('change', function () {
        if (fileUpload.files.length > 0) {
            selectedImage.src = URL.createObjectURL(fileUpload.files[0]);
        }
    });

    // Event listener for predict button click
    predictButton.addEventListener('click', function () {
        // Ensure a file is selected
        if (fileUpload.files.length > 0) {
            const formData = new FormData();
            formData.append('image', fileUpload.files[0]);

            // Perform prediction
            fetch('/predict', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Display the prediction message
                predictionMessage.textContent = 'Prediction: ' + data.prediction;
            })
            .catch(error => {
                console.error('Error:', error);
                // Log any errors related to setting the image source
            });
        } else {
            alert('Veuillez choisir un fichier avant de prédire.');
        }
    });
});
