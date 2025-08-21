import random

def random_num_guessing():
    random_number=random.randint(1,100)
    attempts=0

    print("WELCOME TO RANDOM NUMBER GUSSING GAME\n")

    while True:
        try:
            guess_number=int(input("ENTER A NUMBER YOU ARE GUESSING\n"))
            
            attempts+=1

            if guess_number < random_number:
                print("enter  higher number than this ( either less or  high)")

            elif guess_number > random_number:
                print("enter lower number than this( either less or high)")

            else:
                print(f"Congratulation you have guessed the number after {attempts} attempts")
                break
            
        except ValueError:
            print("input value is not acceptable")

random_num_guessing()







