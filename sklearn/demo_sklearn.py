''' sklearn.
├── datasets          # Sample datasets
├── model_selection   # Train/test split, cross-validation
├── preprocessing     # Data scaling, encoding
├── linear_model      # Linear algorithms
├── tree              # Decision trees
├── ensemble          # Random Forest, Gradient Boosting
├── svm               # Support Vector Machines
├── cluster           # Clustering algorithms
├── decomposition     # PCA, dimensionality reduction
└── metrics           # Evaluation metrics
 '''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
x,y = datasets.load_iris(return_x_y=True)

# split data
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# preprocess
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# create model
model = LogisticRegression()

# fit model
model.fit(x_train_scaled,y_train)

# predict(
y_pred = model.predict(x_test_scaled)

# evaluate
accuracy = accuracy_score(y_test,y_pred)







