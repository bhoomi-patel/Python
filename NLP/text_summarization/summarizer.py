'''Text summarization is the task of shortening a long piece of text while preserving its key information and meaning.
Extractive summarization selects the most important sentences verbatim from the text.
Abstractive summarization generates new sentences, paraphrasing or condensing content, much like what a human would do.
Transformer Role: Modern abstractive summarization models are almost exclusively built using Transformer encoder-decoder architectures.'''

# Abstractive Summarization with Hugging Face Transformers
'''Encoder-Decoder Transformers: The model's encoder processes the input document, and its decoder generates the summary based on the encoder's understanding.
Pre-trained Models: Models like t5-small, facebook/bart-large-cnn, google/pegasus-cnn_dailymail are commonly used.
Generation Parameters: min_length, max_length, num_beams, do_sample, temperature are used to control the summary's length, quality, and creativity.'''
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
# 1. Choose a pre-trained summarization model
# 't5-small' is a small, fast model. 't5-base', 'facebook/bart-large-cnn' are larger.
model_name = "t5-small"
# 2. Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
# Set model to evaluation mode and move to device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

print(f"\nLoaded {model_name} tokenizer and model for summarization.")

# 3. Input Text to Summarize
article = """
Artificial intelligence (AI) has been a field of study for decades,
but recent advancements, particularly in machine learning and deep learning,
have propelled it into mainstream applications. AI's ability to process vast
amounts of data, identify patterns, and make predictions or decisions
has led to breakthroughs in areas such as natural language processing,
computer vision, and autonomous systems. One of the most significant
developments is the Transformer architecture, which underpins models
like BERT and GPT, enabling more sophisticated language understanding
and generation. These models are now used in everything from chatbots
and translation services to content creation and drug discovery.
The ethical implications and potential societal impact of AI are
also increasingly becoming a focus of discussion among researchers,
policymakers, and the public.
"""
# 4. Prepare Input for the Model
# T5 models typically expect a prefix like "summarize: "
input_text = "summarize: " + article
inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
# Move inputs to the same device as the model
inputs = {key: val.to(device) for key, val in inputs.items()}
# 5. Generate Summary
with torch.no_grad():
    # `generate` method handles the decoding process
    # `num_beams`: Higher value (e.g., 4) improves summary quality but is slower.
    # `length_penalty`: Encourages/discourages longer summaries.
    # `max_new_tokens`: Max length of the generated summary.
    summary_ids = model.generate(
        inputs["input_ids"],
        num_beams=4, # Beam search for better quality
        max_new_tokens=50, # Max tokens for the summary
        min_length=15,
        early_stopping=True # Stop when all beam hypotheses have finished
    )

# 6. Decode and Print Summary
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("\nOriginal Article:")
print(article)
print("\nGenerated Summary:")
print(summary)

#  Extractive Summarization (Brief Introduction)
''' Extractive summarization identifies the most important sentences in a document and stitches them together to form a summary. It does not generate new text.

Key Concepts:
Sentence Scoring: Various methods to score the importance of each sentence (e.g., TF-IDF, TextRank, sentence embeddings similarity to document centroid).
Redundancy Removal: Ensuring the selected sentences don't repeat information.
Cohesion: Selecting sentences that flow well together'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string

# 1. Input Text
article_extractive = """
The Amazon rainforest is the largest tropical rainforest in the world.
It covers an area of approximately 6.7 million square kilometers
(2.6 million square miles), spanning nine countries in South America:
Brazil, Peru, Colombia, Ecuador, Bolivia, Guyana, Suriname, French Guiana, and Venezuela.
The Amazon River, which flows through the rainforest, is the largest river by discharge volume in the world.
Deforestation in the Amazon is a significant environmental concern.
It contributes to climate change and threatens biodiversity.
Efforts are underway by international organizations and local governments to protect this vital ecosystem.
"""

# 2. Preprocessing & Sentence Tokenization
# Simple preprocessing (lowercase, remove punctuation, remove stopwords)
stop_words_english = set(stopwords.words('english'))
def preprocess_sentence(sentence):
    return ' '.join([
        word for word in word_tokenize(sentence.lower())
        if word.isalpha() and word not in stop_words_english
    ])

sentences = sent_tokenize(article_extractive)
# Filter out very short sentences or those that are just punctuation etc.
filtered_sentences = [s for s in sentences if len(word_tokenize(s)) > 5]
preprocessed_sentences = [preprocess_sentence(s) for s in filtered_sentences]

# 3. TF-IDF Vectorization for sentences
# Each sentence becomes a "document" for TF-IDF
vectorizer = TfidfVectorizer()
sentence_vectors = vectorizer.fit_transform(preprocessed_sentences)

# 4. Calculate Similarity Matrix
# We want to find sentences that are most similar to each other (or to the "centroid" of the document)
# Here, we'll calculate similarity of each sentence vector to the average vector of all sentences (document centroid)
document_centroid_vector = sentence_vectors.sum(axis=0) / sentence_vectors.shape[0]
# Reshape centroid for cosine_similarity (needs 2D array)
document_centroid_vector = document_centroid_vector.reshape(1, -1)

# Calculate cosine similarity between each sentence and the document centroid
sentence_scores = cosine_similarity(sentence_vectors, document_centroid_vector).flatten()

# 5. Rank Sentences and Select Top N
num_summary_sentences = 3 # Desired number of sentences in the summary
ranked_sentence_indices = sentence_scores.argsort()[-num_summary_sentences:][::-1] # Get indices of top N, in descending order of score
ranked_sentence_indices.sort() # Sort by original order to maintain flow

extractive_summary = [filtered_sentences[i] for i in ranked_sentence_indices]

print("\nOriginal Article:")
print(article_extractive)
print(f"\nExtractive Summary ({num_summary_sentences} sentences):")
print("\n".join(extractive_summary))