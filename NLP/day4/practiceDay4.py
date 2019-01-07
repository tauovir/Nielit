from textblob import TextBlob

# term Frequency 
def qa1():
    print("khan")
    str1 = "We are no longer the Knights who say Ni. We are now the Knights who say Ekki ekki ekki PTANG"
    blobText = TextBlob(str1)
    print(blobText.word_counts['are'])
    freqList = {}
    for word in str1.split(" "):
        freqList[word] = blobText.word_counts[word]
    print(freqList)

def qa1Test():
    s1 = "The game of life is a game of everlasting learning"
    s2 = "The unexamined life is not worth living game"
    s3 = " Never stop learning"
    blob1 = TextBlob(s1)
    blob2 = TextBlob(s2)
    blob3 = TextBlob(s3)
    listOfBlob = [s1,s2,s3]
    frequencyList = []
    freqDict = {}
    for doc in listOfBlob:
        blobText = TextBlob(doc)
        l1 = []
        for word in doc.split(" "):
            tuple1 = word, blobText.word_counts[word]
            l1 = [tuple1]
        frequencyList.append(l1)
   
    print(frequencyList)

#qa1()
qa1Test()
                  
                  
