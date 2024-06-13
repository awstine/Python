password = "pass123"
your_answer = ""

#No. of tries
number_of_tries = 0
number_max_of_tries = 5
max_try = "Not Reached"

while your_answer != password and max_try != "Reached":

    if number_of_tries < number_max_of_tries:
        your_answer = input("What is the password")
        number_of_tries = number_of_tries + 1
    else:
        max_try = "Reached"

if max_try == "Reached":
    print("Account Blocked")
else:
    print("Access Granted")
