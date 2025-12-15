'''The Functional API is more flexible than the Sequential API. It allows you to build models that are non-linear (e.g., multi-input, multi-output, shared layers, or models with branches). You explicitly define the input tensors and how layers connect.'''
import warnings
warnings.filterwarnings('ignore')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow logging
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU if not available
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
# 1. Single Input, Single Output Model (Equivalent to Sequential but using Functional API)
inputs = tf.keras.Input(shape=(28,28,1),name='img_input')
x = layers.Flatten()(inputs)
x = layers.Dense(128,activation='relu')(x)
outputs = layers.Dense(10,activation='softmax')(x)
# Create model by specifying inputs and outputs
model_functional_simple = models.Model(inputs=inputs,outputs=outputs,name ='simple_functional_model')
print("Simple Functional Model Summary:")
model_functional_simple.summary()

# 2. Multi-Input Model (Example: Combine image features with numerical features)
image_input = tf.keras.Input(shape=(32,32,3),name='image_input')
x_img = layers.Conv2D(32,(3,3),activation='relu')(image_input)
x_img = layers.MaxPooling2D((2,2))(x_img)
x_img = layers.Flatten()(x_img)
# Numerical input branch
numerical_input = tf.keras.Input(shape=(10,), name='numerical_input') # 10 numerical features
x_num = layers.Dense(16, activation='relu')(numerical_input)

# Concatenate (merge) the outputs of the two branches
concatenated = layers.concatenate([x_img, x_num])
# Add a final Dense layer for classification
combined_output = layers.Dense(64, activation='relu')(concatenated)
final_output = layers.Dense(1, activation='sigmoid', name='output_layer')(combined_output) # Binary classification

model_multi_input = models.Model(inputs=[image_input, numerical_input],
                                 outputs=final_output,
                                 name='multi_input_model')
print("\nMulti-Input Functional Model Summary:")
model_multi_input.summary()

# 3. Multi-Output Model (Example: Predict two things from one input)
# Input
text_input = tf.keras.Input(shape=(128,), name='text_features') # E.g., 128-dim word embeddings
shared_dense = layers.Dense(64, activation='relu')(text_input)

# Output 1: Sentiment classification
sentiment_output = layers.Dense(1, activation='sigmoid', name='sentiment_output')(shared_dense)

# Output 2: Topic classification (e.g., 5 topics)
topic_output = layers.Dense(5, activation='softmax', name='topic_output')(shared_dense)

model_multi_output = models.Model(inputs=text_input,
                                  outputs=[sentiment_output, topic_output],
                                  name='multi_output_model')
print("\nMulti-Output Functional Model Summary:")
model_multi_output.summary()

# --------- Task --------- #
'''Build a functional model with shared layers.

Input: tf.keras.Input(shape=(100,), name='features')
Shared hidden layer: Dense(64, activation='relu')
Branch 1: Another Dense(32, activation='relu') followed by an output Dense(1, activation='sigmoid', name='output_A')
Branch 2: Another Dense(32, activation='relu') followed by an output Dense(1, activation='sigmoid', name='output_B')
The two branches should take the output of the shared hidden layer as their input.'''

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models

inputs = tf.keras.Input(shape=(100,), name='features')

# Shared hidden layer
shared_layer = layers.Dense(64, activation='relu')(inputs)

# Branch 1
branch_1_hidden = layers.Dense(32, activation='relu')(shared_layer)
output_A = layers.Dense(1, activation='sigmoid', name='output_A')(branch_1_hidden)

# Branch 2
branch_2_hidden = layers.Dense(32, activation='relu')(shared_layer)
output_B = layers.Dense(1, activation='sigmoid', name='output_B')(branch_2_hidden)

# Create the model with multiple outputs
model_shared_branches = models.Model(inputs=inputs, outputs=[output_A, output_B], name='shared_branch_model')
print("Shared Branch Functional Model Summary:")
model_shared_branches.summary()
