# Given:
# arr = np.array([10, 25, 30, 45, 50, 65, 70, 85])
# Create a new array containing only values between 30 and 70 inclusive.
# Restriction: No for loop.
import importlib
np = importlib.import_module("numpy")

arr = np.array([10, 25, 30, 45, 50, 65, 70, 85])

new_arr = np.array(arr[(arr >= 30) & (arr <= 70)])

print(new_arr)