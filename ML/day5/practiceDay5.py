import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import  mean_squared_error,accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler,MinMaxScaler,LabelEncoder,OneHotEncoder
import math
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
    print("Mean Swaure Error:",math.sqrt(mean_squared_error(y_test, yPredVal)))
    #Visualize Data
    plt.scatter(y_test,yPredVal)
    plt.show()

#qa2()
def qa3():
    print("question 2")
    dataset = pd.read_csv("ex3.txt",delimiter = ',', skiprows=1)
    print(dataset.head())
    X = dataset.iloc[:,[0,1]].values
    y = dataset.iloc[:,-1].values
    #Split Dataset into Training set
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
    #We are doing normalization or standardization for increasing accuracy
    stdScalar = MinMaxScaler()
    #stdScalar = StandardScaler()
    X_train = stdScalar.fit_transform(X_train)
    X_test = stdScalar.fit_transform(X_test)
    #Now Build Model
    model = LogisticRegression()
    model.fit(X_train,y_train)
    predictVal = model.predict(X_test)
    print("********Predict Value*******")
    print(predictVal)
    print("Accuracy Score:",accuracy_score(y_test,predictVal))
    plt.scatter(y_test, predictVal,cmap=['red','green'])
    plt.xlabel("Actual Value")
    plt.ylabel("Predicted Value")   
    plt.show()

#qa3()

def qa4():
    dataset = pd.read_csv("titanic.csv",delimiter=",")
    print(dataset.head())
    dataset['Age'] = dataset['Age'].fillna(np.mean(dataset['Age'])) # Fill Blank Value
    X = dataset.iloc[:,[2,4,5,6,7,9]].values
    y = dataset.iloc[:,1].values
    print(X)
    #We Have One CAtegorical Data so we need to encoe it
    lblEncoder = LabelEncoder()
    X[:,1] = lblEncoder.fit_transform(X[:,1])
    #print("After Encoding")
    #print(X)
    #Split Data into Training Set
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3,random_state = 0)
    stdScalar = StandardScaler()
    X_train = stdScalar.fit_transform(X_train)
    X_test = stdScalar.fit_transform(X_test)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    predictVal = model.predict(X_test)
    print("Predicted Value:",predictVal)
    cmm = confusion_matrix(y_test, predictVal)
    print(cmm)
    print("Accuracy Score:",accuracy_score(y_test, predictVal))

#qa4()
def qa5():
    dataset = pd.read_csv('mining.csv', delimiter=",")
    print(dataset.head())
    X = dataset.iloc[:,3:11].values
    y = dataset.iloc[:,0]
    #Spllit Dataset into Traing set
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3)
    model = KNeighborsClassifier(n_neighbors=2)
    model.fit(X_train, y_train)
    predictVal = model.predict(X_test)
    print("*******Predicted value********")
    print(predictVal)
    cmm = confusion_matrix(y_test,predictVal)
    accuracy = accuracy_score(y_test,predictVal)
    print("Confusion Matrix")
    print(cmm)
    print("accuracy:",accuracy)




qa5()

