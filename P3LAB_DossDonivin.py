 #Doss, Donivin

 #12/05/2025

 #P3LAB

 #Coin Calculator


amount = float(input("Enter amount: $"))
cents = int(amount * 100)

coins = [
    (100, "dollar", "dollars"),
    (25, "quarter", "quarters"),
    (10, "dime", "dimes"),
    (5, "nickel", "nickels"),
    (1, "penny", "pennies")
]

result = []

index = 0
while index < len(coins):
    coin_value, singular, plural = coins[index]
    count = cents // coin_value
    if count > 0:
        cents -= count * coin_value
        coin_name = singular if count == 1 else plural
        result.append(f"{count} {coin_name}")
    index += 1

print(", ".join(result))