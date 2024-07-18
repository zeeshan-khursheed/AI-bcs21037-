import random

random_guess = random.randint(1,9) #includes 9
#random_guess = random.randrange(1,9) #not includes 9

print("Guess a number between 1 and 9")

while True:
  guess = int(input("Enter a number to guess:   "))

  if guess == random_guess:
    print("Congratulations! You guessed the correct number.")
    break
  else:
    print("Wrong guess, Try again!")