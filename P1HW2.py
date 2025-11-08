 # Doss, Donivin
 # 11/08/2025
 # P1HW2
 # travel expenses

budget=int(input("Enter your budget:"))
destination=input("Enter your destination:")
gas=int(input("How much do you think you'll spend on gas?"))
accomodations=int(input("How much will you spend on accomodations?"))
food=int(input("How much will you spend on food?"))
print()
print()
print("Travel Expenses")
print("location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodations:", accomodations)
print("Food:", food)
print()
print("Remaining Balance", budget-gas-accomodations-food)
