# Debug a program with nested loops producing incorrect multiplication tables.
for i in range(1, 6):
    for j in range(1, 11):
        print(i + j, end="\t")
    print()
# it prints addition 
# change the inner loop print statement with this 
# print(i * j, end="\t")






# Fix a student grading program where percentages are calculated incorrectly.
marks = 350
total = 500
percentage = total / marks * 100
print("Percentage:", percentage)
# wrong formula 
# correct formula is  
percentage = (marks / total) * 100






# Debug a recursive Fibonacci function that never stops.
def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5))
# no base conditon occur so program never stops....correct function is below 
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5))






# Find and fix multiple bugs in a file-processing program.
file = open("numbers.txt", "r")
total = 0
for line in file:
    total += line
print(total)
file.close()
# line is string so it give error because string never added integer 
try:
    file = open("numbers.txt", "r")
    total = 0
    for line in file:
        try:
            total += int(line.strip())
        except ValueError:
            print("Invalid number:", line.strip())
    file.close()
    print("Total =", total)
except FileNotFoundError:
    print("File not found.")







# Debug a menu-driven banking application containing syntax, runtime, and logical errors.
balance = 5000
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == 1:
        amount = int(input("Amount: "))
        balance = amount
    elif choice == 2:
        amount = int(input("Amount: "))
        if amount > balance:
            print("Insufficient Balance")
        else:
            balance = amount
    elif choice == 3:
        break
# in this some logical error which fixes below 
balance = 5000
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        amount = float(input("Amount: "))
        balance += amount
        print("Deposit Successful")
    elif choice == "2":
        amount = float(input("Amount: "))
        if amount > balance:
            print("Insufficient Balance")
        else:
            balance -= amount
            print("Withdrawal Successful")
    elif choice == "3":
        print(f"Available balance = {balance}")
    elif choice == "4":
        print("Program ended")
        break
    else:
        print("Invalid choice")