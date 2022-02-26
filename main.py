import random

### Generate random number
randomNumber = random.randint(1,10)

while True:
  try:
    userGuess = int(input("Please guess a number between 1 and 10: "))
    if(userGuess == randomNumber):
      break
  except:
    print("Please provide an integer")

print("Game over! Congrats you win! The number was: ", randomNumber)
