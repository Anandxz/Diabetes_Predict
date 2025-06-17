from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load model and scaler
try:
    model = joblib.load('diabetes_model.pkl')
    scaler = joblib.load('scaler.pkl')
    print("Model and scaler loaded successfully!")
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    model = None
    scaler = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if model is loaded
        if model is None or scaler is None:
            return jsonify({
                'success': False,
                'error': 'Model not loaded properly'
            }), 500
        
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data received'
            }), 400
        
        # Extract features in the correct order
        features = [
            data.get('pregnancies', 0),
            data.get('glucose', 0),
            data.get('bloodPressure', 0),
            data.get('skinThickness', 0),
            data.get('insulin', 0),
            data.get('bmi', 0),
            data.get('diabetesPedigree', 0),
            data.get('age', 0)
        ]
        
        # Validate input
        if any(f is None for f in features):
            return jsonify({
                'success': False,
                'error': 'Missing required fields'
            }), 400
        
        # Convert to numpy array and reshape
        input_array = np.asarray(features).reshape(1, -1)

        # Standardize and predict
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)
        probabilities = model.predict_proba(input_scaled)
        
        # Analyze risk factors
        risk_factors = analyze_risk_factors(data)
        
        # Get confidence (probability of predicted class)
        confidence = probabilities[0][prediction[0]]
        
        return jsonify({
            'success': True,
            'prediction': int(prediction[0]),
            'confidence': float(confidence),
            'probabilities': {
                'no_diabetes': float(probabilities[0][0]),
                'diabetes': float(probabilities[0][1])
            },
            'risk_factors': risk_factors
        })
        
    except Exception as e:
        print(f"Prediction error: {e}")
        return jsonify({
            'success': False,
            'error': f'Prediction failed: {str(e)}'
        }), 500

def analyze_risk_factors(data):
    """Analyze input data to identify risk factors"""
    factors = []
    
    glucose = data.get('glucose', 0)
    bmi = data.get('bmi', 0)
    age = data.get('age', 0)
    pregnancies = data.get('pregnancies', 0)
    blood_pressure = data.get('bloodPressure', 0)
    diabetes_pedigree = data.get('diabetesPedigree', 0)
    
    if glucose >= 126:
        factors.append("🚨 High glucose level (≥126 mg/dL)")
    elif glucose >= 100:
        factors.append("⚠️ Elevated glucose level (100-125 mg/dL)")
    
    if bmi >= 30:
        factors.append("🚨 Obesity (BMI ≥30)")
    elif bmi >= 25:
        factors.append("⚠️ Overweight (BMI 25-29.9)")
    
    if age >= 45:
        factors.append("⚠️ Age 45 or older")
    
    if pregnancies >= 4:
        factors.append("⚠️ Multiple pregnancies")
    
    if blood_pressure >= 90:
        factors.append("⚠️ High blood pressure")
    
    if diabetes_pedigree >= 0.5:
        factors.append("⚠️ Strong family history")
    
    return factors

if __name__ == '__main__':
    app.run(debug=True)
