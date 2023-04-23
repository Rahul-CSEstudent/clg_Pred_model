import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("university_recommendations.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("login.html")

@flask_app.route("/clg_details")
def clg_details():
    return render_template("clg_details.html")

@flask_app.route("/clg_predict")
def clg_predict():
    return render_template("index.html")

@flask_app.route("/clg_india")
def clg_india():
    return render_template("clg_ped_ind.html")

@flask_app.route("/clg_predict_india")
def clg_predict_india():
    return render_template("index_india.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text = "The Chance of Admission in MIT is 90% , Illinois Institute of Technology is 89% and AVIT is 85%")

if __name__ == "__main__":
    flask_app.run(debug=True)