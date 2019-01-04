import numpy as np
import pandas as pd

#Import iris dataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def qa1():
    '''
    Day1 first question.
    '''
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
    scores = list()
    for i in range(1,25):
        knn1 = KNeighborsClassifier(n_neighbors = i)
        knn1.fit(X_train,y_train)
        p1 = knn1.predict(X_test)
        a1 = accuracy_score(y_test, p1)
        scores.append(a1)
    print(scores)
    plt.plot(range(1,25),scores)
    plt.xlabel("Y value")
    plt.ylabel("Accuarcy")
    plt.show()

#qa1()  # uncomment to Call this function

def qa2():
    #Load Data using pandas
    dataset = pd.read_csv("Immunotherapy.csv", delimiter = ",")
    dataset = dataset.as_matrix()
    X = dataset[:,0:7]
    y = dataset[:,-1]
    #Split Datset into traning set
    X_train, X_test,y_train,y_test = train_test_split(X, y, test_size = 0.2)
    print(X_train)
    #Train Model
    classifier = KNeighborsClassifier(n_neighbors = 1)
    classifier.fit(X_train,y_train)
    yPredict = classifier.predict(X_test)
    print("Predicted value")
 
    print("=Y_test value")
   
    print("====Confusion Matrix===========")
    cnM = confusion_matrix(y_test,yPredict)
    print(cnM)
    print("=====Accuracy======")
    print(accuracy_score(y_test,yPredict))

    #Now Plot Grapgh
    scores = []
    error = []
   #Calculating K value between 1 - 25
    for i in range(1,25):
        knn1 = KNeighborsClassifier(n_neighbors = i)
        knn1.fit(X_train,y_train)
        p1 = knn1.predict(X_test)
        a1 = accuracy_score(y_test, p1)
        scores.append(a1)
        error.append(np.mean(p1 != y_test))

    print("==========Error======================")
    print(error)
    print("Predict value")
    print(scores)
    #========Plot mean square Error of mis classification=======
    plt.figure(figsize=(12, 6))  
    plt.plot(range(1, 25), error, color='red', linestyle='dashed', marker='o',  
             markerfacecolor='blue', markersize=10)
    plt.title('Error Rate K Value')  
    plt.xlabel('K Value')  
    plt.ylabel('Mean Error')
    #===========Plot Diffrent classification=============
    plt.plot(range(1,25),scores, color="green",marker = "*")
    plt.xlabel("Y value")
    plt.ylabel("Accuarcy")
    
    plt.show()
    
qa2()

def qa3():
    # Assigning features and label variables
    # First Feature
    weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
    'Rainy','Sunny','Overcast','Overcast','Rainy']
    # Second Feature
    temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

    # Label or target varible
    play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
    #Create encoder
    labelEncoder = LabelEncoder()
    #Weather Encoder
    weather_encoded=labelEncoder.fit_transform(weather)
    #Conver temprature to number
    temp_encode = labelEncoder.fit_transform(temp)
    #Conver play into label
    label = labelEncoder.fit_transform(play)
    print(label)
    #Now Combine Both data
    feature = list(zip(weather_encoded,temp_encode))
    print(feature)
    #Now generate Model
    model = KNeighborsClassifier(n_neighbors = 3)
    model.fit(feature,label)
    #Now Predict value
    predictVal = model.predict([[0,2]]) #O:over cast, 2: mid
    print(predictVal)

#qa3()
