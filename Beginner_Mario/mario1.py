# Print a pyramid of bricks using a specified height

# get user desired height (between 1 - 8)
# Loop that prints out specified height


# Body
def main():
    n = getHeight()
    for i in range(n):
        print(" " * (n - 1 - i) + "#" * (i + 1))


# get height function
def getHeight():
    while True:
        try:
            n = int(input("Enter height: "))
            if n >= 1 and n <= 8:  # Allowed range
                return n  # Continue with code
        except ValueError:
            print("Not an integer")


main()
