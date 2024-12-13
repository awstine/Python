class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


my_dog = Dog("Jack", 5)
print(my_dog.bark())
