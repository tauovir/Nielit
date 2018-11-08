from textblob import TextBlob
text = "what is forest ? Forest is place of animal.where they can live peacfully. Many people says that this crucial for human"
textObj = TextBlob(text)

noun = textObj.noun_phrases
print noun
sen = textObj.sentences
word = textObj.words
#Print Sentences======
print "========sentence \n"
for s in sen:
    print s
#=====Print worsd in paragraph=======
print "========words \n"
for w in word:
    print w


#=====Print tags in paragraph=======
tag1 = textObj.tags 
print "========Tags \n"
print tag1

#=====Transalate paragraph=======
tran = textObj.translate(to="es") 
print "========Translate \n"
print tran



