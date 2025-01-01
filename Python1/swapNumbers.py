# Step 1: Get the number of students
num_students = int(input("Enter the number of students: "))

# Step 2: Initialize variables for highest and second-highest scores
highest_score = -1
second_highest_score = -1
highest_student = ""
second_highest_student = ""

# Step 3: Get the student's name and score, and compare to find the top two
for _ in range(num_students):
    name = input("Enter the student's name: ")
    score = int(input(f"Enter {name}'s score: "))

    # Step 4: Determine if the current score is the highest or second-highest
    if score > highest_score:
        second_highest_score = highest_score
        second_highest_student = highest_student
        highest_score = score
        highest_student = name
    elif score > second_highest_score:
        second_highest_score = score
        second_highest_student = name

# Step 5: Display the results
print(f"Student with the highest score: {highest_student} with score {highest_score}")
print(f"Student with the second-highest score: {second_highest_student} with score {second_highest_score}")
