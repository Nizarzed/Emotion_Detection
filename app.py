from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model('best_model.h5')

# Class names for predictions
CLASS_NAMES = ["angry", "happy", "sad"]

# Prediction function
def predict_emotion(image):
    image = Image.open(BytesIO(image))
    
    # Convert the image to grayscale
    image = image.convert('RGB')
    image = tf.image.rgb_to_grayscale(image)
    
    image = image.resize((256, 256))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.expand_dims(image, 0)
    prediction = model.predict(image)
    predicted_class = CLASS_NAMES[tf.argmax(prediction, axis=-1)[0]]
    return predicted_class

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' in request.files:
        # Get the uploaded image from the form
        uploaded_image = request.files['image'].read()
        
        # Perform prediction
        predicted_class = predict_emotion(uploaded_image)
        
        return jsonify({'prediction': predicted_class})

    return jsonify({'error': 'No image provided for prediction'})

if __name__ == '__main__':
    app.run(debug=True)



