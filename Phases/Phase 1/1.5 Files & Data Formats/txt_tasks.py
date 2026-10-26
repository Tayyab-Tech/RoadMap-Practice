# # Create a file and write your biodata.

# bio = '''Name: Ali
# Age: 20
# City: Lahore
# Course: Computer Science'''
# # with open("Phase 1\\1.5 Files & Data Formats\\txt\\txt_task.txt",'w') as file:
# #     file.writelines(bio)



# # Read and display the entire file.

# with open("Phase 1\\1.5 Files & Data Formats\\txt\\txt_task.txt",'r') as file:
#     print(file.read())


# # Count the number of lines in a TXT file.

# count = 0
# with open("Phase 1\\1.5 Files & Data Formats\\txt\\txt_task.txt",'r') as file:
#     for line in file:
#         count+=1
# print(count)



# # Count the total words in a TXT file.

# with open("Phase 1\\1.5 Files & Data Formats\\txt\\txt_task.txt", "r") as file:
#     text = file.read()
# words = text.split()
# print(len(words))



# # Count the frequency of each character.

# with open("Phase 1\\1.5 Files & Data Formats\\txt\\txt_task.txt", "r") as file:
#     text = file.read()
# frequency = {}
# for i in text:
#     if i in frequency:
#         frequency[i]+=1
#     else:
#         frequency[i]=1
# print(frequency)



# # Copy the contents of one TXT file into another.

# with open("Phase 1\\1.5 Files & Data Formats\\txt\\txt_task.txt", "r") as file:
#     text = file.read()

# with open("Phase 1\\1.5 Files & Data Formats\\txt\\txt_task.txt",'w') as file:
#     file.writelines(text)



# # Append a new student record without deleting existing data.

# with open("Phase 1\\1.5 Files & Data Formats\\txt\\txt_task.txt",'a') as file:
#     file.write("\nName: Ahmed")
#     file.write("\nAge: 21")
#     file.write("\nCity: Karachi\n")



# # Read a file and print only lines containing the word "Python".

# with open("Phase 1\\1.5 Files & Data Formats\\txt\\txt_task.txt", "r") as file:
#     for line in file:
#         if "Python" in line:
#             print(line,end="")


# ========================================= Interview Questions ===========================================

# Question 1: Log File Analyzer

# You are given a file named log.txt.
# INFO: User logged in
# ERROR: Database failed
# INFO: User logged out
# ERROR: Invalid password
# WARNING: Low memory
# Task
# Count the total number of INFO messages.
# Count the total number of ERROR messages.
# Count the total number of WARNING messages.

# counts = {
#     "INFO": 0,
#     "ERROR": 0,
#     "WARNING": 0
# }

# with open(r"Phase 1\\1.5 Files & Data Formats\\txt\\log.txt", "r") as file:
#     for line in file:
#         for level in counts:
#             if level in line:
#                 counts[level] += 1

# for level, count in counts.items():
#     print(f"{level} : {count}")





# Question 2: Student Report
# You are given a file named students.txt.
# Ali,80
# Ahmed,95
# Usman,70
# Sara,88
# Task
# Find the highest-scoring student.
# Find the lowest-scoring student.
# Calculate the average marks.

# highest_marks = 0
# highest_student = ""
# lowest_marks = None
# lowest_student = ""
# total = 0
# count = 0
# with open("Phase 1\\1.5 Files & Data Formats\\txt\\report.txt","r") as file:
#     for line in file:
#         # print(line,end="")
#         data = line.strip().split(",")
#         # print(data)
#         name = data[0]
#         marks = int(data[1])
#         # print(name)
#         # print(marks)
#         if marks > highest_marks:
#             highest_marks = marks
#             highest_student = name
#         if lowest_marks is None or marks < lowest_marks:
#             lowest_marks = marks
#             lowest_student = name
#         total+=marks
#         count+=1
# print(f"Highest student : {highest_student} , Highest marks : {highest_marks}")
# print(f"Lowest student : {lowest_student} , Lowest marks : {lowest_marks}")
# avg = total / count
# print(avg)







# Question 3: Find Duplicate Records 
# You are given a file containing student names.
# Ali
# Ahmed
# Ali
# Usman
# Ahmed
# Sara
# Task
# Print only the duplicate names.

# orignal = set()
# duplicate = set()
# with open("Phase 1\\1.5 Files & Data Formats\\txt\\duplicate.txt","r") as file:
#     for line in file:
#         name = line.strip()
#         # print(name)
#         if name in orignal:
#             duplicate.add(name)
#         else:
#             orignal.add(name)
# print(duplicate)







# Question 4: Search in a File 
# A user enters a keyword.
# Python
# Task
# Search the file and print:
# Line number
# Complete line

# with open("Phase 1\\1.5 Files & Data Formats\\txt\\txt_task.txt","r") as f:
#     for index,line in enumerate(f,start=1):
#         if "Python" in line:
#             print(f"Line {index}:")
#             print(line)




# Question 5: Word Frequency
# Given a text file,
# Task
# Without using:
# collections.Counter
# count()
# Find:
# Most frequent word
# Least frequent word

# frequency = {}
# with open("Phase 1\\1.5 Files & Data Formats\\txt\\txt_task.txt","r") as f:
#     for line in f:
#         words = line.strip().split()
#         # print(words)
#         for word in words:
#             if word in frequency:
#                 frequency[word]+=1
#             else:
#                 frequency[word]=1
# # print(frequency)
# most_frequent = ""
# least_frequent = ""
# most_count=0
# least_count=None
# for i in frequency:
#     # print(i)
#     # print(frequency[i])
#     if frequency[i] > most_count:
#         most_count = frequency[i]
#         most_frequent = i
#     if least_count is None or frequency[i] < least_count:
#         least_count = frequency[i]
#         least_frequent = i
# print("Most Frequent Word:", most_frequent, "-", most_count)
# print("Least Frequency words : ")
# for i in frequency:
#     if frequency[i] == least_count:
#         print(f"{i} : {least_count}")







# Question 6: Mini Login System
# Given a file:
# Ali,1234
# Ahmed,abcd
# Sara,pass
# Task
# Ask the user for:
# Username
# Password
# Print:
# Login Successful
# or
# Invalid Username or Password

# username = input("Enter Username: ")
# password = input("Enter Password: ")
# login = False
# with open("Phase 1\\1.5 Files & Data Formats\\txt\\login.txt","r") as f:
#     for line in f:
#         data = line.strip().split(",")
#         file_username = data[0]
#         file_password = data[1]
#         if username == file_username and password == file_password:
#             login = True
#             break
# if login:
#     print("Login Successful")
# else:
#     print("Invalid username or password")







# Question 7: Merge Two files
# Task
# Merge both files into:
# merge.txt
# without duplicate names.

# new_file = set()
# with open("Phase 1\\1.5 Files & Data Formats\\txt\\log.txt","r") as f:
#     for line in f:
#         new_file.add(line.strip())
# with open("Phase 1\\1.5 Files & Data Formats\\txt\\login.txt","r") as f:
#     for line in f:
#         new_file.add(line.strip())
# with open("Phase 1\\1.5 Files & Data Formats\\txt\\merge.txt","w") as f:
#     for i in new_file:
#         f.write(i+"\n")
# print("File merged")







# Question 9: Student Database (CRUD)
# Create a menu-driven program.
# 1. Add Student
# 2. Search Student
# 3. Update Student
# 4. Delete Student
# 5. Exit
# Store all data in:
# students.txt
# Every change should be saved to the file.

filepath = "Phase 1\\1.5 Files & Data Formats\\txt\\student.txt"
def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    with open(filepath , "a") as f:
        f.write(f"{student_id},{name},{marks}"+"\n")
    print("Student Added")

def search_student():
    search = input("Enter student id : ")
    found = False
    with open(filepath,"r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == search:
                print("\nStudent Found")
                print("ID:", data[0])
                print("Name:", data[1])
                print("Marks:", data[2])
                found = True
                break
    if not found:
        print("Student Not Found")

def update_student():
    student_id = input("Enter Student ID: ")
    students = []
    found = False
    with open(filepath,"r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0]==student_id:
                data[1]=input("Enter new name : ")
                data[2]=input("Enter new marks : ")
                found = True
            students.append(",".join(data))
    with open(filepath,"w") as f:
        for student in students:
            f.write(student + "\n")
    print("Student Updated")                
    if not found:
         print("Student not found")

def delete_student():
    student_id = input("Enter Student ID: ")
    students = []
    found = False
    with open(filepath,"r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0]!=student_id:
                students.append(",".join(data))
            else:
                found=True
    with open(filepath,"w") as f:
        for student in students:
            f.write(student+"\n")
    if found:
        print("Student Deleted Successfully.")
    else:
        print("Student Not Found")

while True :
    print('''Select Any of the following :-
    1. Add Student
    2. Search Student
    3. Update Student
    4. Delete Student
    5. Exit
    ''')
    user_input = int(input("Enter choice : "))
    if user_input == 1:
        add_student()
    elif user_input == 2:
        search_student()
    elif user_input == 3:
        update_student()
    elif user_input == 4:
        delete_student()
    elif user_input == 5:
        print("Program Ended.")
        break
    else:
        print("Invalid Choice")
