# Student Dataset

# Create a 5 × 4 array:

# Rows    → Students
# Columns → Math, English, Science, Computer

# Requirements:

# Total marks per student.
# Average marks per student.
# Highest subject score per student.
# Highest score in each subject.
# Student with highest total.
# Students whose average is above 80.
# Rank students according to total marks.

# No loops.

import importlib
np = importlib.import_module("numpy")

marks = np.array([
    [85, 78, 92, 88],
    [72, 81, 79, 90],
    [95, 89, 94, 97],
    [68, 75, 70, 82],
    [88, 91, 85, 93]
])
total = marks.sum(axis=1)
print(total)
avg = marks.mean(axis=1)
print(avg)
print(marks.max(axis=1))
print(marks.max(axis=0))
print(np.argmax(total))
print(avg[avg>80])

# ranking = np.argsort(total)+1 # for lowest to highest argument sorting
ranking = np.argsort(total)[::-1]+1 # for highest to lowest argument sorting
print(ranking)