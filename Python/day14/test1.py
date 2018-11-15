import re
class Reg:
    def __init__(self):
        self.fd = open("emp.csv")
        self.listData = []
    def update(self):
        fileData = self.fd.readline()
        with  self.fd as f:
            contents = f.readlines()
            self.listData = [x.strip() for x in contents]
        #print self.listData
    def scientistData(self):
        fd1 = open('f1','w')
        for str1 in self.listData:
            if re.search('scientist',str1):
                print "===match"
                fd1.write(str1)
                fd1.write("\n")
            
        fd1.close()
    def initialLetter(self):
        fd1 = open('f2','w')
        pattern = '^M'
        for str1 in self.listData:
            if re.search(pattern,str1):
                print "===match"
                fd1.write(str1)
                fd1.write("\n")
            
        fd1.close()
    def initialLetterAnywhere(self):
        fd1 = open('f3','w')
        pattern = 'a'
        for str1 in self.listData:
            if re.search(pattern,str1):
                print "===match"
                fd1.write(str1)
                fd1.write("\n")
            
        fd1.close()
    def replaceStr(self):
       
        fd1 = open('f4','w')
        pattern = '\{|\}|\(|\)\-|\[|\]|-|_'
        for str1 in self.listData:
            list1 = str1.split(',')
            s2 = re.sub(pattern,'',list1[-1])
            list1[-1] = s2
            finalStr = ",".join(list1 )
            fd1.write(finalStr)
            fd1.write("\n")
            
        fd1.close()
    def greaterId(self):
       
        fd1 = open('f5','w')
        pattern = '\d{3}'
        for str1 in self.listData:
            searchData = re.search(pattern,str1)
            #print str1
            if searchData:
                val = int(searchData.group())
                print val
                if val > 200:
                    print "********matched*****"
                    fd1.write(str1)
                    fd1.write("\n")
        fd1.close() 

s1 = Reg()
s1.update()
#s1.scientistData()
#s1.initialLetter()
#s1.initialLetterAnywhere()
#s1.replaceStr()
s1.greaterId()



