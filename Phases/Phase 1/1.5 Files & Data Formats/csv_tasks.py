import csv 

# Task 1: Create Student CSV
# Create a students.csv file with the following columns:
# Name
# Age
# Marks
# Store data for 5 students.

# data = [
#     ["Ali", 20, 85],
#     ["Ahmed", 21, 78],
#     ["Sara", 19, 92],
#     ["Ayesha", 20, 88],
#     ["Bilal", 22, 75]
# ]
# with open("Phase 1\\1.5 Files & Data Formats\\csv\\student.csv","w",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name", "Age", "Marks"])
#     writer.writerows(data)
# print("CSV file created successfully.")





# Task 2: Read All Records
# Read the students.csv file and display all records in a clean format.
# Example Output:
# Name: Ali | Age: 20 | Marks: 85
# Name: Ahmed | Age: 21 | Marks: 78

# with open("Phase 1\\1.5 Files & Data Formats\\csv\\student.csv","r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(f"Name : {row["Name"]} | Age : {row["Age"]} | Marks : {row["Marks"]}")





# Task 3: Calculate Average Marks
# Read the CSV file and calculate the average marks of all students.

# total = 0
# count = 0
# with open("Phase 1\\1.5 Files & Data Formats\\csv\\student.csv","r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         total += int(row["Marks"])
#         count += 1
# avg = total / count
# print("Average marks : ",avg)





# Task 4: Find Highest Marks
# Read the CSV file and display:
# Student Name
# Highest Marks

# highest = -1
# name = ""
# with open("Phase 1\\1.5 Files & Data Formats\\csv\\student.csv","r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if int(row["Marks"]) > highest:
#             highest = int(row["Marks"])
#             name = row["Name"]
# print("Student Name:", name)
# print("Highest Marks:", highest)






# Task 5: Search Student
# Take a student name as input.
# If found, display the complete record; otherwise print "Student not found".

# user_input = input("Enter Name to Search : ")
# found = False
# with open("Phase 1\\1.5 Files & Data Formats\\csv\\student.csv","r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if row["Name"] == user_input:
#             print("Student Found : ")
#             print(f"Name : {row["Name"]} | Age : {row["Age"]} | Marks : {row["Marks"]}")
#             fount = True
# if found:
#     print("Not Found")






# Task 6: Update Student Record
# Take a student's name as input and update only their marks in the CSV file.

# user_input = input("Enter student name : ")
# new_marks = input("Enter new marks : ")
# rows = []
# found = False
# with open("Phase 1\\1.5 Files & Data Formats\\csv\\student.csv","r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if row["Name"] == user_input:
#             if row["Name"].lower() == user_input.lower():
#                 row["Marks"] = new_marks
#                 found = True

#         rows.append(row)
# with open("Phase 1\\1.5 Files & Data Formats\\csv\\student.csv","w",newline="") as f:
#     field_names = ["Name","Age","Marks"]
#     writer = csv.DictWriter(f,fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(rows)
# if found:
#     print("Student marks updated successfully.")
# else:
#     print("Student not found.")








# Task 7: Delete Student Record
# Delete a student's record from the CSV file using their name.

# user_input = input("Enter student name : ")
# rows = []
# found = False
# with open("Phase 1\\1.5 Files & Data Formats\\csv\\student.csv","r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if row["Name"].lower() == user_input.lower():
#             found = True
#         else:
#             rows.append(row)
# with open("Phase 1\\1.5 Files & Data Formats\\csv\\student.csv","w",newline="") as f:
#     field_names = ["Name", "Age", "Marks"]
#     writer = csv.DictWriter(f,fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(rows)
# if found:
#     print("Student record deleted successfully.")
# else:
#     print("Student not found.")







# Task 8: Top 3 Students
# Read the CSV file, sort students by marks in descending order, and print the top 3 students.

# rows = []
# with open("Phase 1\\1.5 Files & Data Formats\\csv\\student.csv","r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         rows.append(row)
# rows.sort(key = lambda x: int(x["Marks"]), reverse=True)
# print("Top 3 Students:")
# for i, row in enumerate(rows[:3],start=1):
#     print(f"{i}. Name: {row['Name']} | Age: {row['Age']} | Marks: {row['Marks']}")









# Task 9: Subject-wise Result
# Create a CSV with columns:
# Name
# Math
# English
# Science
# For each student:
# Calculate Total
# Calculate Average
# Assign Grade (A, B, C, D, F)
# Display the complete result.

# data = [
#     ["Ali", 80, 75, 90],
#     ["Ahmed", 65, 70, 68],
#     ["Sara", 95, 92, 98],
#     ["Ayesha", 88, 84, 90],
#     ["Bilal", 55, 60, 58]
# ]

# # with open("Phase 1\\1.5 Files & Data Formats\\csv\\subject_result.csv","w",newline="") as f:
# #     writer = csv.writer(f)
# #     writer.writerow(["Name", "Math", "English", "Science"])
# #     writer.writerows(data)
# # print("Subject_result.csv created successfully")

# with open("Phase 1\\1.5 Files & Data Formats\\csv\\subject_result.csv","r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         # print(row)
#         math = int(row["Math"])
#         english = int(row["English"])
#         science = int(row["Science"])
#         total = math+english+science
#         # print(total)
#         avg = total/3
#         # print(avg)
#         if avg >= 90:
#             grade = "A"
#         elif avg >= 80:
#             grade = "B"
#         elif avg >= 70:
#             grade = "C"
#         elif avg >= 60:
#             grade = "D"
#         else:
#             grade = "F"

#         print("---------------------------")
#         print("Name    :", row["Name"])
#         print("Math    :", math)
#         print("English :", english)
#         print("Science :", science)
#         print("Total   :", total)
#         print("Average :", round(avg, 2))
#         print("Grade   :", grade)










# Task 5: Attendance Report
# Create attendance.csv with:
# Name
# Present Days
# Total Days
# Calculate the attendance percentage for each student and print:
# Students with attendance ≥ 75%
# Students with attendance < 75%

data = [
    ["Ali", 90, 100],
    ["Ahmed", 65, 100],
    ["Sara", 80, 100],
    ["Ayesha", 75, 100],
    ["Bilal", 70, 100]
]

# with open("Phase 1\\1.5 Files & Data Formats\\csv\\attendence.csv","w",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name","Present Days","Total Days"])
#     writer.writerows(data)
# print("attendence.csv created successfully")
above_75 = []
below_75 = []
with open("Phase 1\\1.5 Files & Data Formats\\csv\\attendence.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        percentage = (int(row["Present Days"]) / int(row["Total Days"])) * 100
        if percentage >= 75:
            above_75.append((row["Name"], percentage))
        else:
            below_75.append((row["Name"], percentage))
print("Students with Attendance >= 75%\n")
for name, percentage in above_75:
    print(f"{name} - {percentage:.2f}%")
print("\nStudents with Attendance < 75%\n")
for name, percentage in below_75:
    print(f"{name} - {percentage:.2f}%")