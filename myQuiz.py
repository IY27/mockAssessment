questions = [None]
def menu():
    print("")

def question():
    None

def description():
    with open('description.txt','r')as f:
            description = f.read()
            print(description)
            print()

description()