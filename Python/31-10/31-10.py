

def div_f(divident,divisor=2):
    q = divident / divisor
    r = divident % divisor
    return (q,r)

def div_f2(**param):
    print param
    print param['divident']
    divident = param['divident']
    divisor = param['divisor']
    q = divident / divisor
    r = divident % divisor
    return (q,r)
   


#x = input("enter divident")
#y = input("enter divisor=")
#result = div_f(x,y)
#print result


# Second Program

x = input("enter divident=")
y = input("enter divisor=")
result = div_f2(divident = x,divisor=y)
print result
