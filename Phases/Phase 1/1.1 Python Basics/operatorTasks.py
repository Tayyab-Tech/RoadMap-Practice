# Task 6 – Basic Calculator
# Take two numbers.
# Display:
# Addition
# Subtraction
# Multiplication
# Division
# Modulus
# Power

# num1 = int(input("Enter 1st number : "))
# num2 = int(input("Enter 2nd number : "))

# print(f"Addition : {num1} + {num2} = {num1 + num2}")
# print(f"Subtraction : {num1} - {num2} = {num1 - num2}")
# print(f"Multiplication : {num1} * {num2} = {num1 * num2}")
# print(f"Division : {num1} / {num2} = {num1 / num2}")
# print(f"Modulus : {num1} % {num2} = {num1 % num2}")
# print(f"Power : {num1} ** {num2} = {num1 ** num2}")

# Task 7 – Seconds Converter
# Take total seconds.
# Convert into:
# Hours
# Minutes
# Remaining Seconds

# sec = int(input("Enter seconds : "))
# hours = sec // 3600
# minutes = (sec % 3600) // 60
# seconds = sec % 60
# print(f"{hours} Hours")
# print(f"{minutes} Minutes")
# print(f"{seconds} Seconds")


# Task 8 – Shopping Bill
# Take:
# Price of Item 1
# Price of Item 2
# Price of Item 3
# Calculate:
# Total
# 10% Tax
# Final Bill

# item1 = int(input("Enter Price of Item 1 : "))
# item2 = int(input("Enter Price of Item 2 : "))
# item3 = int(input("Enter Price of Item 3 : "))
# total = item1 + item2 + item3
# tax = total * 0.10
# final = total + tax
# print(f"Total = {total}")
# print(f"Tax = {tax}")
# print(f"Final = {final}")


# Task 9 – Salary
# Take monthly salary.
# Calculate:
# Annual Salary
# Bonus (15%)
# Total Income

# salary = int(input("Enter mounthly salary : "))
# annual = salary * 12
# bonus = annual * 0.15
# total = annual + bonus
# print(f"Salary is {salary}")
# print(f"Annual Salary is {annual}")
# print(f"Bonus on Salary is {bonus}")
# print(f"Total Salary is {total}")


# Task 10 – Marks
# Take marks of five subjects.
# Display:
# Total Marks
# Percentage
# Average

sub1 = int(input("enter marks of subject 1 out of 100 : "))
sub2 = int(input("enter marks of subject 2 out of 100 : "))
sub3 = int(input("enter marks of subject 3 out of 100 : "))
sub4 = int(input("enter marks of subject 4 out of 100 : "))
sub5 = int(input("enter marks of subject 5 out of 100 : "))

total = sub1 + sub2 + sub3 + sub4 + sub5
per = (total / 500)*100
avg = total / 5

print(f"Total marks : {total}")
print(f"Percentage : {per}")
print(f"Average : {avg}")