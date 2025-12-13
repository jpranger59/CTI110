 # Doss, Donivin
 # 11/08/2025
 # P1HW2
 # travel expenses
 # program Pseudocode (logic)

budget=float(input("Enter your budget:"))
print()
destination=input("Enter your destination:")
print()
gas=float(input("How much do you think you'll spend on gas?"))
print()
accomodations=float(input("How much will you spend on accomodations?"))
print()
food=float(input("How much will you spend on food?"))
print()
remaining = budget - gas - accomodations - food


print()
print("----------Formatted Travel Expenses----------")
print(f"Location:              {destination}")
print(f"Initial Budget:        ${budget:.2f}")
print(f"Fuel:                  ${gas:.2f}")
print(f"Accomodations:         ${accomodations:.2f}")
print(f"Food:                  ${food:.2f}")
print("---------------------------------------------")
print(f"Remaining Balance:     ${remaining:.2f}")
