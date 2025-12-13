# Doss Donivin

# 12/03/2025

# P3HW2

# Multiple EmployeeSalary Calculation with Overtime



total_regular_pay = 0.0
total_overtime_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

name = input("Enter employee's name (or 'Done' to exit): ")

while name.lower() != "done":
    
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
    
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1
    
    print("----------------------------")
    print(f"Employee name:        {name}")
    print(f"Hours worked:         {hours:.2f}")
    print(f"Pay rate:             ${pay_rate:.2f}")
    print(f"Overtime hours:       {overtime_hours:.2f}")
    print(f"Overtime pay:         ${overtime_pay:.2f}")
    print(f"Pay for regular hours:${regular_pay:.2f}")
    print(f"Gross pay:            ${gross_pay:.2f}")
    print()
    name = input("Enter employee's name (or 'Done' to exit): ")

print("===========================")
print(f"Number of employees:    {employee_count}")
print(f"Total regular pay:    ${total_regular_pay:.2f}")
print(f"Total overtime pay:   ${total_overtime_pay:.2f}")
print(f"Total gross pay:      ${total_gross_pay:.2f}")
print("===========================")

#Pseudocode (detail algorithm)