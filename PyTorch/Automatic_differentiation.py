'''PyTorch's autograd system automatically computes gradients for all operations on tensors that have requires_grad=True. This is the mechanism for backpropagation in neural networks. When a tensor x has requires_grad=True, all operations involving x will build a computation graph, allowing .backward() to calculate gradients.'''
import torch
# 1. simple scalar example
x = torch.tensor(3.0,requires_grad=True) # tell autograd to track gradients for x
y = x*x
# y = x^2
y.backward() # computes the gradients (derivatives)
print(f"y = x^2 , where x={x}. dy/dx={x.grad}")

# 2. example with multiple variables
a = torch.tensor(2.0,requires_grad=True)
b = torch.tensor(3.0,requires_grad=True)
c = a*b + a**2
c.backward() # computes the gradients (derivatives)
print(f"\nc= a*b + a^2, a={a}, b={b}")
print(f"dc/da = {a.grad}")
print(f"dc/db = {b.grad}")

# 3. working with a tf.Variable
# Tensors that are part of nn.Module parameters automatically have requires_grad=True
w = torch.tensor(2.0,requires_grad=True)
b = torch.tensor(1.0,requires_grad=True)
x_input = torch.tensor(4.0)
z = w*x_input + b
z.backward() # computes the gradients (derivatives)
print(f"\nz = w*x + b, where w={w}, b={b}, x={x_input}")
print(f"dz/dw = {w.grad} (expected x = 4)")
print(f"dz/db = {b.grad} (expected 1)")

# --------Task ----------
'''You have a simple function f(x) = 3*x^3 + 2*x^2 + 5.

Define x as a PyTorch tensor with an initial value of 2.0 and requires_grad=True.
Calculate f(x).
Call .backward() on f(x) to compute the derivative.
Print the gradient of x.
Expected result: f'(x) = 9*x^2 + 4*x. For x=2, f'(2) = 9*(2^2) + 4*2 = 9*4 + 8 = 36 + 8 = 44'''

x= torch.tensor(2.0,requires_grad=True,dtype=torch.float32)
f_x = 3*x**3 + 2*x**2 + 5 # f(x) = 3x^3 + 2x^2 + 5
print(f"x = {x}")
print(f"f(x) = {f_x}")

f_x.backward() # compute the derivative
print(f"f'(x) = {x.grad}")