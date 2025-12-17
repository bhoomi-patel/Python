'''Recurrent Neural Networks (RNNs) are a class of neural networks specifically designed to process sequential data, where the order of information matters. Unlike traditional neural networks that treat inputs independently, RNNs have "memory" – they can use information from previous steps in a sequence to influence the processing of the current step. 
LSTMs (Long Short-Term Memory) An improved version of RNNs that solves the problems of “forgetting” old context and vanishing/exploding gradients , this are a special type of RNN that are much better at remembering long-term dependencies.'''

'''Traditional neural networks (like the nn.Linear layers we used for classic classification) treat each input as independent. However, language is sequential: the meaning of "bank" depends on whether it's near "river" or "money." RNNs solve this by having connections that allow information to loop, creating an internal "state" or "memory."'''
# Sample Code (Conceptual RNN Cell with PyTorch)
import torch
import torch.nn as nn

print(f" --- The Challenge of Sequential Data & Introduction to RNNs ---")
# Imagine a single RNN cell. It takes an input at time 't' and a hidden state from 't-1'.
# Parameters: input_size (dim of word embedding), hidden_size (dim of internal memory)
input_size = 10 # e.g., word embedding size
hidden_size = 20 # size of RNN hidden state
rnn_cell = nn.RNN(input_size, hidden_size, batch_first=True,num_layers=1)
# batch_first=True means input/output tensors are (batch, seq, feature)

# --- Simulate a sequence of 3 words (embeddings) for 2 sentences ---
batch_size = 2
seq_len = 3
# Dummy input: (batch_size, sequence_length, input_size)
dummy_input = torch.randn(batch_size, seq_len, input_size)
# For a simple RNN, num_layers=1, num_directions=1, so (1, batch_size, hidden_size)
h0 = torch.zeros(1, batch_size, hidden_size)

print(f"\nDummy Input Sequence Shape: {dummy_input.shape}")
print(f"Initial Hidden State Shape: {h0.shape}")

output , hn = rnn_cell(dummy_input, h0)
print(f"\nRNN Output Shape (output at each time step): {output.shape}")
print(f"RNN Final Hidden State Shape (final memory): {hn.shape}")

# --- LSTM (Long Short-Term Memory) ---
'''LSTMs are a special type of RNN explicitly designed to overcome the vanishing gradient problem, making them much better at learning and remembering long-term dependencies. They achieve this through a complex internal structure called "gates."
It uses three main "gates" to control the flow of information:
Forget Gate: Decides what information to throw away from the cell state.
Input Gate: Decides what new information to store in the cell state.
Output Gate: Decides what parts of the cell state to output as the hidden state. '''

print(f"\n--- LSTM Cell Example ---")
input_size = 10
hidden_size = 20
batch_size = 2
seq_len = 3
# create LSTM module
lstm_cell = nn.LSTM(input_size,hidden_size,batch_first=True,num_layers=1)
# Dummy input
dummy_input = torch.randn(batch_size, seq_len , input_size)
# For LSTM, the initial state is a tuple: (h0, c0)
# h0: initial hidden state (num_layers * num_directions, batch_size, hidden_size)
# c0: initial cell state   (num_layers * num_directions, batch_size, hidden_size)
h0 = torch.zeros(1, batch_size, hidden_size)
c0 = torch.zeros(1, batch_size, hidden_size)
print(f"\nDummy Input Sequence Shape: {dummy_input.shape}")
print(f"Initial Cell State (c0) Shape: {c0.shape}")

output_lstm, (hn_lstm, cn_lstm) = lstm_cell(dummy_input, (h0, c0))

print(f"\nLSTM Output Shape (output at each time step): {output_lstm.shape}")
print(f"LSTM Final Hidden State Shape: {hn_lstm.shape}")
print(f"LSTM Final Cell State Shape: {cn_lstm.shape}")

#  Building an LSTM-based Text Classifier in PyTorch
'''We combine what we've learned: input text is converted to word embeddings, which are then fed into an LSTM layer. The final hidden state of the LSTM (or a concatenation of all hidden states) serves as a fixed-size representation of the entire sequence, which is then fed into a standard feed-forward layer (classifier head) to make a prediction.'''

'''implement LSTM for Number Sequence Classification
Instead of words, let's classify sequences of numbers.
Task: Create a simple nn.LSTM model in PyTorch to classify if a sequence of 3 numbers (each number between 0-9) sums to an even or odd number.
input_size = 1 (each number is an input)
hidden_size = 10
output_dim = 1
Generate a small dataset: [[1,2,3], [4,5,6], [7,8,9]] with labels [0, 1, 0] (0=even sum, 1=odd sum).
Create TensorDataset and DataLoader.
Define the model, criterion (BCEWithLogitsLoss), optimizer (Adam).
Run a very short training loop (e.g., 2-3 epochs).'''

import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
import numpy as np

# Generate dataset
# 1. Generate Data
task_sequences = torch.tensor([
    [1, 2, 3], # Sum=6 (Even) -> Label 0
    [4, 5, 6], # Sum=15 (Odd)  -> Label 1
    [7, 8, 9], # Sum=24 (Even) -> Label 0
    [1, 1, 1], # Sum=3 (Odd)   -> Label 1
    [2, 2, 2]  # Sum=6 (Even)  -> Label 0
], dtype=torch.float32).unsqueeze(2) # Add feature dimension: (batch, seq_len, 1)

task_labels = (task_sequences.sum(dim=1) % 2 != 0).float()
print(f"\nTask Sequences:\n{task_sequences.squeeze(2)}")
print(f"Task Labels:\n{task_labels.squeeze(1)}")
task_dataset = TensorDataset(task_sequences, task_labels)
task_loader = DataLoader(task_dataset, batch_size=2, shuffle=True)

task_dataset = TensorDataset(task_sequences, task_labels)
task_loader = DataLoader(task_dataset, batch_size=2, shuffle=True)

# 2. Define the LSTM Model
class SequenceSumClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # x: (batch_size, seq_len, input_size)
        _, (hidden, _) = self.lstm(x)
        # hidden: (num_layers * num_directions, batch_size, hidden_size)
        # For 1 layer, unidirectional: hidden[-1,:,:] -> (batch_size, hidden_size)
        return self.fc(hidden[-1,:,:])

task_model = SequenceSumClassifier(input_size=1, hidden_size=10, output_size=1)
task_criterion = nn.BCEWithLogitsLoss()
task_optimizer = optim.Adam(task_model.parameters(), lr=0.01)

# 3. Training Loop
print("\n--- Easy Task Solution: LSTM for Number Sequence Classification ---")
for epoch in range(5): # Train for 5 epochs
    task_model.train()
    for X_batch, y_batch in task_loader:
        task_optimizer.zero_grad()
        task_preds = task_model(X_batch)
        task_loss = task_criterion(task_preds, y_batch)
        task_loss.backward()
        task_optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {task_loss.item():.4f}")

# Test prediction
task_model.eval()
with torch.no_grad():
    test_seq = torch.tensor([[1,2,2]], dtype=torch.float32).unsqueeze(2) # Sum=5 (Odd)
    pred_logit = task_model(test_seq).item()
    pred_prob = torch.sigmoid(torch.tensor(pred_logit)).item()
    predicted_label = 1 if pred_prob > 0.5 else 0
    print(f"\nTest Sequence: {test_seq.squeeze(2).tolist()}")
    print(f"Predicted Probability (Odd): {pred_prob:.4f}, Predicted Label: {predicted_label} (Expected: 1)")