questions = {""}

max_age = 18
min_age = 12

def user_info():
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    if age < min_age:
        print("You are too young to do this quiz")
    elif age > max_age:
         print("You are too old to do this quiz")
    else:
        option_menu()

def option_menu():
    print("Please choose an option")
    print("1. Play Quiz \n2. Exit")
    print()
    while True:
        option = int(input("Enter option : "))
        while option == 1 or option == 2:
            if option == 1:
                question()
            elif option == 2:
                print("You have exited the quiz")
                exit()
        else: 
                print("Please choose between 1 or 2")

def question():
    None

def description():
    with open('description.txt','r')as f:
            description = f.read()
            print(description)
            print()

description()
user_info()