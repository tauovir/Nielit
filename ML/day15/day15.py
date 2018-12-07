import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import pandas as pd
from sklearn import preprocessing

class Day15:
    def __init__(self):
        self.iris_data = load_iris()
        self.X = self.iris_data.data
        self.y = self.iris_data.target.reshape(-1, 1)

    def deepPrediction(self):
        encoder = OneHotEncoder()
        encoder = OneHotEncoder(sparse=False)
        y = encoder.fit_transform(self.y)
        
        train_x, test_x, train_y, test_y = train_test_split(self.X,y, test_size=0.20)
        model = Sequential()
        print("************")
        model.add(Dense(10, input_shape=(4,), activation='relu', name='fc1'))
        model.add(Dense(10, activation='relu', name='fc2'))
        model.add(Dense(3, activation='softmax', name='output'))

        optimizer = Adam(lr=0.001)
        model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

        print('Neural Network Model Summary: ')
        print(model.summary())

        model.fit(train_x, train_y, verbose=2, batch_size=5, epochs=10)

        results = model.evaluate(test_x, test_y)

        print('Final test set loss: {:4f}'.format(results[0]))
        print('Final test set accuracy: {:4f}'.format(results[1]))

    def sonarCsv(self):
        data = pd.read_csv("sonar.csv")
        data =data.as_matrix()
        #print(data.shape)
        y = data[:,-1]
        #y = y.reshape(-1, 1)
        X = data[:,0:60]
        #print(y)
        le = preprocessing.LabelEncoder()
        le.fit(y)
        k = le.transform(y)
        #print(k)
        k = k.reshape(-1, 1)
        #print("=======")
        #print(k)
        train_x, test_x, train_y, test_y = train_test_split(X,k, test_size=0.20)
        model = Sequential()
        print("**************")
        print(train_x.shape)
        model.add(Dense(10, input_shape=(60,), activation='tanh', name='fc1'))
        model.add(Dense(12, activation='relu', name='fc2'))
        model.add(Dense(1, activation='softmax', name='output'))

        optimizer = Adam(lr=0.001)
        model.compile(optimizer, loss='binary_crossentropy', metrics=['accuracy'])

        print('Neural Network Model Summary: ')
        print(model.summary())

        model.fit(train_x, train_y, verbose=2, batch_size=5, epochs=40)

        results = model.evaluate(test_x, test_y)

        print('Final test set loss: {:4f}'.format(results[0]))
        print('Final test set accuracy: {:4f}'.format(results[1]))
        
        




s1 = Day15()
#s1.deepPrediction()
s1.sonarCsv()


