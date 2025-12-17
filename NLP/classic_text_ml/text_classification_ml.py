'''Text classification is the task of assigning pre-defined categories (labels) to text documents. It's a fundamental supervised learning problem in NLP. "Classic" text classification refers to using traditional machine learning algorithms (like Naive Bayes or Logistic Regression) coupled with count-based text features (like BoW or TF-IDF).'''
# 1. Text Classification
'''We'll use a small custom dataset for demo for Spam Detection '''
# Sample: toy spam/ham dataset
documents = [
    "Congratulations, you have won a free lottery ticket!", # spam
    "Call this number now to claim your prize.",            # spam
    "Low loan interest rates available, click for details.",# spam
    "Let's study for our data science exam tomorrow.",      # ham
    "Are we meeting for coffee later?",                     # ham
    "Don't forget to bring your laptop for the workshop."   # ham
]
labels = ["spam", "spam", "spam", "ham", "ham", "ham"]

print("--- Step 1: Data ---")
print(list(zip(documents, labels)))

#  step 2 - create features (tf-idf)
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(documents)
print("\n--- Step 2: TF-IDF Features Created ---")
print(x.toarray())  # Each row is a vector for a document

# Step 3: Train-Test Split
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x,labels,test_size=0.5,random_state=42)

# Step 4: Training a Classifier
'''We'll use Multinomial Naive Bayes (simple, works great for text).'''
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(x_train,y_train)
print("\n--- Step 4: Model Trained ---")

# Step 5: Make Predictions
y_pred = model.predict(x_test)
print("\n--- Step 5: Predictions on Test Data ---")
for text,pred in zip(x_test,y_pred):
    print(f"Predicted : {pred}")

# Step 6: Evaluate
from sklearn.metrics import accuracy_score,classification_report
print("\n--- Step 6: Metrics ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Try with Logistic Regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(x_train,y_train)
y_pred_lr = logreg.predict(x_test)
print("\n--- Logistic Regression ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred_lr):.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred_lr))