import math

def factorial(n):
    if n < 0:
        return "factorial not defined"
    return math.factorial(n)

n = int(input("enter a number"))
print("factorial is " ,factorial(n))