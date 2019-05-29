# -*- coding: utf-8 -*-
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler,MinMaxScaler

import pandas as pd

data = pd.read_csv('practice\Immunotherapy.csv')
dataset = data.iloc[:,0:7]
target = data.iloc[:,7]

# Split Data into traingin set and test set
xTrain,xTest,yTrain,yTest = train_test_split(dataset,target, test_size = 0.3, random_state = 4)

#Preprocessiing Data
stdScalar = MinMaxScaler()
#stdScalar = StandardScaler()
xTrain = stdScalar.fit_transform(xTrain)
xTest = stdScalar.fit_transform(xTest)

#Call Classifier
knn  = KNeighborsClassifier(n_neighbors = 25)
knn.fit(xTrain, yTrain)
predictValue = knn.predict(xTest)
cnMatrix = confusion_matrix(yTest,predictValue)
accuracy = accuracy_score(yTest, predictValue)

# find which n_)neighbors whoul be more suitable

scores = list()
for i in range(1,25):
    knn1 = KNeighborsClassifier(n_neighbors =i)
    knn1.fit(xTrain, yTrain)
    predictValue = knn1.predict(xTest)
    ac = accuracy_score(yTest, predictValue)
    scores.append(ac)
    
#NowPlot graph
plt.plot(range(1,25), scores)
plt.ylabel("yellow of knn neighbors")
plt.xlabel("Accuracy")
plt.show()
