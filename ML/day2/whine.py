from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score,confusion_matrix
import pandas as pd
import  matplotlib.pyplot as plt

data = pd.read_csv('/home/ai20/Desktop/workStatus/ML/day2/winequality-white-1.csv')
print data 
