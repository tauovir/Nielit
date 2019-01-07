from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def qa1():
    print("khan")
    s1 = "The sky is blue"
    s2 = "The sun is bright"
    s3 = "The flowers are beautiful"
    s4 = "The school days are happy and funny"
    s5 = "I like to have good food"
    query = "The day is bright and beautiful"
    dataset = [s1,s2,s3]
    obj = TfidfVectorizer()
    obj.fit(dataset)
    #print(obj.vocabulary_)
    dataset1 = [query,s1,s2,s3,s4,s5]
    matrix = obj.fit_transform(dataset1)
    dict2 = obj.vocabulary
    print("Dict2")
    print(dict2)
    print("Cosine Similarity:",cosine_similarity(matrix[0:1],matrix))

#qa1()
def qa2():
    print("qa2")
    obj = TfidfVectorizer()
    file1 = open("cow.txt","r")
    para = file1.read()
    #print(para)
    query = "Cow is pet animal and it gives milk"
    dataset = [query,para]
    matrix = obj.fit_transform(dataset)
    dict2 = obj.vocabulary_
    print(dict2)
    print("**********Confusion matrix*******")
    print(cosine_similarity(matrix[0:1],matrix))

qa2()


