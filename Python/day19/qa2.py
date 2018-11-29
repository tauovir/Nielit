import numpy as np
arr = np.array([
    [1,5,2,3],
    [5,6,3,1],
    [7,6,2,1]
    ])
price = np.array([[30000,35000,40000]])
print price
    
arr2 = np.dot(price, arr)
print arr2
