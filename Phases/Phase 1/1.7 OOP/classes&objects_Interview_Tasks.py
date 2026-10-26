# Task 1
# Create a Rectangle class.
# Create 20 rectangles.
# Find rectangle having largest area.

# class Rectangle:
#     def __init__(self,l,w):
#         self.length = l
#         self.width = w
#     def area(self):
#         return self.length*self.width
# rectangles = []
# for i in range(1,21):
#     l = int(input("Length : "))
#     w = int(input("Width : "))
#     rectangles.append(Rectangle(l,w))
# largest = rectangles[0]
# for r in rectangles:
#     if r.area() > largest.area():
#         largest = r
# print(f"Largest Area : {largest.area()}")




print("==========================================================================")



# Task 2 
# Create a Player class.
# Store:
# name
# runs
# wickets
# Sort players according to runs.

class Player:
    def __init__(self,n,r,w):
        self.name = n
        self.runs = r
        self.wickets = w
players = [
    Player("Ali", 450, 5),
    Player("Ahmed", 700, 10),
    Player("Sara", 500, 8)
]
players.sort(key = lambda player: player.runs)
for player in players:
    print(player.name,player.runs,player.wickets)



print("==========================================================================")


# Task 3
# Create a HospitalPatient class.
# Find:
# oldest patient
# youngest patient
# average age

class HospitalPatient:
    def __init__(self,n,a):
        self.name = n
        self.age = a
patients = [
    HospitalPatient("Ali", 45),
    HospitalPatient("Ahmed", 18),
    HospitalPatient("Sara", 60)
]
oldest_patient = patients[0]
youngest_patient = patients[0]
total = 0
for p in patients:
    if p.age > oldest_patient.age:
        oldest_patient = p
    if p.age < youngest_patient.age:
        youngest_patient = p
    total += p.age
avg = total/len(patients)
print(f"Oldest patient : {oldest_patient.name} , {oldest_patient.age}")
print(f"Youngest patient : {youngest_patient.name} , {youngest_patient.age}")
print(f"Average age is : {avg}")





print("==========================================================================")




# Task 4
# Create a Course class.
# Each course contains:
# name
# duration
# fee
# Find course with highest fee.

class Course:
    def __init__(self,n,d,f):
        self.name = n
        self.duration = d
        self.fee = f
courses = [
    Course("Python", "3 Months", 20000),
    Course("Java", "4 Months", 25000),
    Course("Web", "6 Months", 35000)
]
highest = courses[0]
for c in courses:
    if c.fee > highest.fee:
        highest = c
print(f"Course with highest fee is : {highest.name} , {highest.duration} , {highest.fee}")







print("==========================================================================")





# Task 5
# Create a Flight class.
# Display flights departing after a particular time entered by user.

# class Flight:
#     def __init__(self,f_no,d):
#         self.flight_no = f_no
#         self.departure = d
# flights = [
#     Flight("PK101", "09:00"),
#     Flight("PK102", "12:30"),
#     Flight("PK103", "18:45")
# ]
# time = input("Enter time (HH:MM): ")
# for f in flights:
#     if f.departure > time:
#         print(f.flight_no, f.departure)





print("==========================================================================")




# Task 6
# Create a UniversityStudent class.
# Count students department-wise.

class UniversityStudent:
    def __init__(self,n,d):
        self.name = n
        self.department = d
students = [
    UniversityStudent("Ali", "CS"),
    UniversityStudent("Ahmed", "IT"),
    UniversityStudent("Sara", "CS"),
    UniversityStudent("Ayesha", "SE"),
    UniversityStudent("Bilal", "IT")
]
count = {}
for s in students:
    if s.department in count:
        count[s.department] += 1
    else:
        count[s.department] = 1
print(count)





print("==========================================================================")





# Task 7
# Design a LibraryBook class and create 100 objects.
# Find:
# total books
# unique authors
# average pages

class LibraryBook:
    def __init__(self,b,a,p):
        self.book = b
        self.author = a 
        self.pages = p
books = []
for i in range(100):
    books.append(
        LibraryBook(
            f"Book{i+1}",
            f"Author{(i % 10) + 1}",
            100 + i
        )
    )
total_books = len(books)
unique_author = set()
total_pages = 0
for b in books:
    total_pages += b.pages
    unique_author.add(b.author)
print("Total Books:", total_books)
print("Unique Authors:", len(unique_author))
print("Average Pages:", total_pages / total_books)