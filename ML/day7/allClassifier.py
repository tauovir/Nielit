from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score,KFold
from matplotlib import pyplot as plt
iris = load_iris()
X = iris.data
y = iris.target
kfold = KFold(n_splits = 10, random_state = 7)
tree1 = DecisionTreeClassifier()
a = cross_val_score(tree1, X, y, cv = kfold)
#print a

#==== Check all Classifier cross_validation so we can rectify which is the best classifier

classifierList = [
        ('DT',DecisionTreeClassifier),
        ('KN',KNeighborsClassifier),
        ('NB',GaussianNB),
        ('LR',LogisticRegression),
        ('SV',SVC)
        ]
classifierNames = []
classifierValue = []
#=====Store Classifier cross validation value to list
for name,classifier in classifierList:
       a = cross_val_score(classifier(), X, y, cv = kfold)
       classifierNames.append(name)
       classifierValue.append(a)
#Plot figure
fig = plt.figure()
fig.suptitle("Comparison")
ax = fig.add_subplot(111)
plt.boxplot(classifierValue)
ax.set_xticklabels(classifierNames)
plt.show()