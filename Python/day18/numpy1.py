import numpy as np

a1 = np.zeros((2,3),dtype = 'i4')
#print a1
#print a1.dtype

a2 = np.array((2, 3), dtype = 'f8')
#print a2.dtype
a3 = np.array((2,3),dtype = 'i8')
#print a1
#print a3.dtype

#=====Str
astr = np.zeros((3,3),dtype='S')
#print astr
#print astr.dtype

str2 = astr.copy()
#print str2

#===========Slicing===============
a11 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
    ])
print a11
# First row
#print a11[0]
#===Third row===
#print a11[2]
#====Select second column====
#print a11[:,[1]]
#=====First two element of second and third row===
#print a11[[1,2],:2]

#========Select Last element of each row
#print a11[:,[2]]

#=======create store num from 11-50=====
arr = np.array(range(11,51,1))
arr1 = arr.reshape(10,4)
#print arr1

def getDiagnal():
    arr2 = np.array(range(1,10,1))
    ar12 = arr2.reshape(3,3)
    return np.diag(ar12)
def occure(arr1,num):
    x = 0
    for i in range(arr1.shape[0]):
        for j in range(arr1.shape[1]):
            if arr1[i][j] == num:
                x = x+1
    print x    

print"diagnaol=", getDiagnal()
print arr1
occure(arr1,12)





