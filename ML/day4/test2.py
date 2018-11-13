"""Prepare an ML model using KMeans algorithm to cluster some sample input
generated using make_moon function. Plot the clusters. Also plot the same
points by clustering it with Spectral Clustering Model.
"""
from sklearn.datasets.samples_generator  import make_moons
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
import sklearn.metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

X,y_true = make_moons(n_samples = 300,noise = 0.05)
kmeans = KMeans(n_clusters = 4)
kmeans.fit(X)
y_means = kmeans.predict(X)
plt.scatter(X[ :,0], X[ :,1], s=50,c = y_means, cmap = 'viridis' )
#plt.show()

model = SpectralClustering(2,affinity = 'nearest_neighbors')
labels = model.fit_predict(X)
plt.scatter(X[ :,0], X[ :,1], s=50,c = labels, cmap = 'viridis' )
plt.show()

