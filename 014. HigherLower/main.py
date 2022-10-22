from game_data import data
from art import logo,vs
from replit import clear
import random
import time

random.seed(time.time())
score=0
A=''
B=''
def guess_check(A,B,guess):
  if A['follower_count']>=B['follower_count']:
    higher='A'
  else:
    higher='B'
  if guess==higher:
    return True
  else:
    return False



def game():
  print(logo)
  global score
  global A
  global B
  if score>0:
    print(f"You're right! Current score is {score}")
  if B == '' :
    A=random.choice(data)
  else:
    A=B
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
  print(vs)
  B=random.choice(data)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
  guess=input("Who has more followers? Type 'A' or 'B':").upper()
  if guess_check(A,B,guess):
    score+=1
    if A['follower_count']>=B['follower_count']:
      B=A
    clear()
    game()
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
  
game()