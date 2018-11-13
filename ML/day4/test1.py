"""Prepare an ML model using KMeans algorithm to cluster some sample input
generated using make_blob function. Plot the clusters.
"""
from sklearn.datasets.samples_generator  import make_blobs
from sklearn.cluster import KMeans
import sklearn.metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


X,y_true = make_blobs(n_samples = 300, centers = 4,cluster_std = 0.60)
print y_true
kmeans = KMeans(n_clusters = 4)
kmeans.fit(X)
y_means = kmeans.predict(X)
plt.scatter(X[ :,0], X[ :,1], s=50,c = y_means, cmap = 'viridis' )
plt.show()




