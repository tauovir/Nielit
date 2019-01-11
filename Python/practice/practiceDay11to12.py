import xml.sax
import xml.dom.minidom as dm

class XmlParser(xml.sax.ContentHandler):    # Inherit xml parser Handler
    def __init__(self):
        print("khan is her")
        self.category = ''
        self.title = ''
        self.author = ''
        self.year = ''
        self.price = ''
        self.curTag = ''
        self.str1 = ''
        self.fd = open('xmlFile','w')
    def startElement(self,tagName, attrs):
        '''
        This is inbuild of Xl parsing method,thihs is a starting point
        '''
        self.curTag = tagName
        if self.curTag == 'book':
            self.category = attrs['category']
        print("Starting tag:",tagName)
        print("*******************")
    def characters(self, content):
        '''
        It will excute in each iteration of Xml Data from starting Tag
        '''
        print("***********Tag Content********")
        print(content)
        if self.curTag == 'title':
            self.title = content
        if self.curTag == 'author':
            self.author = content
        if self.curTag == 'year':
            self.year = content
        if self.curTag == 'price':
            self.price = content
    def endElement(self,tag):
        '''
        This will execute when each tag going to close
        '''
        print("***********End Tag Content********")
        print(tag)
        #The book Think Python belongs to python category and is written by AB downy.
        #This book is published in the year 2015 with a price of 300. 
        if tag == 'title':
            self.str1 = self.str1 + "The book "+ self.title + " belongs to " + self.category
        if tag  == 'author':
            self.str1 = self.str1 + " and is written by " + self.author + "\n"
        if tag  == 'year':
            self.str1 = self.str1 + " This book is published in the year" + self.year
        if tag  == 'price':
            self.str1 = self.str1 + " with price " + self.price + "\n"
            self.fd.write(self.str1)
            self.fd.write("\n")
            self.str1 = ''
        if tag == 'itbooks':
            self.fd.close()
            print("End  file")

# poj = xml.sax.make_parser()
# s1 = XmlParser()
# poj.setContentHandler(s1)
# poj.parse('book.xml')

#========================DAy12==============================
def parseUsingDom():
    #The book Think Python belongs to python category and is written by AB downy.
    #This book is published in the year 2015 with a price of 300. 
    dtree = dm.parse("book.xml")
    rootElement = dtree.documentElement
    bookElement = dtree.getElementsByTagName('book')
    sr1 = ''
    fd = open("domXml",'w')
    for ele in bookElement:
        tns = ele.getElementsByTagName('title')
        #print(tns[0].childNodes[0].nodeValue)
        str1 = " The book " + tns[0].childNodes[0].nodeValue + "belongs to " + ele.getAttribute('category')
        authorEle = ele.getElementsByTagName('author')
        str1 = str1 + " and is written by " + authorEle[0].childNodes[0].nodeValue + "\n"
        yearEle = ele.getElementsByTagName('year')
        str1 = str1 + " This book is published in the year  " + yearEle[0].childNodes[0].nodeValue 
        priceEle = ele.getElementsByTagName('price')
        str1 = str1 + " with price of  " + priceEle[0].childNodes[0].nodeValue 
        fd.write(str1)
        fd.write("\n")
    fd.close()
        


parseUsingDom()      
