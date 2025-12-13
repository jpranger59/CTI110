import random

 #Doss, Donivin

 #12/12/2025

 #P5LAB

 #Coin Calculator UPDATED

round(random.uniform(0.01, 100.00), 2)

def disperse_change(change_amount: float) -> None:
    cents = int(round(change_amount * 100))
    d = cents // 100
    cents %= 100
    q = cents // 25
    cents %= 25
    di = cents // 10
    cents %= 10
    n = cents // 5
    p = cents % 5
    print(f"Change: {d} dollars, {q} quarters, {di} dimes, {n} nickels, {p} pennies")

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed:.2f}")
    payment = float(input("Enter amount to put into self-checkout: $"))
    while payment < total_owed:
        print("Insufficient amount. Please enter at least the total owed.")
        payment = float(input("Enter amount to put into self-checkout: $"))
    change = round(payment - total_owed, 2)
    disperse_change(change)

if __name__ == "__main__":
    main()
