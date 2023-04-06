import random
import math
# Taking Inputs
lower = int(input("Enter Lower Bound:- "))
upper = int(input("Enter Upper Bound:- "))

# Generating random number between lower and upper bound
x = random.randint(lower, upper)
# Minimum number of guess calculation
min_guess = math.log(upper-lower+1, 2)
print("\n You have only ", round(min_guess),"chances to guess the integer!")

# Initializing the number of guesses.
count = 0

# for calculation of min number of guesses depends upon range

while count < min_guess:
    count += 1

    # taking guessing number as input
    guess = int(input("Guess the number:- "))

    # Condition Testing
    if x == guess:
        print("Congratulations you did it in ", count, "try")
        break
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print("You guessed too high")

    # If guessing is more than required guesses
    if count >= min_guess:
        print(f"The number is {x}")
        print("Better luck next time")