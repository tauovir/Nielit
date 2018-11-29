#!/usr/bin/env python
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
#from sklearn.svm import KNeighborsRegressor
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
import  matplotlib.pyplot as plt
import numpy
data = load_boston()

X = data.data
y = data.target
#Random Forest regressor

rf = RandomForestRegressor()
rf.fit(X, y)
p = rf.predict(X)
print mean_squared_error(y, p)
plt.scatter(y, p)
plt.show()


#USing SVR

rf = SVR()
rf.fit(X, y)
p = rf.predict(X)
print mean_squared_error(y, p)
plt.scatter(y, p)
plt.show()

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


