from textblob import TextBlob
import tweepy
class Day6:
    def __init__(self):
        self.para = "Ganga is bad girl but she is rude"
        self.txtBlob = TextBlob(self.para)
        self.consumerKey = 'DQFkwD2QRt0LuaD9ik64ETd1j'
        self.consumerSecret = 'xZeIc4o3lFYIvg2R7G79XVgZYVj317RHE9DwfWbh0GK6m0cNAq'
        self.accessToken = '841968176481083393-XqynBe7KCOrEVmZSAz7EspCdb70GjXM'
        self.accessTokenSecrete = 'f35iId8NtuX7Ol6ZoTfgRGEgniK7Cr2wABGQgAbpcTLS0'

    def getPolarity(self):
         print("========Sentiment========")
         print(self.txtBlob.sentiment)
        
    def checkPositivity(self):
       
        if self.txtBlob.sentiment.polarity > 0:
            print("Sentence is Positive")
        elif self.txtBlob.sentiment.polarity < 0:
             print("Sentence is Negative")
        else :
            print("Nutral")
    def tweetSentiment(self):
        
        auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
        auth.set_access_token(self.accessToken, self.accessTokenSecrete)
        api = tweepy.API(auth)
        public_tweets = api.home_timeline()
        #print(public_tweets)
        for tweet in public_tweets:
            print tweet.text
            
    def tweenPolarity(self):
        auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
        auth.set_access_token(self.accessToken, self.accessTokenSecrete)
        api = tweepy.API(auth)
        public_tweets = api.home_timeline()
        print(public_tweets)
        for tweet in public_tweets:
            if self.txtBlob.sentiment.polarity > 0:
                print("Sentence is Positive")
            elif self.txtBlob.sentiment.polarity < 0:
                 print("Sentence is Negative")
            else :
                print("Nutral")
                
    def tweenPolarityCount(self):
        auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
        auth.set_access_token(self.accessToken, self.accessTokenSecrete)
        api = tweepy.API(auth)
        public_tweets = api.user_timeline('narendramodi')
        pos = 0
        neg = 0
        nt = 0
        #print(public_tweets)
        for tweet in public_tweets:
            self.txtBlob = TextBlob(tweet.text)
            if self.txtBlob.sentiment.polarity > 0:
                print("Sentence is Positive")
                pos = pos + 1
            elif self.txtBlob.sentiment.polarity < 0:
                 print("Sentence is Negative")
                 neg = neg + 1
            else :
                print("Nutral")
                nt = nt + 1
        
        print("==========Count==============")
        print("Positive",pos)
        print("Negative",neg)
        print("Nutral",nt)
        

s1 = Day6()
#s1.getPolarity()
#s1.checkPositivity()
#s1.tweetSentiment()
#s1.tweenPolarity()
s1.tweenPolarityCount()

