
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score,KFold
from sklearn.metrics import  accuracy_score,confusion_matrix
from matplotlib import pyplot as plt
from sklearn import preprocessing
import pandas as pd
from sklearn import preprocessing
data = pd.read_csv('banking.csv')
data = data.as_matrix()

#======Label Data according to gender====

servivedList = data[:,[1,2,3,5,6,14]]
servivedList = servivedList.tolist()
#print servivedList
le = preprocessing.LabelEncoder()
job = []
marital = []
edu = []
house = []
loan = []
potcamp = []

for x in servivedList:
   job.append(x[0])
   marital.append(x[1])
   edu.append(x[2])
   house.append(x[3])
   loan.append(x[4])
   potcamp.append(x[5])

le.fit(job)
k1=le.transform(job)

le.fit(marital)
k2=le.transform(marital)

le.fit(edu)
k3=le.transform(edu)

le.fit(house)
k4=le.transform(house)

le.fit(loan)
k5=le.transform(loan)

le.fit(potcamp)  
k6=le.transform(potcamp)

# data[:,[1,2,3,5,6,14]]
print "==========================="
data[:,1] = k1
data[:,2] = k2
data[:,3] = k3
data[:,5] = k4
data[:,6] = k5
data[:,14] = k6
#========Assign numeric value to gender===========

#data = data.as_matrix()
X = data[:,[1,2,3,5,6,14]]
y =  data[:,-1]
y = y.astype('int')  # convert y object to int

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)

#======MinMax Scalar============
#min_max_scaler = preprocessing.MinMaxScaler()
#X_train_minmax = min_max_scaler.fit_transform(X_train)
#X_test_minmax = min_max_scaler.fit_transform(X_test)
#====== Standard Scalar============
X_train_minmax = preprocessing.StandardScaler().fit(X_train).transform(X_train)
X_test_minmax = preprocessing.StandardScaler().fit(X_test).transform(X_test)


#Knn Classifier
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train_minmax,y_train)
p = knn.predict(X_test_minmax)
print p
#===Print Confusion matrix
print confusion_matrix(y_test,p)
#print accuracy
print accuracy_score(y_test,p)

