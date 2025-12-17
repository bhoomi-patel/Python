'''Transformers are neural networks (introduced in 2017) that use self-attention to process entire text sequences in parallel.
They replaced RNNs/LSTMs for almost all large NLP tasks because they are faster, scale better, and capture context much more effectively.
Examples: BERT (Bidirectional Encoder Representations from Transformers), GPT-2/3/4, RoBERTa, DistilBERT, etc.
Hugging Face (transformers library) makes it EASY to use, fine-tune, and deploy dozens of the world’s best NLP (and vision/audio) models, all with PyTorch backend.
Key Components in Hugging Face:-
AutoTokenizer: Handles text preprocessing (tokenization, adding special tokens, padding) specific to each Transformer model.
AutoModel: Automatically loads the pre-trained Transformer model architecture and its weights.
Trainer: A high-level API for fine-tuning models, abstracting away the training loop.'''

# Basic Example: Sentiment Analysis with Pretrained BERT
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
# test predictions
texts= [
    "I absolutely loved this movie!",
    "The plot was boring and predictable.",
    "An average experience, nothing special."
]
results = classifier(texts)
for text,pred in zip(texts,results):
    print(f"'{text}' => {pred['label']} (score: {pred['score']:.2f})")

# -- Custom Example: Text Embedding with BERT (for semantic search!)
from transformers import AutoTokenizer, AutoModel
import torch

# Load the BERT tokenizer and model (Hugging Face)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

text = "Transformers are amazing for NLP tasks!"

# Tokenize and get PyTorch tensors
inputs = tokenizer(text, return_tensors="pt")

# Get the model's last hidden state (embeddings for each token)
with torch.no_grad():
    outputs = model(**inputs)
    last_hidden_state = outputs.last_hidden_state  # shape: (batch_size, seq_len, hidden_dim)

# Get a "sentence embedding" by averaging the hidden states
sentence_embedding = last_hidden_state.mean(dim=1).squeeze()  # shape: (hidden_dim,)
print(f"Sentence embedding shape: {sentence_embedding.shape}")
print(f"First 5 values: {sentence_embedding[:5]}")



# -----------#
# Fine-tuning a Pretrained Transformer for Text Classification
'''Fine-tuning involves taking a pre-trained model and training it on a specific task (like sentiment analysis) with a smaller dataset. This allows the model to adapt its learned representations to the nuances of the new task without starting from scratch.'''
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
import numpy as np
# Sample dataset
texts = [
    "I love this product!",
    "This is the worst service ever.",
    "Absolutely fantastic experience.",
    "I will never buy this again."
]
labels = [1, 0, 1, 0]  # 1=positive, 0=negative
# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)
# Tokenize dataset
encodings = tokenizer(texts, truncation=True, padding=True, return_tensors="pt")
labels = torch.tensor(labels)
# Create a custom dataset class
class SentimentDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        item['labels'] = self.labels[idx]
        return item

    def __len__(self):
        return len(self.labels)
dataset = SentimentDataset(encodings, labels)
# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=2,
    per_device_train_batch_size=2,

    logging_dir="./logs",
    logging_steps=10,
    no_cuda=True  # Set to False if GPU is available
)
# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)
# Fine-tune the model
trainer.train()
print("\n--- Fine-tuning Complete ---")
# Test the fine-tuned model
test_texts = [
    "I had a wonderful time!",
    "This was a terrible experience."
]
test_encodings = tokenizer(test_texts, truncation=True, padding=True, return_tensors="pt")
with torch.no_grad():
    outputs = model(**test_encodings)
    predictions = torch.argmax(outputs.logits, dim=-1)
for text, pred in zip(test_texts, predictions):
    label = "positive" if pred.item() == 1 else "negative"
    print(f"'{text}' => {label}")

