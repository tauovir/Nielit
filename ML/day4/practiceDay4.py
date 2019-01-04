from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets.samples_generator  import make_moons
from sklearn.cluster import KMeans
import sklearn.metrics 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def qa1():
    print("khan")
    X,y = make_blobs(n_samples = 300,centers = 4,cluster_std = 0.60)
    print(y)
    #Plot Elbow Graph to find minimal number of Clusetr
    wcss = []
    for i in range(1,11):
        kmeans1 = KMeans(n_clusters = i, init = 'k-means++',max_iter = 300,n_init = 10,random_state = 0)
        kmeans1.fit(X)
        wcss.append(kmeans1.inertia_)
    '''
    plt.plot(range(1,11), wcss)
    plt.title("Elbow Method to find minimal No: Cluster")
    plt.xlabel("Number of cluster")
    plt.ylabel("Wcss")
    '''

    #Now Find clusetr
    kMeansModel = KMeans(n_clusters = 4)
    kMeansModel.fit(X)
    y_means = kMeansModel.predict(X)
    print("Predicted value")
    print(y_means)

        
    #Plot Graph
    plt.scatter(X[:,0],X[:,1],c=y_means, cmap = 'viridis')
    plt.show()

#qa1()

def qa2():
    print("khan")
    X,y =make_moons(n_samples = 300,noise = 0.05)
    print(y)
    #Plot Elbow Graph to find Minimal Optimal Cluisetr
    wcss = []
    for i in range(1,11):
        kmeans1 = KMeans(n_clusters = i, init = 'k-means++',max_iter = 300,n_init = 10,random_state = 0)
        kmeans1.fit(X)
        wcss.append(kmeans1.inertia_)
    """ 
    plt.plot(range(1,11), wcss)
    plt.title("Elbow Method to find minimal No: Cluster")
    plt.xlabel("Number of cluster")
    plt.ylabel("Wcss")
    """
   # plt.show()
    #Now Make Model
    kMeanModel = KMeans(n_clusters = 4)
    kMeanModel.fit(X)
    predictVal = kMeanModel.predict(X)
    print("****Predict Value*****")
    print(predictVal)
    fobj = plt.figure(figsize = (6,6), facecolor = (1,0,1))
    fobj.canvas.set_window_title('Plot Diagram')
    spobj1=fobj.add_subplot(221)
    spobj1.scatter(range(1,11), wcss)
    
    spobj2=fobj.add_subplot(223)
    spobj2.scatter(X[:,0],X[:,1], c=predictVal, cmap = 'viridis')
    plt.show()
    
    #Plot Graph for Kmeans Cluster
    #plt.scatter(X[:,0],X[:,1], c=predictVal, cmap = 'viridis')
    #plt.show()
    
    
    
qa2()
    

