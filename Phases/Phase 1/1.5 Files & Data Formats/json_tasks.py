import json

# Task 1: Store Student Data
# Create a JSON file containing one student's:
# Name
# Age
# City
# Marks
# Read and display the data.

# student = {
#     "Name": "Ali",
#     "Age": 20,
#     "City": "Lahore",
#     "Marks": 85
# }
# with open("Phase 1\\1.5 Files & Data Formats\\json\\students.json","w",newline="") as f:
#     json.dump(student,f,indent=4)
# print("Students.json created successfully")






# Task 2: Store Multiple Students
# Store information for 5 students in a JSON file and print all records.

# students = [
#     {
#         "Name": "Ali",
#         "Age": 20,
#         "City": "Lahore",
#         "Marks": 85
#     },
#     {
#         "Name": "Ahmed",
#         "Age": 21,
#         "City": "Karachi",
#         "Marks": 78
#     },
#     {
#         "Name": "Sara",
#         "Age": 19,
#         "City": "Islamabad",
#         "Marks": 92
#     },
#     {
#         "Name": "Ayesha",
#         "Age": 20,
#         "City": "Faisalabad",
#         "Marks": 88
#     },
#     {
#         "Name": "Bilal",
#         "Age": 22,
#         "City": "Multan",
#         "Marks": 75
#     }
# ]
# with open("Phase 1\\1.5 Files & Data Formats\\json\\students.json","w",newline="") as f:
#     json.dump(students,f,indent=4)
# print("Updated Students.json successfully")









# Task 3: Search Student
# Take a student's name as input and display their complete information from the JSON file.

# user = input("Enter Student name to search : ")
# found = False
# with open("Phase 1\\1.5 Files & Data Formats\\json\\students.json","r") as f:
#     reader = json.load(f)
#     for data in reader:
#         # print(data)
#         if user.lower() == data["Name"].lower():
#             print("Student Found  : ")
#             print("Name :", data["Name"])
#             print("Age  :", data["Age"])
#             print("City :", data["City"])
#             print("Marks:", data["Marks"])
#             found = True
#             break
# if not found:
#     print("Student not found")







# Task 4: Count Students
# Read the JSON file and print the total number of students stored.

# count = 0
# with open("Phase 1\\1.5 Files & Data Formats\\json\\students.json","r") as f:
#     reader = json.load(f)
#     for data in reader:
#         # print(data)
#         count+=1
# print(f"{count} student's stored in file")







# Task 5: Add New Student
# Take student details from the user and append the new student to the existing JSON file.

# name = input("Enter Name: ")
# age = int(input("Enter Age: "))
# city = input("Enter City: ")
# marks = int(input("Enter Marks: "))
# new_student = {
#     "Name": name,
#     "Age": age,
#     "City": city,
#     "Marks": marks
# }
# with open("Phase 1\\1.5 Files & Data Formats\\json\\students.json","r") as f:
#     reader = json.load(f)
# reader.append(new_student)
# with open("Phase 1\\1.5 Files & Data Formats\\json\\students.json", "w") as f:
#     json.dump(reader, f, indent=4)
# print("New student added successfully.")









# Task 6: Student Management System
# Implement a menu-driven program using a JSON file.
# Menu:
# Add Student
# View Students
# Search Student
# Update Student
# Delete Student
# Exit

# import os
# file_path = "Phase 1\\1.5 Files & Data Formats\\json\\management.json"
# if not os.path.exists(file_path):
#     with open(file_path, "w") as f:
#         json.dump([], f)
# def load_data():
#     with open(file_path,"r") as f:
#         return json.load(f)
# def save_data(data):
#     with open(file_path,"w") as f:
#         json.dump(data,f,indent=4)
# def add_student():
#     print("Add New Student : ")
#     name = input("Enter Name: ")
#     age = int(input("Enter Age: "))
#     city = input("Enter City: ")
#     marks = int(input("Enter Marks: "))
#     new_student = {
#         "Name": name,
#         "Age": age,
#         "City": city,
#         "Marks": marks
#     }
#     student = load_data()
#     student.append(new_student)
#     save_data(student)
#     print("Student added Successfully")
# def view_students():
#     print("All Students Shown below : \n")
#     students = load_data()
#     for data in students:
#         print("-----------------------")
#         print("Name :", data["Name"])
#         print("Age  :", data["Age"])
#         print("City :", data["City"])
#         print("Marks:", data["Marks"])
# def search_Student():
#     user_search = input("Enter student name to search : ")
#     print()
#     found = False
#     students = load_data()
#     for data in students:
#         if data["Name"].lower()==user_search.lower():
#             print("-----------------------")
#             print("Name :", data["Name"])
#             print("Age  :", data["Age"])
#             print("City :", data["City"])
#             print("Marks:", data["Marks"])
#             found = True
#     if not found:
#         print("Student not found")
# def update_student():
#     students = load_data()
#     user_choose = input("Enter Student name to update : ")
#     found = False
#     for data in students:
#         if data["Name"].lower() == user_choose.lower():
#             data["Age"] = int(input("Enter updated Age : "))
#             data["City"] = input("Enter updated City : ")
#             data["Marks"] = int(input("Enter updated Marks : "))
#             save_data(students)
#             print("Student Updated Successfully.\n")
#             found = True
#             return
    
#     if not found:
#         print("Student not found.")
# def delete_student():
#     students = load_data()
#     user_choose = input("Enter Student name to update : ")
#     found = False
#     new_student = []
#     for data in students:
#         if data["Name"].lower()==user_choose.lower():
#             found=True
#         else:
#             new_student.append(data)
#     save_data(new_student)
#     if found:
#         print("Student Deleted Successfully")
#     else:
#         print("Student not found!")
# while True:
#     print('''\n1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Exit''')
#     choice = input("Enter your choice : ")
#     print()
#     if choice == "1":
#         add_student()
#     elif choice == "2":
#         view_students()
#     elif choice == "3":
#         search_Student()
#     elif choice == "4":
#         update_student()
#     elif choice == "5":
#         delete_student()
#     elif choice == "6":
#         print("Program ended!")
#         break
#     else:
#         print("Invalid Choice! Please Re-enter")










# Task 7: Analyze Nested JSON
# Given a nested JSON structure containing departments and employees:
# Count total departments.
# Count total employees.
# Find the employee with the highest salary.
# Print all employee names department-wise.

# company = {
#     "Departments": [
#         {
#             "Department": "IT",
#             "Employees": [
#                 {
#                     "Name": "Ali",
#                     "Salary": 60000
#                 },
#                 {
#                     "Name": "Ahmed",
#                     "Salary": 75000
#                 }
#             ]
#         },
#         {
#             "Department": "HR",
#             "Employees": [
#                 {
#                     "Name": "Sara",
#                     "Salary": 50000
#                 },
#                 {
#                     "Name": "Ayesha",
#                     "Salary": 70000
#                 }
#             ]
#         }
#     ]
# }
# filepath = "Phase 1\\1.5 Files & Data Formats\\json\\company.json"
# # with open(filepath,"w") as f:
# #     json.dump(company,f,indent=4)
# # print("company.json created successfully.")
# with open(filepath,"r") as f:
#     company = json.load(f)
# # print(company)
# employee_count = 0 
# highest_salary = 0
# highest_employee = ""
# print(f"Total Departments : {len(company["Departments"])}")
# for department in company["Departments"]:
#     print(f"{department["Department"]} : ")
#     for employee in department["Employees"]:
#         print("  ", employee["Name"])
#         employee_count+=1
#         if employee["Salary"] > highest_salary:
#             highest_salary = employee["Salary"]
#             highest_employee = employee["Name"]
# print(f"{employee_count} employees are working in company")
# print(f"Highest Salary Employee : {highest_employee}")
# print(f"Highest Salary : {highest_salary}")










# Task 5: Merge Two JSON Files
# Given two JSON files containing student records:
# Merge both files.
# Remove duplicate students (based on Roll Number or ID).
# Save the merged data into a new JSON file.
# Sort the final records alphabetically by name.

students1 = [
    {
        "ID": 1,
        "Name": "Ali",
        "Age": 20
    },
    {
        "ID": 2,
        "Name": "Ahmed",
        "Age": 21
    },
    {
        "ID": 3,
        "Name": "Sara",
        "Age": 19
    }
]

with open("Phase 1\\1.5 Files & Data Formats\\json\\students1.json", "w") as f:
    json.dump(students1, f, indent=4)

students2 = [
    {
        "ID": 3,
        "Name": "Sara",
        "Age": 19
    },
    {
        "ID": 4,
        "Name": "Bilal",
        "Age": 22
    },
    {
        "ID": 5,
        "Name": "Ayesha",
        "Age": 20
    }
]
with open("Phase 1\\1.5 Files & Data Formats\\json\\students2.json", "w") as f:
    json.dump(students2, f, indent=4)

with open("Phase 1\\1.5 Files & Data Formats\\json\\students1.json","r") as f:
    student1 = json.load(f)
with open("Phase 1\\1.5 Files & Data Formats\\json\\students2.json","r") as f:
    student2 = json.load(f)

merge_student = student1 + student2
unique_student = []
ids = set()
for student in merge_student:
    # print(student)
    if student["ID"] not in ids:
        ids.add(student["ID"])
        unique_student.append(student)

unique_student.sort(key = lambda x: x["Name"])
with open("Phase 1\\1.5 Files & Data Formats\\json\\merged_student.json","w") as f:
    json.dump(unique_student,f,indent=4)
print("File Merged Successfully")