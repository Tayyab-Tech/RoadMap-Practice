# Create a NumPy array containing marks of 10 students.

# Requirements:

# Print the array.
# Print total marks.
# Print average marks.
# Find highest and lowest marks.
# Print students who scored 70 or above.
# Print students who scored below 50.

# Concepts: arrays, aggregation, boolean indexing.
import importlib

np = importlib.import_module("numpy")

marks = np.array([65, 72, 48, 91, 56, 83, 39, 70, 44, 77])

print(marks)
print(marks.sum())
print(marks.sum()/len(marks))
print(marks.max())
print(marks.min())
print(marks[marks >= 70])
print(marks[marks < 70])