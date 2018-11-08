from textblob import TextBlob
from textblob import Word
import random

class Summary:
    def result(self):
        try:
            fd = open(raw_input('enter file:'),'r')
            para =  fd.read()
            self.showContent(para)
        except Exception as e:
            print "Exception occure=",str(e)
        else:
            #print fd.read()
            print ""
        finally:
            #fd.close()
             print ""
    def showContent(self,para):
        #print para
        blob = TextBlob(para)
        print 'number of sentence:',str(len(blob.sentences))
        print 'number of word:',str(len(blob.words))
        #self.getMainWords(blob)
        self.sumaryOfContent(blob)
        
    def getMainWords(self,blob):
        #print para
        nounList = set()
        wordList = blob.tags
        for word,tag in blob.tags:
           if (tag == 'NN') or (tag == 'NNS'):
               nounList.add(word)
        #print nounList
        print ','.join(nounList)
    def sumaryOfContent(self,blob):
        #print para
        nounList = list()
        for word,tag in blob.tags:
           if tag == 'NN':
               nounList.append(word.lemmatize())
        
        wordFre = [nounList.count(w) for w in nounList]
        print 'pair',str(zip(nounList,wordFre))
        result = max(nounList, key=nounList.count)
       # print result
        print "Summary of Content:"
        word = Word(result)
        print (word.pluralize())
        
s1 = Summary()
s1.result()
