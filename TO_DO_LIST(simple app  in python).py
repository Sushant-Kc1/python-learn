print("WELCOME TO TO DO LIST APP\n")


from datetime import date
today=date.today()
print("todays date is:\t",today)

def to_do_list():
     
    Task=[] # list 
    
    while True:
        print("<---TO DO LIST MENU--->\n")
        print(" 1.Add Task\n")
        print(" 2.View Task\n")
        print(" 3.Delete Task\n")
        print(" 4.Quit\n") 

        option=input("choose a option:\t")

        if option == "1":
            task=input("enter the task you want to add:\t")
            Task.append(task)
            print("task added succesfully!")

        elif option == "2":
            if not Task:
                print("no task available\n")

            else:
                print("your task are:\n")
                for i, task in enumerate(Task, 1):
                 print(f"{i}.{task}")

        elif option == "3":
            if not Task:
                print("no task available\n")

            else:
                try:
                    task_no=int(input("enter the task no you want to remove"))
                    if 1<= task_no <=len(Task):
                        remove = Task.pop(task_no - 1)
                        print(f"{remove},removed succesfully!")

                    else:
                        print("enter valid task no:\n")

                except ValueError:
                    print("choose valid task no\n")
              
        elif option == "4":
            print("thanks for visiting our app!\n")
            break

        else:
            print("invalid choice!")
    


to_do_list()