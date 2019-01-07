from sklearn.linear_model import LogisticRegression  
from sklearn.model_selection import train_test_split
import sklearn.metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("ex3.txt", delimiter=",")

data = data.as_matrix()
#print data
x1 = data[:,[0]]
y1 = data[:,[1]]
ad = data[:,[2]]
#===Plot score data==========

#plt.scatter(x1,y1,c=ad,alpha = 0.3)
#plt.show()

X = data[:,[0,1]]
y = data[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.8)
lgl = LogisticRegression()

lgl.fit(X_train,y_train)
p = lgl.predict(X_test)
plt.scatter(y_test,p)
plt.show()
