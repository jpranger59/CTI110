#Doss, Donivin

#11/23/2025

#P3HW1

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
mod_1 = input('Enter grade for Module 1: ')
mod_1 = float(mod_1)
mod_2 = input('Enter grade for Module 2: ')
mod_2 = float(mod_2)
mod_3 = input('Enter grade for Module 3: ')
mod_3 = float(mod_3)
mod_4 = input('Enter grade for Module 4: ')
mod_4 = float(mod_4)
mod_5 = input('Enter grade for Module 5: ')
mod_5 = float(mod_5)
mod_6 = input('Enter grade for Module 6: ')
mod_6 = float(mod_6)
# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades
print ('------- Results -------')
low = min(grades)
print(f"Lowest Grade:              {min(grades):.2f}")
high = max(grades)
print(f"Highest Grade:             {max(grades):.2f}")
sum_grades = sum(grades)
print(f"Sum of Grades:             {sum_grades:.2f}")
avg = sum_grades / len(grades)
print(f"Average Grade:             {avg:.2f}")
# determine letter grade for average
print('------------------------')
if avg >= 90:
    print('Your grade is: A')
elif avg > 80:
    print('Your grade is: B')
else:
    print('Your grade is: F') 
        
# TO DO: finish this