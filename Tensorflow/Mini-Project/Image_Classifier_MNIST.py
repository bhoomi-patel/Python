'''Project Goal: Build, train, evaluate, save, and load a Convolutional Neural Network (CNN) using TensorFlow/Keras to classify images of clothing from the Fashion MNIST dataset.
1.Loading and preprocessing image data.
2.Defining a CNN architecture using the Keras Sequential API.
3.Compiling the model with an optimizer, loss function, and metrics.
4.Training the model using model.fit().
5.Evaluating the model's performance on unseen data using model.evaluate().
6.Making predictions on new images using model.predict().
7.Saving the trained model and loading it back.
8.(Optional) Visualizing the training history.
'''
# setup and data loading
'''The Fashion MNIST dataset consists of 70,000 grayscale images of 10 fashion categories (e.g., T-shirt, Trouser, Sneaker). 60,000 images are for training, and 10,000 for testing. Each image is 28x28 pixels.'''
import tensorflow as tf
from tensorflow.keras import layers,models,callbacks
from tensorflow.keras.datasets import fashion_mnist
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

# Clear Keras cache to force redownload if corrupted
cache_dir = os.path.expanduser('~/.keras/datasets')
if os.path.exists(cache_dir):
    shutil.rmtree(cache_dir)

try:
    (train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()
except (ConnectionResetError, EOFError, Exception) as e:
    print(f"Error loading Fashion MNIST dataset: {e}")
    print("This may be due to network issues or corrupted cache. Please check your internet connection and try running the script again.")
    exit(1)
class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
print(f"\nTraining images shape: {train_images.shape}")
print(f"Training labels shape: {train_labels.shape}")
print(f"Test images shape: {test_images.shape}")
print(f"Test labels shape: {test_labels.shape}")

# Display few sample images
plt.figure(figsize=(10,5))
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(train_images[i],cmap='gray')
plt.title(class_names[train_labels[i]])
plt.axis('off')
plt.suptitle("Sample Fashion MNIST Images")
plt.show()

# 2. Data Preprocessing
# Normalize pixel values from [0, 255] to [0, 1]
train_images = train_images/255.0
test_images = test_images/255.0
train_images = train_images[...,tf.newaxis]
test_images = test_images[...,tf.newaxis]
print(f"\nNormalized & Reshaped Training images shape: {train_images.shape}")
print(f"Normalized & Reshaped Test images shape: {test_images.shape}")
# train_dataset = tf.data.Dataset.from_tensor_slices((train_images, train_labels)).batch(32).prefetch(tf.data.AUTOTUNE)
# test_dataset = tf.data.Dataset.from_tensor_slices((test_images, test_labels)).batch(32).prefetch(tf.data.AUTOTUNE)

# 3. Build CNN Model (Sequential API)
model = models.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(128,activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10,activation='softmax')
])
print("\n--- Model Architecture Summary ---")
model.summary()

# 4. Compile Model
model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(),metrics=['accuracy'])
print("\nModel compiled with Adam optimizer, SparseCategoricalCrossentropy loss, and Accuracy metric.")

# 5. Train Model
early_stopping = callbacks.EarlyStopping(monitor='val_accuracy',patience=3,verbose=1,mode='max')
model_save_path = 'best_fashion_mnist_model.keras'
model_checkpoint = callbacks.ModelCheckpoint(filepath=model_save_path,monitor='val_accuracy',save_best_only=True,verbose=1,mode='max')
print("\n--- Training Model ---")
history = model.fit(
    train_images,train_labels,epochs=10,batch_size=32,validation_data=(test_images,test_labels),callbacks=[early_stopping,model_checkpoint],verbose=1
)
print("\nTraining complete.")

# 6. Evaluate Model
print("\n--- Evaluating Model on Test Data ---")
test_loss,test_accuracy = model.evaluate(test_images,test_labels,verbose=2)
print(f"\nFinal Test Loss: {test_loss:.4f}")
print(f"Final Test Accuracy: {test_accuracy:.4f}")

# 7.Make Predictions
print("\n--- Making Predictions ---")
# Take a few random images from the test set for prediction
num_predictions = 5
random_indices = np.random.choice(len(test_images),num_predictions,replace=False)
sample_images = test_images[random_indices]
sample_true_labels = test_labels[random_indices]

# Make predictions
predictions = model.predict(sample_images)
print(f"\nPredictions for {num_predictions} sample test images:")
for i in range(num_predictions):
    predicted_class_idx = np.argmax(predictions[i])
    true_class_idx = sample_true_labels[i]

    print(f"  Image {i+1}:")
    print(f"    Predicted class: {class_names[predicted_class_idx]} (Index: {predicted_class_idx})")
    print(f"    True class:      {class_names[true_class_idx]} (Index: {true_class_idx})")
    print(f"    Probabilities:   {np.round(predictions[i], 2)}") # Show rounded probabilities
    plt.figure(figsize=(3, 3))
plt.imshow(sample_images[i].squeeze(),cmap='gray')
plt.title(f"True: {class_names[true_class_idx]}\nPred: {class_names[predicted_class_idx]}",
              color='green' if predicted_class_idx == true_class_idx else 'red')
plt.axis('off')
plt.show()

# 8. Saving and Loading Model
print("\n--- Saving and Loading the Model ---")
print(f"Best model automatically saved to: {model_save_path}")
# Load the saved model
loaded_model = models.load_model(model_save_path)
print("\nModel loaded successfully from disk.")
# Verify the loaded model by evaluating it
print("\nEvaluating the loaded model on test data:")
loaded_loss, loaded_accuracy = loaded_model.evaluate(test_images, test_labels, verbose=2)
print(f"Loaded Model Test Loss: {loaded_loss:.4f}")
print(f"Loaded Model Test Accuracy: {loaded_accuracy:.4f}")

# 9. Visualize Training History
if history:
    print("\n--- Visualizing Training History ---")
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs_range = range(len(acc))

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1) # 1 row, 2 columns, first plot
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.grid(True)
    plt.subplot(1, 2, 2) # 1 row, 2 columns, second plot
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("\nNo training history found to plot.")