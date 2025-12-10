'''
model.fit(): The method used to train your compiled model on your input data and target labels. It performs the forward and backward passes iteratively.
model.evaluate(): Assesses the model's performance on a given dataset (usually a validation or test set) and returns the loss value and metric values.
model.predict(): Generates predictions (outputs) for new input samples.
Epochs: One complete pass through the entire training dataset.
Batch Size: Number of samples processed before the model's internal parameters are updated.
Validation Data: A subset of the data used to evaluate the model's performance during training and tune hyperparameters.
'''

import warnings
warnings.filterwarnings('ignore')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow logging
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU if not available
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.datasets import fashion_mnist # A common dataset for examples

# 1. Load and Preprocess Data (using NumPy for now, will cover tf.data.Dataset later)
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Normalize image pixel values to be between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# Reshape images to add a channel dimension (28, 28) -> (28, 28, 1) for Conv2D layers
train_images = train_images[..., tf.newaxis]
test_images = test_images[..., tf.newaxis]

# Use a small subset for quick demonstration
train_images_sub = train_images[:10000]
train_labels_sub = train_labels[:10000]
test_images_sub = test_images[:2000]
test_labels_sub = test_labels[:2000]


# 2. Build the Model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax') # 10 output classes
])

# 3. Compile the Model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False), # Labels are integers (0-9)
              metrics=['accuracy'])

model.summary()

# 4. Train the Model (`model.fit()`)
print("\n--- Training Model ---")
history = model.fit(
    train_images_sub,
    train_labels_sub,
    epochs=5,           # Number of complete passes through the training data
    batch_size=32,      # Number of samples per gradient update
    validation_data=(test_images_sub, test_labels_sub), # Data to evaluate after each epoch
    verbose=1           # Display training progress
)
print("\nTraining complete.")

# 5. Evaluate the Model (`model.evaluate()`)
print("\n--- Evaluating Model on Test Data ---")
test_loss, test_acc = model.evaluate(test_images_sub, test_labels_sub, verbose=2)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f}")

# 6. Make Predictions (`model.predict()`)
print("\n--- Making Predictions ---")
predictions = model.predict(test_images_sub[:5]) # Predict on first 5 test images
print(f"Predictions for first 5 test images (raw probabilities):\n{predictions}")

predicted_classes = np.argmax(predictions, axis=1) # Get the class with highest probability
print(f"\nPredicted classes for first 5 test images: {predicted_classes}")
print(f"True labels for first 5 test images: {test_labels_sub[:5].numpy()}")

# ----- task ---- #
'''Create dummy training data: X_train (100 samples, 5 features, random values) and y_train (100 samples, binary labels 0 or 1, random).
Create dummy validation data similarly: X_val, y_val (20 samples each).
Compile the model (Adam optimizer, BinaryCrossentropy loss, accuracy metric).
Train the model for 10 epochs with a batch size of 16, using the validation data.
Evaluate the trained model on the validation data.'''
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
import numpy as np

# 1. Create dummy data
num_train_samples = 100
num_val_samples = 20
num_features = 5

X_train = np.random.rand(num_train_samples, num_features).astype(np.float32)
y_train = np.random.randint(0, 2, size=(num_train_samples, 1)).astype(np.float32) # Binary labels

X_val = np.random.rand(num_val_samples, num_features).astype(np.float32)
y_val = np.random.randint(0, 2, size=(num_val_samples, 1)).astype(np.float32)

# 2. Build the Model (from 4.4 Easy Coding Task)
model_binary = models.Sequential([
    layers.Dense(32, activation='relu', input_shape=(num_features,)),
    layers.Dropout(0.3),
    layers.Dense(1, activation='sigmoid')
])

# 3. Compile the Model
model_binary.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
model_binary.summary()

# 4. Train the Model
print("\n--- Training Binary Model ---")
history_binary = model_binary.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=16,
    validation_data=(X_val, y_val),
    verbose=1
)
print("\nBinary Model Training Complete.")

# 5. Evaluate the Model
print("\n--- Evaluating Binary Model on Validation Data ---")
val_loss, val_acc = model_binary.evaluate(X_val, y_val, verbose=2)
print(f"Validation Loss: {val_loss:.4f}")
print(f"Validation Accuracy: {val_acc:.4f}")
