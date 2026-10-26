# Joining Lists --> +,extend(),*

# + Operator
# Do ya zyada lists ko join karta hai aur new list return karta hai.
# Original lists change nahi hotin.
# syntax : new_list = list1 + list2

a = [10,20]
b = [30,40]
c = a + b
print(c)


# extend()
# Dusri list ke tamam items ko current list ke end mein add karta hai.
# Original list modify hoti hai.
a = [1,3]
b = [2,4]
a.extend(b)
print(a)

# | +                         | extend()                       |
# | ------------------------- | ------------------------------ |
# | New list return karta hai | Original list modify karta hai |
# | Original safe             | Original change hoti hai       |
# | Slower (new memory)       | Faster (in-place)              |


# * Operator
# List ko repeat karta hai.
# Join nahi karta.

numbers = [1,2]
print(numbers * 3)

matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)
# don't do that
matrix = [[0 for _ in range(3)] for _ in range(3)] #do this
matrix[0][0]=1
print(matrix)