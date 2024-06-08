# Liver Disease Prediction

## Introduction

The liver, the largest organ in the human body, plays a crucial role in various essential functions such as digestion, energy storage, and detoxification. Any malfunctioning of the liver can lead to severe health complications and diseases. This project aims to leverage machine learning techniques to identify patients with liver disease early, thereby reducing the burden on healthcare professionals and improving patient outcomes.

## Causes of Liver Malfunction

Liver malfunction can be caused by several factors, including:
- Viral infections (e.g., hepatitis)
- Excessive alcohol consumption
- Exposure to harmful gases
- Consumption of contaminated or stale food, including pickles
- Inherited diseases

## Increasing Incidence of Liver Disease

The incidence of liver disease is on the rise globally, making it imperative to develop efficient and accurate methods for early detection. Early identification of liver disease can lead to timely intervention and better management of the condition.

## Role of Machine Learning

Machine learning (ML) can assist in the early identification of liver disease by evaluating vital parameters such as liver enzymes, bilirubin levels, and other biomarkers. This approach aims to provide a more efficient and accurate means of identifying at-risk patients, thereby aiding healthcare professionals in their diagnostic processes.

## Project Overview

### Dataset

The dataset used in this project contains medical data related to liver functions. It includes several vital parameters and biomarkers that are essential for diagnosing liver disease. The dataset, however, is small, contains many outliers, and has a few missing values, which posed challenges during the modeling phase.

### Models Used

Based on performance metrics comparison and evaluation, the following models were identified as the best performers:
1. Gradient Boosting
2. Artificial Neural Network (ANN)
3. Decision Tree
4. Random Forest

### Local Deployment

This project has been implemented for local deployment using Flask. The application provides an interface where users can input medical parameters and receive predictions on whether they may have liver disease. The Flask application consists of the following components:
- `app.py`: The main Flask application file that handles the server and prediction logic.
- `index.html`: The front-end HTML file for user input.
- `result.html`: The front-end HTML file for predicted page.
- `requirements.txt`: The file listing the required Python packages for the project.

### Prerequisites

- Python 3.x
- Flask
- NumPy
- Pandas
- scikit-learn

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/liver-disease-prediction.git
    cd liver-disease-prediction
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

4. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

### File Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the web interface.
- `templates/result.html`: The HTML file for styling the web interface.
- `requirements.txt`: The file listing the required Python packages.

## Usage

1. Open the application in your web browser.
2. Enter the medical parameters in the input fields.
3. Click the "Predict" button to get the model's prediction.
