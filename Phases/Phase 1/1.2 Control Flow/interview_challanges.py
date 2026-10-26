# Reverse a number without slicing.
# Reverse a string using loops.
# Check palindrome.
# Check Armstrong number.
# Find factorial.
# Find GCD.
# Print Fibonacci.
# Print prime numbers from 1–100.
# Find second largest element.
# Remove duplicates without set().
# Rotate a list.
# Count vowels.
# Count frequency without count().
# Matrix multiplication.



# Reverse a number without slicing.

# num = 5674
# reverse = 0 
# while num>0:
#     last_num = num%10
#     reverse = reverse*10+last_num
#     num = num//10
# print(f"Reversed : {reverse}")

# time complexity of while loop in it is O(n) and n is the last_num so it's time complexity is o(1)




# Reverse a string using loops.
# string = "this is string"
# reverse_string = ""
# # for i in range(len(string)-1,-1,-1):
# #     # print(i)
# #     reverse_string += string[i]
# for i in string:
#     reverse_string = i + reverse_string
# print(reverse_string)

# for loop time complexity is o(n) and n is the characters
# Time complexity: O(n²) (Python string concatenation ki wajah se)
# Space complexity: O(n)





# Check palindrome.
# # for simple string 
# orignal = "1221"
# palindrome = ""
# for i in orignal:
#     palindrome = i + palindrome
# print(palindrome)
# if orignal == palindrome:
#     print(f"{palindrome} is palindrome")
# else:
#     print(f"{orignal} is not a palindrome")

# # for phrases included symbols 
# orignal = "Was it a car or a cat I saw?"
# clean = ""
# for i in orignal:
#     if i.isalnum():
#         clean+=i.lower()
# print(clean)
# palindrome = ""
# for i in clean:
#     palindrome = i + palindrome
# if clean == palindrome:
#     print("Palindrome")
# else:
#     print("Not a palindrome")






# Check Armstrong number.
# num = 153
# original = num
# digits = 0
# temp = num
# while temp > 0:
#     digits += 1
#     temp //= 10
# print(digits)
# print(temp)
# total = 0
# temp = num
# while temp > 0:
#     digit = temp%10
#     # print(digit)
#     total += digit**digits
#     temp //= 10
#     # print(total)
#     # print(temp)
# if total == original:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")









# Find factorial.
# num = 5
# fac = 1
# for i in range(num,0,-1):
#     fac*=i
# print(fac)









# Find GCD.(Greatest Common Divisor)
# num1 = 12
# num2 = 18
# gcd=1
# small = min(num1,num2)
# for i in range(1,small+1):
#     # print(i)
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i
# print("GCD is :", gcd)








# Print Fibonacci.
# num = 10
# first = 0
# second = 1
# fab = []
# for i in range(1,num+1):
#     addition = first+second
#     first = second
#     second = addition
#     fab.append(addition)
# print(fab)





# Print prime numbers from 1–100.
# for i in range(2,101):
#     prime = True
#     for j in range(2,i):
#         if i%j==0:
#             prime = False
#     if prime:
#         print(i)







# Find second largest element.
# numbers = [32,23,43,23,12,32,35,54,65,56]
# largest_num = numbers[0]
# second_largest_num = numbers[0]
# for i in numbers:
#     # print(i)
#     if largest_num<i:
#         second_largest_num = largest_num
#         largest_num = i
#     elif i>second_largest_num and i!=second_largest_num:
#         second_largest_num = i
# print(largest_num)
# print(second_largest_num)




# Remove duplicates without set().
# numbers = [2, 3, 2, 5, 3, 3, 7, 2]
# new_num = []
# for i in numbers:
#     # print(i)
#     if i not in new_num:
#         new_num.append(i)
# print(new_num)



# Rotate a list. (last element sends to first)
# numbers = [1, 2, 3, 4, 5]
# rotate_list = []
# rotate_list.append(numbers[-1])
# print(rotate_list)
# for i in range(len(numbers)-1):
#     rotate_list.append(numbers[i])
# print(rotate_list)





# Count vowels.
# text = "this is a tExt"
# vowels = 'aeiou'
# count = 0
# for ch in text:
#     print(ch)
#     if ch.lower() in vowels:
#         count +=1
# print(count)







# Count frequency without count().
# orignal_list = [1,2,2,3,1,4,2,5,5]
# counted = []
# for n in orignal_list:
#     if n not in counted:
#         count = 0
#         for j in orignal_list:
#             # print("j",j)
#             if n == j:
#                 count+=1
#         print(n, " -> ",count)
#         counted.append(n)
# print(counted)






# Matrix multiplication.
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
result = []
for i in range(3):
    # print(matrix1[i])
    row = []
    for j in range(3):
        mul = matrix1[i][j] * matrix2[i][j]
        # print(mul)
        row.append(mul)
    # print(row)
    result.append(row)
print(result)
