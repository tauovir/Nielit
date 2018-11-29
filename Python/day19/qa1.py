import numpy as np
def store(num1, num2):
   list1 = range(num1, num2 +1,1)
   arr = np.array(range(num1, num2+1,1))
   print list1
   len1 = len(list1)
   print len1
   row = 0
   col = 0
   if len1%5 == 0:
       row = 5
       col = len1 / 5
   elif len1%4 == 0:
        row = 4
        col = len1 / 4
   elif len1%3 == 0:
        row = 3
        col = len1 / 3
   elif len1%2 == 0:
        row = 2
        col = len1 / 2
   else:
       row = (len1 - 1) / 2
       col = 2
       total = row * col
       remain = len1 - total
      
       print "babab=",remain
       if remain > 0:
           print "khjan"
           arr = np.append(arr,[0])
           row = row +1
           
   arr = arr.reshape(row,col)
   data = firstAndSecondArr(arr, 2)
   np.save("FileData",data)

def firstAndSecondArr(arr, num):
    #a1 = arr % num == 0
    a1 =  arr[arr % num == 0,np.newaxis]
    a2 =  arr[arr % num != 0,np.newaxis]
    return a1,a2
    
num1 = input("enter start number: ")
num2 = input("enter start number: ")

store(num1, num2)

