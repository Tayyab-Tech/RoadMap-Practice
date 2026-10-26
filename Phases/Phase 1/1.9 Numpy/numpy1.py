import importlib
np = importlib.import_module("numpy")

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)


# 2D array
print("=========== 2D Array ===========")
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(arr)

# 3D array
print("=========== 3D Array ===========")
arr1 = np.array([
[
    [1,2],
    [3,4]
],
[
    [5,6],
    [7,8]
]
])
print(arr1)


# Creating Special Arrays
print("Zeros")
print(np.zeros((3,4)))

print("Ones")
print(np.ones((2,3)))

print("Identity matrix")
print(np.eye(3))

print("Full")
print(np.full((2,3),5))

print("Range")
print(np.arange(1,10))

print("Even Numbers")
print(np.arange(2,20,2))

print("Linear spaced numbers")
print(np.linspace(0,2,5))

print("Random numbers")
print(np.random.rand(3))

print("Random integers")
print(np.random.randint(1,100,5))

print("Reshaping Arrays")
arr = np.arange(12)
print(arr)
arr = arr.reshape(3,4)
print(arr)
print("Flatten")
print(arr.flatten())



print("Indexing")

# 1D array 
print("1D array")
arr = np.array([10,20,30,40])
print(arr[0])
print(arr[2])

# 2D array 
print("2D array")
arr = np.array([
[1,2,3],
[4,5,6]
])
print(arr[0][1])
# better way 
print(arr[0,1])



# 3D array 
print("2D array")
arr1[1,0,1]




# Slicing
print("Slicing")
arr = np.array([1,2,3,4,5,6])
print("First three")
print(arr[:3])
print("Last two")
print(arr[-2:])
print("Middle")
print(arr[2:5])


print("2D Slicing")
arr = np.array([
[1,2,3],
[4,5,6],
[7,8,9]
])
print("First row")
print(arr[0])
print("Second column")
print(arr[:,1])
print("Last row")
print(arr[-1])




# Boolean Indexing
print("Boolean Indexing")
arr = np.array([10,23,30,40,53])
print(arr[arr>25])
print("Even numbers")
print(arr[arr%2==0])



# Fancy Indexing
print("Fancy Indexing")
arr = np.array([10,20,30,40,50])
print(arr[[0,2,4]])



# Array Operations
print("Array Operations")
a = np.array([1,2,3])
b = np.array([4,5,6])
print("Addition")
print(a+b)
print("subtraction")
print(a-b)
print("multiplication")
print(a*b)
print("division")
print(a/b)
print("power")
print(a**2)
print("square root")
print(np.sqrt(a))


# Aggregation Functions
print("Aggregation Functions")
arr = np.array([10,20,30])

print("sum")
print(arr.sum())

print("mean")
print(arr.mean())

print("maximum")
print(arr.max())

print("minimum")
print(arr.min())

print("Standard division")
print(arr.std())

print("Variance")
print(arr.var())



# Axis
print("Axis")
arr = np.array([
[1,2,3],
[4,5,6]
])
print("Column sum")
print(arr.sum(axis=0))
print("row sum")
print(arr.sum(axis=1))



# Broadcasting
# Broadcasting allows NumPy to perform operations on arrays of different shapes by automatically expanding dimensions when they are compatible.
print("Broadcasting")
arr = np.array([1,2,3])
print(arr + 5)

# row broadcasting
print("row broadcasting")
a = np.array([
[1,2,3],
[4,5,6]
])
b = np.array([10,20,30])
print(a+b)

# Column broadcasting
print("Column broadcasting")
a = np.array([
[1,2],
[3,4]
])
b = np.array([
[10],
[20]
])
print(a+b)


# Broadcasting Rules
# 1. Compare shapes from the last dimension.
# 2. Dimensions are compatible if they are equal or one of them is 1.
# 3. If not compatible, NumPy raises a ValueError.

# print(np.array([1,2,3]) + np.array([1,2])) raises value error because array dimensional is not same 





# Vector Operations
print("Vector Operations")
a = np.array([1,2,3])
b = np.array([4,5,6])

print("dot product")
print(np.dot(a,b))

print("Element-wise Multiplication")
print(a*b)

print("Magnitude (Norm)")
print(np.linalg.norm(b))

print("Normalize vector")
print(a / np.linalg.norm(a))

print("Cross Product")
print(np.cross(a,b))


# Matrix Operations
print("Matrix Operations")
arr = np.array([
[1,2,3],
[4,5,6]
])

# Transpose
print("Transpose")
print(arr.T)

# matrix multiplication
print("matrix multiplication")
print(np.matmul(a,b))
# or 
print(a@b)


arr = np.array([
[1,2],
[4,5]
])
# Inverse
print("Inverse")
print(np.linalg.inv(arr)) # it works with 2D arrays

# Determinant
print("Determinant")
print(np.linalg.det(arr))

# Eigenvalues
print("Eigenvalues")
print(np.linalg.eig(arr))
print(np.linalg.eig(arr))


# Copy vs View
print("Copy vs View")
print("view")
a = np.array([1,2,3])
b = a.view()
b[0] = 100
print(a)

print("copy")
a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(a)
print(b)