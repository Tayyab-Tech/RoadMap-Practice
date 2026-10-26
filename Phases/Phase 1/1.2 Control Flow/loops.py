# Exercise 1: Find the Second Largest Number
# Concept: Loops + Conditions
# Take n integers from the user.
# Find the second largest number without using:
# sort()
# max()


# number = [12,324,43,4543,432,2314,3245,6432,2432,43,453]
# l_number = number[0]
# sl_number = number[0]

# for n in number:
#     if n > l_number:
#         sl_number = l_number
#         l_number = n
#     elif n > l_number and n!=l_number:
#         sl_number = n
# print(sl_number)




# Exercise 2: Remove Duplicate Values
# Concept: Loops
# Take a list from the user.
# Create a new list that contains only unique values while preserving the original order.
# Example
# Input:
# [1,2,2,3,1,4,5,5]
# Output:
# [1,2,3,4,5]
# Constraint: Don't use set().

# # orignal_list = [1,2,2,3,1,4,2,5,5]
# orignal_list = list(map(int, input("Enter numbers separated by space: ").split()))
# new_list = []
# for n in orignal_list:
#     if n not in new_list:
#         new_list.append(n)
# print(new_list)




# Exercise 3: Frequency Counter
# Concept: Nested Loops
# Take a list of integers.
# Print how many times each element appears.
# Example
# Input:
# [2,3,2,5,3,3]
# Output:
# 2 -> 2
# 3 -> 3
# 5 -> 1
# Constraint: Don't use count() or dictionaries.

# orignal_list = [1,2,2,3,1,4,2,5,5]
# counted = []
# for n in orignal_list:
#     # print("nnnnnnn",n)
#     if n not in counted:
#         count = 0
#         for j in orignal_list:
#             # print("j",j)
#             if n == j:
#                 count+=1
#         print(n, " -> ",count)
#         counted.append(n)
# print(counted)



# Exercise 4: Longest Increasing Sequence
# Concept: Loops
# Given a list of numbers, find the length of the longest consecutive increasing sequence.
# Example:
# Input:
# [2,4,5,7,9,3,6,10,15,20,11,12] 
# Output:
# 6
# Because:
# 4,5,7,8 ❌
# Actual increasing consecutive elements are:
# [2, 3, 4, 5, 6, 7]
# (Define your own increasing logic carefully.)

# orignal_list = [2,4,5,7,9,3,6,10,15,20,11,12] 
# numset = set(orignal_list)
# longest = 0
# longest_list = []
# for n in orignal_list:
#     if (n-1) not in numset:
#         length = 0
#         current_list = []
#         while (n+length) in numset:
#             current_list.append(n + length)
#             length+=1
#         if length > longest:
#             longest = length
#             longest_list = current_list
# print("Length:", longest)
# print("Sequence:", longest_list)




# Exercise 5: Matrix Addition
# Concept: Nested Loops
# Take two 3×3 matrices.
# Print their sum.
# Example
# 1 2 3
# 4 5 6
# 7 8 9
# +
# 9 8 7
# 6 5 4
# 3 2 1
# Print the resulting matrix.


# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]
# result = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         one = matrix1[i][j]
#         two = matrix2[i][j]
#         sum_matrix = one+two
#         # print("one",one)
#         # print("two",two)
#         # print("sum",sum_matrix)
#         row.append(sum_matrix)
#     result.append(row)
# print(result)





# Exercise 6: Diamond Pattern
# Concept: Nested Loops
# Print a full diamond.
# Example
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# Do not hardcode spaces or stars.

# num = 5
# for i in range(0,num):
#     # print("*"*i)
#     for j in range(num-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(0,num):
#     # print("*"*i)
#     for j in range(i):
#         print(" ",end="")
#     for j in range(num-i):
#         print("*",end=" ")
#     print()





# Exercise 7: Spiral Pattern
# Concept: Nested Loops
# For a given n, print numbers in spiral order.
# Example (n = 4)
# 1  2  3  4
# 12 13 14 5
# 11 16 15 6
# 10 9  8  7



# n = 4
# matrix = [[0] * n for i in range(n)]
# top = 0
# bottom = n - 1
# left = 0
# right = n - 1
# num = 1
# while top <= bottom and left <= right:
#     # Left → Right
#     for i in range(left,right+1):
#         matrix[top][i] = num
#         # print("tttttttt",top)
#         # print("ii1",i)
#         num+=1
#     top+=1
#     # Top → Bottom
#     for i in range(top, bottom + 1):
#         matrix[i][right] = num
#         # print("rrrrrrr",right)
#         # print("ii2",i)
#         num += 1
#     right -= 1
#     # Right → Left
#     if top <= bottom:
#         for i in range(right, left - 1, -1):
#             matrix[bottom][i] = num
#             # print("bbbbbb",bottom)
#             # print("ii3",i)
#             num += 1
#         bottom -= 1
#     # Bottom → Top
#     if left <= right:
#         for i in range(bottom, top - 1, -1):
#             matrix[i][left] = num
#             # print("lllllll",left)
#             # print("ii4",i)
#             num += 1
#         left += 1
# for row in matrix:
#     for value in row:
#         print(f"{value:2}", end=" ")
#     print()




# Exercise 9: Magic Square Checker
# Concept: Nested Loops
# Take a 3×3 matrix.
# Check whether it is a Magic Square.
# A Magic Square has:
# Equal row sums
# Equal column sums
# Equal diagonal sums
# Print:
# Magic Square
# or
# Not Magic Square


# matrix = [
#     [8, 1, 6],
#     [3, 5, 7],
#     [4, 9, 2]
# ]
# target = sum(matrix[0])
# # print(target)
# magic = True
# for i in range(3):
#     row_sum = 0
#     for j in range(3):
#         row_sum += matrix[i][j]
#     # print(row_sum) #row checked
#     if row_sum != target:
#         magic = False

# for i in range(3):
#     col_sum = 0
#     for j in range(3):
#         col_sum += matrix[j][i]
#     # print(col_sum) column checked
#     if col_sum != target:
#         magic = False
# diag1 = 0
# for i in range(3):
#     # print(i,i)
#     diag1 += matrix[i][i]
#     # print(diag1)
# # print(diag1)
# diag2 = 0
# for i in range(3):
#     print(i,2-i)
#     diag2 += matrix[i][2 - i]
#     # print(diag1)
# # print(diag1)
# if diag1 != target or diag2 != target:
#     magic = False
# if magic:
#     print("Magic Square")
# else:
#     print("Not Magic Square")





# Exercise 10: Tic-Tac-Toe Winner
# Concept: Nested Loops + Conditions
# Given a 3×3 board containing:
# X
# O
# _
# Determine whether:
# X wins
# O wins
# Draw
# Game not finished


# board = [
#     ['X', 'O', 'X'],
#     ['O', '_', 'O'],
#     ['X', 'X', 'X']
# ]
# x_wins = False
# o_wins = False
# # Check rows
# for row in board:
#     if row[0] != '_' and row[0] == row[1] == row[2]:
#         if row[0] == 'X':
#             x_wins = True
#         elif row[0] == 'O':
#             o_wins = True
# # Check columns
# for col in range(3):
#     if board[0][col] != '_' and board[0][col] == board[1][col] == board[2][col]:
#         if board[0][col] == 'X':
#             x_wins = True
#         elif board[0][col] == 'O':
#             o_wins = True
# # Check main diagonal
# if board[0][0] != '_' and board[0][0] == board[1][1] == board[2][2]:
#     if board[0][0] == 'X':
#         x_wins = True
#     elif board[0][0] == 'O':
#         o_wins = True
# # Check secondary diagonal
# if board[0][2] != '_' and board[0][2] == board[1][1] == board[2][0]:
#     if board[0][2] == 'X':
#         x_wins = True
#     elif board[0][2] == 'O':
#         o_wins = True
# # Final Result
# if x_wins and o_wins:
#     print("Invalid Board")
# elif x_wins:
#     print("X Wins")
# elif o_wins:
#     print("O Wins")
# elif any('_' in i for i in board):
#     print("Game Not Finished")
# else:
#     print("No Winner")




# enumerate funtion 
names = ["Ali","Ahmed"]

for index, name in enumerate(names):
    print(index, name)

# zip funtion 
names = ["Ali","Ahmed"]
marks = [90,85]

for n,m in zip(names, marks):
    print(n,m)


