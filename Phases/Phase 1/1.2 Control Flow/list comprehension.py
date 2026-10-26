# List comprehension = A concise way to create lists in Python Compact 
#                      and easier to read than traditional loops 
#                      [expression for value in iterable if condition]  
# doubles = [x * 2 for x in range(1, 11)]
# print(doubles)

# fruits = ["apple", "orange", "banana", "coconut"] 
# fruit_chars = [fruit[0].upper() for fruit in fruits] 
# print(fruit_chars)


# numbers = [0, 1, -2, -3, 4, 5, -6, ] 
# positive_nums = [num for num in numbers if num >= 0] 
# negative_nums = [num for num in numbers if num < 0]  
# print(positive_nums)
# print(negative_nums)





nums = (i for i in range(5))
print(nums)
print(list(nums))