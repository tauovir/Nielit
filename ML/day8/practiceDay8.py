from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error,confusion_matrix
import matplotlib.pyplot as plt
dict1 = {}
def random1():
    dataset = load_boston()
    #print(type(dataset))
    X = dataset.data
    y = dataset.target
    #Split Dataset into training set
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3)
    print(y_test)
    #Build RandomForest Model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    yPredictVal = model.predict(X_test)
    #Mean Sqaure Error
    print("Random Forest Mean Square Error:",mean_squared_error(y_test,yPredictVal))
    dict1['RF'] = mean_squared_error(y_test,yPredictVal)
   # print("Confusion Matrix:",confusion_matrix(y_test, yPredictVal))
    plt.scatter(y_test,yPredictVal)
    plt.title("Random Forest Regressor")
    plt.show()
random1()

def svr1():
    dataset = load_boston()
    X = dataset.data
    y = dataset.target
    #Split Data into Training Set
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3)
    model = SVR()
    model.fit(X_train, y_train)
    yPredictVal = model.predict(X_test)
    print("SVR Square Error:",mean_squared_error(y_test,yPredictVal))
    dict1['SVR'] = mean_squared_error(y_test,yPredictVal)
    plt.scatter(y_test,yPredictVal)
    plt.title("Using SVR")
    plt.show()

svr1()

def ridge():
    dataset = load_boston()
    X = dataset.data
    y = dataset.target
    #Split Data into Training Set
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3)
    model = Ridge()
    model.fit(X_train, y_train)
    yPredictVal = model.predict(X_test)
    print("Ridge Square Error:",mean_squared_error(y_test,yPredictVal))
    dict1['Ridge'] = mean_squared_error(y_test,yPredictVal)
    plt.scatter(y_test,yPredictVal)
    plt.title("Using Ridge")
    plt.show()
ridge()
def lasso():
    dataset = load_boston()
    X = dataset.data
    y = dataset.target
    #Split Data into Training Set
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3)
    model = Lasso()
    model.fit(X_train, y_train)
    yPredictVal = model.predict(X_test)
    print("Lasso Square Error:",mean_squared_error(y_test,yPredictVal))
    dict1['Lasso'] = mean_squared_error(y_test,yPredictVal)
    print("***************Mean Square Error****************")
    print(dict1)
    plt.scatter(y_test,yPredictVal)
    plt.title("Using Lasso")
    plt.show()
lasso()