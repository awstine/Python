decide = input("do you want to convert km or m")
if (decide == "km"):
    km = int(input("enter km "))
    ans = km * 18/5
    print(ans)
else:
    m = int(input("enter m"))
    ans1 = m* 5/18
    print(ans1)

