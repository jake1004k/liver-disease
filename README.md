# Liver Disease Prediction Project on docker

This project aims to predict liver disease in patients based on various features related to their health. The dataset includes features such as age, gender, bilirubin levels, liver enzyme levels, and other blood parameters. The target variable indicates whether the patient has liver disease or not.

## Purpose of the Project

The purpose of this project is to develop a predictive model that can accurately classify patients as having liver disease or not based on their health parameters. This model can be used by healthcare professionals to identify at-risk patients early and provide appropriate interventions.

## Exploratory Data Analysis (EDA)

### Describe the Dataset and its Features

- Key parameters of numerical and categorical features.

### Data Visualization

- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis

### Numerical Summaries

- Mean, median, minimum, and maximum values of numerical features.
- Correlation matrix of numerical features.

## Data Preprocessing

- Replacing missing values in `Albumin_and_Globulin_Ratio` with the median.
- Encoding categorical values to numerical values.
- Processing duplicates in the dataset.

## Feature Engineering

- Train-test split of the dataset.
- Feature selection: Dropping constant features.
- Scaling the features.

## Model Evaluation

The following machine learning models were evaluated using different metrics:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Classifier (SVC)
- Gradient Boosting Classifier
- Artificial Neural Network (ANN)

### Model Performance

| Model                                    | F1-score | Accuracy | Precision | Recall | Confusion Matrix               |
|------------------------------------------|-----------|-----------|-----------|---------|---------------------------------|
| Logistic Regression without hyperparameter | 78.0     | 72.0      | 67.0      | 94.0   | [[72, 5], [35, 31]]             |
| Logistic Regression with hyperparameter   | 79.0     | 73.0      | 67.0      | 95.0   | [[72, 4], [35, 32]]             |
| Decision Tree using RandomizedSearchCV    | 80.0     | 70.0      | 79.0      | 80.0   | [[85, 21], [22, 15]]            |
| Random Forest using RandomizedSearchCV    | 82.0     | 73.0      | 80.0      | 83.0   | [[86, 18], [21, 18]]            |
| SVC using RandomizedSearchCV              | 71.0     | 66.0      | 57.0      | 95.0   | [[61, 3], [46, 33]]             |
| GradientBoostingClassifier using RandomizedSearchCV | 83.0 | 76.0 | 82.0 | 85.0 | [[88, 16], [19, 20]]             |
| ANN                                       | 83.0     | 73.0      | 89.0      | 78.0   | [[95, 27], [12, 9]]             |

## Local Deployment

This project has been implemented for local deployment using Flask. The application provides an interface where users can input medical parameters and receive predictions on whether they may have liver disease. The Flask application consists of the following components:

- `app.py`: The main Flask application file that handles the server and prediction logic.
- `index.html`: The front-end HTML file for user input.
- `result.html`: The front-end HTML file for the predicted page.
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


2. Install the required packages:
pip install -r requirements.txt

3.Run the Flask application:
python app.py

Open your web browser and go to http://127.0.0.1:81 to access the application.

### File Structure 

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the web interface.
- `templates/result.html`: The HTML file for styling the web interface.
- `requirements.txt`: The file listing the required Python packages.

### Usage

1. Open the application in your web browser.
2. Enter the medical parameters in the input fields.
3. Click the "Predict" button to get the model prediction.

## Docker Deployment in docker folder

This project can also be deployed using Docker. The Docker image is available with the tag `sanjay1004k/liver`. To deploy the project using Docker, follow these steps:

### Pull the Docker image:

```bash
docker pull sanjay1004k/liver

### Run the Docker container:

docker run -p 5000:5000 sanjay1004k/liver01

op:
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:81
 * Running on http://172.17.0.2:81

Open your web browser and go to http://127.0.0.1:81 to access the application.
