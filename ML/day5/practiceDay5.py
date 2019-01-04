import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  accuracy_score,confusion_matrix,classification_report
def qa1():
    dataset = pd.read_csv("ex1.txt",delimiter = ',')
    dataMatrix = dataset.as_matrix()
    X = dataMatrix[:,[0]]
    X = X * 10000
    y  = dataMatrix[:,[1]]
    y = y * 10000
    print(dataset.head())
    print("*****Matrix*****")
    print(y)
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
    yPredictVal = model.predict(x1)
    yPredictVal = model.predict(X_test)
    print("*******Predicted Value******")
    print(yPredictVal.reshape(-1,1))
   # accuracy = accuracy_score(y_test,yPredictVal)
    #plt.scatter(y_test.ravel(), yPredictVal.ravel())
    #plt.show()
    print(confusion_matrix(y_test.reshape(-1,1),yPredictVal.reshape(-1,1)))
    print("*****END Program***")
    

qa1()
