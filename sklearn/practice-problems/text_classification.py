from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Sample data
texts = [
    "This movie is fantastic! Best film ever",
    "Terrible movie, waste of time",
    "Great acting and amazing plot",
    "Boring and predictable storyline",
    "Must watch! Highly recommended",
    "Worst movie I've ever seen"
]
labels = [1, 0, 1, 0, 1, 0]  # 1: positive, 0: negative

# Create more training data
texts = texts * 50  # Replicate for more samples
labels = labels * 50

# Split data
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Create pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

# Train
pipeline.fit(X_train, y_train)

# Predict
y_pred = pipeline.predict(X_test)

# Evaluate
print(classification_report(y_test, y_pred, target_names=['Negative', 'Positive']))

# Test on new data
new_reviews = [
    "This is an excellent movie with great performances",
    "I fell asleep watching this boring film"
]
predictions = pipeline.predict(new_reviews)
for review, pred in zip(new_reviews, predictions):
    sentiment = "Positive" if pred == 1 else "Negative"
    print(f"Review: {review}\nSentiment: {sentiment}\n")
