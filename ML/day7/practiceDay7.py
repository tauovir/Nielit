import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score,KFold
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import matplotlib.pyplot as plt

def usingIris():
    dataset = load_iris()
    X = dataset.data
    y = dataset.target
    #Data is diveded into multiple chunks
    kfold = KFold(n_splits=10,random_state=7)
    #Make Dicstionary of model
    classifierList = [
                    ('DT',DecisionTreeClassifier),
                    ('KNN',KNeighborsClassifier),
                    ('NB',GaussianNB),
                    ('LR',LogisticRegression),
                    ('SVC',SVC)
                    ]   
    classifierName = []
    classifierValue = []
    for name,classifier in classifierList:
        a = cross_val_score(classifier(), X, y, cv = kfold)
        classifierName.append(name)
        classifierValue.append(a)
    print(classifierValue)
    #Now Plot Graphp
    fig = plt.figure()
    fig.suptitle("Comparison")
    ax = fig.add_subplot(111)
    plt.boxplot(classifierValue)
    ax.set_xticklabels(classifierName)
    plt.show()
#usingIris()

def usingPiamendence():
    data = pd.read_csv('pimaindians.csv')
    print(data.head())
    data = data.as_matrix()
    X = data[:,range(0,8)]
    y = data[:,-1]
    kfold = KFold(n_splits=10,random_state=7)
    #Make Tuple of list
    classifierList = [
                    ('DT',DecisionTreeClassifier),
                    ('KNN',KNeighborsClassifier),
                    ('NB',GaussianNB),
                    ('LR',LogisticRegression),
                    ('SVC',SVC)
    ]
    classifierName = []
    classifierValue = []
    for name,classifer in classifierList:
        a = cross_val_score(classifer(), X, y, cv=kfold)
        classifierValue.append(a)
        classifierName.append(name)
    fig = plt.figure()
    fig.suptitle("*****Comparision*****")
    ax = fig.add_subplot(111)
    plt.boxplot(classifierValue)
    ax.set_xticklabels(classifierName)
    plt.show()
#usingPiamendence()

def usingBankData():
    dataset = pd.read_csv("bank.csv",delimiter = ",")
    print(dataset.head())
    print("Using Bank Data")
    datasetAsMatrix = dataset.as_matrix()
    X = datasetAsMatrix[:,[0,1,2,3,4,5,6,10,11,12,13,14,15,16,17,18,19]]
    y = datasetAsMatrix[:,-1]
    print("*********Dataset**********")
    #Now Encode categorical data LabelEncoder,OneHotEncoder
    labelEncoder = LabelEncoder()
    X[:,1]  = labelEncoder.fit_transform(X[:,1])
    X[:,2]  = labelEncoder.fit_transform(X[:,2])
    X[:,3]  = labelEncoder.fit_transform(X[:,3])
    X[:,4]  = labelEncoder.fit_transform(X[:,4])
    X[:,5]  = labelEncoder.fit_transform(X[:,5])
    X[:,6]  = labelEncoder.fit_transform(X[:,6])
    X[:,11]  = labelEncoder.fit_transform(X[:,11])
    
    hot = OneHotEncoder(categorical_features=[1,2,3,4,5,6,11])
    X  = hot.fit_transform(X).toarray()
    print(X)
    #X[:,[1]]  = np.array([labelEncoder.fit_transform(X[:,[1]])]).reshape(X[:,[1]].size,1)
    # X[:,[2]]  = np.array([labelEncoder.fit_transform(X[:,[2]])]).reshape(X[:,[2]].size,1)
    # X[:,[3]]  = np.array([labelEncoder.fit_transform(X[:,[3]])]).reshape(X[:,[3]].size,1)
    # X[:,[4]]  = np.array([labelEncoder.fit_transform(X[:,[4]])]).reshape(X[:,[4]].size,1)
    # X[:,[5]]  = np.array([labelEncoder.fit_transform(X[:,[5]])]).reshape(X[:,[5]].size,1)
    # X[:,[6]]  = np.array([labelEncoder.fit_transform(X[:,[6]])]).reshape(X[:,[6]].size,1)
    # X[:,[11]]  = np.array([labelEncoder.fit_transform(X[:,[11]])]).reshape(X[:,[11]].size,1)
    # #Now Make list of Tuple to store classifier
    
    kfold = KFold(n_splits=10,random_state=7)
    #Make Dicstionary of model
    classifierList = [
                    ('DT',DecisionTreeClassifier),
                    ('KNN',KNeighborsClassifier),
                    ('NB',GaussianNB),
                    ('LR',LogisticRegression)
                    #('SVC',SVC)
                    ]   
    classifierName = []
    classifierValue = []
    #print(X)
    y = y.astype('int')
    for name,cl in classifierList:
        #kfold = KFold(n_splits = 10, random_state = 7)
        a = cross_val_score(cl(), X, y, cv = kfold)
        print("dd")
        classifierName.append(name)
        classifierValue.append(a)
    print("****************")
    fig = plt.figure()
    fig.suptitle("*****Comparision*****")
    ax = fig.add_subplot(111)
    plt.boxplot(classifierValue)
    ax.set_xticklabels(classifierName)
    plt.show()
    #print(X[0])
usingBankData()

