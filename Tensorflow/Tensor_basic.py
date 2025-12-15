# Tensors - Multi dimensional arrays (like numpy arrays but optimized for DL).
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow logging
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU if not available
import tensorflow as tf
import numpy as np

# 1 ---- create tensors
tensor_py_list = tf.constant([1,2,3,4,5])
print(f"list is : {tensor_py_list}")
# from numpy array
numpy_arr = np.array([[10,20],[30,40]])
tensor_numpy = tf.constant(numpy_arr)
print("Tensor from numpy array: ", tensor_numpy)
# Specific data type (e.g., float32 for calculations)
tensor_float = tf.constant([1.0, 2.5, 3.0], dtype=tf.float32)
print("\nTensor with specific dtype:\n", tensor_float)
# tensor with specified shape and value
tensor_zeros = tf.zeros(shape=(2,3),dtype=tf.int32)
print("Tensor of zeros (2x3):",tensor_zeros)
tensor_ones = tf.ones(shape=(1,4))
print("tensor of ones (1,4):",tensor_ones)
tensor_random = tf.random.normal(shape=(2,2),mean=0.0,stddev=1.0)
print("Tensor of random normal values (2x2) : ",tensor_random)

# 2 ---- Tensor Properties
print(" --- Tensor Properties (using tensor_numpy) ---")
print("Shape:" , tensor_numpy.shape) # (rowsxcolumns)
print("Number of dimensions:",tensor_numpy.ndim)
print("Data type:",tensor_numpy.dtype)
print("Element value (Python scalar):", tensor_numpy[0, 0].numpy()) # .numpy() converts to NumPy scalar

# 3 ---- Basic Operations(Element-wise operations)
print("\n--- Tensor Operations ---")
a = tf.constant([1, 2])
b = tf.constant([3, 4])
print("a + b:", a + b)           # Element-wise addition
print("a * b:", a * b)           # Element-wise multiplication
print("a / 2:", a / 2)           # Scalar division
print("tf.square(a):", tf.square(a)) # Element-wise square

matrix_a = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
matrix_b = tf.constant([[5, 6], [7, 8]], dtype=tf.float32)
print("\nMatrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
print("Matrix multiplication (tf.matmul(A, B)):\n", tf.matmul(matrix_a, matrix_b))

# Broadcasting: Automatically expands smaller tensor to match larger one
print("\nBroadcasting (matrix_a + tensor_py_list[0]):\n", matrix_a + tf.cast(tensor_py_list[0], tf.float32))

# -------- mini task ------- #
'''Task: Tensor Creation & Operation
Create a 2x2 TensorFlow tensor named weights with random uniform values between -1 and 1.
Create a 2x1 TensorFlow tensor named biases with all zeros.
Perform matrix multiplication of a 2x2 input tensor tf.constant([[2., 3.], [1., 4.]]) with weights, and then add biases to the result.
Self-correction: Ensure all tensors have tf.float32 dtype for consistent matrix operations.'''

import tensorflow as tf

# 1. Create weights tensor (2x2, random uniform)
weights = tf.random.uniform(shape=(2, 2), minval=-1.0, maxval=1.0, dtype=tf.float32)
print("Weights Tensor:\n", weights)

# 2. Create biases tensor (2x1, all zeros)
biases = tf.zeros(shape=(2, 1), dtype=tf.float32)
print("\nBiases Tensor:\n", biases)

# 3. Input tensor and operations
input_tensor = tf.constant([[2., 3.], [1., 4.]], dtype=tf.float32)
print("\nInput Tensor:\n", input_tensor)

# Matrix multiplication (tf.matmul)
product = tf.matmul(input_tensor, weights)
print("\nProduct (Input * Weights):\n", product)

# Add biases (broadcasting will handle the shape difference for addition)
output = product + biases
print("\nOutput (Product + Biases):\n", output)