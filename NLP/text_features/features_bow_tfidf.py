'''Text feature extraction is the process of transforming raw text (or cleaned tokens from preprocessing) into numerical representations (vectors) that machine learning algorithms can understand and process.
Algorithms like linear regression, SVMs, or neural networks cannot directly work with text strings. Bag-of-Words and TF-IDF are two foundational techniques for achieving this.'''

# 1. Bag-of-Words (BoW)
'''Counts how many times each word (from your entire vocabulary) appears in a document. Ignores order and grammar.'''
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
documents = [
    "Cats and dogs are great pets.",
    "Dogs are loyal animals.",
    "Cats are independent creatures."
]
# Initialize vectorizer
vectorizer = CountVectorizer()

# Learn vocabulary and transform texts into feature matrix
bow_matrix = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names_out()
print(f"\nVocabulary: {feature_names}")

# Convert sparse matrix to DataFrame for easy inspection
df_bow = pd.DataFrame(bow_matrix.toarray(),columns=feature_names)
print("--- Bag-of-Words Feature Matrix ---\n")
print(df_bow)

# 2. TF-IDF (Term Frequency–Inverse Document Frequency)
'''TF-IDF is a statistical measure that evaluates how relevant a word is to a document within a collection of documents (corpus). It assigns a weight to each word, increasing with the number of times a word appears in the document (Term Frequency) but decreasing with the number of documents the word appears in (Inverse Document Frequency). This down-weights common words (like "the," "is") that appear everywhere, and highlights rare, important words.
TF-IDF Score: TF * IDF. A high TF-IDF score means the word is frequent in this document but rare across all documents, making it a good indicator of the document's content.'''
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
documents = [
    "Cats and dogs are great pets.",
    "Dogs are loyal animals.",
    "Cats are independent creatures."
]
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

tfidf_features_name = tfidf_vectorizer.get_feature_names_out()
print(f"\nVocabulary: {tfidf_features_name}")

tfidf_df = pd.DataFrame(tfidf_matrix.toarray(),columns=tfidf_features_name)
print("\nDocument-Term Matrix (TF-IDF):\n", tfidf_df)

# ------ Task ------
'''Given these two short reviews:
"I love sunny weather and clear skies."
"Rainy weather makes me sad, but a clear sky cheers me up."
Build a BoW and TF-IDF feature matrix for them.'''

reviews = [
    "I love sunny weather and clear skies.",
    "Rainy weather makes me sad, but a clear sky cheers me up."
]

# Bag-of-Words
vec = CountVectorizer()
X_bow = vec.fit_transform(reviews)
df_bow = pd.DataFrame(X_bow.toarray(), columns=vec.get_feature_names_out())
print("\nBoW for Reviews:\n", df_bow)

# TF-IDF
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(reviews)
df_tfidf = pd.DataFrame(X_tfidf.toarray(), columns=tfidf.get_feature_names_out())
print("\nTF-IDF for Reviews:\n", df_tfidf)

# 3. N-grams (Bi-grams, Tri-grams)
''' Instead of single words, you can count pairs (bigrams) or triplets (trigrams) of words, capturing short phrases and some order.'''
bi_vectorizer = CountVectorizer(ngram_range=(1,2))
x_ngrams = bi_vectorizer.fit_transform(documents)
df_ngram = pd.DataFrame(x_ngrams.toarray(),columns=bi_vectorizer.get_feature_names_out())

print("\n--- Bag-of-Words (with Bigrams) ---\n")
print(df_ngram)