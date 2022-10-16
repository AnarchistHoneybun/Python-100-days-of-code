import random
import time
import hangman_art
import hangman_words
from replit import clear
random.seed(time.time())

print(hangman_art.logo)

def list_print(display):
  for i in range(0,len(display)):
    print(display[i], end="")
  print("\n")



chosen_word=random.choice(hangman_words.word_stack)
c_length=len(chosen_word)
print(chosen_word)
display=[]
for i in range(0,c_length):
  display+="_"
list_print(display) 

i=6

while i>0:
  guess=input("Guess a letter-> ").lower()
  clear()
  if guess in display:
    print(f"You have already guessed {guess}.")
  for j in range(0,c_length):
    if guess==chosen_word[j]:
      display[j]=guess
  
  if guess not in chosen_word:
    print(f"You guessed {guess}, which is not in the word. You lose a life.")
    i-=1
  list_print(display)
  print(hangman_art.stages[i])
  if "_" not in display:
    clear()
    break

if i==0:
  print("You Lost :(")
elif "_" not in display:
  print("YOU WIN")
  print(hangman_art.balloon)