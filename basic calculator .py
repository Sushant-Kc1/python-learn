print(" This is calculator\n")


num1=float(input("Enter 1st number\n"))
num2=float(input("Enter 2nd number\n"))

operation=input("Enter the operation you want to perform( + , - , * , / ,% )\n")


while True:
    try:
     match operation:
      case '+':
        print(f"The Addition of {num1} and {num2} is ",num1+num2)

      case '-':
        print(f"The subtraction of {num1} and {num2} is ",num1-num2)

      case '*':
         print(f"The multiplication of {num1} and {num2} is ",num1*num2)
        
      case '/':
         print(f"The division of {num1} and {num2} is ",num1/num2)

      case '%':
         print(f"The remainder between  {num1} and {num2} is ",num1%num2)
        
      case _:
       print("invalid choice")

    except ValueError:
       print("invalid entry!\n")

