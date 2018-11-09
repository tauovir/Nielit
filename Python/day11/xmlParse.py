import xml.sax
class XmlParser(xml.sax.ContentHandler):
    def __init__(self):
        self.title = ''
        self.author = ''
        self.price = ''
        self.year = ''
        self.category = ''
        self.currTag = ''
        self.str1 = ''
        self.fd = open('f22','w')
        
    def startElement(self, tagName, attrs):
        self.currTag = tagName
        if self.currTag == 'book':
            print "============================="
            self.category = attrs['category']
            print "Category:" ,attrs['category']
    def characters(self, content):
        if self.currTag == 'title':
             self.title = content
        if self.currTag == 'author':
             self.author = content
        if self.currTag == 'year':
             self.year = content
        if self.currTag == 'price':
             self.price = content
    def endElement(self, tag):
        
        if tag == 'title':
           # print "Book Title:", self.title
            self.str1 = "The Book" + self.title + " belongs to " +  self.category
        if tag == 'author':
           # print "Author Name:", self.author
            self.str1 = self.str1 + " written by" + self.author + "\n"
            print self.str1
            self.fd.write(self.str1)
        if tag == 'year':
            #print "Publish Year",self.year
            self.str1 = "This Book is Published in the year " + self.year
        if tag == 'price':
            #print "Book Price:",self.price
            self.str1  = self.str1  + "with Price of " + self.price  + "\n"
            self.fd.write(self.str1)
            self.fd.write("\n")
        if tag == 'itbooks':    #When last tag going to end
            self.fd.close()
            print "Closed"
        
poj = xml.sax.make_parser()
s1 = XmlParser()
poj.setContentHandler(s1)
poj.parse('/home/ai20/Desktop/common/Python_Exercises/book.xml')

