'''
Loss Functions: Quantify the error between the model's predictions and the true labels. PyTorch provides various loss functions in torch.nn and torch.nn.functional.
Optimizers: Algorithms that adjust the model's trainable parameters (weights and biases) based on the computed gradients to minimize the loss. Found in torch.optim.
Training Loop: The iterative process where the model performs a forward pass, computes the loss, performs a backward pass (gradient calculation), and updates parameters using an optimizer. This is typically written manually in PyTorch.
'''
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data  import DataLoader, TensorDataset
# 0. set device (CPU or GPU)
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"\nTraining on device: {device}")

# 1. Prepare Dummy Data
# For a binary classification task
num_samples = 100
num__features = 10
X = torch.randn(num_samples,num__features)
y = torch.randint(0,2,(num_samples,1)).float() # binary labels (0 or 1)

# create tensordataset and dataloader
dataset = TensorDataset(X,y)
dataloader = DataLoader(dataset,batch_size=16,shuffle=True)

# 2. Define simple model
class BinaryClassifier(nn.Module):
    def __init__(self,input_size):
        super(BinaryClassifier,self).__init__()
        self.fc1 = nn.Linear(input_size,64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64,1) 
    def forward(self,x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return  x 
model = BinaryClassifier(input_size=num__features).to(device)
print("\n--- Model for Training ---")
print(model)

# 3. Define Loss Function and Optimizer
# nn.BCEWithLogitsLoss combines sigmoid and binary cross-entropy for numerical stability
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(),lr=0.001)

# 4. training loop
num_epochs = 10
print("\n--- Starting Training Loop ---")
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    correct_predictions = 0
    total_predictions = 0

    for batch_X , batch_y in dataloader:
        batch_X, batch_y = batch_X.to(device), batch_y.to(device)
        # 1. forward pass
        outputs = model(batch_X)

        # 2. calculate loss
        loss = criterion(outputs,batch_y)

        # 3. Backward pass (compute gradients)
        optimizer.zero_grad() # Clear previous gradients
        loss.backward()

        # 4. Update model parameters
        optimizer.step()

        running_loss += loss.item()*batch_X.size(0)

        # Calculate accuracy for this batch (for tracking, not for optimization)
        predicted = (torch.sigmoid(outputs) > 0.5).float() # Apply sigmoid and threshold
        total_predictions += batch_y.size(0)
        correct_predictions += (predicted == batch_y).sum().item()

    epoch_loss = running_loss / len(dataloader.dataset)
    epoch_accuracy = correct_predictions / total_predictions * 100

    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {epoch_loss:.4f}, Accuracy: {epoch_accuracy:.2f}%")

print("\nTraining Finished.")

# 5. Evaluation Mode
model.eval()
print("\n--- Evaluating Model (on training data) ---")
with torch.no_grad():
    total_loss = 0
    total_correct = 0
    total_samples = 0
    for batch_X, batch_y in dataloader:
        batch_X, batch_y = batch_X.to(device), batch_y.to(device)
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        total_loss += loss.item() * batch_X.size(0)

        predicted_labels = (torch.sigmoid(outputs) > 0.5).float()
        total_correct += (predicted_labels == batch_y).sum().item()
        total_samples += batch_y.size(0)

    avg_loss = total_loss / total_samples
    avg_accuracy = total_correct / total_samples * 100
    print(f"Evaluation Loss: {avg_loss:.4f}, Evaluation Accuracy: {avg_accuracy:.2f}%")