# use random module 
import random 
system = ["rock","scissor","paper"] 
items = ["rock","scissor","paper"]

user_choice = int(input("Choose :0 for rock,1 for scissor and 2 for paper : "))
if(user_choice >= 0 and  user_choice<0) :
    print("Please enter the valid number .")
else :
    print(f"User Choice is " + items[user_choice])
    system_choice = random.randint(0,2)
    print(f"System Choice is " +system[system_choice])

if(user_choice == 0 and system_choice == 0 ) :
    print("Draw Again !")
elif(user_choice ==0) & (system_choice == 1) :
    print(" Cherrs !,You Win !") 
elif(user_choice == 0 and system_choice ==2) :
    print("You loose") 
elif(user_choice == 1 and system_choice == 0) :
    print(" !You loose")
elif(user_choice == 1 and system_choice == 1) :
    print("Draw Again")
elif(user_choice == 1 and system_choice == 2) :
    print(" Cherrs !,You Win !")
elif(user_choice == 2 and system_choice == 0) :
    print("You Win")
elif(user_choice == 2 and system_choice == 1) :
    print("You loose")
elif(user_choice == 2 and system_choice == 2) :
    print("Draw Again !")