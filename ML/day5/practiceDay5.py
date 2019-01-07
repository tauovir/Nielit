import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  mean_squared_error
def qa1():
    dataset = pd.read_csv("ex1.txt",delimiter = ',', skiprows=0)
    print(dataset.head())
    dataMatrix = dataset.as_matrix()
    X = dataset.iloc[:,[0]].values
    y = dataset.iloc[:,1].values
    print(dataset.head())
    print("*****Matrix*****")
    
    #plt.scatter(X, y)
    #plt.title("****Scatter Plot****")
    #plt.xlabel("city ")
    #plt.ylabel("profit")
    #plt.show()
    #Now Split Dataset into traing set
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3)
    #print("X_Train",y_train)
    #Now Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)
    x1 = np.array([[85172]])
    print(x1)
    #yPredictVal = model.predict(x1)
    yPredictVal = model.predict(X_test)
    print("Mean Swaure Error:",mean_squared_error(y_test, yPredictVal))
    print("*******Predicted Value******")
    plt.scatter(X_test,y_test)
    plt.plot(X_test,yPredictVal)
    plt.show()
    print("*****END Program***")
#qa1()
def qa2():
    dataset = pd.read_csv("ex2.txt",delimiter = ',', skiprows=1)
    print(dataset.head())
    X = dataset.iloc[:,[0,1]].values
    y = dataset.iloc[:,2].values
    #Split Data into Taring Set
    X_train, X_test, y_train,y_test = train_test_split(X, y,test_size = 0.2)
    print("Training Set")
    print(y_train)
    #Make Model Multi Linear Regression
    model = LinearRegression()
    model.fit(X_train, y_train)
    yPredVal = model.predict(X_test)
    tesVal = model.predict([[1236,3]])
    print("PredictVal:",tesVal)
    #Visualize Data
    plt.scatter(y_test,yPredVal)
    plt.show()

qa2()


