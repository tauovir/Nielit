from textblob import TextBlob
import tweepy

def polarity():
    print("Polarituy")
    para = "Ganga is beautiful but she is rude"
    textBlob = TextBlob(para)
    print("sentiment polarity and subjectivity")
    print(textBlob.sentiment)

def checkPositivity():
    print("Polarituy")
    para = "Ganga is bad also she is rude"
    textBlob = TextBlob(para)
    #print("sentiment polarity and subjectivity")
    #print(textBlob.sentiment)
    if textBlob.sentiment.polarity >0:
        print("Sentencce is positive")
    elif textBlob.sentiment.polarity < 0:
        print("Sentence is Negative")
    else:
        print("Sentence is Neutral")
        

def tweetPolarity():
        consumerKey = 'DQFkwD2QRt0LuaD9ik64ETd1j'
        consumerSecret = 'xZeIc4o3lFYIvg2R7G79XVgZYVj317RHE9DwfWbh0GK6m0cNAq'
        accessToken = '841968176481083393-XqynBe7KCOrEVmZSAz7EspCdb70GjXM'
        accessTokenSecrete = 'f35iId8NtuX7Ol6ZoTfgRGEgniK7Cr2wABGQgAbpcTLS0'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken,accessTokenSecrete)
        api = tweepy.API(auth)
        publicTweet = api.home_timeline()
        print(publicTweet)
        for tweet in publicTweet:
            textBlob = TextBlob(tweet.text)
            if textBlob.sentiment.polarity >0:
                print("Sentencce is positive")
            elif textBlob.sentiment.polarity < 0:
                print("Sentence is Negative")
            else:
                print("Sentence is Neutral")
           
    

#polarity()
#checkPositivity()
tweetPolarity()
