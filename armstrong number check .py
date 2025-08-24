print("Check wether a numbr is armstron or not\n")

number=int(input("Enter the number you want to check:\t"))
back=number
b=0
c=0
rem=0

while (number != 0):
    
    number=int(number/10)
    c=c+1
   
number=back

while(back != 0):
    b=back%10
    rem=rem+(b**c)
    back=int(back/10)
    
if(rem == number):
    print(number,"is armstrong number")

else:
    print(number,"is not armstrong number")
    
   
        
        
    
    