import tweepy
from textblob import TextBlob
consumer_key ='Your key'
consumer_secret ='your secret'

access_token ='1918907928-AVnqp2xvCpHpY9gmJAujRxNivyoKEz8mH46b8JD'
access_token_secret='65mS9HlaGUgYVjk5ctbT4JQnoVLNRb3pcbVxmqw1nOMky'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

public_tweets =api.search('Oneplus6')

for tweet in public_tweets:
	print(tweet.text)
	analysis =TextBlob(tweet.text)
	print(analysis.sentiment)