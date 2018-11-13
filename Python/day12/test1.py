"""
This Progarm is for how to parse Xml using Dom package
"""
import xml.dom.minidom as dm
dtree = dm.parse("book.xml")
rn = dtree.documentElement
#print rn
#print rn.nodeName
#print rn.nodeType
#print rn.nodeValue
bns = rn.getElementsByTagName('book')
st1 = ""
str2 = ""
fd = open("f2","w")
for bn in bns:
    str1 = ""
    str2 = ""
    #print "attr+",bn.getAttribute('category')
    tns = bn.getElementsByTagName('title')
    #print tns[0].childNodes[0].nodeValue
    str1 = "The book" + tns[0].childNodes[0].nodeValue
    str1 = str1 +" belongs to " + bn.getAttribute('category')
    ans = bn.getElementsByTagName('author')
    #print ans[0].childNodes[0].nodeValue
    str1 = str1 +" and is written by  " + ans[0].childNodes[0].nodeValue + "\n"
    
    yearNode = bn.getElementsByTagName('year')
    #print yearNode[0].childNodes[0].nodeValue
    str2 = "This Book is published in the year "+yearNode[0].childNodes[0].nodeValue
  
    priceNode = bn.getElementsByTagName('price')
   # print priceNode[0].childNodes[0].nodeValue
    str2 = str2 + " with price of " + priceNode[0].childNodes[0].nodeValue + "\n"
    print str1
    print str2
    fd.write(str1)
    fd.write(str2)
    fd.write("==============\n")
    print "========================"    
    
fd.close()

