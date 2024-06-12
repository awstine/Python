

def question():
    rule = input("you have to answer every question given ok?")
    if rule!="yes":
        return print("Try again")
    else:
        print("next question")
    quest1 = input("Are you hungry")
    if quest1 != "yes":
        return print("kweraa")

question()