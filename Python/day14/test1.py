import re
class Reg:
    def __init__(self):
        self.fd = open("emp.csv")
        self.listData = []
    def update(self):
        fileData = self.fd.readline()
        while self.fd.readline():
            data1 = self.fd.readline()
            self.listData.append(data1)
       # print self.listData
    def scientistData(self):
        fd1 = open('f1','w')
        print (self.listData)
        for str1 in self.listData:
            print str1
            if re.search('scientist',str1):
                print "===match"
                fd1.write(str1)
            
        fd1.close()
          

s1 = Reg()
s1.update()
s1.scientistData()
        


