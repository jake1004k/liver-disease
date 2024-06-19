
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle



app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
scaler= pickle.load(open('StandardScaler.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    final_features_scaled=scaler.transform(final_features)
    prediction = model.predict(final_features_scaled)

    if prediction[0] == 1:
        prediction_text = "You may have liver disease."
        
        background_image="/static/negative_bg.jpg"
    else:
        prediction_text = "You may not have liver disease."
        background_image="/static/positive_bg.jpg"

    return render_template('result.html', 
                           prediction_text=prediction_text,
                           background_image=background_image)

if __name__ == "__main__":
    app.run(debug=True)
