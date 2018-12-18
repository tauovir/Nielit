import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.cluster.vq import vq
from scipy.cluster.vq import kmeans

class Day21:
    #Initialize data
    def __init__(self):
        self.dset = np.array([2,4,10,12,3,20,30,11,25])
        self.dset = sp.cast['f'](self.dset)
    # find and plot K mean cluster
    def kmeanAlgo(self):
        centr1,dist1 = kmeans(self.dset,2)
        clust1,distan1 = vq(self.dset,centr1)
        cx =np.arange(1,self.dset.size+1)
        c1 = self.dset[clust1==0]
        c2 = self.dset[clust1==1]
        plt.scatter(cx[clust1==0],c1,color='g',label='clusterNumber1')
        plt.scatter(cx[clust1==1],c2,color='r',label='clusterNumber2')
        plt.legend(loc='best')
        plt.show()

s1 = Day21()
s1.kmeanAlgo()
