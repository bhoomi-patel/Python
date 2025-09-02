import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

# Create sample dataset
np.random.seed(42)
n_samples = 1000

# Generate synthetic house data
data = {
    'size_sqft': np.random.normal(2000, 500, n_samples),
    'bedrooms': np.random.randint(1, 6, n_samples),
    'bathrooms': np.random.randint(1, 4, n_samples),
    'age_years': np.random.randint(0, 50, n_samples),
    'garage': np.random.randint(0, 3, n_samples)
}

df = pd.DataFrame(data)

# Create realistic price based on features
df['price'] = (
    df['size_sqft'] * 150 +
    df['bedrooms'] * 10000 +
    df['bathrooms'] * 15000 +
    (50 - df['age_years']) * 1000 +
    df['garage'] * 8000 +
    np.random.normal(0, 20000, n_samples)
)

print("🏠 HOUSE PRICE PREDICTION PROJECT")
print("=" * 50)
print(f"Dataset shape: {df.shape}")
print(f"Dataset info:\n{df.describe()}")

# Prepare features and target
X = df.drop('price', axis=1)
y = df['price']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model 1: Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train)
lr_pred = lr_model.predict(X_test_scaled)

# Model 2: Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)  # RF doesn't need scaling
rf_pred = rf_model.predict(X_test)

# Evaluate models
lr_mse = mean_squared_error(y_test, lr_pred)
lr_r2 = r2_score(y_test, lr_pred)

rf_mse = mean_squared_error(y_test, rf_pred)
rf_r2 = r2_score(y_test, rf_pred)

print("\n MODEL COMPARISON")
print("-" * 30)
print(f"Linear Regression:")
print(f"  MSE: ${lr_mse:,.2f}")
print(f"  R²:  {lr_r2:.3f}")

print(f"\nRandom Forest:")
print(f"  MSE: ${rf_mse:,.2f}")
print(f"  R²:  {rf_r2:.3f}")

# Feature importance (Random Forest)
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print(f"\n FEATURE IMPORTANCE:")
print(feature_importance)

# Prediction example
sample_house = [[2500, 3, 2, 10, 2]]  # 2500 sqft, 3br, 2ba, 10yrs old, 2 garage
sample_scaled = scaler.transform(sample_house)

lr_price = lr_model.predict(sample_scaled)[0]
rf_price = rf_model.predict(sample_house)[0]

print(f"\n SAMPLE PREDICTION:")
print(f"House: 2500 sqft, 3br, 2ba, 10yrs old, 2-car garage")
print(f"Linear Regression: ${lr_price:,.2f}")
print(f"Random Forest: ${rf_price:,.2f}")
