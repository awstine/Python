num1 = input("enter first number")
num2 = input("enter second number")

if (float(num1) < 10000 and float(num2) < 1000):
    result = float(num1) * float(num2)
    print("answer  is ", result)
else:
    print("invalid")

