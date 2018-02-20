#R.P.S
import random
l=["Rock","Paper","Scissor"]
computer=random.choice(l)
print("Rock","Papaer","Scissor")
user=input("enter your choice")
if computer==user:
    print("tie")
elif computer=="Rock" and user=="Paper":
    print("user wins")
elif computer=="Paper" and user=="Rock":
    print("computer wins")
elif computer=="Paper" and user=="Scissor":
    print("user wins")
elif computer=="Scissor" and user=="paper":
    print("computer wins")
elif computer=="Scissor" and user=="Rock":
    print("user wins")
else:
    print("u lost")
        
              
