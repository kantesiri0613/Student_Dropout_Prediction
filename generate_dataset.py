import pandas as pd
import numpy as np

num_students = 1000

data = {
    "age": np.random.randint(18, 25, num_students),
    "gender": np.random.choice(["Male", "Female"], num_students),
    "admission_grade": np.random.randint(90, 150, num_students),
    "attendance_percentage": np.random.randint(40, 100, num_students),
    "study_hours_per_day": np.random.randint(1, 6, num_students),
    "scholarship": np.random.choice(["Yes", "No"], num_students),
    "tuition_fees_paid": np.random.choice(["Yes", "No"], num_students),
    "parents_education": np.random.choice(
        ["HighSchool", "Diploma", "Bachelor", "Master"], num_students
    ),
    "family_income": np.random.randint(10000, 100000, num_students),
    "exam_score": np.random.randint(40, 100, num_students),
}

df = pd.DataFrame(data)

# Improved dropout logic
df["dropout_status"] = np.where(
    (df["attendance_percentage"] < 65) |
    (df["exam_score"] < 55) |
    (df["tuition_fees_paid"] == "No"),
    1,
    0
)

df.to_csv("student_dropout_dataset.csv", index=False)

print("Dataset created successfully!")