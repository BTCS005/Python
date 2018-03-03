import os
import time
i=1
j=1
while (i<5):
     os.system("fswebcam -F 3 --fps 20 -r 1200*800 /home/pi/an"+ str(j)+".jpg")
     time.sleep(4)
     print("pic taken")
     i=i+1
     j=j+1
    
    
