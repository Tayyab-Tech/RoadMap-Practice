# Debugging means finding and fixing bugs. 
# What is a Bug?
# A bug is a mistake in code.
# Example
# a = 5
# b = 0
# print(a / b)
# Bug:
# ZeroDivisionError





# Types of Bugs
# 1. Syntax Error
# if True
#     print("Hello")
# Missing colon.

# 2. Runtime Error
# Program starts but crashes.
# print(10 / 0)

# 3. Logical Error
# Program runs but gives wrong output.
# length = 5
# width = 4
# area = length + width
# Should be
# area = length * width

# Using print() for Debugging
# a = 10
# b = 5
# print(a)
# print(b)
# print(a + b)

# Using breakpoints
# Most IDEs (VS Code, PyCharm) allow breakpoints.
# You can:
# Pause execution
# Check variable values
# Step line by line
# Inspect objects


# Debugging Tips

# ✔ Read the error message carefully.

# ✔ Check line number.

# ✔ Print variables.

# ✔ Test small pieces.

# ✔ Don't guess.





# Assertions
# Assertions help detect unexpected conditions during development.

age = 12
assert age >= 18
# If false
# assert age >= 18
# Output
# AssertionError