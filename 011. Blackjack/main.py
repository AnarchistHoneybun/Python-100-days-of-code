from art import logo
from replit import clear
import random
import time

random.seed(time.time())

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards=[]
computer_cards=[]

def card_deal():
  return random.choice(cards)

def calculate(stack):
  if sum(stack)==21 and len(stack)==2:
    return 0;

  if 11 in stack and sum(stack)>21:
    stack.remove(11)
    stack.append(1)
  return sum(stack)

def compare(player_score, computer_score):

  if player_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if player_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif player_score == 0:
    return "Win with a Blackjack 😎"
  elif player_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif player_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def gameplay():
  clear()
  print(logo)
  player_cards.clear()
  computer_cards.clear()
  for i in range(0,2):
    player_cards.append(card_deal())
    computer_cards.append(card_deal())
  game_run = True
  while game_run:
    player_score=calculate(player_cards)
    computer_score=calculate(computer_cards)
    print(f" Your cards : {player_cards}")
    print(f" Computer's first card: {computer_cards[0]}")
    if player_score==0 or computer_score==0 or player_score>21:
      game_run=False
    elif player_score<21:
      pl_draw=input("Do you want to draw another card? Type 'y' or 'n':")
      if pl_draw=='y':
        player_cards.append(card_deal())
        game_run=False
      else:
        game_run==False
    player_score=calculate(player_cards)
    while computer_score!=0 and computer_score<17:
      computer_cards.append(card_deal())
      computer_score=calculate(computer_cards)
    print(f"Your final hand: {player_cards}. Your final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}.")
  print(compare(player_score,computer_score))
  replay=input("Do you wish to play again? Type 'y' or 'n':")
  if replay=='n':
    clear()
    print("Thank you.")
  elif replay=='y':
    clear()
    gameplay()

start=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start=='n':
  clear()
  print("Good-Bye")
elif(start=='y'):
  gameplay()
  