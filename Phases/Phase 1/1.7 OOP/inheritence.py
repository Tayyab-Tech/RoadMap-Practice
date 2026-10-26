# Task 1
# Create a Person class.
# Create a Student class inheriting from Person.
# Display student information.

class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a
class Student(Person):
    def __init__(self, n, a, g):
        super().__init__(n, a)
        self.grade = g
    def display(self):
        print(self.name,self.age,self.grade)
# p = Person()
s = Student("Ali", 20, "A")
s.display()



print("==========================================================================")



# Task 2
# Create an Animal class.
# Create Dog class.
# Add barking behavior.

class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def bark(self):
        print("Dog Bark")
d = Dog()
d.eat()
d.bark()




print("==========================================================================")



# Task 3
# Create Vehicle.
# Create Bike.
# Print both parent and child properties.

class Vehicle:
    def __init__(self, company):
        self.company = company

class Bike(Vehicle):
    def __init__(self, company, model):
        super().__init__(company)
        self.model = model

    def display(self):
        print(self.company)
        print(self.model)

b = Bike("Honda", "CD70")
b.display()



print("==========================================================================")



# Task 4
# Create Employee.
# Create Manager.
# Manager should have additional bonus.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def em_total(self):
        print("Employee Salary : ",self.salary)

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def total_salary(self):
        print("Manager Salary : ",self.salary + self.bonus)

m = Manager("Ali", 50000, 10000)
m.em_total()
m.total_salary()



print("==========================================================================")



# Task 5
# Create Shape.
# Create Rectangle.
# Calculate area.

class Shape:
    def __init__(self,r):
        self.radius = r
        self.pai = 3.14
class Rectangle(Shape):
    def __init__(self, r):
        super().__init__(r)
    def area(self):
        print("Area = ", self.pai * (self.radius**2))
r = Rectangle(5)
r.area()

print("==========================================================================")
