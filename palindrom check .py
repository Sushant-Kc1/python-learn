print("CHECK WETHER  NUMBER IS PALINDROM OR NOT\n")

# int is not taken because there occurs type error and if we convert 
#  reversed number to integer  the 0 dissapears because the leading zeros are not stored by variable
#  why because in mathematics 007 is considered as 7 an when we let a = 1200 in python its acceptable 
#  but when reversed it has to follow mathematical rule but we want it exact 0021 so we cant use int if int is used it 
#  gives output as 21
num1=int(input("Enter the number you want to check( only integer value) \n"))

reversenum=num1[::-1]

if(num1 == reversenum):
    print(f"The number u entered {num1} is palindrom\n")

else:
     print(f"The number u entered {num1} is not palindrom\n")

# slicing[start : stop : step]
#  by default start means from 0
#  stop means len(word)
#  step means from which portion of string the letter must be picked

# also if the steps is negative 
#   if start is 0 means start from end 
#  if stop is zero  means go until the beginning
#  step backward according to the no provided

# eg

 # word="person"
# print(word[::-2])
# start from  end
# reach till beginning
# 2 step from last a time
# p index 0  "skip"
# e     1  "e"
# r     2   "skip"
# s     3    "s"
# o     4    "skip"
# n     5     "n"
# output nse

#  slicing concept
# word="person"
# print(word[::2])
# start from 0 index
# stop at end
# 2 step a time
# p index 0  "p"
# e     1  "skip"
# r     2   "r"
# s     3    "skip"
# o     4    "o"
# n     5     "skip"
# output pro




