# Build a calculator (+, -, *, /) with proper exception handling.
try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Answer:", num1 + num2)

    elif operator == "-":
        print("Answer:", num1 - num2)

    elif operator == "*":
        print("Answer:", num1 * num2)

    elif operator == "/":
        print("Answer:", num1 / num2)

    else:
        print("Invalid Operator")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")






# Ask for age and raise a ValueError if age is below 18.
try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("Access Granted")

except ValueError as e:
    print(e)




# Convert a list of strings to integers, skipping invalid values.
data = ["10", "20", "abc", "40", "xyz", "50"]

numbers = []

for item in data:
    try:
        numbers.append(int(item))
    except ValueError:
        print(item, "is invalid and skipped.")

print("Valid Numbers:", numbers)




# Create a function that divides two numbers and returns a custom error message if division fails.
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Please enter valid numbers."

print(divide(20, 4))
print(divide(10, 0))
print(divide("10", 2))




# Read numbers from a file and handle invalid numeric data.
try:
    file = open("Phase 1\\1.6 Reliability\\exception\\number.txt", "r")

    for line in file:
        try:
            number = int(line.strip())
            print(number)
        except ValueError:
            print("Invalid number found:", line.strip())

    file.close()

except FileNotFoundError:
    print("File not found.")