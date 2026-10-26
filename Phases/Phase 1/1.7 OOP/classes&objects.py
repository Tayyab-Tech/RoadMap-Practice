# Task 1
# Create a Student class with:
# name
# age
# grade
# Create three student objects and print their data.

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
students = [
    Student("Ali", 20, "A"),
    Student("Ahmed", 19, "B"),
    Student("Sara", 21, "A+")
]
for s in students:
    print(s.name, s.age, s.grade)




print("==========================================================================")


# Task 2
# Create an Employee class with:
# name
# salary
# Create five employees and display their salaries.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
employee = [
    Employee("Ali",50000),
    Employee("Ahmed",60000),
    Employee("Kashif",70000),
    Employee("Hassan",80000),
    Employee("Fahad",90000),
]
for e in employee:
    print(e.name,e.salary)





print("==========================================================================")




# Task 3
# Create a Laptop class having:
# brand
# model
# price
# Store four laptops in a list and print only laptops costing above 100000.

class Laptop:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
laptops = [
    Laptop("Dell", "Latitude", 120000),
    Laptop("HP", "Pavilion", 90000),
    Laptop("Lenovo", "ThinkPad", 150000),
    Laptop("Asus", "Vivobook", 95000)
]
for l in laptops:
    if l.price > 100000:
        print(l.brand,l.model,l.price)




print("==========================================================================")





# Task 4
# Create a Book class with:
# title
# author
# pages
# Print the book having maximum pages.
class Book:
    def __init__(self,t,a,p):
        self.title = t
        self.author = a
        self.pages = p
books = [
    Book("Python", "Ali", 300),
    Book("Java", "Ahmed", 500),
    Book("C++", "Sara", 450)
]
largest = books[0]
for b in books:
    if b.pages > largest.pages:
        largest = b
print(largest.title,largest.pages)





print("==========================================================================")





# Task 5
# Create a Car class with:
# company
# model
# year
# Print all cars manufactured after 2020.

class Car:
    def __init__(self,c,m,y):
        self.company = c
        self.model = m
        self.year = y 
cars = [
    Car("Toyota", "Corolla", 2019),
    Car("Honda", "Civic", 2022),
    Car("Kia", "Sportage", 2023),
    Car("Suzuki", "Alto", 2020)
]
for car in cars:
    if car.year > 2020:
        print(car.company,car.model,car.year)






print("==========================================================================")





# Task 6
# Create a Product class with:
# name
# quantity
# price
# Calculate total inventory value.

class Product:
    def __init__(self,n,q,p):
        self.name = n
        self.quantity = q
        self.price = p
products = [
    Product("Mouse", 20, 1000),
    Product("Keyboard", 15, 2000),
    Product("Monitor", 10, 25000)
]
total = 0
for product in products:
    total += product.price
print("Total Inventory Value is : ",total)




print("==========================================================================")




# Task 7
# Create a Movie class with:
# name
# rating
# duration
# Display only movies having rating greater than 8.

class Movie:
    def __init__(self,n,r,d):
        self.name = n
        self.rating = r
        self.duration = d
movies = [
    Movie("Movie A", 8.5, 120),
    Movie("Movie B", 7.8, 150),
    Movie("Movie C", 9.2, 130),
    Movie("Movie D", 5.2, 160),
]
for movie in movies:
    if movie.rating>8:
        print(movie.name,movie.rating,movie.duration)




print("==========================================================================")




# Task 8
# Create a BankAccount class with:
# account number
# holder name
# balance
# Print account holders whose balance is below 5000.

class BankAccount:
    def __init__(self,a_n,h_n,b):
        self.account_number = a_n
        self.holder_name = h_n
        self.balance = b
accounts = [
    BankAccount(101, "Ali", 3000),
    BankAccount(102, "Ahmed", 10000),
    BankAccount(103, "Sara", 4500)
]
for a in accounts:
    if a.balance<5000:
        print(a.account_number,a.holder_name,a.balance)