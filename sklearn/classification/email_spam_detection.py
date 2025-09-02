import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report , accuracy_score
from sklearn.pipeline import Pipeline 
import re

# Create sample email dataset
emails = [  # Spam emails
    "URGENT! You've won $1,000,000! Click here NOW!",
    "Make money fast! Work from home! Limited time offer!",
    "FREE VIAGRA! No prescription needed! Order now!",
    "You're pre-approved! Get your credit card today!",
    "CONGRATULATIONS! You've been selected for a special offer!",
    "Lose weight fast! Amazing results guaranteed!",
    "Get rich quick! Investment opportunity of a lifetime!",
    "FREE iPhone! Just pay shipping! Limited time!",
    "Your account will be closed! Update payment info now!",
    "URGENT: Your payment is overdue! Pay immediately!",

     # Ham (legitimate) emails
    "Hi John, let's meet for lunch tomorrow at 1 PM.",
    "The quarterly report is ready for review.",
    "Your appointment is confirmed for next Tuesday.",
    "Thank you for your purchase. Your order will ship soon.",
    "Meeting rescheduled to Friday at 3 PM.",
    "Here's the presentation we discussed yesterday.",
    "Your subscription renewal is due next month.",
    "Great job on the project! Looking forward to the next phase.",
    "Can you send me the updated budget proposal?",
    "Welcome to our newsletter! We're glad you joined.",
    "The conference call is scheduled for 2 PM today.",
    "Your technical support ticket has been resolved.",
    "Please review the attached contract and let me know.",
    "Happy birthday! Hope you have a wonderful day.",
    "The system maintenance is scheduled for this weekend."
    ]
labels = [1]*10  + [0] *15  # 0 = no spam (ham) , 1 = spam
# create dataframe
df = pd.DataFrame({'email':emails , 'label': labels })
print(" ----- EMAIL SPAM DETECTION PROJECT -----")
print("=" * 50 )
print(f"Dataset Shape: {df.shape}")
print (f"Spam emails: {sum(labels)}")
print(f"Ham emails: {len(labels)-sum(labels)}")

# text preprocessing function
def preprocess_text(text):
    text = text.lower()
    # remove special characters and digits
    text=re.sub(r'[^a-zA-Z\s]','',text)
    return text

df['email_clean']=df['email'].apply(preprocess_text)
x= df['email_clean']
y= df['label']

# split data
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42,stratify=y)

#create pipelines
models = {
    'Naive Bayes':Pipeline([('tfidf',TfidfVectorizer(max_features=1000,stop_words='english')),('nb',MultinomialNB())]),
    'Logistic Regression':Pipeline([('tfidf',TfidfVectorizer(max_features=1000,stop_words='english')),('lr',LogisticRegression(random_state=42)) ]),
    'SVM':Pipeline([('tfidf',TfidfVectorizer(max_features=1000,stop_words='english')),('svm',SVC(random_state=42))])
}

# train and evaluate models
results = {}
for name , model in models.items():
    model.fit(x_train,y_train)
    # make prediction
    y_pred = model.predict(x_test)
    # calculate accuracy
    accuracy = accuracy_score(y_test,y_pred)
    results[name] = accuracy

    print(f"\n {name.upper()}")
    print("-"*30)
    print(f"Accuracy : {accuracy:.3f}")
    print("\n classification Report :")
    print(classification_report(y_test,y_pred,target_names=['Ham (No Spam)' , 'Spam']))

# best model
best_model = max(results,key=results.get)
print(f"\n BEST MODEL : {best_model} (Accuracy:{results[best_model]:.3f})")

# test with new emails
test_emails = [
    "Congratulations! You've won a free vacation!",
    "Can we schedule a meeting for next week?",
    "FREE MONEY! No strings attached! Act now!"
]

print(f"\n Testing New Emails : ")
print("-"*30)

for email in test_emails:
    clean_email=preprocess_text(email)
    prediction = models[best_model].predict([clean_email])[0]
    probability = models[best_model].predict_proba([clean_email])[0]

    label = "SPAM" if prediction == 1 else "HAM (NO SPAM)"
    confidence = max(probability)

    print(f"Email:'{email}' ")
    print(f"Prediction : {label} (confidence : {confidence:.2f})")
    print()