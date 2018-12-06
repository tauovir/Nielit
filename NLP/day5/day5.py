from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Day5:
    '''
Have a list of minimum 5 sentences. Find how close they are to a query string using tfidfVectorizer and cosine_similarity.
    '''
    def similarity(self):
        s1 = "The sky is blue"
        s2 = "The sun is bright"
        s3 = "The flowers are beautifull"
        s4 = "The school days are haapy and funny"
        s5 = "I like to have good food"
        query = "The day is bright and beautifull"

        dataset = [s1,s2,s3]
        obj = TfidfVectorizer()
        #obj.fit(dataset)
        #dict1 = obj.vocabulary_
        #for key in dict1.keys():
            #print(key + " " + str (dict1[key]))

        dataset = [query, s1, s2, s3,s4,s5]
        matrix = obj.fit_transform(dataset)
        dict2 = obj.vocabulary_
        print(cosine_similarity(matrix[0:1],matrix))
    '''
    Modify the program to read strings from files.
    '''
    def fromFile(self):
        obj = TfidfVectorizer()
        file1 = open('cow.txt','r')
        str1 = file1.read()
        query = "t is of great importance for the people of Hindu religion."
        dataset = [query, str1]
        matrix = obj.fit_transform(dataset)
        dict2 = obj.vocabulary_
        print("=================Close========================")
        print(cosine_similarity(matrix[0:1],matrix))


s1 = Day5()
s1.similarity()
s1.fromFile()
