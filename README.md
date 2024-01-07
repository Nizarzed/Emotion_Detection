# Emotion Detection Model Repository

## Overview

This repository contains a web application for emotion detection using a machine learning model. The model is trained to classify human faces into three main emotions: angry, happy, and sad.

## Getting Started

To run the application locally, follow these steps:

1. Clone the repository to your local machine.
   
2. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```
   
3. Run the Flask web application.
   ```bash
   python app.py
   ```
   
4.Open your web browser and navigate to http://localhost:5000.

5.Upload an image of a human face to see the emotion prediction.

## Project Structure

**app.py**: Flask web application for serving the model and handling predictions.
**static/**: Static files including images and styles.
**image.jpg**: Placeholder image displayed on the web page.
**css/style.css**: Styles for the web page.
**js/script.js**: JavaScript code for handling user interactions.
**templates/**: HTML templates for the web pages.
**index.html**: Main page for the web application.

## Model
The machine learning model used for emotion detection is stored in the file **`best_model.h5`**. It has been trained on a dataset containing facial expressions of anger, happiness, and sadness. To see all the details of the training, check the **`model_training.ipynb`** notebook in the [model_training](model_training) directory.


## Contributors
Zerrad Nizar

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.








