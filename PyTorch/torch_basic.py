'''A torch.Tensor is the primary data structure in PyTorch. It's a multi-dimensional array, highly optimized for numerical operations, and can reside on a CPU or GPU. It's essentially PyTorch's equivalent of a NumPy ndarray with added GPU acceleration and automatic differentiation capabilities.'''
import torch
import numpy as np

print(f"pytorch version: {torch.__version__}")
# check for gpu availability
device = "cuda" if torch.cuda.is_available() else "cpu" 
print(f"Using device: {device}")

# 1. create a tensor
# from a list
lst = torch.tensor([1,2,3,4,5])
print(f"Tensor from list: {lst}")
# from a numpy array
arr = np.array([[10,20],[30,40]])
tensor_numpy = torch.tensor(arr)
print(f"Tensor from numpy array: {tensor_numpy}")
# specific data type
tensor_float = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
print(f"Tensor with specific dtype: {tensor_float}, dtype: {tensor_float.dtype}")
# specified shape and value
tensor_zeros = torch.zeros(2,3,dtype=torch.int32)
print("Tensor of zeros (2x3):",tensor_zeros)
tensor_ones = torch.ones(3,2)
print("Tensor of ones (3x2):",tensor_ones)
tensor_random = torch.rand(2,2)
print("Tensor with random values (2x2):",tensor_random)

# 2. tensor properties
print("Shape:",tensor_numpy.shape)
print("Number of dimensions:",tensor_numpy.ndim)
print("Data type:",tensor_numpy.dtype)
print("Device:",tensor_numpy.device)

# 3. moving tensors to GPU (if available)
if device == "cuda":
    tensor_gpu = tensor_numpy.to(device)
    print(f"\nTensor moved to GPU: {tensor_gpu}, Device: {tensor_gpu.device}")
    tensor_gpu_zeros = torch.zeros((2,3), device=device)
    print("Tensor of zeros on GPU (2x3):",tensor_gpu_zeros)
    tensor_gpu_zeros = torch.zeros(2, 2, device=device)
    print(f"Zeros tensor on GPU: {tensor_gpu_zeros} (device: {tensor_gpu_zeros.device})")
else:
    print("\nGPU not available, skipping GPU tensor example.")

# 4. basic tensor operations
a = torch.tensor([1,2])
b = torch.tensor([3,4])
print("a+b:", a + b)
print("a-b:", a - b)
print("a*b:", a * b)
print("a/b:", a / b)
print("torch.square(a):", torch.square(a))

# Matrix multiplication (torch.matmul or @ operator)
matrix_a = torch.tensor([[1,2],[3,4]],dtype=torch.float32)
matrix_b = torch.tensor([[5,6],[7,8]],dtype=torch.float32)
matrix_product = torch.matmul(matrix_a, matrix_b)
print("Matrix multiplication (torch.matmul):", matrix_product)
matrix_product_op = matrix_a @ matrix_b
print("Matrix multiplication (@ operator):", matrix_product_op)

# Broadcasting : Automatically expands smaller tensor to match larger one
print("\nBroadcasting (matrix_a + lst[0]):\n",matrix_a + lst[0])

# 5. indexing and slicing
tensor_index = torch.tensor([[10,20,30],[40,50,60],[70,80,90]])
print("\nOriginal Tensor:\n", tensor_index)
print("Element at (1,2):", tensor_index[1,2])
print("First row:", tensor_index[0])
print("First column:", tensor_index[:,0])
print("Sub-tensor (rows 0-1, cols 1-2):\n", tensor_index[0:2, 1:3])

# --------Task ----------
'''Create a 2x2 PyTorch tensor named weights with random uniform values between -1 and 1. Ensure its dtype is torch.float32.
Create a 2x1 PyTorch tensor named biases with all zeros. Also torch.float32.
Perform matrix multiplication of a 2x2 input tensor torch.tensor([[2., 3.], [1., 4.]], dtype=torch.float32) with weights, and then add biases to the result.
If a GPU is available, move weights and biases to the GPU before performing the operations.'''

device = "cuda" if torch.cuda.is_available() else "cpu"

# 1. Create weights tensor (2x2, random uniform)
weights = torch.rand(2, 2, dtype=torch.float32) * 2 - 1 # uniform between -1 and 1
print("Weights Tensor (CPU):\n", weights)

# 2. Create biases tensor (2x1, all zeros)
biases = torch.zeros(2, 1, dtype=torch.float32)
print("\nBiases Tensor (CPU):\n", biases)

# Move to GPU if available
weights = weights.to(device)
biases = biases.to(device)
print(f"\nWeights Tensor (on {weights.device}):\n", weights)
print(f"Biases Tensor (on {biases.device}):\n", biases)

# 3. Input tensor and operations
input_tensor = torch.tensor([[2., 3.], [1., 4.]], dtype=torch.float32).to(device)
print(f"\nInput Tensor (on {input_tensor.device}):\n", input_tensor)

# Matrix multiplication
product = torch.matmul(input_tensor, weights)
print("\nProduct (Input * Weights):\n", product)

# Add biases (broadcasting will handle the shape difference for addition)
output = product + biases
print("\nOutput (Product + Biases):\n", output)