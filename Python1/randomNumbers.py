import random


def randomNumbers(count, start,end):
    random_numbers = [random.randint(start,end)for _ in range(count)]
    return random_numbers

count = 20
start = 1
end = 20

random_numbers = randomNumbers(count, start, end)
print("rndom numbers: ",random_numbers)