# Personal AI Research Assistant: Prior Knowledge Alerter
'''This PyTorch mini-project builds a "Personal Knowledge Base" (PKB) from technical articles you "read." It intelligently alerts you when new articles mention concepts you've seen before, helping you recall context or notice new developments. It acts like a smart memory, highlighting connections across your reading history to prevent information overload.
We use a tiny PyTorch neural network to make sense of the meanings and compare old vs. new concepts.
You’ll see “recall prompts” showing what’s old, what’s new, and exactly where you encountered things before!
'''
# Step 1: Synthetic "Tech Paper" Data
'''We’ll simulate small "research articles", each with 2-3 key concepts and a one-line description.'''
import random
# Each article: title, {concept: description}
fake_papers=[
    {
       'title': "EfficientNet's New Scaling Rule",
        'concepts': {
            "EfficientNet": "A family of neural networks balancing depth, width, and resolution.",
            "Compound Scaling": "A method to scale all dimensions of a network together, not just one."
        }
    },
    {
        'title': "Understanding Attention in Transformers",
        'concepts': {
            "Attention Mechanism": "Allows transformers to focus on relevant words by weighting input tokens.",
            "Self-Attention": "Each word in a sequence attends to all other words to establish context.",
            "Transformer": "A deep learning model architecture using stacked self-attention and feedforward layers."
        }
    },
    {
        'title': "What’s New in Diffusion Models",
        'concepts': {
            "Diffusion Model": "A generative model that learns data distributions by simulating gradual noise addition and removal.",
            "Latent Diffusion": "Compresses images into a smaller space before modeling the diffusion process.",
            "Self-Attention": "Used in diffusion models to enhance image generation quality."
        }
    }
]
# Step 2: Mini Text Encoder in PyTorch
'''A simple neural net to embed each concept+description into a vector.'''
import torch
import torch.nn as nn
ALL_CHARS = 'abcdefghijklmnopqrstuvwxyz -'
MAX_LEN = 40

def vectorize(text):
    arr = torch.zeros(MAX_LEN,len(ALL_CHARS))
    text = text.lower()[:MAX_LEN]
    for i,c in enumerate(text):
        idx = ALL_CHARS.find(c) if c in ALL_CHARS else 0
        arr[i,idx]=1.
    return arr.flatten() # Shape: (MAX_LEN * n_chars,)

# very simple mlp encoder
class SimpleEncoder(nn.Module):
    def __init__(self, in_dim, out_dim=32):
        super().__init__()
        self.linear = nn.Sequential(
            nn.Linear(in_dim, 64),
            nn.ReLU(),
            nn.Linear(64, out_dim)
        )
    def forward(self, x): return self.linear(x)

encoder = SimpleEncoder(MAX_LEN * len(ALL_CHARS))

# Step 3: Build and Update Your PKB (“Memory Graph”)
# PKB: concept -> {embedding, first_seen_in_title}
PKB = {}

def get_embedding(concept, desc):
    x = vectorize(concept + " " + desc)
    with torch.no_grad():
        emb = encoder(x)
        emb = emb / emb.norm()  # Normalize for cosine
        return emb

# Step 4: Recall Prompts When Reading a New Paper
from torch.nn.functional import cosine_similarity

def recall_prompts_for_paper(paper, PKB, threshold=0.85):
    alerts = []
    new_concepts = []
    for concept, desc in paper['concepts'].items():
        emb = get_embedding(concept, desc)
        found = False
        for pkb_concept, info in PKB.items():
            sim = cosine_similarity(emb.unsqueeze(0), info['embedding'].unsqueeze(0)).item()
            if sim > threshold:
                alerts.append(f" Recall: '{concept}' matches your prior '{pkb_concept}' from '{info['origin']}' (sim={sim:.2f})")
                found = True
                break
        if not found:
            new_concepts.append((concept, desc, emb))
            alerts.append(f" New concept: '{concept}' not in your PKB yet.")
    # Update PKB with new concepts
    for concept, desc, emb in new_concepts:
        PKB[concept] = {'embedding': emb, 'origin': paper['title']}
    return alerts

# Let’s simulate a session:
for i, paper in enumerate(fake_papers):
    print(f"\n=== You Open: '{paper['title']}' ===")
    prompts = recall_prompts_for_paper(paper, PKB)
    for p in prompts: print(p)
    print("PKB now contains:", list(PKB.keys()))