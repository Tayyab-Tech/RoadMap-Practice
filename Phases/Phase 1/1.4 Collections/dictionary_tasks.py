# # Question 1
# # Given the following dictionary:
# # Print all keys and all values separately.

# student = {
#     "name":"Ali",
#     "age":20,
#     "city":"Lahore"
# }
# print(student.keys())
# print(student.values())


# # Question 2
# # Add a new key "course" with the value "Python".
# student["course"] = "python"
# print(student)


# # Question 3
# # Update the student's age from 20 to 21.
# student.update({
#     "age" : 21
# })
# print(student)


# # Question 4
# # Remove the "city" key using pop().
# student.pop("city")
# print(student)



# # Question 5
# # Reverse the following dictionary.

# marks = {
#     "Ali":80,
#     "Ahmed":90,
#     "Usman":70
# }
# rev_dict = {}
# for key, value in marks.items():
#     rev_dict[value] = key
# print(rev_dict)






# Question 6
# Find the student who obtained the highest marks.

# marks = {
#     "Ali":80,
#     "Ahmed":95,
#     "Usman":70,
#     "Ayesha":88
# }
# highest = marks["Ali"]
# for value in marks.values():
#     if value > highest:
#         highest = value
# for key in marks:
#     if marks[key] == highest:
#         print("Student:", key)
#         print("Marks:", highest)






# Question 7
# Merge the following dictionaries.

# d1 = {
#     "a":1,
#     "b":2
# }
# d2 = {
#     "c":3,
#     "d":4
# }
# d1.update(d2)
# print(d1)






# Question 8
# Count the frequency of each word.
# text = "Python is easy Python is powerful"
# Expected Output:
# {
# "Python":2,
# "is":2,
# "easy":1,
# "powerful":1
# }

# text = "Python is easy Python is powerful"
# words = text.split()
# frequency = {}
# for i in words:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1
# print(frequency)






# Question 9
# Given the following dictionary:
# employees = {
#     101:"Ali",
#     102:"Ahmed",
#     103:"Usman"
# }
# Check whether employee ID 102 exists.

# employees = {
#     101:"Ali",
#     102:"Ahmed",
#     103:"Usman"
# }
# if 102 in employees:
#     print("Employee ID 102 exists.")
# else:
#     print("Employee ID 102 does not exist.")







# Question 10
# Write a program that:
# Prints the student with the highest marks.
# Calculates the average marks.
# Prints the names of students scoring below 80.
# Adds a new student.
# Updates the marks of student 103.
# Removes student 101.
# Given:

students = {
    101: {"name":"Ali","marks":80},
    102: {"name":"Ahmed","marks":90},
    103: {"name":"Usman","marks":70},
    104: {"name":"Ayesha","marks":85}
}

highest_id = 101
highest_marks = students[101]["marks"]
for id in students:
    # print(id)
    # print(students[id])
    # print(students[id]["marks"])
    if students[id]["marks"] > highest_marks:
        highest_marks = students[id]["marks"]
        highest_id = id
print("Highest Marks Student:", students[highest_id]["name"])
print("Marks:", highest_marks)

total = 0
for i in students:
    total += students[i]["marks"]
avg = total / len(students)
print(f"Average : {avg}")

print("Students below 80:")
for i in students:
    if students[i]["marks"]<80:
        print(students[i]["name"])

students[105] = {
    "name":"New",
    "marks":60
}
# print(students)

students.update({
    103 : {
        "name":"Usman",
        "marks":75
    }
})
# print(students)

del students[101]
print(students)