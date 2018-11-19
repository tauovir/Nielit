from sklearn.linear_model import LogisticRegression  
from sklearn.model_selection import train_test_split
import sklearn.metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing

data = pd.read_csv("titanic.csv",delimiter= ",")
#=====Preprocess data=========
data= data.fillna(0)
data['Age'] = data['Age'].fillna(round(np.mean(data['Age'])))
data['SibSp'] = data['SibSp'].fillna(round(np.mean(data['SibSp'])))
data['Parch'] = data['Parch'].fillna(round(np.mean(data['Parch'])))
data['Fare'] = data['Fare'].fillna(round(np.mean(data['Fare'])))

print ((data['Sex']))
genderList =  data['Sex'].tolist()
data = data.as_matrix() # Convert it into matrix
#======Label Data according to gender====

servivedList = data[:,[4]]
servivedList = servivedList.tolist()
le = preprocessing.LabelEncoder()
list1 = [x[0] for x in servivedList]
le.fit(list1)
#k=le.transform(["male", "female"])
k=le.transform(genderList)  #Convert gender value into numeric
#print type(k)
#========Assign numeric value to gender===========
data[:,4] = k  #Assign k value
#print data[0:,4]
#==========
X = data[0:,[4,5,6,7,9]]
y = data[0:,1]
y=y.astype('int')   # convert y object to int
#print X


#===========Train Data for Linear Regression==========

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
#print"X train===", X_train
#print"Ytrain===", y_train
#print(y_train.shape)
#print(X_train.shape)
lgl = LogisticRegression()
lgl.fit(X_train,y_train) 
p = lgl.predict(X_test)
print p 
plt.scatter(y_test,p)
plt.show()
