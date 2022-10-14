import random
import time

random.seed(time.time())

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("Welcome to RPS against cpu!")
player=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors:\n"))
if player==0:
  print(rock)
elif player==1:
  print(paper)
elif player==2:
  print(scissors)

print("cpu chose->")
cpu=random.randint(0,2)

if cpu==0:
  print(rock)
elif cpu==1:
  print(paper)
elif cpu==2:
  print(scissors)

if player==0 and cpu==0:
  print("IT'S A DRAW")
elif player==0 and cpu==1:
  print("you lose:(")
elif player==0 and cpu==2:
  print("!!YOU WIN!!")
elif player==1 and cpu==0:
  print("!!YOU WIN!!")
elif player==1 and cpu==1:
  print("IT'S A DRAW")
elif player==1 and cpu==2:
  print("you lose:(")
elif player==2 and cpu==0:
  print("you lose:(")
elif player==2 and cpu==1:
  print("!!YOU WIN!!")
elif player==2 and cpu==2:
  print("IT'S A DRAW")
