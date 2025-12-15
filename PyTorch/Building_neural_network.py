'''torch.nn.Module is the base class for all neural network modules in PyTorch. It defines how a module processes input (forward() method) and provides functionality for managing parameters (weights, biases) and submodules. Layers are specific types of nn.Module.
Key Topics:
- nn.Module (base class for custom layers/models).
- __init__ (define layers/submodules).
- forward() (define the forward pass computation).
- Common layers: nn.Linear (fully connected), nn.Conv2d (convolutional), nn.MaxPool2d (max pooling), nn.ReLU (activation), nn.Flatten.
- nn.Sequential (a container for chaining layers).
'''
import torch
import torch.nn as nn
# Input tensor shape typically (batch_size, features)
dummy_input_img = torch.randn(1,1,28,28) # e.g., batch of 1 grayscale 28x28 image
dummy_input_vec = torch.randn(1, 784) # e.g., batch of 1 flattened 28x28 image

# 1. nn.Linear (Fully Connected Layer)
# Defines a linear transformation: y = xA^T + b
linear_layer = nn.Linear(in_features=784,out_features=128)
output_linear = linear_layer(dummy_input_vec)
print(f"\nLinear Layer input shape: {dummy_input_vec.shape}")
print(f"Linear Layer output shape: {output_linear.shape}")
print(f"Linear Layer weights shape: {linear_layer.weight.shape}")
print(f"Linear Layer bias shape: {linear_layer.bias.shape}")

# 2. nn.Conv2d (Convolutional Layer)
# (in_channels, out_channels,kernel_size, stride=1, padding=0)
conv_layer = nn.Conv2d(in_channels=1,out_channels=32,kernel_size=3,stride=1,padding=0)  # stride=1 → the filter moves 1 pixel (or unit) at a time 
output_conv = conv_layer(dummy_input_img)
print(f"\nConv2d Layer input shape:{dummy_input_img.shape}")
print(f"\nConv2d Layer output shape: {output_conv.shape}") # # Output size reduces: (28-3+0)/1 + 1 = 26x26

# 3. nn.MaxPool2d (Max Pooling Layer)
maxpool_layer = nn.MaxPool2d(kernel_size=2, stride=2) # Reduces by factor of 2
output_maxpool = maxpool_layer(output_conv)
print(f"\nMaxPool2d Layer input shape: {output_conv.shape}")
print(f"MaxPool2d Layer output shape: {output_maxpool.shape}") # Output size reduces: 26/2 = 13x13

# 4. nn.ReLU (Activation Function)
relu_activation = nn.ReLU()
output_relu = relu_activation(output_linear) # Applies ReLU element-wise
print(f"\nReLU Activation applied to linear output. First 5 elements:\n{output_relu[0, :5]}")


# 5. nn.Flatten (Flattens multi-dimensional input into a 1D vector)
flatten_layer = nn.Flatten()
output_flatten = flatten_layer(output_maxpool)
print(f"\nFlatten Layer input shape: {output_maxpool.shape}")
print(f"Flatten Layer output shape: {output_flatten.shape}") # 32 * 13 * 13 = 5408

# 6. Building a simple model using nn.Module
class SimpleMLP(nn.Module):
    def __init__(self,input_size,hidden_size,num_classes):
        super(SimpleMLP,self).__init__() # call the constuctor of parent class
        self.fc1 = nn.Linear(input_size,hidden_size) # first fully connected layer
        self.relu = nn.ReLU() #Relu activation
        self.fc2 = nn.Linear(hidden_size,num_classes) # Second fully connected layer (output)
    def forward(self,x):
        # define forward pass 
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out
mlp_model = SimpleMLP(input_size=784,hidden_size=128,num_classes=10)
print("\nSimple MLP Model (using nn.Module):")
print(mlp_model)
print(f"Output shape for dummy input (1, 784): {mlp_model(dummy_input_vec).shape}")

# 7. nn.Sequential (Convenient way to stack layers)
sequential_model = nn.Sequential(
    nn.Conv2d(1, 32, kernel_size=3, padding=1), # Padding to maintain size: (28+2*1-3)/1 + 1 = 28
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2), # Output: 14x14
    nn.Conv2d(32, 64, kernel_size=3, padding=1), # Output: 14x14
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2), # Output: 7x7
    nn.Flatten(),
    nn.Linear(64 * 7 * 7, 128),
    nn.ReLU(),
    nn.Linear(128, 10) # 10 output classes
)
print("\nSequential CNN Model:")
print(sequential_model)
print(f"Output shape for dummy input (1, 1, 28, 28): {sequential_model(dummy_input_img).shape}")