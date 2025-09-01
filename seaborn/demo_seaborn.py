"""
🎨 Simple Seaborn Demo - Essential Plots
========================================
A clean, straightforward demo of key Seaborn plots using the tips dataset.
Uncomment sections to run different plot types.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load example dataset
tips = sns.load_dataset('tips')
print("📊 Tips Dataset Info:")
print(tips.head())
print(f"Shape: {tips.shape}")
print(f"Columns: {list(tips.columns)}")
print("-" * 50)

# ======================
# 📈 DISTRIBUTION PLOTS
# ======================

# Histograms and KDE
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.histplot(tips['total_bill'], kde=True, bins=20)
plt.title("📊 Total Bill Distribution")

plt.subplot(1, 3, 2)
sns.histplot(tips['tip'], kde=True, bins=15, color='orange')
plt.title("💰 Tip Distribution")

plt.subplot(1, 3, 3)
sns.kdeplot(data=tips, x='total_bill', hue='time', fill=True, alpha=0.6)
plt.title("🌊 KDE by Time")

plt.tight_layout()
plt.show()

# ======================
# 📦 BOX & VIOLIN PLOTS
# ======================

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title("📦 Box Plot by Day")
plt.xticks(rotation=45)

plt.subplot(1, 3, 2)
sns.violinplot(x='day', y='total_bill', data=tips)
plt.title("🎻 Violin Plot by Day")
plt.xticks(rotation=45)

plt.subplot(1, 3, 3)
sns.swarmplot(x='day', y='total_bill', data=tips, size=4)
plt.title("🐝 Swarm Plot by Day")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ======================
# 🎯 SCATTER & REGRESSION
# ======================

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.scatterplot(x='total_bill', y='tip', hue='time', data=tips)
plt.title("🎯 Scatter Plot (Bill vs Tip)")

plt.subplot(1, 3, 2)
sns.regplot(x='total_bill', y='tip', data=tips)
plt.title("📈 Regression Plot")

plt.subplot(1, 3, 3)
sns.scatterplot(x='total_bill', y='tip', hue='smoker', style='time', data=tips)
plt.title("🎨 Scatter with Hue & Style")

plt.tight_layout()
plt.show()

# ======================
# 📊 CATEGORICAL PLOTS
# ======================

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.barplot(x='day', y='total_bill', data=tips)
plt.title("📊 Bar Plot")
plt.xticks(rotation=45)

plt.subplot(1, 3, 2)
sns.countplot(x='day', hue='smoker', data=tips)
plt.title("📈 Count Plot")
plt.xticks(rotation=45)

plt.subplot(1, 3, 3)
sns.pointplot(x='day', y='total_bill', hue='time', data=tips)
plt.title("📍 Point Plot")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ======================
# 🔥 CORRELATION & HEATMAP
# ======================

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
# Correlation matrix
numeric_data = tips.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title("🔥 Correlation Heatmap")

plt.subplot(1, 2, 2)
# Pivot table heatmap
pivot_data = tips.pivot_table(values='total_bill', index='day', columns='time', aggfunc='mean')
sns.heatmap(pivot_data, annot=True, cmap='YlOrRd', fmt='.1f')
plt.title("🗂️ Average Bill by Day & Time")

plt.tight_layout()
plt.show()

# ======================
# 🔄 PAIRPLOT & JOINTPLOT
# ======================

# Pairplot
print("Creating Pairplot...")
g = sns.pairplot(tips, hue='smoker', diag_kind='kde', height=2.5)
g.fig.suptitle('🔄 Pairplot - All Relationships', y=1.02)
plt.show()

# Joint plot
print("Creating Joint Plot...")
g = sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg', height=6)
g.fig.suptitle('🎯 Joint Plot - Bill vs Tip', y=1.02)
plt.show()

# ======================
# 📋 FACETGRID (ADVANCED)
# ======================

print("Creating FacetGrid...")
# Multiple plots in a grid
g = sns.FacetGrid(tips, col='time', row='smoker', margin_titles=True, height=4)
g.map(sns.scatterplot, 'total_bill', 'tip', alpha=0.7)
g.add_legend()
g.fig.suptitle('📋 FacetGrid - Multiple Comparisons', y=1.02)
plt.show()

# ======================
# 🎨 STYLING EXAMPLES
# ======================

# Different styles showcase
styles = ['darkgrid', 'whitegrid', 'dark', 'white']
plt.figure(figsize=(16, 4))

for i, style in enumerate(styles):
    sns.set_style(style)
    plt.subplot(1, 4, i+1)
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='smoker')
    plt.title(f"🎨 Style: {style}")

plt.suptitle('🎨 Different Seaborn Styles', fontsize=16)
plt.tight_layout()
plt.show()

# Reset to default
sns.set_style('whitegrid')

# ======================
# 💡 QUICK TIPS
# ======================

# 💡 SEABORN QUICK REFERENCE
# 📊 Distribution: histplot, kdeplot, boxplot, violinplot
# 🎯 Relationships: scatterplot, regplot, jointplot, pairplot
# 📈 Categorical: barplot, countplot, pointplot, swarmplot
# 🔥 Advanced: heatmap, clustermap, FacetGrid
# 🎨 Styling: set_style(), set_palette(), set_context()
# 🚀 Key Parameters:
# - hue: Color by category
# - style: Marker style by category
# - size: Marker size by value
# - alpha: Transparency (0-1)
# - figsize: Figure size (width, height)
# ✅ Demo Complete! Try modifying the code above.
