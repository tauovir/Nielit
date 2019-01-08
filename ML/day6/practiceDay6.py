import  matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix
#Load Dataset of digits
data=load_digits()
X=data.images
y=data.target
print(y)
ilabels=list(zip(X,y))
