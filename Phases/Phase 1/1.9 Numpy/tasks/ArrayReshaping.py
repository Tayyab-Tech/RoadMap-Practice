# Create an array containing numbers from 1 to 24.

# Requirements:

# Reshape it into 4 × 6.
# Reshape it into 3 × 8.
# Reshape it into 2 × 3 × 4.
# Extract the first 2 × 2 section from the 4 × 6 version.
# Flatten the 3 × 8 version.
# Explain what happens if you try to reshape 24 elements into 5 × 5.

# Concepts: reshape(), dimensions, slicing, flattening.\


import importlib
np = importlib.import_module("numpy")

numbers = np.arange(1,25)
# print(numbers)
reshape1 = numbers.reshape(4,6)
reshape2 = numbers.reshape(3,8)
print("reshap1 : \n",reshape1)
print("reshap2 : \n",reshape2)
print("reshap3 : \n",numbers.reshape(2,3,4))
print(reshape1[0:2,0:2])
print(reshape2.flatten())
# print("error : ",numbers.reshape(5,5))
# ValueError: cannot reshape array of size 24 into shape (5,5)