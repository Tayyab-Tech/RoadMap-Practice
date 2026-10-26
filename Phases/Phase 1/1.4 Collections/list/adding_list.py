# Adding Elements
# append() 
numbers = [1, 2]
numbers.append(3)
numbers.append([4, 5]) # multiple elements as 1 item in list
print(numbers)
# append return None 

# extend() 
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

fruits = ["Apple"]
fruits.extend(["Banana", "Orange"])
print(fruits)

# String is iterable
letters = ["A"]
letters.extend("BC")
print(letters)
# extend return None 

# append() = ek item add karta hai
# extend() = iterable ke tamam items add karta hai


# insert()
names = ["Ali", "Usman"]
names.insert(1, "Ahmed") #(1,"ahmed") 1 is index and ahmed is item which is inserted in list 
# if index is greater than actual indexex of list than it add item at the end of list
print(names)
# Negative index
numbers = [10, 20, 30]
numbers.insert(-1, 99)
print(numbers)
# insert return None