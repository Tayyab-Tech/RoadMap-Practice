# Task 1
# numbers = [10,20,30,20,10,40,50,40]
# Duplicate remove karo without using set().

# numbers = [10,20,30,20,10,40,50,40]
# orignal = []
# for n in numbers:
#     if n not in orignal:
#         orignal.append(n)
# print(orignal)




# Task 2
# numbers = [5,8,2,10,1,7]
# Second largest number find karo.

# without sort 
# numbers = [5,8,2,10,1,7]
# largest = numbers[0]
# sec_largest = numbers[0]
# for i in numbers:
#     if largest<i:
#         sec_largest = largest
#         largest = i
#     elif i == sec_largest and i != sec_largest:
#         sec_largest = i
# print(sec_largest)
# # with sort 
# numbers.sort()
# print(numbers[-2])



# Task 3
# Ek list ko reverse karo without using reverse() ya [::-1].

# numbers = [1,2,3,4,5]
# # numbers.reverse()
# # print(numbers)
# reverse_list = []
# for i in range(len(numbers)-1,-1,-1):
#     # print(i)
#     reverse_list.append(numbers[i])
# print(reverse_list)



# Task 4
# a = [1,2,3,4]
# b = [3,4,5,6]
# Common elements nikalo.

# a = [1,2,3,4]
# b = [3,4,5,6]
# common = []
# for i in a:
#     if i in b:
#         common.append(i)
# print(common)



# Task 5
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# Sab numbers ka sum nikalo.

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # total = sum(j for i in matrix for j in i)
# # print(total)
# total = 0
# for i in matrix:
#     for j in i:
#         total+=j
# print(total)





# Task 6
# Ek list mein sirf even numbers ki new list banao.

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even = []
# for i in numbers:
#     if i%2==0:
#         even.append(i)
# print(even)



# Task 7
# Ek list mein maximum aur minimum ka difference nikalo.

# numbers = [5,8,6,12,10,4,7,14,11,19]
# # maximum = max(numbers)
# # minimum = min(numbers)
# # difference = maximum - minimum
# # print(difference)
# maximum = numbers[0]
# minimum = numbers[0]
# for i in numbers:
#     if i>maximum:
#         maximum = i
#     if i<minimum:
#         minimum = i
# print("Differnce between maximum and minimum : ", maximum-minimum)



# Task 8
# Ek list ko rotate karo.

# number = [1,2,3,4,5]
# last = number[-1]
# print(last)
# number.pop()
# number.insert(0,last)
# print(number)




# Task 9
# Ek list mein har element kitni baar aaya hai dictionary ki form mein nikalo.
# Example
# [1,2,1,3,2,2]
# Output
# {
# 1:2,
# 2:3,
# 3:1
# }

# num = [1,2,1,3,2,2]
# frequency = {}
# for n in num:
#     if n in frequency:
#         frequency[n]+=1
#     else:
#         frequency[n]=1
# for key, value in frequency.items():
#     print(f"{key}: {value}")



# Task 10 
# Without using sort()
# Bubble Sort implement karo.

numbers = [78, 23, 45, 12, 89, 34, 67, 90, 11, 56, 43, 29, 88, 15, 72]
n = len(numbers)
for i in range(n):
    # print("iiii",i)
    for j in range(n-i-1):
        # print("jj",j)
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1],numbers[j]
print(numbers)
        
