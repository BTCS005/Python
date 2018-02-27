# importing the module
import tweepy
 
# personal details
consumer_key ="tpzDe0Xbi7RuWWuzuy36MIBpS"
consumer_secret ="69b0sEnjxh0Yr7tb5KQhbq1LLaQzhl0XbJHzAE8fBjJ7IQR2Q4"
access_token ="967253019149643777-VmmjiPHXCy7hReRarItHvDY2xwsD5Ix"
access_token_secret ="UDeZNOAdFFwQZEZDp1JsygTvvi1uNGC0CHhnd3lgckSfn"

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hi Anulekha!")
