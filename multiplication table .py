number1=int(input("enter the number you want multiplication of:-"))

number2=int(input(f"enter upto which  multiplication of { number1} you want:-"))

print(f"The multiplication of {number1} upto {number2} is:-\n")
i=1
for i in range(number2 + 1):
    print(f"{number1}*{i}=",number1*i)