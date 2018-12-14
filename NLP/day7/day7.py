from textblob import TextBlob
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

import tweepy
class Day7:
    def __init__(self):
        self.documents = [
            "Browser helps us to search for information",
            "Game refersh our mind",
            "Chrome is Browser",
            "Foot ball is an interesting game",
            "Cricket is also an interesting game",
            "You can open many tabs in browser"
            ]
            
    def getVocabulary(self):
        list1 = []
        listMap = dict()
        obj = TfidfVectorizer()
        dataset = self.documents
        matrix = obj.fit_transform(dataset)
        dict2 = obj.vocabulary_
        for key in dict2.keys():
            print(key,dict2[key] )
   

                    
    def cosineSimilarity(self):
        obj = TfidfVectorizer()
        dataset = self.documents
        matrix = obj.fit_transform(dataset)
        dict2 = obj.vocabulary_
        print(cosine_similarity(matrix[0:1],matrix))
    
        

s1 = Day7()
s1.getVocabulary()
s1.cosineSimilarity()

