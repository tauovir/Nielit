from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score,confusion_matrix
import pandas as pd
import  matplotlib.pyplot as plt
from sklearn import preprocessing
data = pd.read_csv('Immunotherapy.csv',delimiter = ",")
ndraData = data.as_matrix()
X = ndraData[:,0:7]
y =ndraData[:,7]


#min_max_scaler = preprocessing.MinMaxScaler()
#X_train_minmax = min_max_scaler.fit_transform(X_train)

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

#===Print Confusion matrix
print confusion_matrix(y_test,p)
#print accuracy
print accuracy_score(y_test,p)


'''
#=====Plot graph=======
scores = list()
for i in range(1,25):
    knn1 =  KNeighborsClassifier(n_neighbors = i)
    knn1.fit(X_train,y_train)
    p1 = knn1.predict(X_test)
    a1 = accuracy_score(y_test,p1)
    scores.append(a1)
    
#print scores
plt.plot(range(1,25),scores)
plt.xlabel("Y value")
plt.ylabel("accuracy")
plt.show()
'''
