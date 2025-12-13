 #Doss, Donivin

 #11/20/2025

 #P4HW1

 #grade lists



num_scores = int(input("How many scores would you like to enter? "))

student_scores = []

for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score {i + 1}: "))
            if 0 <= score <= 100:
                student_scores.append(score)
                break
            else:
                print("Invalid score! Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

print("------------results------------")
lowest_score = min(student_scores)
print(f"Lowest score: {lowest_score}")

modified_scores = student_scores.copy()
modified_scores.remove(lowest_score)
print(f"Modified list: {modified_scores}")

average_score = sum(modified_scores) / len(modified_scores)
print(f"Scores Average: {average_score:.2f}")

if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Grade: {letter_grade}")
print("-------------------------------")    

#psuedocode