# An exception is an error that occurs while the program is running.
# Example:
# print(10 / 0)


# Common Python Exceptions
# | Exception         | Reason                  |
# | ----------------- | ----------------------- |
# | ZeroDivisionError | Divide by zero          |
# | ValueError        | Invalid value           |
# | TypeError         | Wrong data type         |
# | IndexError        | Invalid list index      |
# | KeyError          | Dictionary key missing  |
# | NameError         | Variable doesn't exist  |
# | FileNotFoundError | File not found          |
# | AttributeError    | Object has no attribute |


# try and except
# Used to catch errors instead of crashing.
# Syntax
# try:
#     # risky code
# except:
#     # runs if error occurs

try:
    num = int(input("Enter number: "))
    print(10 / num)
except:
    print("Something went wrong.")

try:
    num = int(input("Enter number: "))
    print(10 / num)
except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
else: # Runs only if no exception occurs.
    print("Success")
finally:
    print("Closing file")

# finally Block
# Always executes.
# Useful for:
# Closing files
# Closing database connections
# Cleaning resources

# Raising Exceptions
# You can create your own errors.
# age = int(input("Enter age : "))
# if age < 18:
#     raise ValueError("Age must be at least 18")

# Custom Exceptions
class InvalidAgeError(Exception):
    pass
age = 15
if age < 18:
    raise InvalidAgeError("Not eligible")