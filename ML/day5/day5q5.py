from sklearn.linear_model import LogisticRegression  
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import sklearn.metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing

F = pd.read_csv("mining.csv", delimiter = ",")
F.fillna(F.mean(), inplace=True)

Q = F.as_matrix()

knn = KNeighborsClassifier(n_neighbors=2)
le = preprocessing.LabelEncoder()
le.fit(Q[:,1])
k = le.transform(Q[:,1])

Q[:,1] = k

X = Q[:,[1,3,4,5,6,7,8,9,10]]
y = Q[:, 0]

y=y.astype('int')

knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X,y)

p = knn.predict([[12, 2807, 90.25, 0.346, 11.5, 20.23, 3.1, 1, 0.34]])

print(p)
