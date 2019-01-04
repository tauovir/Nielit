import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import  matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def qa1():
    dataset = pd.read_csv("Advertising.csv")
    print(dataset.head())
    dataset = dataset.as_matrix()
    X = dataset[:,[1,2,3]]
    y = dataset[:,-1]
    #Split data into taining set
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3)
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    p = lr.predict(X_test)
    print(p)
    plt.scatter(y_test,p)
    plt.show()
    print(y_train)
    
    
#qa1()

def bankPrediction():
    dataset = pd.read_csv("bank.csv", delimiter = ",")
    #print(dataset.head())
    dataset = dataset.as_matrix()
    X = dataset[:,[0,1,2,3,4,5,6,10,11,12,13,14,15,16,17,18,19]]
    y = dataset[:,-1]
    #print(X)
    print(X[1])
    # Now Encode categorical data
    labelEnc = LabelEncoder()
    X[:,1] = labelEnc.fit_transform(X[:,1])
    X[:,2] = labelEnc.fit_transform(X[:,2])
    X[:,3] = labelEnc.fit_transform(X[:,3])
    X[:,4] = labelEnc.fit_transform(X[:,4])
    X[:,5] = labelEnc.fit_transform(X[:,5])
    X[:,6] = labelEnc.fit_transform(X[:,6])
    X[:,11] = labelEnc.fit_transform(X[:,11])
    print("***************")
   #Now split dataset into training set
    X_train,X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
    #Now Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)
    #Predict data
    preValued = model.predict(X_test)
    print("******testValue******")
    print(y_test)
    print("Predicted value")
    print(preValued)
    print("=========test===========")
    plt.scatter(y_test,preValued)
    plt.show()
   
    
    
    
    

bankPrediction()
