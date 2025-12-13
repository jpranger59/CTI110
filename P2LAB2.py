# Doss, Donivin
# 11/18/2025
# P2LAB2
# Dictionary

vehicles = {"Camaro":18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}
keys = vehicles.keys()
print(keys)
vehicle= input("Enter a vehicle to see it's mpg: ")
mpg= vehicles[vehicle]
print(f"The {vehicle} gets {mpg} mpg.")
miles = float(input(f"How many miles will you drive the {vehicle}? "))
gallons = miles / mpg
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles}.")
