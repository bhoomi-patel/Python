# Word Embeddings: Word2Vec, GloVe
'''Word embeddings represent each unique word as a vector of real numbers, such that words used in similar contexts have similar vectors. This makes it possible for ML models to "sense" semantic meaning and analogies (e.g., king - man + woman ≈ queen) , The key idea is that words with similar meanings or that appear in similar contexts will have similar vector representations.'''
'''setup : install gensim for Word2Vec and FastText.  --> python -m pip install gensim'''

# Word2Vec
'''Simple Definition: A neural network framework that learns word embeddings from large corpora by predicting which words occur together.
Main Models:
CBOW (Continuous Bag of Words): Predict the current word from surrounding context.
Skip-gram: Predict the surrounding context from the current word (better for finding rare word representations).'''
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
# nltk.download('punkt')  # If running for the 1st time
sentences = [
    "A cat chases a mouse.",
    "The quick brown fox jumps over the lazy dog.",
    "Dogs and cats are great pets.",
    "I love my pet dog."
]
# Tokenize sentences
tokenized = [word_tokenize(sent.lower()) for sent in sentences]

# Train word2vec on corpus
model = Word2Vec(tokenized,vector_size=50,window=2,min_count=1,sg=1) # sg=1 for skip gram
print("\nVocabulary:",list(model.wv.key_to_index.keys()))

# Find similarity between "cat" and other words
print("\nWords similar to 'cat':", model.wv.most_similar("cat"))

# Vector for a word
print("\nVector for 'dog':", model.wv['dog'])

# --- GloVe (Global Vectors)---
'''Another embedding technique, but instead of predicting context, it directly uses the co-occurrence counts of words in the entire corpus.'''

import numpy as np
glove = {
    "cat" : np.array([0.2, 0.1, 0.7]),
    "kitten": np.array([0.21, 0.09, 0.75]),
    "dog": np.array([0.27, 0.19, 0.60]),
    "puppy": np.array([0.25, 0.12, 0.69])
}
# calculate cosine similarity between vectors
def cosine_similarity(a,b):
    a = a/np.linalg.norm(a)
    b = b/np.linalg.norm(b)
    return np.dot(a,b)
print("\nCosine similarity between 'cat' and 'kitten':", cosine_similarity(glove['cat'], glove['kitten']))
print("Cosine similarity between 'cat' and 'dog':", cosine_similarity(glove['cat'], glove['dog']))

# ---- Visualizing Word Embeddings ---
'''With hundreds of dimensions, visualizing embeddings directly is hard. We use t-SNE or PCA to reduce dimensions for plotting.'''
from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt
words = list(glove.keys())
vectors = np.array([glove[w] for w in words])
reduced = PCA(n_components=2).fit_transform(vectors)

for i,word in enumerate(words):
    plt.scatter(reduced[i,0],reduced[i,1])
    plt.annotate(word,xy=(reduced[i,0],reduced[i,1]))
plt.title("Word Embeddings (Simulated GloVe) Visualized with PCA")
plt.show()