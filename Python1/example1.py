from math import *

person_name = input("Whats your name")
course_code = input("Whats your course code")


eng = input("What did u get in english")
kis = input("What did u get in kiswahili")
math = input("What did u get in math")

total_sum = float(eng)+ float(kis)+ float(math)
average = float(total_sum)/3


print("Name: "+person_name, "Course code: "+course_code, "Total :" ,total_sum, "Average :" ,average)