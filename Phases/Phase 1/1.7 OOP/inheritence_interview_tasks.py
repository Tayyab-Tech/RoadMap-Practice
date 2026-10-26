# Task 9
# Create multi-level inheritance:
# Person → Employee → Developer
# Print all inherited properties.
class Person:
    def __init__(self,n):
        self.name = n
class Employee(Person):
    def __init__(self, n,s):
        super().__init__(n)
        self.salary = s
class Developer(Employee):
    def __init__(self, n, s, l):
        super().__init__(n, s)
        self.language = l
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.language)
d = Developer("Ali", 100000, "Python")
d.display()




print("==========================================================================")





# Task 10
# Create:
# Animal → Mammal → Dog
# Override a method in Dog.

class Animal:
    def sound(self):
        print("Animal makes sound")
class Mammal(Animal):
    pass
class Dog(Mammal):
    def sound(self):
        print("Dog barks")
d = Dog()
d.sound()







print("==========================================================================")




# Create:
# Account → SavingAccount
# Override withdrawal method to maintain minimum balance.

class Account:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        self.balance -= amount
class SavingAccount(Account):
    def withdraw(self, amount):
        if self.balance - amount >= 1000:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Minimum Balance Required")
s = SavingAccount(5000)
s.withdraw(3000)
print(s.balance)
s.withdraw(1500)




print("==========================================================================")




# Create an Employee hierarchy:
# Employee
# Manager
# Developer
# Intern
# Calculate salary differently for each class.

class Employee:
    def salary(self):
        pass
class Manager(Employee):
    def salary(self):
        print(100000)
class Developer(Employee):
    def salary(self):
        print(80000)
class Intern(Employee):
    def salary(self):
        print(30000)
m = Manager()
d = Developer()
i = Intern()
m.salary()
d.salary()
i.salary()




print("==========================================================================")





# Design a complete Library Management System using inheritance.
# Requirements:
# Person
# Student
# Teacher
# Book
# PrintedBook
# DigitalBook
# Implement methods for:
# issue book
# return book
# display details
# calculate overdue fine (different for students and teachers)

class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def fine(self, days):
        return days * 5
class Teacher(Person):
    def fine(self, days):
        return days * 2
class Book:
    def __init__(self, title):
        self.title = title
        self.issued = False
    def issue_book(self):
        if not self.issued:
            self.issued = True
            print(self.title, "Issued")
        else:
            print("Already Issued")
    def return_book(self):
        self.issued = False
        print(self.title, "Returned")
class PrintedBook(Book):
    def display(self):
        print("Printed Book:", self.title)
class DigitalBook(Book):
    def display(self):
        print("Digital Book:", self.title)
student = Student("Ali")
teacher = Teacher("Ahmed")
book1 = PrintedBook("Python")
book2 = DigitalBook("AI")
book1.issue_book()
book1.return_book()
book2.display()
print("Student Fine:", student.fine(4))
print("Teacher Fine:", teacher.fine(4))