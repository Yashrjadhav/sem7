import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Load the dataset
df = pd.read_csv('sales_data.csv', encoding='latin-1')

# Display the first few rows
print(df.head())

# Drop unnecessary columns
df2 = df.drop(['PRODUCTLINE', 'ORDERDATE', 'STATUS', 'PRODUCTCODE', 'CUSTOMERNAME', 'PHONE',
                'ADDRESSLINE1', 'ADDRESSLINE2', 'CITY', 'STATE', 'POSTALCODE',
                'COUNTRY', 'TERRITORY', 'CONTACTLASTNAME', 'CONTACTFIRSTNAME',
                'DEALSIZE'], axis=1)

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df2)

# Determine the optimal number of clusters using the elbow method
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# Visualize the results using a line plot
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.show()

# Fit the KMeans model with the optimal number of clusters
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=0)
pred = kmeans.fit_predict(scaled_data)

# Display the predictions
print(pred)
