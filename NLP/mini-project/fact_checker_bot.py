'''Fact Checker Bot helps you keep all your important text documents (like company FAQs, rules, policies, knowledge base) up-to-date.
When you give it a new update or news, it automatically checks if an old document has any statements that might now be wrong, outdated, or need updating—by really understanding the meaning of the old and new facts, not just matching words.
It will highlight, for example: "Old: 'Return period is 30 days.' | New: 'Return period is 60 days.' → Please update your docs!" '''
'''Pre-requisite Setup :python -m pip install sentence-transformers pandas scikit-learn'''



from sentence_transformers import SentenceTransformer
import torch
import numpy as np

# --- 1. Setup: Load a Simple, Fast Embedding Model
print("Loading AI 'brain' for understanding meaning...")
model = SentenceTransformer('all-MiniLM-L6-v2')  # small, good for CPU

# --- 2. Your "Old" Knowledge Base Documents (as simple sentences)
old_facts = [
    "Our return policy allows returns within 30 days.",
    "Free shipping is offered on orders above $50.",
    "Customer support is available from 9am to 5pm.",
    "Warranty covers devices for one year only.",
    "Gift cards cannot be redeemed for cash."
]

# --- 3. New Updates/Announcements (incoming info)
new_updates = [
    "The return policy now gives you 60 days to return items.",
    "Support hours are extended to 8pm.",
    "Free shipping now requires a minimum order of $100.",
    "We now offer two-year warranty coverage."
]

# --- 4. Get Sentence Embeddings (meaning vectors)
old_vecs = model.encode(old_facts, convert_to_tensor=True)
new_vecs = model.encode(new_updates, convert_to_tensor=True)

# --- 5. Fact Checker Logic: Find Old Facts Most Similar to Each New Update
# (use cosine similarity to measure meaning closeness)
threshold = 0.8  # similarity threshold: 1.0 is identical; try 0.8 for a good match

for i, new_fact in enumerate(new_updates):
    scores = torch.nn.functional.cosine_similarity(
        new_vecs[i].unsqueeze(0), old_vecs
    ).cpu().numpy()
    best_idx = np.argmax(scores)
    best_score = scores[best_idx]

    if best_score > threshold:
        print("\n  Fact Checker Alert!")
        print(f"- POSSIBLY OUTDATED: {old_facts[best_idx]}")
        print(f"- NEW UPDATE:        {new_fact}")
        print(f"- Similarity score: {best_score:.2f}")
    else:
        print("\n(Info): No close matching fact found for this new info.")
        print(f"- NEW UPDATE: {new_fact}")
