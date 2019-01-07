import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import  matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.metrics import  accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import LabelEncoder

def qa1():
    dataset = pd.read_csv("Advertising.csv")
    #print(dataset.head())
    dataset = dataset.as_matrix()
    X = dataset[:,[1,2,3]]
    #print(X[:,[0]].ravel().size)
    #print(X[:,[0]].ravel().size)
    y = dataset[:,-1]
    #Split data into taining set
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3)
    #Build Model
    lr = LinearRegression()
    lr.fit(X_test, y_test)
    p = lr.predict(X_test)
   #Get coefficient ans slop
    #m,b = slopIntercept(X_test[:,[0]].ravel(),y_test)
    #regressionLine = [(m*x) + b for x in X_test[:,[0]].ravel()]
    # print("Regression Line:",regressionLine)
    # plt.scatter(X_test[:,[0]].ravel(),y_test,color="red")
    # plt.xlabel("Independent Variable")
    # plt.ylabel("Dependent VAriable")
    # plt.plot(X_test[:,[0]].ravel(),regressionLine,c = 'green')
    plt.scatter(y_test,p)
    plt.show()
    
    plt.show()
    print(X_test[:,[0]].ravel())
        
def slopIntercept(xVal, yVal):
    '''
    A linear regression line has the equation Y = mx+c, where m is the coefficient of independent variable and c is the intercept.
    The mathematical formula to calculate slope (m) is:
    (mean(x) * mean(y) – mean(x*y)) / ( mean (x)^2 – mean( x^2))
    The formula to calculate intercept (c) is:
    mean(y) – mean(x) * m
    '''
    #x = np.array(xVal)
    #y = np.array(yVal)
    x = xVal
    y = yVal
    #print(np.mean(x))
    m = (np.mean(x)*np.mean(y) - np.mean(x*y)) / (np.mean(x)* np.mean(x) - np.mean(x*x))
    m = round(m,2)
    print("coefficent:",m)
    b = (np.mean(y) - np.mean(x)) * m
    return m,b


qa1()
    #Question 2
def loanPredict():
    dataset = pd.read_csv('loan.csv')
    print("********Dataset*********")
    print(dataset.head())
    print("********Dataset*********")
    matrix = dataset.as_matrix()
    #print(matrix)
    X = matrix[:,[0,1]]
    y = matrix[:,-2]
    #There is not much data so , no need to split it into training set
    model = LinearRegression()
    model.fit(X, y)
    predictVal = model.predict(X)
    print("Predictedd value")
    print(predictVal)

    #Plot Graph
    fobj = plt.figure(figsize = (6,6), facecolor = (1,0,1))
    fobj.canvas.set_window_title('Plot Diagram')
    #Train X and Y vaue graph
    spobj1=fobj.add_subplot(221)
    spobj1.scatter(X[:,[0]],y)
    #Xtest and predict value graph
    spobj2=fobj.add_subplot(223)
    spobj2.scatter(X[:,[0]],y)
    spobj2.plot(X[:,[0]],predictVal)
    plt.show()
 
#loanPredict()
def qa3():
    dataset = pd.read_csv('pimaindians.csv')
    print(dataset.head())
    matrix = dataset.as_matrix()
    X = matrix[:,range(0,8)]
    y = matrix[:,-1]
    #Now Break it into training set
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3)
    #Now Build Model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    predictVal = model.predict(X_test)
    print("Predicted value")
    print(predictVal)
    plt.scatter(y_test,predictVal)
    plt.show()
    
#qa3()
def qa5():
    dataset = pd.read_csv("city.csv")
    print(dataset.head())
    matrix = dataset.as_matrix()
    X = matrix[:,range(1,5)]
    y = matrix[:,-2]
    #Split data into taining set
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3)
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    p = lr.predict(X_test)
    print("Predicted value")
    print(p)
    plt.scatter(y_test,p)
    plt.show()
    print (metrics.mean_absolute_error(y_test,p))
    print (metrics.mean_squared_error(y_test,p))
    print (np.sqrt(metrics.mean_squared_error(y_test,p)))

#qa5()
def qa6():
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
    
    #Knn Classifier
    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train,y_train)
    p = knn.predict(X_test)
    print("============")
    print(p)
    print("Confusion matrix")
    cm = confusion_matrix(y_test,p)
    print(cm)
    accuracy = accuracy_score(y_test,p)
    print("****Accuracy****")
    print(accuracy)
    #=====F1 score====
    score = cross_val_score(knn, X,y, cv=10)
    print("Score")
    print(score)
    print("******Report******")
    print(classification_report(y_test, p))
    
qa6()
     

