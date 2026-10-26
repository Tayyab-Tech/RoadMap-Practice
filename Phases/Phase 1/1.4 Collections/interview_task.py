# Mixed Data Structure
# Given
students = [
    {
        "name":"Ali",
        "skills":{"Python","SQL"},
        "marks":(80,85,90)
    },
    {
        "name":"Ahmed",
        "skills":{"Java","Python"},
        "marks":(75,70,80)
    },
    {
        "name":"Usman",
        "skills":{"Python","React"},
        "marks":(90,92,95)
    }
]
# Find:
# Student with highest average marks.
# Students who know Python.
# All unique skills.
# Average marks of every student.

# highest_average = 0
# highest_student = ""
# all_skills = set()

# print("Average Marks:")

# for i in students:
#     total = 0
#     for j in i["marks"]:
#         total += j
#     avg = total / len(i["marks"])
#     print(i["name"], ":", avg)

#     if avg > highest_average:
#         highest_average = avg
#         highest_student = i["name"]

#     if "Python" in i["skills"]:
#         print(i["name"],"knows python")
#     for skill in i["skills"]:
#         all_skills.add(skill)

# print("\nStudent with Highest Average:")
# print(highest_student, "-", highest_average)
# print("\nAll Unique Skills:")
# print(all_skills)






# Employee Database 
# Given
employees = [
    {
        "id":101,
        "name":"Ali",
        "department":"IT",
        "salary":70000
    },
    {
        "id":102,
        "name":"Ahmed",
        "department":"HR",
        "salary":50000
    },
    {
        "id":103,
        "name":"Usman",
        "department":"IT",
        "salary":90000
    },
    {
        "id":104,
        "name":"Ayesha",
        "department":"Finance",
        "salary":65000
    }
]

# Write a program to:
# Print all employees working in the IT department.
# Find the highest-paid employee.
# Calculate the average salary.
# Count employees in each department.
# Increase the salary of every IT employee by 10%.
# Print the updated employee list.

for i in employees:
    if i["department"] == "IT":
        print(f"{i["name"]} working in {i["department"]} department")

highest_salary = employees[0]['salary']
highest_emoloyee_paid = employees[0]['name']
for i in employees:
    if i["salary"] > highest_salary:
        highest_salary = i["salary"]
        highest_emoloyee_paid = i["name"]
print(f"{highest_emoloyee_paid} has highest salary which is {highest_salary}")

total = 0 
for i in employees:
    total+=i["salary"]
avg = total/len(employees)
print(f"Average salary is {avg}")
department_count = {}
for i in employees:
    department = i["department"]
    if department in department_count:
        department_count[department]+=1
    else:
        department_count[department]=1
print("\nDepartment Counts:")
print(department_count)
for i in employees:
    if i["department"] == "IT":
        i["salary"] = i["salary"]+i["salary"]*0.10

print("\nUpdated Employee List:")
for i in employees:
    print(i)
