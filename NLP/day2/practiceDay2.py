from textblob import TextBlob
from textblob import Word

def qa1():
    print("day2 Question")
    noune = input("Enter single nuone:")
    blobText = TextBlob(noune)
    pluralForm = blobText.words
    print(pluralForm[0].pluralize())
    print("****Singularize***")
    print(pluralForm[0].singularize())

def qa3():
    sentence = input("Enter a sentence:")
    blobText = TextBlob(sentence)
    partofSpeach = blobText.tags
    print(partofSpeach)

def qa4():
    fd = open(raw_input('enter file name:'),'r')
    paragrapgh = fd.read()
    blobText = TextBlob(paragrapgh)
    #Print Number of sentence;
    print("No: of Sentence:",len(blobText.sentences))
    #Print Number of words
    print("No: of words", len(blobText.words))
    # Now Fetch Main words
    nounList = set()
    partOfSpeach = blobText.tags
    for word,tag in blobText.tags:
        if tag == 'NN' or tag == 'NNS':
            nounList.add(word)
    print("Main words;",nounList)
    #Now get Summary of Paragraph
    print("Summary of content")
    sumaryOfContent(blobText)

def sumaryOfContent(blob):
    nounList = list()
    for word,tag in blob.tags:
        if tag == 'NN':
            nounList.append(word.lemmatize())
      
    wordFre = [nounList.count(w) for w in nounList]
    print 'pair',str(zip(nounList,wordFre))
    result = max(nounList, key=nounList.count)
    # print result
    print "Summary of Content:"
    print("Result",result)
    word = Word(result)
    print (word.pluralize())

def gamePlural():
    nounList = ['child','man','people','tree']
    plural = []
    print("None List:")
    for noun in nounList:
        word = Word(noun)
        plural.append(word.pluralize())
        print(noun)
    data = {'singular':nounList,'plural':plural}
    answer = raw_input("Enter plural form of noun with space:")
    answerList = answer.split(' ')
    #Check answer;
    for wrd in answerList:
        if wrd in data['plural']:
            print(wrd,"Right")
        else:
            print(wrd,"Wrong")
    #Correct answer is
    correctAnswer = zip(data['singular'],data['plural'])
    print("*******Correct answer is:")
    print(correctAnswer)

def gameSingular():
    plural = ['children','men','peoples','trees']
    singular = []
    print("None List:")
    for noun in plural:
        word = Word(noun)
        singular.append(word.singularize())
        print(noun)
    data = {'singular':singular,'plural':plural}
    answer = raw_input("Enter Singular form of noun with space:")
    answerList = answer.split(' ')
    #Check answer;
    for wrd in answerList:
        if wrd in data['singular']:
            print(wrd,"Right")
        else:
            print(wrd,"Wrong")
    #Correct answer is
    correctAnswer = zip(data['plural'],data['singular'])
    print("*******Correct answer is:")
    print(correctAnswer)
    
        
    
    
#qa1()
#qa3()
#qa4()
#gamePlural()
gameSingular()
=======
def plular():
    text = input("Enter Noune:")
    blob = Word(text)
    #======Pluralize
    print(blob.pluralize())
    #=====Singular======
    print("Singular",blob.singularize())
    
def partOfSpeach():
    para = input("Enter paragraph:")
    blob = TextBlob(para)
    print(blob.tags)

#plular()
partOfSpeach()

