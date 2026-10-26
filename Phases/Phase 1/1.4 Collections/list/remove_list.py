# Removing Elements
# remove() ----> value ke basis par list se pehli matching value remove karta hai.
fruits = ["Apple", "Banana", "Orange","Banana"]
fruits.remove("Banana")
print(fruits)
# remove return None


# pop()---> index ke basis par item remove karta hai aur removed item return bhi karta hai.
numbers = [10, 20, 30]
numbers.pop(1)
print(numbers)
# pop only returns removed item 
numbers = [90, 80, 70]
deleted = numbers.pop(1)
print(deleted)
print(numbers)
# if no index given last item popped and wrong index gives index error




# del is not a method.
# Ye Python ka keyword hai.
# Ye variables bhi delete karta hai aur list items bhi.
numbers = [10, 20, 30]
del numbers[1]
print(numbers)
# Multiple items
numbers = [10, 20, 30, 40, 50]
del numbers[1:4]
print(numbers)
# Whole list delete 
numbers = [10, 20]
del numbers
# print(numbers) # show name error 


# clear()
# List ke andar ke saare elements remove kar deta hai.
# Lekin list object exist karta rehta hai.
numbers = [10, 20, 30]
numbers.clear()
print(numbers)
# clear() Return None 