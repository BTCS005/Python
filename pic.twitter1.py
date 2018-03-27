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
    "consumer_key"        : "JS7bbVBAo0j5ZDDMq5nJMVJV1",
    "consumer_secret"     : "7bTkI1c06sf8j2uDtRehCAkSQLuhUWACCLuG1FgKgrmImQODxM",
    "access_token"        : "967252071517970433-IsKl2YTxcjtUhE8LkFpXRXzcF6SNl3B",
    "access_token_secret" : "F3BAuVQfciu7EaSncW7T68WLXSIVROM78Y4G8lsVKg7xK" 
    }
  api = get_api(cfg)
  tweet = "Nice!!! one"
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing
if __name__ == "__main__":
  main()
  print("success")
