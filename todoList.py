def TODO():
 Todo = [["dis","time"]] #multiDimentional List
 def Show():
    for itr in range(len(Todo)):
        print(f"{itr+1}: {Todo[itr]}")

 while True:
     print("1.Add Todo \n2.remove\n3.Show \n4.Exit")
     choice = int(input("Enter by Number:~~> "))
     if(choice == 1):
        discription = input("//Add TODO::: Todo Task=> ")
        time = input("Time=> ")
        Todo.append([discription,time])
     elif(choice == 2):
        Show()
        removeTodo = int(input("//Remove TODO::: Remove by Number: "))
        removeTodo = removeTodo - 1

        if 0 <= removeTodo < len(Todo):
            del Todo[removeTodo]
            print(f"Updated ToDo: {Todo}")
        else:
            print("Invalid Todo.")
     elif(choice == 3):
        print("//Show TODO:::")
        Show()
     elif(choice == 4):
        print("//Exit TODO::: \nYou have Exited Program!")
        sure = input("//Exit TODO::: \nAre You Sure Yes(y) / No(N) : ")
        if(sure == "y" or sure == "Y"):
           break
        else:
           continue
        
        
if 1 == 1:
   TODO()
