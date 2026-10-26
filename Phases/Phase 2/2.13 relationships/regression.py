import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "study_hours": [1, 2, 3, 4, 5, 6],
    "exam_score": [45, 50, 58, 65, 72, 78]
}

df = pd.DataFrame(data)

x = df["study_hours"]
y = df["exam_score"]

slope, intercept = np.polyfit(x, y, 1)

print("Slope:", slope)
print("Intercept:", intercept)

predicted = intercept + slope * x

print(predicted)


plt.scatter(x, y)

plt.plot(
    x,
    predicted
)

plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score")

plt.show()