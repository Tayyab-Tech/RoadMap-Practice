# Create a reusable validation function that accepts a custom validation rule.

def validate(value, condition, message):
    if condition(value):
        return True
    else:
        raise ValueError(message)

try:
    age = int(input("Enter Age: "))
    validate(age, lambda x: x >= 18, "Age must be at least 18.")
    print("Valid Age")

except ValueError as e:
    print(e)



# Build a student registration form that validates name, age, email, phone number, GPA, and roll number.

name = input("Name: ")
age = int(input("Age: "))
email = input("Email: ")
phone = input("Phone: ")
gpa = float(input("GPA: "))
roll = input("Roll Number: ")

if not name.isalpha():
    print("Invalid Name")
elif age < 18:
    print("Invalid Age")
elif "@" not in email or "." not in email:
    print("Invalid Email")
elif len(phone) != 11 or not phone.isdigit():
    print("Invalid Phone Number")
elif not (0 <= gpa <= 4):
    print("Invalid GPA")
elif roll == "":
    print("Invalid Roll Number")
else:
    print("Registration Successful")



# Create an account creation system that validates username uniqueness, password strength, and email format.

users = ["ali", "ahmed"]

username = input("Username: ")
password = input("Password: ")
email = input("Email: ")

if username in users:
    print("Username already exists")

elif len(password) < 8:
    print("Password too short")

elif "@" not in email or "." not in email:
    print("Invalid Email")

else:
    users.append(username)
    print("Account Created Successfully")



# Read employee data from a CSV file and validate every record before processing.
import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            age = int(row["Age"])
            salary = float(row["Salary"])
            if age <= 0:
                raise ValueError("Invalid Age")
            if salary <= 0:
                raise ValueError("Invalid Salary")
            print("Valid Record:", row)
        except ValueError as e:
            print("Invalid Record:", row)
            
# Build a complete user registration system that combines validation, exception handling, and logging while storing only valid records.

import logging
logging.basicConfig(
    filename="users.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
users = []
try:
    username = input("Username: ")
    email = input("Email: ")
    age = int(input("Age: "))
    if username == "":
        raise ValueError("Username required")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid Email")
    if age < 18:
        raise ValueError("Age must be 18+")
    users.append({
        "Username": username,
        "Email": email,
        "Age": age
    })
    logging.info(f"User Registered: {username}")
    print("Registration Successful")
except Exception as e:
    logging.error(e)
    print(e)