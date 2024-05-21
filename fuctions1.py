#Always start with a def

def person_1(name):
    print(name+ "how can I i help you")

def person_2(food,desert,drink,name):
    name = input("What is your name: ")
    food = input("what food do u wanna eat ")
    drink = input("What drink do u want ")
    desert = input("What desert do you want ")

    print(name+ " took",food, "and",drink, "then finished with" +desert )

def person_3(name):
    print(name+ "Thank you")

person_1("Cashier")
person_2("food","desert","drink","name")
person_3("Cashier")
