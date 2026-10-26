# Password Validator
# Create a function that checks whether a password:
# Minimum 8 characters
# One uppercase letter
# One lowercase letter
# One digit
# One special character
# Return all validation errors.


def Minimum_length(password):
    if len(password)<8:
        return "Password must be at least 8 characters long."
    return None
def uppercase_letter(password):
    for char in password:
        if char.isupper():
            return None
    return "Password must contain at least one uppercase letter."  
def lowercase_letter(password):
    for char in password:
        if char.islower():
            return None
    return "Password must contain at least one lowercase letter."  
def one_digit(password):
    for char in password:
        if char.isdigit():
            return None
    return "Password must contain at least one digit."  
def special_character(password):
    special = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|"

    for char in password:
        if char in special:
            return None
    return "Password must contain at least one special character."

def validation_errors(password):
    errors = []

    checks = [
        Minimum_length,
        uppercase_letter,
        lowercase_letter,
        one_digit,
        special_character
    ]

    for check in checks:
        error = check(password)
        if error:
            errors.append(error)

    return errors


password = input("Enter password: ")

errors = validation_errors(password)

if len(errors) == 0:
    print("Password is valid.")
else:
    print("Password is invalid.")
    print("Errors:")
    for error in errors:
        print("-", error)