print("Welcome to snake,water & gun game\n")

import random
number=[-1,0,1]
computer=random.choice(number)
print(computer)
"""
1 is for snake
-1 is for water
0 is for gun

"""
yourchoice=input("Enter your choice among (snake,water,gun):\t")
yourdict={"snake" : -1 , "water" : 0 , "gun" : 1}
compdict={-1: "snake" ,  0: "water", 1 : "gun" }
you=yourdict[yourchoice]

print(f"your choice:-\t{yourchoice}")
print(f"computer choice:-\t{compdict[computer]}\n")

if(yourdict == computer):
    print("Tie")
    
else:
    if (you == -1 and computer == 0 ):
      print("you win,computer lose")

    elif(you == 0 and computer == 1 ):
      print("you win,computer lose")

    elif(you == 1 and computer == -1):
      print("you win,computer lose")
      
    else:
      print("computer wins,you lose")



