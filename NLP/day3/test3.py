from os import listdir
from os.path import isfile, join
from textblob.classifiers import NaiveBayesClassifier

folderPath = "/home/ai20/Desktop/common/NLP/NLP3/Assignment 3/C0"
folderPath1 = "/home/ai20/Desktop/common/NLP/NLP3/Assignment 3/C"
#mypath = "/home/ai20/Desktop/common/NLP/NLP3/Assignment 3/C01"
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

trainData = []
catList = []
i = 1
category = "C0"
category1 = "C"

while i <=10:
    if i == 10:
        folderPath = folderPath1
        print folderPath
    mypath = folderPath + str(i) +"/"
   # print "===================folder path=============",mypath
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file1 in onlyfiles:
        fileName = mypath + str(file1)
        fd = open(fileName)
        if i == 10:
            category = category1
        fileData = fd.read()
        cat1 = category + str(i)
        tpl = fileData,cat1#make tuple
        trainData.append(tpl)
        catList.append(cat1)
        #print fileName
    i = i +1
#print "category list",catList

testStr = "External fixation for type III open tibial fractures.An analysis of 51 type III open tibial fractures treated by external skeletal fixation is presented.The fractures are subdivided according to the classification of Gustilo, Mendoza and Williams (1984) into types IIIa, IIIb and IIIc.The different prognoses of these fracture subtypes is examined.The use of the Hoffmann and Hughes external fixators in the management of type III open tibial fractures is presented and it is suggested that the prognosis is independent of the type of fixator used."
cl = NaiveBayesClassifier(trainData)
print "Classification",cl.classify(testStr)
print "==========end============="
