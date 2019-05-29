from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pyplot as plt

#Load Iris Data
irisData = load_iris()
X = irisData.data   #get Dataset
Y = irisData.target     #Get Target Data

#Split Data into training Set and test set
Xtrain,xTest,yTrain,Ytest = train_test_split(X, Y, test_size = 0.2,random_state = 4)
print(Xtrain.shape)

#Now We have to classify the category,so we are going to use KnnClassifier
knn = KNeighborsClassifier( n_neighbors = 10)
knn.fit(Xtrain, yTrain)
p = knn.predict(xTest)
#Now find Confusion matrix and accuracy rate
cnMatrix = confusion_matrix(Ytest, p)
accuracy = accuracy_score(Ytest, p)
report = classification_report(Ytest , p)

scores = list()
for i in range(1,25):
    knn1 =  KNeighborsClassifier(n_neighbors = i)
    knn1.fit(Xtrain,yTrain)
    p1 = knn1.predict(xTest)
    a1 = accuracy_score(Ytest,p1)
    scores.append(a1)
    
plt.plot(range(1,25),scores)
plt.xlabel("value of k for Knn")
plt.ylabel("accuracy")
plt.show()  # check value of k for highr accuracy
