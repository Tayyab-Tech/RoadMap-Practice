
import pandas as pd
import matplotlib.pyplot as plt

# 1. Create the dataset
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "exam_score": [42, 48, 51, 57, 65, 68, 75, 79, 88, 91]
}

df = pd.DataFrame(data)

# 2. Calculate Pearson correlation
correlation = df["study_hours"].corr(df["exam_score"])

print("Dataset:")
print(df)

print("\nPearson Correlation Coefficient:")
print(round(correlation, 4))

# 3. Create a scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(
    df["study_hours"],
    df["exam_score"],
    label="Students",
    marker="o"
)

plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Scores")
plt.grid(True)
plt.legend()

plt.show()
