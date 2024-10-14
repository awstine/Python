number = int(input("enter limit "))

for i in range(1,number+1):
    if i % 2 == 0:
        # if i % 2 != 0: suppose it was prime or odd number
        print(i)