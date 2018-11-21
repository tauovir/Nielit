import numpy as np
#1
a1 = np.array([1,2,3,4,5,8,9])
#print a1.dtype

l1 = [1,2,3]
l2 = [2,3,4]
l3 = [5,6,7]
#3
a11 = np.ones((2,3,4))
print a11
print a11.ndim
print a11.shape
print "size",a11.size

# array ans asarray
l1 = [10,20,30,40,50]
a2 = np.array(l1)
print a2
a21 = np.array(a2)
print a21
a22 = np.asarray(a2)

print a21 is a2
print a22 is a2
#==============
#=======I dentity metrix============
arr = np.eye(3)
print arr
