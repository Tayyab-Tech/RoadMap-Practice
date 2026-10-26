# Write a program to calculate the sum of all values in the tuple.
# numbers = (12,15,20,30,18)
# # total = sum(numbers)
# # print(total)
# total = 0
# for i in numbers:
#     total+=i
# print(total)






# Question 2
# Convert the following tuple into a list, replace 20 with 100, and convert it back into a tuple.
# numbers = (10, 20, 30, 40)
# numbers_list = list(numbers)
# for i in range(len(numbers_list)):
#     if numbers_list[i] == 20:
#         numbers_list[i] = 100
# numbers = tuple(numbers_list)
# print(numbers)





# Question 3
# Count how many times 10 appears.

# numbers = (10,20,30,10,40,10)
# count = 0
# for i in numbers:
#     if i == 10:
#         count+=1
# print(f"10 appears '{count}' times in this tuple")





# Question 4
# Find the largest and smallest values.

# numbers = (22,45,11,78,35)
# smallest = numbers[0]
# largest = numbers[0]
# for i in numbers:
#     if i > largest:
#         largest = i
#     if i < smallest:
#         smallest = i
# print(largest)
# print(smallest)




# Question 5
# Reverse the tuple.

# numbers = (1,2,3,4,5)
# rev_list = []
# for i in range(len(numbers)-1,-1,-1):
#     rev_list.append(numbers[i])
# rev_tuple = tuple(rev_list)
# print(rev_tuple)




# Question 6
# Using tuple unpacking, store the first value in first, the last value in last, and all remaining values in middle.

# numbers = (10,20,30,40,50)
# first,*middle,last = numbers
# print(first)
# print(middle)
# print(last)




# Question 7
# Access and print 40 from the following nested tuple.

# data = (
#     (10,20),
#     (30,40),
#     (50,60)
# )
# print(data[1][1])




# Question 8
# Join the following tuples.

# t1 = (1,2,3)
# t2 = (4,5,6)
# a = t1 + t2
# print(a)




# Question 9
# Check whether all values in the tuple are unique.

# numbers = (10,20,30,20,40)
# unique = True
# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i]==numbers[j]:
#             unique = False
#             break
# if unique:
#     print("All values are unique")
# else:
#     print("Duplicate values found")






# Question 10
# Convert the following tuple into a dictionary.

student = (
    ("Ali",80),
    ("Ahmed",90),
    ("Usman",70)
)
dic = dict(student)
print(dic.get("Ahmed"))
print(dic)