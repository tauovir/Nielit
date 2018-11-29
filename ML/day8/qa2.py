#!/usr/bin/env python
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
#from sklearn.svm import KNeighborsRegressor
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
import  matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv("f1.csv", delimiter = '\s+')

data = data.as_matrix()
X = data[:,-1]  #Body wieght
y = data[:,[1]] #Brain weight
y = y.reshape(1,-1)
X = X.reshape(1,-1)
#Random Forest regressor
'''
rf = RandomForestRegressor()
rf.fit(X, y)
p = rf.predict(X)
print mean_squared_error(y, p)
plt.scatter(y, p)
plt.show()
'''

#USing SVR
'''
rf = SVR()
rf.fit(X, y)
p = rf.predict(X)
print mean_squared_error(y, p)
plt.scatter(y, p)
plt.show()
'''
#======Using Ridge =====

rf = Ridge()
rf.fit(X, y)
p = rf.predict(X)
print mean_squared_error(y, p)
plt.scatter(y, p)
plt.show()

#======Using Lasso =====
rf = Lasso()
rf.fit(X, y)
p = rf.predict(X)
print mean_squared_error(y, p)
plt.scatter(y, p)
plt.show()



