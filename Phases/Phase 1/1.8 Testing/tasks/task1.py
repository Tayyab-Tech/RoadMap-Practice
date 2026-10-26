# Write unit tests for a function that adds two numbers.

def add(a, b):
    return a + b


# Test a function that checks whether a number is even or odd.
def is_even(num):
    return num%2==0


# Test a palindrome-checking function with different inputs. 
def is_palindrome(text):
    return text == text[::-1]


# Write tests for a factorial function, including edge cases. 
def factorial(n):
    if n < 0:
        raise ValueError("Number cannot be negative")
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


# Test a function that finds the maximum value in a list.
def find_max(numbers):
    return max(numbers)


# Write tests for a password validation function. 
def validate_password(password):
    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    return True



# Test a student grade calculator for different score ranges.
def calculate_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    else:
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"


# Write unit tests for a shopping cart total calculation with discounts. 
def calculate_total_after_discount(price, discount):
    return price - (price * discount / 100)