# sort() original list ko permanently sort karta hai. 

numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)


# Descending Order 
numbers = [40, 10, 30, 20]
numbers.sort(reverse=True)
print(numbers)

# strings sort alphabetically
names = ["Usman", "Ali", "Ahmed"]
names.sort()
print(names)
# sort returns None 


# sorted()--> original list ko change nahi karta.
# Ye new sorted list return karta hai.
# return new sorted list 
numbers = [40, 10, 30]
new_list = sorted(numbers)
print(new_list)
print(numbers)

# descending 
numbers = [10,30,20]
print(sorted(numbers, reverse=True))


# reverse()--> list ka current order ulta karta hai.

numbers = [10,30,20]
numbers.reverse()
print(numbers)
# Returns None 


# reversed()---> original list ko change nahi karta.
# Ye ek iterator return karta hai.
numbers = [10,30,20]
x = reversed(numbers)
print(x) #---> return iterator object
print(list(x))
