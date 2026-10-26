# Task 1
# Create a Calculator class having methods:
# add()
# subtract()
# multiply()
# divide()

class Calculator:
    def add(self, a, b):
        print("Addition =", a + b)

    def subtract(self, a, b):
        print("Subtraction =", a - b)

    def multiply(self, a, b):
        print("Multiplication =", a * b)

    def divide(self, a, b):
        if b != 0:
            print("Division =", a / b)
        else:
            print("Cannot divide by zero")
cal = Calculator()
cal.add(10, 5)
cal.subtract(10, 5)
cal.multiply(10, 5)
cal.divide(10, 5)




print("==========================================================================")



# Task 2
# Create a Student class.
# Method should print complete student information.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)
s1 = Student("Ali", 20, "A")
s1.display()




print("==========================================================================")





# Task 3
# Create a BankAccount class.
# Methods:
# deposit()
# withdraw()

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Balance =", self.balance)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance =", self.balance)
        else:
            print("Insufficient Balance")
account = BankAccount(10000)
account.deposit(2000)
account.withdraw(3000)


print("==========================================================================")



# Task 4
# Create a Circle class.
# Method should calculate area.

class Circle:
    def __init__(self,r):
        self.radius = r
    def area(self):
        area = 3.14 * (self.radius**2)
        print(f"Area of Circle is : {area}")
c = Circle(5)
c.area()



print("==========================================================================")



# Task 5
# Create a Rectangle class.
# Method should calculate perimeter.

class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w
    def perimeter(self):
        per = 2 * (self.length + self.width)
        print(f"Perimeter of rectangle is : {per}")
c = Rectangle(5,8)
c.perimeter()




print("==========================================================================")



# Task 7
# Create a Number class.
# Method checks whether number is even or odd.

class Number:
    def __init__(self,n):
        self.num = n
    def check(self):
        if self.num % 2 == 0:
            print(f"{self.num} is even")
        else:
            print(f"{self.num} is odd")
number = Number(10)
number.check()


print("==========================================================================")



# Task 8
# Create a Password class.
# Method validates password according to:
# minimum length
# contains number
# contains uppercase letter

class Password:
    def __init__(self, password):
        self.password = password
    def validate(self):
        if len(self.password) < 8:
            print("Password too short")
            return
        has_number = False
        has_upper = False
        for ch in self.password:
            if ch.isdigit():
                has_number = True
            if ch.isupper():
                has_upper = True
        if has_number and has_upper:
            print("Valid Password")
        else:
            print("Invalid Password")
p = Password("Hello123")
p.validate()




print("==========================================================================")