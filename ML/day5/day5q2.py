"""
Suppose you are selling your house and you want to see what a good market
price would be. The ex2.txt contains a training set of housing prices in India.
The first column is the size of the house (in square feet). The second column
is the number of bedrooms and the third column is the price of the house.
a) Use scatter plots to visualize the data
b) Develop an ML model to predict the house price.

"""
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
import sklearn.metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("ex2.txt",delimiter = ',')
#print data
data = data.as_matrix()

X = data[:,[0,1]]
y = data[:,-1]
#print y
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
print X_test
lr =  LinearRegression()
lr.fit(X_train, y_train)

p = lr.predict(X_test)  #Predict profit and loss with test data
print p 
plt.scatter(y_test,p)
plt.show()

