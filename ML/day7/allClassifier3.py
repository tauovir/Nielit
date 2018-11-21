
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score,KFold
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import preprocessing
data = pd.read_csv('bank.csv')
#print data
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
print k3
# data[:,[1,2,3,5,6,14]]
print "==========================="
data[:,1] = k1
data[:,2] = k2
data[:,3] = k3
data[:,5] = k4
data[:,6] = k5
data[:,14] = k6
#print data
#========Assign numeric value to gender===========

#data = data.as_matrix()
X = data[:,[1,2,3,5,6,14]]
y =  data[:,-1]
y = y.astype('int')  # convert y object to int
print X

kfold = KFold(n_splits = 10, random_state = 7)
tree1 = DecisionTreeClassifier()


#==== Check all Classifier cross_validation so we can rectify which is the best classifier

classifierList = [
        ('DT',DecisionTreeClassifier),
        ('KN',KNeighborsClassifier),
        ('NB',GaussianNB),
        ('LR',LogisticRegression)
        #('SV',SVC)
        ]
classifierNames = []
classifierValue = []
print classifierNames
#=====Store Classifier cross validation value to list
for name,classifier in classifierList:
       a = cross_val_score(classifier(), X, y, cv = kfold)
       classifierNames.append(name)
       classifierValue.append(a)
print classifierNames

#Plot figure
fig = plt.figure()
fig.suptitle("All Classifier Comparison with pimaindians data")
ax = fig.add_subplot(111)
plt.boxplot(classifierValue)
ax.set_xticklabels(classifierNames)
plt.show()

