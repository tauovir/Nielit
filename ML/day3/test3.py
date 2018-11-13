from sklearn.linear_model import LogisticRegression  
from sklearn.model_selection import train_test_split
import sklearn.metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("pimaindians.csv")
data = data.as_matrix()

X = data[:,range(0,9)]
y = data[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
#print y_test
lgl = LogisticRegression()
lgl.fit(X_train,y_train)
p = lgl.predict(X_test)
print p 
plt.scatter(y_test,p)
plt.show()
