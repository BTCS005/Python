#R.P.S
import random
l=["Rock","Paper","Sessior"]
computer=random.choice(l)
print("Rock","Papaer","Sessior")
user=input("enter your choice")
if computer==user:
    print("tie")
elif computer=="Rock" and user=="Paper":
    print("user wins")
elif computer=="Paper" and user=="Rock":
    print("computer wins")
elif computer=="Paper" and user=="Sessior":
    print("user wins")
elif computer=="Sessior" and user=="paper":
    print("computer wins")
elif computer=="Sessior" and user=="Rock":
    print("user wins")
else:
    print("u lost")
        
              
