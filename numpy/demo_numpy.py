import numpy as np

#-----1 Array Creation -----
# 1D Array
arr = np.array([1,2,3,4,5])
print("1D Array:", arr)
# Output: [1 2 3 4 5]

# 2D Array (Matrix)
matrix = np.array([[1,2,3],[4,5,6]])
print("2D Array:\n", matrix)
# Output:
# [[1 2 3]
#  [4 5 6]]

# --> Special Arrays
# Array of zeros
zeros = np.zeros(5)
print("Zeros:", zeros)
# Output: [0. 0. 0. 0. 0.]

# 2D Array of ones
ones = np.ones((2,3))
print("Ones:\n", ones)
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]]

# Range array
range_arr = np.arange(10)
print("Range:", range_arr)
# Output: [0 1 2 3 4 5 6 7 8 9]

# --> Random Arrays
# Normal distribution (3x3 matrix)
random_arr = np.random.randn(3,3)
print("Random Normal:\n", random_arr)

# Random integers (0-9, size=5)
random_int = np.random.randint(0,10,size=5)
print("Random Integers:", random_int)

#--> Linear Space
linespace = np.linspace(0,10,5)  # 5 evenly spaced numbers from 0 to 10
print("Linspace:", linespace)
# Output: [ 0.   2.5  5.   7.5 10. ]

# Formula: Step = (10-0)/(5-1) = 2.5

#----- 2 Array Properties -----
arr = np.array([1,2,3,4,5])

print("Shape:", arr.shape)      # (5,) - dimensions
print("Size:", arr.size)        # 5 - total elements
print("Data Type:", arr.dtype)  # int64 - data type  
print("Dimensions:", arr.ndim)  # 1 - number of dimensions

#----- 3 Array Operations -----
arr1 = np.array([1,2,3,4])
arr2 = np.array([10,20,30,40])

print("Addition:", arr1 + arr2)     # [11 22 33 44]
print("Multiplication:", arr1 * arr2) # [10 40 90 160]
print("Power:", arr1 ** 2)          # [1 4 9 16]
print("Scalar Add:", arr1 + 10)     # [11 12 13 14]
print("Scalar Multiply:", arr1 * 2)  # [2 4 6 8]

print("Comparison:", arr1 > 2)      # [False False  True  True]
print("Boolean indexing:", arr1[arr1 > 2])  # [3 4]


# ----- 4 Array Indexing and Slicing -----
# Indexing
print("Element at index 2:", arr1[2])  # 3
print("Element at index -1:", arr1[-1])  # 4 (last element)
print("Elements from index 1 to 3:", arr1[1:3])  # [2 3]
# Slicing
print("Slicing [1:3]:", arr1[1:3])  # [2 3]
print("Slicing [:3]:", arr1[:3])    # [1 2 3]
print("Slicing [::2]:", arr1[::2])  # [1 3]
print("Slicing [1:4:2]:", arr1[1:4:2])  # [2 4]


#----- 5 Reshape and Indexing -----
# Create 3x4 matrix from 1D array
m = np.arange(12).reshape(3,4)
print("Matrix:\n", m)
# Output:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Indexing
print("Element [0,1]:", m[0,1])  # 1
print("Row 1:", m[1])            # [4 5 6 7]
print("Column 2:", m[:,2])       # [ 2  6 10]

# ----- 6 Matrix Operations -----
a = np.array([[1,2],[3,4]])
b = np.eye(2)  # Identity matrix

print("Matrix A:\n", a)
print("Matrix B (Identity):\n", b)

# Matrix multiplication
print("A dot B:\n", a.dot(b))  # Method 1
print("A @ B:\n", a @ b)       # Method 2 (preferred)

# ----- 7 Statistics  and Aggregations -----
arr = np.array([1,2,3,4,5])

print("Sum:", arr.sum())        # 15
print("Mean:", arr.mean())      # 3.0
print("Max:", arr.max())        # 5
print("Min:", arr.min())        # 1
print("Std Dev:", arr.std())    # 1.58...
