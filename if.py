
def fun1():
    i_want_to_eat = True
    i_want_to_drink= False

    if i_want_to_drink:
        print("drink water")
    elif i_want_to_eat:
        print("eat your food")
    else:
        print("Do nothing")

def fun2(num1,num2):
    num1 = input("Enter numbe 1: ")
    num2= input("Enter number 2: ")
    if num1 == num2:
        print("True")
    else:
        print("No")

def fun3():
    user1 = input("What is your name: ")
    user1_wallet = input("How muh cash you got: ")

    user2 = input("What is your name: ")
    user2_wallet = input("How muh cash you got: ")

    user3 = input("What is your name: ")
    user3_wallet = input("How muh cash you got: ")

    if float(user1_wallet)>float(user2_wallet) and float(user1_wallet)>float(user3_wallet):
        print(user1, "is the richest")
    elif float(user2_wallet)>float(user1_wallet) and float(user2_wallet)>float(user3_wallet):
        print(user2, "is the richest")
    elif float(user3_wallet)>float(user2_wallet) and float(user3_wallet)>float(user1_wallet):
        print(user3, "is the richest")

fun3()
