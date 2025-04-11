question_list = {
"A ball is dropped from 5m off the ground.\n What is the speed of the ball before it hits the ground?":["9.9ms^-1","8.2ms^-1","10ms^-1","2.5ms^-1"],
"What is the time it takes for the ball to hit the ground?":["1.01s","2s","10.9s","2mins"],
"A car goes from rest to a speed of 20ms^-1 in 10 seconds.\n What is the acceleration of the car?. ":["2ms^-2","1ms^-2","2.2ms^-2","10ms^-2"],
"Find the distance travelled by the car.":["100m","50m","1km","3m"],
"A car hits a wall with a speed of 50ms^-1 and penetrates 1m into the wall.\n What is the deceleration as the car enters the wall?":["1250ms^-2","100km/h","1000ms^1","100ms^-2"]
}

max_age = 18
min_age = 12

def user_info():
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    if age < min_age:
        print("You are too young to do this quiz")
        exit()
    elif age > max_age:
        print("You are too old to do this quiz")
        exit()
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
    for questions, answers in question_list.items():
        correct_answer = answers[0]
        sorted_answers = sorted(answers)
        print(f"{questions}")
        for labels, answers in enumerate(sorted_answers):
            label = labels+1
            print(f"  {label}) {answers}")
        while True:
            answer_label = int(input("Enter answer : "))
            while 1 <= answer_label <= 4:
                answer = sorted_answers[answer_label-1]
                if answer == correct_answer:
                    print("Correct!")
                    print()
                    break
                else:
                    print(f"Incorrect. The answer is {correct_answer}, not {answer}")
                    print()
                    break
            else:
                print("Please enter 1 - 4")
                continue
            break
    retry_menu()

def retry_menu():
    print("You have completed the quiz!")
    print("Would you like to retry?")
    print("1. Retry \n2. Exit")
    print()
    while True:
        option = int(input("Enter option : "))
        while option == 1 or option == 2:
            if option == 1:
                print()
                question()
            elif option == 2:
                print("You have exited the quiz")
                exit()
        else: 
                print("Please choose between 1 or 2")

def description():
    with open('description.txt','r')as f:
            description = f.read()
            print(description)
            print()

description()
user_info()
question()
