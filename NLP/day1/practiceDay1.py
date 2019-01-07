from textblob import TextBlob
import pandas as pd

def qa1():
    print("My First Tex Blob")
    text = "Diwali is one the most important festival of Hindus It is celebrated with great enthusiasm throughout the length and breadth of India. It is a festival of lights."
    print(text)
    blob = TextBlob(text)
    print("Tags")
    print(blob.tags)
   # nounPharase = blob.noun_phrases
    print(" Noune Pharase")
    #print(nounPharase)
    #Now Get Sentence
    print("***********Sentence********************")
    for sentence in blob.sentences:
        print(sentence.sentiment.polarity)
    #Now Get Word
    print("*******WordList******")
    print(blob.words)
    #Pluralize Words
    print("*****Pluralize Words***")
    print(blob.words.pluralize())
    noun = []
    for word,tag in blob.tags:
        if tag == 'NN' or tag == 'NNS':
            noun.append(word)
    print("******Noune********")
    print(noun)
            
    
def qa2():
    print("Start Question2")
    text = input("Enter word:")
    blobText = TextBlob(text)
    #Now Correct spelling of word
    print(blobText.correct())
    #Conver text to frech language
    print("Translate to french")
    print(blobText.translate(to = 'fr'))

def additionalQa():
    print("khan")
    data = open("file.txt",'r')
    text = data.read()
    blobText = TextBlob(text)
    sentenceList = []
    for sentence in blobText.sentences:
        sentenceList.append(sentence)
    print(sentenceList)
    print("sent ence length:",len(sentenceList))
    wordsList = []
    wordsList = blobText.words
    print("****Words List******")
    print(wordsList)
    #==========nth length of words and sentence=======
    nSentenceList = []
    nWordsList = []
    n = input("Enter Number")
    i = 0
    for sentence in blobText.sentences:
        if i < n:
            nSentenceList.append(sentence)
        i = i +1
    # Same for Words
    i = 0
    for word in blobText.words:
        if i <  n:
            nWordsList.append(word)
        i = i +1
    print("********Nth number of sentence and words***********")
    print(nSentenceList)
    print("sent ence length:",len(nSentenceList))
    print(nWordsList)
    
    

#qa1()
#qa2()
additionalQa()
