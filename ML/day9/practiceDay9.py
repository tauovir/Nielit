import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

def qa2():
    dataset = pd.read_csv("Immunotherapy.csv",delimiter = ',')
    print(dataset.head())
    X = dataset.iloc[:,0:7].values
    y = dataset.iloc[:,-1].values
    #Split Dataset into Traing set
    X_train, X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3,random_state = 0)
    print("X Train")
    #Now Normalize Data to get more accurate result
    stdScalar = MinMaxScaler()
    #stdScalar = StandardScaler()
    X_train = stdScalar.fit_transform(X_train)
    X_test = stdScalar.fit_transform(X_test)

    #Build Model
    knMOdel = KNeighborsClassifier(n_neighbors = 1)
    knMOdel.fit(X_train, y_train)
    predcitVal = knMOdel.predict(X_test)
    print("*****Predicted Value*****")
    print(predcitVal)
    print("Confusion Matrix:",confusion_matrix(y_test, predcitVal))
    print("Accuracy Score:",round(accuracy_score(y_test, predcitVal),2))
#qa2()

def qa3():
    dataset = pd.read_csv("banking.csv",delimiter = ',')
    print(dataset.head())
    X = dataset.iloc[:,[0,1,2,3,4,5,6,10,11,12,13,14,15,16,17,18,19]].values
    y = dataset.iloc[:,-1].values
    #Now Encode all categorical Data
    lblEncoder = LabelEncoder()
    X[:,1] = lblEncoder.fit_transform(X[:,1])
    X[:,2] = lblEncoder.fit_transform(X[:,2])
    X[:,3] = lblEncoder.fit_transform(X[:,3])
    X[:,4] = lblEncoder.fit_transform(X[:,4])
    X[:,5] = lblEncoder.fit_transform(X[:,5])
    X[:,6] = lblEncoder.fit_transform(X[:,6])
    X[:,11] = lblEncoder.fit_transform(X[:,11])
    hot = OneHotEncoder(categorical_features = [1,2,3,4,5,6,11])
    #X = hot.fit_transform(X).toarray()
    #Split Dataset ot Training Set
    X_train, X_test, y_train,y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
    #Normalize Data
    stdScalar = StandardScaler()
    X_train = stdScalar.fit_transform(X_train)
    X_test = stdScalar.fit_transform(X_test)
    #Build Model
    knMOdel = KNeighborsClassifier(n_neighbors = 1)
    knMOdel.fit(X_train, y_train)
    yPredictVal = knMOdel.predict(X_test)
    print("**********Predicted Value********")
    print(yPredictVal)
    print("Confusion Matrix:",confusion_matrix(y_test, yPredictVal))
    print("Accuracy Score:",round(accuracy_score(y_test, yPredictVal),2))

    

qa3()
