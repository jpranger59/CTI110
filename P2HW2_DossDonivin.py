 #Doss, Donivin

 #11/20/2025

 #P2HW2

 #grade lists

#psuedocode

module_grade_list = ["module1", "module2", "module3", "module4", "module5", "module6"]

module1 = input("Enter your grade for module 1: ")
module_grade_list[0] = float(module1)

module2 = input("Enter your grade for module 2: ")
module_grade_list[1] = float(module2)

module3 = input("Enter your grade for module 3: ")
module_grade_list[2] = float(module3)

module4 = input("Enter your grade for module 4: ")
module_grade_list[3] = float(module4)

module5 = input("Enter your grade for module 5: ")
module_grade_list[4] = float(module5)

module6 = input("Enter your grade for module 6: ")
module_grade_list[5] = float(module6)

print("------------results------------")
print(f"Lowest Grade:              {min(module_grade_list):.2f}")
print(f"Highest Grade:             {max(module_grade_list):.2f}")
print(f"sum of Grades:             {sum(module_grade_list):.2f}")
average = sum(module_grade_list) / len(module_grade_list)
print(f"Average Grade:             {average:.2f}")
print("-------------------------------")    