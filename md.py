from gpiozero import MotionSensor
import os
import time
import tweepy
pir=MotionSensor(4)
time.sleep(4)
if pir.motion_detected:
    print("motion detected")
else:
    print("no detection of motion")
    
os.system("fswebcam -F 3 --fps 20 -r 1200*800 /home/pi/Desktop/csea2.jpg")
print("intruder alert")
a=0
while a<=2:
  img="/home/cs2017a106/im.jpg"
  cmd="fswebcam -r 1280x720 -S 3 --jpeg 100 "+img
  os.system(cmd)
  print("pic taken")
  time.sleep(5)
  a+=1

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "tpzDe0Xbi7RuWWuzuy36MIBpS",
    "consumer_secret"     : "69b0sEnjxh0Yr7tb5KQhbq1LLaQzhl0XbJHzAE8fBjJ7IQR2Q4",
    "access_token"        : "967253019149643777-VmmjiPHXCy7hReRarItHvDY2xwsD5Ix",
    "access_token_secret" : "UDeZNOAdFFwQZEZDp1JsygTvvi1uNGC0CHhnd3lgckSfn" 
    }
  api = get_api(cfg)
  tweet = "Nice!!!"
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing
if __name__ == "__main__":
  main()
  print("success")
