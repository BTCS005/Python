import os
import time
import tweepy
consumer_key='tpzDe0Xbi7RuWWuzuy36MIBpS'
consumer_secret='69b0sEnjxh0Yr7tb5KQhbq1LLaQzhl0XbJHzAE8fBjJ7IQR2Q4'
access_token='967253019149643777-VmmjiPHXCy7hReRarItHvDY2xwsD5Ix'
access_token_secret='UDeZNOAdFFwQZEZDp1JsygTvvi1uNGC0CHhnd3lgckSfn'
#these are the keys and access secret codes for sending the tweet
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
b=1
a=0
while a<=2:
    img="/home/cs2017a104/anitha/img"+str(b)+".jpg"
    cmd="fswebcam -r 1280x720 -S 3 --jpeg 100 "+img
    os.system(cmd)
    print("pic taken")
    #read image from location
    api.update_with_media(img, status="nice one")
    print("wait for 5 seconds for selfii!")
    time.sleep(5)
    a+=1
    b+=1
    print("success")
