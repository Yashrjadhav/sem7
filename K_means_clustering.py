import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load the dataset
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# Display the first few rows
print(df.head())

# Display dataset information
df.info()

# Summary statistics
print(df.describe())

# Plot correlation heatmap
fig = plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, fmt='.2f')
plt.show()

# Select relevant columns
df = df[['PRICEEACH', 'MSRP']]
print(df.head())

# Check for missing values
print(df.isna().any())

# Summary statistics of selected columns
print(df.describe().T)

# Shape of the dataset
print(df.shape)

# Apply K-Means clustering
inertia = []
for i in range(1, 11):
    clusters = KMeans(n_clusters=i, init='k-means++', random_state=42)
    clusters.fit(df)
    inertia.append(clusters.inertia_)

# Plot the inertia to determine the optimal number of clusters (Elbow method)
plt.figure(figsize=(6, 6))
sns.lineplot(x=list(range(1, 11)), y=inertia)
plt.show()

# Perform K-Means clustering with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
y_kmeans = kmeans.fit_predict(df)

# Plot the clustered data
plt.figure(figsize=(8, 8))
sns.scatterplot(x=df['PRICEEACH'], y=df['MSRP'], hue=y_kmeans, palette="deep")
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', label='Centroids')
plt.legend()
plt.show()

# Display cluster centers
print(kmeans.cluster_centers_)
