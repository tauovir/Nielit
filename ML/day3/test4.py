from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("deathRateCsv.csv")
#print data
data = data.as_matrix()

X = data[:,:-1]
y = data[:,-1]
print X
#print y
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.4)
#print y_test
lr =  LinearRegression()
lr.fit(X_train,y_train)
p = lr.predict(X_test)
#print p 
plt.scatter(y_test,p)
#plt.show()
print (metrics.mean_absolute_error(y_test,p))
print (metrics.mean_squared_error(y_test,p))
print (np.sqrt(metrics.mean_squared_error(y_test,p)))


