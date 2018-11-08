from textblob import TextBlob
from textblob import Word

class Singular:
    def take(self):
        intext = input('enter noune=')
        blob = Word(intext)
        print "=====Pluralize========"
        print '%s => %s'%(intext, blob.pluralize())
        print "=====Singularize========"
        print '%s => %s'%(intext, blob.singularize())

class PartofSpeech:
    def takeInput(self):
        para = input('enter  paragraph')
        blob = TextBlob(para)
        print blob.tags
#s1 = Singular()
#s1.take()
p1 = PartofSpeech()
p1.takeInput()
