# Create a custom exception InvalidSalaryError for salaries less than 0.
class InvalidSalaryError(Exception):
    pass

try:
    salary = float(input("Enter salary: "))

    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative.")

    print("Salary:", salary)

except InvalidSalaryError as e:
    print(e)




# Create a custom exception InsufficientFundsError for a bank withdrawal system.
class InsufficientFundsError(Exception):
    pass
try:
    balance = 50000
    print("Availabe balance 50000.")
    amount = int(input("Enter withdrawal amount : "))
    if amount > balance:
        raise InsufficientFundsError("Insufficient Balance")
    balance -= amount
    print("Remaining Balance:", balance)
except InsufficientFundsError as e:
    print(e)






# Build an ATM program that handles invalid PINs, insufficient balance, and invalid withdrawal amounts.
class InvalidPINError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass


correct_pin = "1234"
balance = 5000
try:
    pin = input("Enter PIN: ")

    if pin != correct_pin:
        raise InvalidPINError("Invalid PIN.")

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than zero.")

    if amount > balance:
        raise InsufficientFundsError("Insufficient balance.")

    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)

except InvalidPINError as e:
    print(e)

except InvalidAmountError as e:
    print(e)

except InsufficientFundsError as e:
    print(e)






# Create a student registration system that raises exceptions for duplicate roll numbers and invalid marks.
class DuplicateRollNumberError(Exception):
    pass

class InvalidMarksError(Exception):
    pass

students = {
    101: 85,
    102: 78
}
try:
    roll = int(input("Enter Roll Number: "))

    if roll in students:
        raise DuplicateRollNumberError("Roll number already exists.")

    marks = int(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")

    students[roll] = marks

    print("Student Registered Successfully")
    print(students)

except DuplicateRollNumberError as e:
    print(e)

except InvalidMarksError as e:
    print(e)






# Build a library management system using multiple custom exceptions (book not found, already issued, invalid member).
class BookNotFoundError(Exception):
    pass

class BookAlreadyIssuedError(Exception):
    pass

class InvalidMemberError(Exception):
    pass

books = {
    "Python": False,
    "Java": True,
    "C++": False
}
members = ["Ali", "Ahmed", "Sara"]
try:
    member = input("Enter member name: ")

    if member not in members:
        raise InvalidMemberError("Invalid member.")

    book = input("Enter book name: ")

    if book not in books:
        raise BookNotFoundError("Book not found.")

    if books[book]:
        raise BookAlreadyIssuedError("Book is already issued.")

    books[book] = True

    print("Book issued successfully.")

except InvalidMemberError as e:
    print(e)

except BookNotFoundError as e:
    print(e)

except BookAlreadyIssuedError as e:
    print(e)