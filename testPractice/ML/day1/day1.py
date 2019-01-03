import numpy as np
import pandas as pd

#Import iris dataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

#Load data
iris = load_iris()
#Load Target Data
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.2)

#Know Build Model
classifier = KNeighborsClassifier(n_neighbors = 1)
classifier.fit(X_train,y_train)
#Now Pridict value
p = classifier.predict(X_test)
print("===========Predicted value==============")
print(p)
print(y_test)
#Print Accuracy
accu = confusion_matrix(y_test,p)
print("=======Confusion Matrix========")
print(accu)
print("===========Accuracy================")
print(accuracy_score(y_test, p))
print("========Plot Grapgh===========")


