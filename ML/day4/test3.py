"""
Using Urban 3 data
"""
from sklearn.datasets.samples_generator  import make_moons
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
import sklearn.metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_csv("urban1.csv", )
d1 = data['x']
d2 = data['y']
X = np.array(zip(d1,d2))

kmeans = KMeans(n_clusters = 8)
kmeans.fit(X)
y_means = kmeans.predict(X)
print y_means
plt.scatter(X[ :,0], X[ :,1], s=50,c = y_means, cmap = 'viridis' )
plt.show()

