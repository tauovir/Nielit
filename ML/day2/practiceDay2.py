import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
import matplotlib.pyplot as plt

def qa1():
    dataset = load_iris()
    print("*********Dataset*******")
    X = dataset.data
    y = dataset.target
    #Split Dataset to training set
    X_train, X_test, y_train,y_test = train_test_split(X, y, test_size = 0.3)
    #Now Load model and build models
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X_train,y_train)
    predictedVal = model.predict(X_test)
    print("Predicted value")
    print(predictedVal)
    cmm = confusion_matrix(y_test,predictedVal)
    print("Confusion matrix:")
    print(cmm)
    print("Accuracy:",accuracy_score(y_test,predictedVal))

def qa2():
    dataset = load_iris()
    print("*********Dataset*******")
    X = dataset.data
    y = dataset.target
    #Split Dataset to training set
    X_train, X_test, y_train,y_test = train_test_split(X, y, test_size = 0.3)
    #Now Load model and build models
    score = []
    for i in range(1,25):
        model = KNeighborsClassifier(n_neighbors=i)
        model.fit(X_train,y_train)
        predictedVal = model.predict(X_test)
        a1 = accuracy_score(y_test,predictedVal)
        score.append(a1)
    # Now Plot Accuracy Score
    plt.plot(range(1,25), score)
    plt.xlabel("Neighbors")
    plt.ylabel("Accuracy")
    plt.show()
#qa1()
#qa2()
def qa3():
    dataset = pd.read_csv("Immunotherapy.csv",delimiter=",", skiprows=1)
    print(dataset.head())
    datasetasMatrix = dataset.as_matrix()
    X = datasetasMatrix[:,0:7]
    y = datasetasMatrix[:,-1]
    #Split Dataset into Training set
    X_train, X_test, y_train,y_test = train_test_split(X, y, test_size = 0.3)
    #Now Bulid Model or Train Model
    model = KNeighborsClassifier(n_neighbors=15)
    model.fit(X_train,y_train)
    predictVal = model.predict(X_test)
    print("Predicted Value:")
    print(predictVal)
    cm = confusion_matrix(y_test,predictVal)
    print("Confusion MAtrix")
    print(cm)
    print("Accuracy score:",accuracy_score(y_test, predictVal))
    #================================================================
    # score = []
    # for i in range(1,25):
    #     model = KNeighborsClassifier(n_neighbors=i)
    #     model.fit(X_train,y_train)
    #     predictedVal = model.predict(X_test)
    #     a1 = accuracy_score(y_test,predictedVal)
    #     score.append(a1)
    # # Now Plot Accuracy Score
    # plt.plot(range(1,25), score)
    # plt.xlabel("Neighbors")
    # plt.ylabel("Accuracy")
    # plt.show()
qa3()