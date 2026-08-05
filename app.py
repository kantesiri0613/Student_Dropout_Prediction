from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# load trained model
model = joblib.load("student_dropout_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form["age"])
    gender = request.form["gender"]
    attendance = float(request.form["attendance"])
    study_hours = float(request.form["study_hours"])
    scholarship = request.form["scholarship"]
    tuition = request.form["tuition"]
    parents_education = request.form["parents_education"]
    income = float(request.form["family_income"])
    exam_score = float(request.form["exam_score"])

    if age > 25 or age < 18:
        return "Age must be between 18 and 25"

    if attendance > 100 or attendance < 0:
        return "Attendance must be between 0 and 100"

    if study_hours > 10 or study_hours < 0:
        return "Study hours must be between 0 and 10"

    if exam_score > 100 or exam_score < 0:
        return "Exam score must be between 0 and 100"

    data = pd.DataFrame([[
        age, gender, attendance, study_hours,
        scholarship, tuition, parents_education,
        income, exam_score
    ]], columns=[
        'age','gender','attendance_percentage','study_hours_per_day',
        'scholarship','tuition_fees_paid','parents_education',
        'family_income','exam_score'
    ])

    prediction = model.predict(data)
    prob = model.predict_proba(data)[0][1] * 100

    if prediction[0] == 1:
      result = "High Dropout Risk"
      color = "red"
    else:
      result = "Low Dropout Risk"
      color = "green"

    return render_template(
    "index.html",
    prediction_text=result,
    probability=round(prob, 2),
    color=color
)


if __name__ == "__main__":
    app.run(debug=True)
    