# Task 1
# Create a Library class.
# Methods:
# issueBook()
# returnBook()
# Maintain available books.

class Library:
    def __init__(self):
        self.books = ["Python", "Java", "C++"]
    def issueBook(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} issued")
        else:
            print(f"Book not available")
    def returnBook(self,book):
        self.books.append(book)
        print(book,"returned")
library = Library()
library.issueBook("Python")
library.returnBook("Python")
print(library.books)





print("==========================================================================")



# Task 2
# Create a ShoppingCart class.
# Methods:
# add item
# remove item
# calculate bill

class ShoppingCart:
    def __init__(self):
        self.items = {}
    def addItem(self,name,price):
        self.items[name] = price
    def removeItem(self,name):
        if name in self.items:
            del self.items[name]
    def calculateBill(self):
        total = sum(self.items.values())
        print("Total bill : ", total)
s = ShoppingCart()
s.addItem("Mouse", 1000)
s.addItem("Keyboard", 2500)
s.calculateBill()
s.removeItem("Mouse")
s.calculateBill()




print("==========================================================================")



# Task 15
# Create a ParkingLot class.
# Methods:
# park vehicle
# remove vehicle
# available spaces

class ParkingLot:
    def __init__(self,spaces):
        self.total = spaces
        self.available = spaces
    def park_vehicle(self):
        if self.available > 0:
            self.available -= 1
            print("Vehicle Parked")
        else:
            print("Parking Full")
    def remove_vehicle(self):
        if self.available < self.total:
            self.available += 1
            print("Vehicle Removed")
        else:
            print("Parking already empty")
    def available_space(self):
        print("Available spaces : ", self.available)
p = ParkingLot(5)
p.park_vehicle()
p.park_vehicle()
p.park_vehicle()
p.available_space()
p.remove_vehicle()
p.available_space()




print("==========================================================================")

