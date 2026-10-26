import pandas as pd
import matplotlib.pyplot as plt

data = {
    "study_hours": [1, 2, 3, 4, 5, 6],
    "exam_score": [45, 50, 58, 65, 72, 78]
}

df = pd.DataFrame(data)

correlation = df["study_hours"].corr(df["exam_score"])

print("Correlation:", correlation)