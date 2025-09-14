# Diabetes Risk Predictor 🩺

A machine learning-powered web application that predicts diabetes risk based on health parameters. Built with Flask and scikit-learn, featuring a modern, responsive user interface.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

- **Machine Learning Prediction**: Uses trained ML model to assess diabetes risk
- **Interactive Web Interface**: Modern, responsive design with real-time validation
- **Risk Factor Analysis**: Identifies and highlights specific risk factors
- **Confidence Scoring**: Provides prediction confidence and probability scores
- **Mobile Responsive**: Works seamlessly across all device sizes
- **Production Ready**: Configured for deployment with Gunicorn

## Demo

The application provides:
- ✅ Real-time form validation
- 🔮 ML-powered risk prediction
- 📊 Detailed probability analysis
- ⚠️ Risk factor identification
- 📱 Mobile-friendly interface

## Technology Stack

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, NumPy
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Deployment**: Gunicorn (WSGI server), Render
- **Model**: Support Vector Machine (SVM) / Random Forest

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Anandxz/diabetes-risk-predictor.git
cd diabetes-risk-predictor
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv diabetes_env

# Activate virtual environment
# On Windows:
diabetes_env\Scripts\activate
# On macOS/Linux:
source diabetes_env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirement.txt
```

### 4. Add Required Model Files

⚠️ **Important**: You need to add the trained model files to run the application:

1. `diabetes_model.pkl` - The trained machine learning model
2. `scaler.pkl` - The feature scaler used during training

Place these files in the root directory of the project.

## Usage

### Development Mode

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Production Mode

```bash
gunicorn app:app
```

Or specify host and port:

```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

## Input Parameters

The application requires the following health parameters:

| Parameter | Description | Range | Unit |
|-----------|-------------|--------|------|
| **Pregnancies** | Number of pregnancies | 0-20 | Count |
| **Glucose** | Fasting blood glucose level | 0-300 | mg/dL |
| **Blood Pressure** | Diastolic blood pressure | 0-200 | mmHg |
| **Skin Thickness** | Triceps skin fold thickness | 0-100 | mm |
| **Insulin** | 2-Hour serum insulin | 0-1000 | μU/mL |
| **BMI** | Body Mass Index | 10-70 | kg/m² |
| **Diabetes Pedigree** | Family history factor | 0-3 | Function |
| **Age** | Age in years | 18-120 | Years |

## API Endpoints

### GET /
- **Description**: Serves the main application interface
- **Returns**: HTML page

### POST /predict
- **Description**: Makes diabetes risk prediction
- **Content-Type**: application/json
- **Request Body**:
```json
{
    "pregnancies": 1,
    "glucose": 120,
    "bloodPressure": 80,
    "skinThickness": 25,
    "insulin": 100,
    "bmi": 25.5,
    "diabetesPedigree": 0.5,
    "age": 30
}
```
- **Response**:
```json
{
    "success": true,
    "prediction": 0,
    "confidence": 0.85,
    "probabilities": {
        "no_diabetes": 0.85,
        "diabetes": 0.15
    },
    "risk_factors": ["⚠️ Elevated glucose level (100-125 mg/dL)"]
}
```

## Project Structure

```
diabetes-risk-predictor/
├── app.py                 # Main Flask application
├── Procfile              # Heroku deployment configuration
├── requirement.txt       # Python dependencies
├── diabetes_model.pkl    # Trained ML model (add this)
├── scaler.pkl           # Feature scaler (add this)
├── templates/
│   └── index.html       # Main web interface
└── README.md           # Project documentation
```


```

## Deployment


### Docker Deployment

Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

## Risk Factor Analysis

The application automatically identifies risk factors:

- 🚨 **High Risk**: Glucose ≥126 mg/dL, BMI ≥30
- ⚠️ **Medium Risk**: Glucose 100-125 mg/dL, BMI 25-29.9, Age ≥45
- 📊 **Monitoring**: Family history, multiple pregnancies, high BP

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create Pull Request

## Medical Disclaimer

⚠️ **Important**: This application is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical decisions.


## Support

For support and questions:
- Open an issue on GitHub
- Contact: [dubeyanand00000@gmail.com]

## Acknowledgments

- Pima Indian Diabetes Dataset
- scikit-learn community
- Flask framework developers

---

**Made with ❤️ by Anand Prakash Dubey**
