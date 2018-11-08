from textblob import TextBlob
from textblob import Word
def correctSpel(str1):
    w = Word(str1)
    chk = w.spellcheck()
    correct1 = w.correct()
    print correct1

word = "goood"    
correctSpel(word)
