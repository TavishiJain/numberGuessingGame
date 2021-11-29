import random

print("Number Guessing Game")
number= random.randint(1,9)
chances=0
print("Guess a number between 1-9:")
while chances < 5:

    guess=int(input("Enter Your Guess:"))
    if guess == number:
        print("Congratulations You Won")
        break
    elif guess < number: 
        print("Your Guess Is Too Low")

    else:
        print("Your Guess Is Too High")

    chances+=1

if not chances < 5:
    print("You Loose!!!The number is",number)