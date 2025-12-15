'''In PyTorch, the most common way to save and load models is by saving/loading the model's state_dict. A state_dict is a Python dictionary object that maps each layer to its trainable parameters (weights and biases). You can also save/load the entire model object, but state_dict is more common for flexibility.
- model.state_dict(): Returns a dictionary containing all the state of the model.
- torch.save(): Serializes and saves an object to disk.
- torch.load(): Deserializes and loads an object from disk.
- model.load_state_dict(): Loads a state_dict into the model.
'''
import torch
import torch.nn as nn
import torch.optim as optim
import os

# 0. Set device
device = "cuda" if torch.cuda.is_available() else "cpu"

# 1. define simple model
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet,self).__init__()
        self.fc1 = nn.Linear(10,20)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(20,1)
    def forward(self,x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

model_to_save = SimpleNet().to(device)
optimizer_to_save = optim.Adam(model_to_save.parameters(), lr=0.001)
print("--- Saving Model State ---")
# Recommended way: Save model's state_dict and optimizer's state_dict
checkpoint = {
    'model_state_dict': model_to_save.state_dict(),
    'optimizer_state_dict': optimizer_to_save.state_dict(),
    'epoch': 5, # You can save other info too
    'loss': 0.123 # Example
}
save_path = 'model_checkpoint.pth' # .pth is a common extension for PyTorch models
torch.save(checkpoint, save_path)
print(f"Model and optimizer state saved to '{save_path}'")

# Another way: Just save model's state_dict (useful if you rebuild model separately)
torch.save(model_to_save.state_dict(), 'model_weights.pth')
print("Only model weights saved to 'model_weights.pth'")

# You can also save the entire model (not generally recommended for production, more for research/development)
torch.save(model_to_save, 'full_model.pth')
print("Full model object saved to 'full_model.pth'")

print("\n--- Loading Model State ---")
# 1. Load from checkpoint (model and optimizer state)
loaded_checkpoint = torch.load(save_path)

# Create new model and optimizer objects, then load their states
loaded_model = SimpleNet().to(device)
loaded_optimizer = optim.Adam(loaded_model.parameters(), lr=0.001) # Must define optimizer again

loaded_model.load_state_dict(loaded_checkpoint['model_state_dict'])
loaded_optimizer.load_state_dict(loaded_checkpoint['optimizer_state_dict'])

# Resume training from where it left off, if desired
# loaded_epoch = loaded_checkpoint['epoch']
# loaded_loss = loaded_checkpoint['loss']

print("Model and optimizer state loaded from checkpoint.")
print("Loaded Model weights (first layer):\n", loaded_model.fc1.weight) # Check if weights are loaded

# 2. Load only weights into a new model (must have the same architecture!)
new_model_for_weights = SimpleNet().to(device)
new_model_for_weights.load_state_dict(torch.load('model_weights.pth'))
print("\nOnly weights loaded into a new model.")
print("New Model weights (first layer):\n", new_model_for_weights.fc1.weight)


# 3. Load entire model object
loaded_full_model = torch.load('full_model.pth')
loaded_full_model.eval() # Set to eval mode
print("\nFull model object loaded.")
print("Loaded Full Model weights (first layer):\n", loaded_full_model.fc1.weight)

# Clean up created files (optional)
# os.remove(save_path)
# os.remove('model_weights.pth')
# os.remove('full_model.pth')