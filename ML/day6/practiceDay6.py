import  matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix
#Load Dataset of digits
data=load_digits()
X=data.images
y=data.target
ilabels=list(zip(X,y))
print(ilabels)
for index,(image,label) in enumerate(ilabels[:4]):
    plt.subplot(2,4,index+1)
	plt.axis('off')
	plt.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')
    plt.title(label)
plt.show()