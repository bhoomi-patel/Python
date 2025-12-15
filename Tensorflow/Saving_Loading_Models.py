'''Once a model is trained, you need to save it to avoid retraining every time. TensorFlow/Keras provides ways to save the entire model (architecture, weights, optimizer state) or just the weights.
.keras format (TensorFlow 2.x recommended): Saves everything in a single file.
H5/HDF5 format: Legacy format for saving entire models or weights.
SavedModel format: A more comprehensive format that includes the computation graph, variables, and assets. Recommended for production deployment with TensorFlow Serving.
'''
import warnings
warnings.filterwarnings('ignore')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow logging
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU if not available

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
import os

# Assume we have a trained model (from previous section)
# Let's quickly define and compile a simple model for demonstration
model_to_save = models.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
model_to_save.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

# Dummy training (optional, just to have trained weights)
# (train_images, train_labels), _ = tf.keras.datasets.fashion_mnist.load_data()
# train_images = train_images[:1000] / 255.0
# train_images = train_images[..., tf.newaxis]
# train_labels = train_labels[:1000]
# model_to_save.fit(train_images, train_labels, epochs=1, verbose=0)


print("--- Saving Models ---")
# 1. Save the entire model in the recommended .keras format
model_to_save.save('my_fashion_model.keras')
print("Model saved as my_fashion_model.keras")

# 2. Save only the weights in H5 format
model_to_save.save_weights('my_fashion_weights.weights.h5')
print("Weights saved as my_fashion_weights.weights.h5")

# You can also save in the .keras format (single file)
model_to_save.save('my_fashion_model_savedmodel.keras')
print("Model saved in .keras format as 'my_fashion_model_savedmodel.keras'")

print("\n--- Loading Models ---")
# 1. Load the entire model from .keras file
loaded_model_keras = models.load_model('my_fashion_model.keras')
print("Model loaded from my_fashion_model.keras:")
loaded_model_keras.summary()
# Loaded model is already compiled with original optimizer, loss, and metrics

# 2. Load weights into a newly created model (must have the same architecture!)
new_model_for_weights = models.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
new_model_for_weights.compile(optimizer='sgd', # Can compile with different settings
                              loss='sparse_categorical_crossentropy',
                              metrics=['accuracy'])

new_model_for_weights.load_weights('my_fashion_weights.weights.h5')
print("\nWeights loaded into a new model:")
new_model_for_weights.summary()

# 3. Load from .keras format
loaded_model_savedmodel = models.load_model('my_fashion_model_savedmodel.keras')
print("\nModel loaded from .keras format:")
loaded_model_savedmodel.summary()


# Clean up created files (optional)
# os.remove('my_fashion_model.keras')
# os.remove('my_fashion_weights.weights.h5')
# os.remove('my_fashion_model_savedmodel.keras')

# ---- Task --- #
'''Create a simple Sequential model (e.g., input 10 features, 1 hidden Dense layer of 20 units with ReLU, output Dense layer of 1 unit with Sigmoid).
Compile it (Adam, binary_crossentropy, accuracy).
Save the entire model using the .keras format to my_classifier.keras.
Load the model back into a new variable reloaded_classifier.
Print the summary of reloaded_classifier to confirm it loaded correctly.'''


# 1. Create a simple Sequential model
my_model = models.Sequential([
    layers.Dense(20, activation='relu', input_shape=(10,)),
    layers.Dense(1, activation='sigmoid')
])

# 2. Compile the model
my_model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
print("Original Model Summary:")
my_model.summary()

# 3. Save the entire model
save_path = 'my_classifier.keras'
my_model.save(save_path)
print(f"\nModel saved to {save_path}")

# 4. Load the model back
reloaded_classifier = models.load_model(save_path)
print(f"\nModel loaded from {save_path}")

# 5. Print the summary of the reloaded model
print("\nReloaded Model Summary:")
reloaded_classifier.summary()

# Clean up (optional)
# os.remove(save_path)
