from textblob import TextBlob
from textblob import Word
import random
import math

s1 = "The game of life is a game of everlasting learning"
s2 = "The unexamined life is not worth living"
s3 = " Never stop learning"

d1 = TextBlob(s1)
d2 = TextBlob(s2)
d3 = TextBlob(s3)
docList = [d1,d2,d3]

frequency = []
l2 = []
inverse = dict()
st = set()
docuntCount = 1
for doc in docList:
    dict2 = dict()
    t1 = []
    t2 = []
    wordList = doc.words
    for word in wordList:
        tf = doc.words.count(word)
        ntf = float(tf)/len(wordList)
        tpl = tf,ntf,len(wordList) # no: of occurance,normalized,total length
        dict2[word] = tpl
        inverse[word] = 1 + math.log(len(docList) / docuntCount) # inverse formula
    frequency.append(dict2)
    docuntCount = docuntCount + 1
        
print frequency
print "================"
print "Inverse of document:"
print inverse

