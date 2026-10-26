# Exercise 1: Even or Odd
# Concept: if-else
# Write a program that asks the user for an integer and prints:
# "Even" if the number is even.
# "Odd" otherwise.

# num = int(input("Enter a number : "))
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")



# Exercise 2: Largest of Three Numbers
# Concept: Nested conditions
# Take three integers from the user and print the largest number.
# Example
# Input:
# 5
# 9
# 2
# Output:
# 9

# num1 = int(input("Enter 1st number : "))
# num2 = int(input("Enter 1st number : "))
# num3 = int(input("Enter 1st number : "))
# num = []
# for i in range(1,4):
#     number = int(input(f"Enter num {i} : "))
#     num.append(number)
# if num[0] > num[1]:
#     if num[0] > num[2]:
#         print(f"Largest number is {num[0]}")
#     else:
#         print(f"Largest number is {num[2]}")
# else:
#     if num[1] > num[2]:
#         print(f"Largest number is {num[1]}")
#     else:
#         print(f"Largest number is {num[2]}")





# Exercise 3: Leap Year Checker
# Concept: Multiple conditions
# Ask the user for a year and determine whether it is a leap year.
# Rules:
# Divisible by 400 → Leap Year
# Divisible by 100 → Not Leap Year
# Divisible by 4 → Leap Year
# Otherwise → Not Leap Year


# year = int(input("Enter year : "))
# if year%400 == 0:
#     print("Leap year")
# elif year%100 == 0:
#     print("not a leap year")
# elif year%4 == 0:
#     print("Leap year")
# else:
#     print("not a leap year")



# Exercise 4: Multiplication Table
# Concept: for loop
# Ask the user for a number and print its multiplication table from 1 to 10.
# Example:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

# num = int(input("Enter num : "))
# # for i in range(10,0,-1):
# for i in range(1,11):
#     print(f"{i} x {num} = {i*num}")




# Exercise 5: Sum of Even Numbers
# Concept: Loop + condition
# Ask the user for a number n.
# Find the sum of all even numbers from 1 to n.

# num = int(input("Enter num : "))
# num_list = []
# for i in range(1,num+1):
#     num_list.append(i)
# even_list = []
# for number in num_list:
#     if number%2==0:
#         even_list.append(number)
# print(f"Sum of even numbers from 1 to {num} is {sum(even_list)}")




# Exercise 6: Count Digits
# Concept: while loop
# Ask the user for an integer.
# Count how many digits it contains.
# Example:
# Input:
# 54321
# Output:
# 5

# num = int(input("Enter number : "))
# i=0
# while num>0:
#     # mod = num%10
#     num = num // 10
#     # print(mod)
#     # print(num)
#     i+=1
# print(i)




# Exercise 7: Reverse a Number
# Concept: while loop
# Take an integer from the user and print its reverse.
# Example:
# Input:
# 12345
# Output:
# 54321



# num = int(input("Enter number : "))
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print(reverse)




# Exercise 8: Prime Number Checker
# Concept: Loop + condition
# Ask the user for an integer.
# Print whether it is a prime number.


# num = int(input("Enter number : "))
# count = 0
# for i in range(1,num+1):
#     # print(f"for loop {num%i}")
#     if num%i==0:
#         # print(num%i)
#         count +=1
# if count == 2:
#     print("It's prime number")
# else:
#     print("It's not a prime number")





# Exercise 9: Fibonacci Series
# Concept: Loops
# Ask the user for n.
# Print the first n Fibonacci numbers.
# Example:
# Input:
# 10
# Output:
# 0 1 1 2 3 5 8


# num = int(input("Enter number : "))
# a = 0
# b = 1
# for i in range(num):
#     print(a)
#     c = a+b
#     a = b
#     b = c





# Exercise 10: Pattern Printing
# Concept: Nested loops
# Print the following pattern for a given n.
# Example (n = 5)
# *
# **
# ***
# ****
# *****


# num = int(input("Enter number : "))

# for i in range(1, num+1):
#     # print(f"{"* "*i}")
#     for j in range(i):
#         print("*", end="")
#     print()





# Exercise 11: List of Squares
# Concept: List comprehension
# Given:
# numbers = [1,2,3,4,5,6,7,8,9,10]
# Create a new list containing the square of every number using a list comprehension.


# numbers = [1,2,3,4,5,6,7,8,9,10]
# square_num = [num**2 for num in numbers]
# print(square_num)




# Exercise 12: Filter Even Numbers
# Concept: List comprehension with condition
# Given:
# numbers = [12,5,8,17,20,31,44,50]
# Create a list containing only the even numbers using a list comprehension.


# numbers = [12,5,8,17,20,31,44,50]
# even_list = [num  for num in numbers if num%2==0]
# print(even_list)





# Exercise 13: Multiples of 3 and 5
# Concept: List comprehension + conditions
# Generate a list of numbers from 1 to 100 that are divisible by both 3 and 5.


# mul_list = [num for num in range(1,101) if num%3==0 or num%5==0]
# print(mul_list)





# Exercise 14: Flatten a Nested List
# Concept: Nested list comprehension
# Given:
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# Create a single list containing all elements in order using a nested list comprehension.
# Expected output:
# [1,2,3,4,5,6,7,8,9]

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# single_list = [i for mini_list in matrix for i in mini_list]
# print(single_list)






# Exercise 15: FizzBuzz
# Concept: Conditions + loops
# Print numbers from 1 to 100.
# Rules:
# If divisible by 3, print "Fizz"
# If divisible by 5, print "Buzz"
# If divisible by both, print "FizzBuzz"
# Otherwise, print the number.
# Example:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# ...
# 14
# FizzBuzz
# ...



# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)




# Print all Armstrong numbers between 0 and 10000
# for number in range(0,10001):
#     num = number
#     orignal_num = num
#     i=0
#     mod_list = []
#     while num>0:
#         mod = num%10
#         num = num // 10
#         mod_list.append(mod)
#         i+=1
#     # print(mod_list)
#     armstrong_list = []
#     for n in mod_list:
#         power_list = n**len(mod_list)
#         armstrong_list.append(power_list)
#     sum_arm = sum(armstrong_list)
#     if sum_arm == orignal_num:
#         print(f"{orignal_num} is armstrong number")
#     else:
#         pass


# Find the second largest number in a list without using sort().
# num = [44,32,34,51,67,23,12,53]
# largest = num[0]
# sec_largest = num[0]
# for n in num:
#     if n > largest:
#         sec_largest = largest
#         largest = n
#     elif n>sec_largest and n!=largest:
#         sec_largest=n
# print(sec_largest)




# Generate Pascal's Triangle using nested loops.

# num = int(input("Enter number of rows: "))

# for i in range(num):
#     # print(num - i - 1)
#     for j in range(num - i - 1):
#         print(" ", end="")
#     n=1
#     for j in range(i+1):
#         print(n, end=" ")
#         n = n * (i-j)//(j+1)
#     print()




# Create a list comprehension that produces all (x, y) pairs where x + y is even.

# x = [1, 2, 3]
# y = [4, 5, 6]

# # for i in x:
# #     for j in y:
# #         if (i+j)%2==0:
# #             print(i,j)
# even_list = [[i,j] for i in x for j in y if (i+j)%2==0]
# print(even_list)




# Print a diamond star pattern using nested loops.


num = int(input("Enter number of rows: "))
for i in range(num):
    # print(num - i - 1)
    for j in range(num - i - 1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(num):
    # print(i)
    for j in range(i):
        print(" ", end="")
    for j in range(num-i):
        print("*", end=" ")
    print()