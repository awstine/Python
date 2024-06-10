

name1 = input("What is your name: ")
name2 = input("What is your name: ")
name3 = input("What is your name: ")

slices_in_pizza = input("How many slices are in the pizza")

price_of_pizza =  input("What is the price of pizza")

percentage_ate_by_person1 = input(name1+ " :What percentage of the pizza have you eaten")
percentage_ate_by_person2 = input(name2+ " :What percentage of the pizza have you eaten")
percentage_ate_by_person3 = input(name3+ " :What percentage of the pizza have you eaten")

number_of_slices_person1 = float(percentage_ate_by_person1)*float(price_of_pizza)
number_of_slices_person2 = float(percentage_ate_by_person2)*float(price_of_pizza)
number_of_slices_person3 = float(percentage_ate_by_person3)*float(price_of_pizza)

#percentage * pizza prize
price_paid_name1 = float(percentage_ate_by_person1)*float(price_of_pizza)
price_paid_name2 = float(percentage_ate_by_person2)*float(price_of_pizza)
price_paid_name3 = float(percentage_ate_by_person3)*float(price_of_pizza)

print(name1, " Has ate", number_of_slices_person1, " slices of pizza and paid ", price_paid_name1)
print(name2, " Has ate", number_of_slices_person2, " slices of pizza and paid ", price_paid_name2)
print(name3, " Has ate", number_of_slices_person3, " slices of pizza and paid ", price_paid_name3)