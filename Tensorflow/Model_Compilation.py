'''After defining your model's architecture, model.compile() configures the model for training. You specify the optimizer, loss function, and metrics it should track.
Key Topics:

Optimizer: Algorithm to adjust model weights based on gradients (e.g., Adam, SGD, RMSprop).
Loss Function: Quantifies the difference between predicted and true values (e.g., SparseCategoricalCrossentropy for integer labels, BinaryCrossentropy for binary classification, MeanSquaredError for regression).
Metrics: Used to evaluate the model's performance during training and testing (e.g., accuracy, precision, recall).'''

import warnings
warnings.filterwarnings('ignore')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow logging
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU if not available
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models

# --- Example 1: Multi-class classification (e.g., Fashion MNIST) ---
model_classifier = models.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax') # 10 classes
])

model_classifier.compile(
    optimizer='adam',                             # Common and effective optimizer
    loss='sparse_categorical_crossentropy',       # For integer labels (0, 1, ..., 9)
    metrics=['accuracy']                          # Track accuracy
)
print("Classifier Model Compiled (Adam, SparseCategoricalCrossentropy, Accuracy)")
model_classifier.summary() # Not printing full summary again, just compilation

# --- Example 2: Binary classification ---
model_binary = models.Sequential([
    layers.Dense(16, activation='relu', input_shape=(10,)),
    layers.Dense(1, activation='sigmoid') # Binary output
])

model_binary.compile(
    optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.001), # Can specify optimizer with hyperparameters
    loss=tf.keras.losses.BinaryCrossentropy(),                 # For binary classification (0 or 1)
    metrics=[tf.keras.metrics.BinaryAccuracy(), 'AUC']         # Track binary accuracy and AUC
)
print("\nBinary Model Compiled (RMSprop, BinaryCrossentropy, BinaryAccuracy, AUC)")

# --- Example 3: Regression ---
model_regressor = models.Sequential([
    layers.Dense(32, activation='relu', input_shape=(5,)),
    layers.Dense(1) # Linear output for regression
])

model_regressor.compile(
    optimizer='sgd',                               # Stochastic Gradient Descent
    loss='mean_squared_error',                     # For regression
    metrics=['mae', 'mse']                         # Mean Absolute Error, Mean Squared Error
)
print("\nRegressor Model Compiled (SGD, MeanSquaredError, MAE, MSE)")


# ---------- Task ----------- #
'''Compile the model_cnn you created earlier (32x32 RGB image input, 10 output classes). Use the Adam optimizer with a learning rate of 0.0005, SparseCategoricalCrossentropy loss, and accuracy as a metric.'''
model_cnn = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
model_cnn.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005),
    loss = tf.keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy']
)
print("CNN Model Compiled with custom Adam learning rate.")