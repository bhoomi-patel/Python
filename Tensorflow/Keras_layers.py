'''Keras is a high-level API for building and training deep learning models.
Layers are the fundamental building blocks of neural networks. They encapsulate a set of computations 
(e.g., matrix multiplication, activation functions) and often have trainable parameters (weights and biases).
'''
import warnings
warnings.filterwarnings('ignore')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow logging
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU if not available
import tensorflow as tf
from tensorflow.keras import layers

# Input layer - defines the expected input shape
# Example for image data: 28x28 grayscale images
input_shape = (28,28,1) # (height,width,channels)
input_tensor = tf.keras.Input(shape = input_shape)
print("Input Tensor shape:", input_tensor.shape)

# 1. Flatten layer : flattens input into 1d array
flatten_layer = layers.Flatten()(input_tensor)
print("Flattened layer output shape (28*28*1 = 784)", flatten_layer.shape)

# 2.Dense (fully connected) layer: y = activation(dot(input,kernel)+bias)
dense_layer = layers.Dense(units=128,activation='relu')(flatten_layer)
print("Dense Layer output shape:", dense_layer.shape)

# 3. Activation layer : applies an activation function 
activation_layer = layers.Activation('sigmoid')(dense_layer)
print("Activation Layer output shape :", activation_layer.shape)

# 4. Dropout Layer : Randomly sets a fraction of input units to 0 at each update during training
dropout_layer = layers.Dropout(0.2)(dense_layer)
print("Dropout layer output shape : " , dropout_layer.shape)

# 5. Convolutional Layer (Conv2D) :Used for image processing
convo_layer = layers.Conv2D(filters=32,kernel_size=(3,3),activation='relu',input_shape=(64,64,3))
dummy_input_for_conv = tf.keras.Input(shape=(64,64,3))
conv_output = convo_layer(dummy_input_for_conv)
print("Conv2D Layer output shape :", conv_output.shape)

# 6. MaxPooling2D Layer 
maxpool_layer = layers.MaxPooling2D(pool_size=(2,2))(conv_output)
print("MaxPooling2D Layer output shape : ",maxpool_layer.shape)


# ------ Task -------
'''Create a sequence of Keras layers that would process a grayscale image of size 32x32:
A Conv2D layer with 16 filters, a 3x3 kernel, ReLU activation.
A MaxPooling2D layer with a 2x2 pool size.
A Flatten layer.
A Dense layer with 10 units and 'softmax' activation (for classification).'''

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models

input_shape = (32, 32, 1) # Grayscale image
model_input = tf.keras.Input(shape=input_shape)

# Layer 1: Conv2D
x = layers.Conv2D(16, (3, 3), activation='relu')(model_input)
print(f"Shape after Conv2D: {x.shape}")

# Layer 2: MaxPooling2D
x = layers.MaxPooling2D((2, 2))(x)
print(f"Shape after MaxPooling2D: {x.shape}")

# Layer 3: Flatten
x = layers.Flatten()(x)
print(f"Shape after Flatten: {x.shape}")

# Layer 4: Dense (output layer for 10 classes)
output_layer = layers.Dense(10, activation='softmax')(x)
print(f"Shape after final Dense layer: {output_layer.shape}")

# You can wrap this into a dummy model to see the summary
model = models.Model(inputs=model_input, outputs=output_layer)
print("\nModel Summary:")
model.summary()
