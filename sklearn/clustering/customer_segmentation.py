import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# Create sample customer dataset
np.random.seed(42)
n_customers = 500

# Generate synthetic customer data
data = {
    'age': np.random.randint(18, 70, n_customers),
    'income': np.random.normal(50000, 20000, n_customers),
    'spending_score': np.random.randint(1, 100, n_customers),
    'frequency': np.random.randint(1, 50, n_customers),
    'recency': np.random.randint(1, 365, n_customers)
}

df = pd.DataFrame(data)
df['income'] = np.abs(df['income'])  # Ensure positive income

print(" CUSTOMER SEGMENTATION PROJECT")
print("=" * 50)
print(f"Dataset shape: {df.shape}")
print("\nDataset Overview:")
print(df.describe())

# Prepare the data
X = df.values

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Find optimal number of clusters using elbow method
inertias = []
silhouette_scores = []
k_range = range(2, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Find optimal k
optimal_k = k_range[np.argmax(silhouette_scores)]
print(f"\n OPTIMAL NUMBER OF CLUSTERS: {optimal_k}")
print(f"Silhouette Score: {max(silhouette_scores):.3f}")

# Apply K-Means with optimal k
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

# Add cluster labels to dataframe
df['cluster'] = clusters

# Analyze clusters
print(f"\n CLUSTER ANALYSIS:")
print("-" * 30)

cluster_summary = df.groupby('cluster').agg({
    'age': 'mean',
    'income': 'mean',
    'spending_score': 'mean',
    'frequency': 'mean',
    'recency': 'mean'
}).round(2)

print(cluster_summary)

# Customer segment interpretation
print(f"\n  CUSTOMER SEGMENTS:")
print("-" * 30)

for cluster_id in range(optimal_k):
    cluster_data = df[df['cluster'] == cluster_id]
    size = len(cluster_data)
    
    avg_age = cluster_data['age'].mean()
    avg_income = cluster_data['income'].mean()
    avg_spending = cluster_data['spending_score'].mean()
    avg_frequency = cluster_data['frequency'].mean()
    avg_recency = cluster_data['recency'].mean()
    
    print(f"Cluster {cluster_id} ({size} customers):")
    print(f"  Average Age: {avg_age:.1f} years")
    print(f"  Average Income: ${avg_income:,.0f}")
    print(f"  Average Spending Score: {avg_spending:.1f}/100")
    print(f"  Average Purchase Frequency: {avg_frequency:.1f}")
    print(f"  Average Days Since Last Purchase: {avg_recency:.1f}")
    
    # Segment characterization
    if avg_spending >= 70 and avg_income >= 60000:
        segment_type = " High-Value Customers"
    elif avg_spending >= 50 and avg_frequency >= 25:
        segment_type = " Loyal Customers"
    elif avg_recency <= 30 and avg_frequency >= 20:
        segment_type = " Active Customers"
    elif avg_age <= 30 and avg_spending >= 60:
        segment_type = " Young Spenders"
    else:
        segment_type = " Low-Engagement Customers"
    
    print(f"  Segment Type: {segment_type}")
    print()

# PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Plot clusters
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(k_range, inertias, 'bo-')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.grid(True)

plt.subplot(1, 2, 2)
colors = plt.cm.Set1(np.linspace(0, 1, optimal_k))
for i in range(optimal_k):
    mask = clusters == i
    plt.scatter(X_pca[mask, 0], X_pca[mask, 1], 
               c=[colors[i]], label=f'Cluster {i}', alpha=0.6)

plt.scatter(pca.transform(scaler.transform(kmeans.cluster_centers_))[:, 0],
           pca.transform(scaler.transform(kmeans.cluster_centers_))[:, 1],
           c='red', marker='x', s=200, linewidths=3, label='Centroids')

plt.title('Customer Segments (PCA Visualization)')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Business recommendations
print(f" BUSINESS RECOMMENDATIONS:")
print("-" * 30)
print("1. Target High-Value Customers with premium products")
print("2. Create loyalty programs for Loyal Customers")
print("3. Send personalized offers to Active Customers")
print("4. Use social media marketing for Young Spenders")
print("5. Re-engagement campaigns for Low-Engagement Customers")
