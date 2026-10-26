# Task 21 – Cricket Stats
# Take:
# Runs
# Balls Faced
# Display Strike Rate.

# runs = int(input("Enter Runs : "))
# balls_faced = int(input("Enter Balls Faced : "))

# strike = round((runs/balls_faced)*100 , 2)

# print(f"Strike rate is : {strike}")




# Task 22 – Movie Ticket
# Take:
# Number of Tickets
# Price per Ticket
# Display Total Cost.

# tickets = int(input("Enter Number of Tickets : "))
# price = int(input("Enter Price per Ticket : "))
# print(f"Total cost : {tickets*price}")



# Task 23 – Mobile Recharge
# Take:
# Recharge Amount
# Display:
# Tax
# Final Amount

# amount = int(input("Enter Recharge Amount : "))
# tax = amount*0.10
# print(f"Total tax : {tax}")
# print(f"Total balance : {amount - tax}")


# Task 24 – Pizza Party
# Take:
# Number of People
# Total Pizza Slices
# Display how many slices each person gets(equal slices) and how many remain.

# people = int(input("Enter Number of People : "))
# slices = int(input("Enter Total Pizza Slices : "))
# divi = slices//people
# remain = slices % people
# print(f"slices each person gets : {divi}")
# print(f"slices remain : {remain}")



# Task 25 – Student Report
# Take:
# Name
# Roll Number
# Marks in 6 Subjects
# Display a formatted report including:
# Total
# Average
# Percentage


# name = str(input("Enter Name : "))
# roll_number = int(input("Enter Roll Number : "))
# marks = []
# for i in range(1,7):
#     mark = int(input(f"Enter marks of subject {i} : "))
#     marks.append(mark)

# total = sum(marks)
# avg = round(total / len(marks) , 2)
# per = round((total / 550) * 100 , 2)

# print(f"Total marks : {total}")
# print(f"Average : {avg}")
# print(f"Percentage : {per}%")




# Swap two numbers.
a = 10
b = 20
print(a)
print(b)
a,b = b,a 
print(a)
print(b)

