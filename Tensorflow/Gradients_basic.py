'''Gradients are essential for optimizing models, as they tell us how much to adjust each parameter to minimize the loss function. tf.GradientTape records operations for automatic differentiation, allowing TensorFlow to compute the gradient of a computation with respect to its inputs.'''
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow logging
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU if not available
import tensorflow as tf
# 1 simple scalar example
x = tf.constant(3.0)
with tf.GradientTape() as tape:
    tape.watch(x)  # Tell the tape to watch x (if it's not a tf.Variable)
    y = x*x 
dy_dx = tape.gradient(y,x) # dy/dx =2x
print(f"y=x^2 , where x={x}.dy/dx = {dy_dx} (expected 2*3=6)")

# 2. Example with a tf.Variable (often weights/biases in a model)
# tf.Variables are automatically watched by GradientTape
w = tf.Variable(tf.constant(2.0))
b = tf.Variable(tf.constant(1.0))
x_input = tf.constant(4.0)

with tf.GradientTape() as tape:
    z= w*x_input + b
# Compute gradients of z with respect to w and b
dz_dw, dz_db = tape.gradient(z, [w, b])
print(f"\nz = w*x + b, where w={w.numpy()}, b={b.numpy()}, x={x_input.numpy()}")
print(f"dz/dw = {dz_dw} (expected x = 4)")
print(f"dz/db = {dz_db} (expected 1)")

# 3. Higher-order gradients (gradients of gradients)
x = tf.constant(3.0)
with tf.GradientTape() as tape2:
    tape2.watch(x)
    with tf.GradientTape() as tape1:
        tape1.watch(x)
        y = x * x # y = x^2
    dy_dx = tape1.gradient(y, x) # dy/dx = 2x
d2y_dx2 = tape2.gradient(dy_dx, x) # d(2x)/dx = 2
print(f"\ny = x^2, first derivative dy/dx = {dy_dx}, second derivative d2y/dx2 = {d2y_dx2}")

# 4. Gradients for multiple outputs (e.g., a loss function)
weights = tf.Variable([[1.0], [2.0]])
x_data = tf.constant([[1.0, 2.0], [3.0, 4.0]])
y_true = tf.constant([[5.0], [11.0]])

with tf.GradientTape() as tape:
    y_pred = tf.matmul(x_data, weights) # Linear model: y_pred = x_data * weights
    loss = tf.reduce_mean(tf.square(y_true - y_pred)) # Mean Squared Error

gradients = tape.gradient(loss, weights)
print(f"\nModel weights: {weights.numpy()}")
print(f"Loss: {loss.numpy()}")
print(f"Gradients of loss w.r.t. weights:\n{gradients.numpy()}")

# ------- Task -------
'''You have a simple function f(x) = 3*x^3 + 2*x^2 + 5.

Define x as a TensorFlow variable with an initial value of 2.0.
Use tf.GradientTape to calculate the derivative of f(x) with respect to x when x = 2.0.
Expected result: f'(x) = 9*x^2 + 4*x. For x=2, f'(2) = 9*(2^2) + 4*2 = 9*4 + 8 = 36 + 8 = 44.'''
import tensorflow as tf

x = tf.Variable(2.0, dtype=tf.float32) # Define x as a tf.Variable

with tf.GradientTape() as tape:
    f_x = 3 * tf.pow(x, 3) + 2 * tf.pow(x, 2) + 5 # f(x) = 3x^3 + 2x^2 + 5

df_dx = tape.gradient(f_x, x)
print(f"x = {x.numpy()}")
print(f"f(x) = {f_x.numpy()}")
print(f"df/dx at x = {x.numpy()} is {df_dx.numpy()} (Expected: 44.0)")