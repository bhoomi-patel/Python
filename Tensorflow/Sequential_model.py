'''The Sequential API is the simplest way to build Keras models. It's used for models where each layer has exactly one input tensor and one output tensor. '''
# sequential model
import warnings
warnings.filterwarnings('ignore')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow logging
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU if not available
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models

# 1. Define a Sequential Model
# Example: A simple Multi-Layer Perceptron (MLP) for classifying 10 categories
# Input is a flattened image of 28x28 pixels
model_mlp = models.Sequential([
    layers.Flatten(input_shape=(28,28,1)),
    layers.Dense(128,activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10,activation='softmax')])
print("Sequential MLP Model Summary:", model_mlp.summary())
# Example: A simple Convolutional Neural Network (CNN)
# Input is a 32x32 RGB image
model_cnn = models.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)),
    layers.MaxPooling2D((2,2)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax') # 10 output classes
])
print('Sequential CNN Model Summary:' , model_cnn.summary())

# -------- Task -------- #
'''Build a sequential model for a binary classification task. The input features are 5 numerical values. The model should have:
An input layer of 5 features.
A Dense hidden layer with 32 units and ReLU activation.
A Dropout layer with a rate of 0.3.
An output Dense layer with 1 unit and Sigmoid activation (for binary classification).'''
model_binary = models.Sequential([
    layers.Dense(32, activation='relu', input_shape=(5,)), 
    layers.Dropout(0.3),
    layers.Dense(1, activation='sigmoid') 
])
print("Binary Classification Sequential Model Summary:")
model_binary.summary()