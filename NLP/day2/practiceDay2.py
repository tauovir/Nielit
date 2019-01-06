from textblob import TextBlob
from textblob import Word

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
    print("Tags", blob.tags)

#plular()
partOfSpeach()