# Print out coins needed for number entered.


# body
def main():
    cents = getFloat()
    #print(cents)  # See Value before hand

    # Calculate respective coin amounts
    coins = 0

    quarters, cents = subtractQuarters(cents)
    coins += quarters

    dimes, cents = subtractDimes(cents)
    coins += dimes

    nickels, cents = subtractNickels(cents)
    coins += nickels

    pennies, cents = subtractPennies(cents)
    coins += pennies

    print("===========================================================")
    print(f"You will get: {round(quarters)} Quarters, {round(dimes)} Dimes, {round(nickels)} Nickels, {round(pennies)} Pennies")
    print(round(coins), "Total coins")
    print("===========================================================")


# get cents (float number)
def getFloat():
    while True:
        try:
            cents = float(input("Change: "))
            if cents > 0:  # Allowed range
                return round(cents * 100, 2)  # Round Amount
        except ValueError:
            print("Not a positive value")


# Calculate how many quarters you need to give customer
def subtractQuarters(cents):
    quarters = cents // 25
    remainingCents = cents % 25
    return quarters, remainingCents


# Calculate how many dimes you need to give customer
def subtractDimes(remainingCents):
    dimes = remainingCents // 10
    remainingCents = remainingCents % 10
    return dimes, remainingCents


# Calculate how many nickels you need to give customer
def subtractNickels(remainingCents):
    nickels = remainingCents // 5
    remainingCents = remainingCents % 5
    return nickels, remainingCents


# Calculate how many pennies you need to give customer
def subtractPennies(remainingCents):
    pennies = remainingCents // 1
    remainingCents = remainingCents % 1
    return pennies, remainingCents


main()
