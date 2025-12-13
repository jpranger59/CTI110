# Doss Donivin

# 11/24/2025

# P3HW2

# Salary Calculation with Overtime

#Pseudocode (detail algorithm)

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's pay rate (e.g. 15.50): "))

OVERTIME_THRESHOLD = 40.0
OVERTIME_MULTIPLIER = 1.5

if hours > OVERTIME_THRESHOLD:
    overtime_hours = hours - OVERTIME_THRESHOLD
    regular_hours = OVERTIME_THRESHOLD
else:
    overtime_hours = 0.0
    regular_hours = hours

regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * pay_rate * OVERTIME_MULTIPLIER
gross_pay = regular_pay + overtime_pay

print("----------------------------")

print(f"Employee name:        {name}")
print(f"Hours worked:         {hours:.2f}")
print(f"Pay rate:             ${pay_rate:.2f}")
print(f"Overtime hours:       {overtime_hours:.2f}")
print(f"Overtime pay:         ${overtime_pay:.2f}")
print(f"Pay for regular hours:${regular_pay:.2f}")
print(f"Gross pay:            ${gross_pay:.2f}")