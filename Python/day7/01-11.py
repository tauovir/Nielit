def table1() :
    x = input("enter any number=")
    str1 = 'x= %d'%(x)
   # s1='value of x is %d and value of y is %d'%(x,y)
    num = range(1,10)
    list = [x*i for i in num]
    readMod = open("readF")
    print readMod.read()
    writeMode = open("readF","w")
    for i in num :
        item = list[i - 1]
        str = '%d X %d = %d'%(x,i,item)
        print str
        writeMode.write(str)
        writeMode.write("\n")
    print readMod.read()

    
table1()
