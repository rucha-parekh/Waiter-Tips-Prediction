from flask import Flask, render_template, request
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the pickle file containing the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get form values
    form_data = request.form
    
    # Extract and convert features to numerical format
    total_bill = float(form_data['total_bill'])
    sex = 1 if form_data['sex'] == 'Male' else 0
    smoker = 1 if form_data['smoker'] == 'yes' else 0
    time = 1 if form_data['time'] == 'dinner' else 0
    size = int(form_data['size'])
    day = form_data['day']
    day_map = {'thur': 0, 'fri': 1, 'sat': 2, 'sun': 3}
    day_value = day_map.get(day, -1) 
    # Combine features into a NumPy array
    features = np.array([[total_bill, sex, smoker, time, size, day_value]])
    
    try:
        # Predict using the loaded model
        prediction = model.predict(features)
        predicted_tip = prediction[0]  # Extract the tip value
    except Exception as e:
        predicted_tip = "Error: Could not predict"
        print(f"Prediction error: {e}")
    
    return render_template("home.html", prediction_text=f"The predicted tip is ${predicted_tip:.2f}")

if __name__ == "__main__":
    app.run(debug=True)
