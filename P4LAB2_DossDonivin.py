 #Doss, Donivin

 #12/05/2025

 #P4LAB2

 #integer multiplication table


def get_valid_number():
    number = int(input("Enter an integer: "))
    if number < 0:
        print("Error: This program cannot use negative numbers.")
        return None
    return number

def get_yes_no_response():
    again = input("Do you wish to run the program again? (yes/no): ").lower()
    if again == "yes":
        return True
    elif again == "no":
        return False
    else:
        print("Please enter 'yes' or 'no'.")
        return get_yes_no_response()

def print_multiplication_table(number):
    print("Multiplication table for " + str(number) + ":")
    for i in range(1, 13):
        print(str(number) + " x " + str(i) + " = " + str(number * i))

run_again = True
while run_again:
    number = get_valid_number()
    if number is not None:
        print_multiplication_table(number)
        run_again = get_yes_no_response()
    
print("Program ended.")