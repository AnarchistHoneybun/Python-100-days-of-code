import art
import random
import time

random.seed(time.time())

def game(answer,diff):
  while (diff>0):
    print(f"You have {diff} guesses left")
    diff-=1
    guess=int(input("Make your guess: "))
    if guess==answer:
      print("You win!")
      return 0;
    elif guess>answer:
      print("Too high")
      continue
    elif guess<answer:
      print("Too low")
      continue
  print("You have 0 guesses left. You lose")
    
  

answer=random.randint(1,100)
print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
diff=input("Choose a difficulty. Type 'easy' or 'hard': ")
if diff=="easy":
  diff=10
elif diff=="hard":
  diff=5

game(answer,diff)

