#snake and ladder
import random #it is a predefined function
tab=0 #tab is to show the position of the player                        
print("start the game")
print("your position is",tab)
while(tab<100):
    j=input("press enter to roll the dice")
    i=random.randint(1,6)
    tab=tab+i
    print("your position is",tab)
    if tab==8:
        tab=37
        print("ladder from 8 to 37")
    elif tab==11:
          tab=2
          print("oops! there is an snake, no go back to 2")
         
    elif tab==13:
          tab=24
          print("yippe,ladder from 13 to34")
    elif tab==38:
          tab=9
          print("oops! there is an snake, no go back to 9")
    elif tab==40:
          tab=68
          print("yippe,ladder from 40 to 68")
    elif tab==65:
          tab=46
          print("oops! there is an snake, no go back to 46")
    elif tab==52:
          tab=81
          print("yippe, ladder from 52 to 81")
    elif tab==89:
          tab=70
          print("oops! there is an snake, no go back to 70")
    elif tab==76:
          tab=97
          print("yippe, ladder from 76 to 97")
    elif tab==93:
          tab=64
          print("oops! there is an snake, no go back to 64")
    elif tab==100:
         print("you win")
         break
while(tab>100):
        print("try again")
        break    
