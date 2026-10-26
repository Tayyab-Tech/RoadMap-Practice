# Task 11 – Swap Variables
# Take two numbers.
# Swap them without using a third variable.
# Display before and after swapping.

# first = int(input("Enter first number : "))
# second = int(input("Enter second number : "))

# print(first)
# print(second)
# first, second = second, first
# print(first)
# print(second)



# Task 12 – Student Data
# Take:
# Name
# Roll Number
# GPA
# Is Graduated (True/False)
# Display all values neatly.

# name = str(input("Enter name : "))
# rollno = int(input("Enter Roll Number : "))
# gpa = float(input("Enter GPA : "))
# isgraduated = bool(input("Is Graduted (yes or no) : "))

# print(name)
# print(rollno)
# print(gpa)
# print(isgraduated)


# Task 13 – Currency Converter
# Take amount in USD.
# Convert into PKR.
# (Assume 1 USD = 285 PKR)

# usd = float(input("Enter amount in USD : "))
# print(f"amount in pkr is {usd*285}")



# Task 14 – Age Calculator
# Take birth year.
# Display current age.
# import datetime
# birthyear = int(input("enter your birth year : "))
# current_age = datetime.datetime.now().year - birthyear

# print(f"your birth year is {birthyear}")
# print(f"your current age is {current_age}")

# Task 15 – Time Converter
# Take minutes.
# Convert into:
# Hours
# Remaining Minutes


mins = int(input("Enter minutes : "))
hours = mins // 60
remaining_min = mins % 60
print(f"{hours} Hours")
print(f"{remaining_min} Minutes")