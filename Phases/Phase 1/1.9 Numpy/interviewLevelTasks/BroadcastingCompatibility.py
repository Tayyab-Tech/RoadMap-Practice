# Broadcasting Compatibility

# Without running the code first, determine whether these operations work:

# A = np.ones((3, 4))
# B = np.ones((4,))
# A + B

# Then determine whether this works:

# A = np.ones((3, 4))
# B = np.ones((3,))

# Explain why one works and the other doesn't.


import importlib
np = importlib.import_module("numpy")


a = np.ones((3, 4))
b = np.ones((4,))
print(a)
print(b)
print(a+b)


# this not work because dimensions are compared from right side
A = np.ones((3, 4))
B = np.ones((3,))
# print(A+B)
# this will show the below value error 
# ValueError: operands could not be broadcast together with shapes (3,4) (3,) 