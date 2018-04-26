#Random_program
import random
r=random.randint(1,6)
print(r)
count=int(input("enter the values"))
count=count+r
if count==8:
    count=37
 if count==11:
     count=2
 if count==100:
     print("won")
else:
    print("continue playing")
