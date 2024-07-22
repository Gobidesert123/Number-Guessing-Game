from Art_Number_gussing import logo
print(logo)
import random
print("Welcome to the number guessing Game!")
print("Im think of a number between 1 and 100")
computer_number = random.randint(1, 100)

# Setting the difficulty
level = int(input("Choose a difficulty. Type 0 for Easy mode or Type 1 for Hard mode: "))

def level_difficulty():
    if level == 0:
        lives = 10
        return lives
    else:
        lives = 5
        return lives
# The below line is so that we have a place to store the lives value
lives_left = level_difficulty()

# going over conditions
def conditions(computer_number, guess, lives_left):
    if guess > computer_number:
        print("Too High")
    elif guess < computer_number:
        print("Too Low")
    else:
        print(f"You got it! The answer was {guess}")

# we used this dummy variable so that we can have a condition that will always take us through for loop

guess = 0

while guess != computer_number and lives_left > 0:
    print(f'You have {lives_left} attempts remaining to guess the number.')
    guess = int(input("Make a guess: "))
    conditions(computer_number, guess, lives_left)
    lives_left -= 1
    if lives_left <= 0:
        print("You've run out of guesses, you lose")
        print(f"The actual value was: {computer_number}")









# Set the number of lives

# Record the number of lives after each go

# Check all the winning and losing conditions

#
