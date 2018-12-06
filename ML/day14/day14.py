from sklearn.datasets import load_iris
from sklearn.datasets import load_boston
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error
from math import sqrt

class Day14:
    def __init__(self):
        iris = load_iris()
        self.X = iris.data
        self.y = iris.target
#Question 1
    def predictFunc(self):
        mlp = MLPClassifier(activation='tanh',hidden_layer_sizes=(15),solver='sgd',learning_rate_init=0.01,max_iter=500,verbose=True)
        #print(mlp.coefs_)
        mlp.fit(self.X, self.y)
        #print(mlp.predict([[3,5,4,2]]))
        p=mlp.predict(self.X)
        print("====Confusion matrix===")
        print(confusion_matrix(self.y,p))
    def mlRegressor(self):
         iris = load_boston()
         self.X = iris.data
         self.y = iris.target
         mlp = MLPRegressor( max_iter=100, activation='logistic',
                           random_state=1, learning_rate_init=0.01)
         mlp.fit(self.X, self.y)
         pred1 = mlp.predict(self.X)
         print("=============Score of prection============")
         #print(confusion_matrix(self.y,pred1))
         score = mlp.score(self.X, self.y)
         print(score)
         rms = sqrt(mean_squared_error(self.y, pred1))
         print("============Route mean square=========")
         print(rms)
        
        

s1 = Day14()
#s1.predictFunc()
s1.mlRegressor()


