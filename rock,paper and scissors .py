print("WELCOME TO ROC PAPER AND SCISSORS GAME\n")

import random
number=[1,2,3]
computer=random.choice(number)

"""
1 for rock
2 for paper
3 for scissors
"""
option=input("pick ( rock  or paper or scissors)\n")

youdict={"rock" : 1 , "paper" : 2 , "scissors" : 3}

compdict={1: "rock" , 2 :"paper" , 3 : "scissors"}

you=youdict[option]
compchoice=compdict[computer]

print("Your choice is:\t",option)
print("Computer choice is:\t",compchoice)

if(you == computer):
     print("Tie")
    
    
else:
     if (you == 1 and computer == 3):
       print("you win,computer lose")

     elif(you == 2 and computer == 1 ):
       print("you win,computer lose")

     elif(you == 3 and computer == 2):
       print("you win,computer lose")
      
     else:
       print("computer wins,you lose")




 

