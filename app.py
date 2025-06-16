from flask import Flask, render_template, request , jsonify
import pickle
import numpy as np
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load model and scaler
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input from form
    features = [float(x) for x in request.form.values()]
    input_array = np.asarray(features).reshape(1, -1)

    # Standardize and predict
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)
    prob = model.predict_proba(input_scaled)

    if prediction[0] == 0:
        result = f"✅ The person is NOT diabetic with {prob[0][0]:.2%} confidence."
    else:
        result = f"⚠️ The person is likely DIABETIC with {prob[0][1]:.2%} confidence."

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
