import cipher
import art
print(art.logo)

application_running=1

while application_running==1:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n")
  shift = int(input("Type the shift number:\n"))
  cipher.caesar(text,shift,direction)
  rerun=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if rerun=='no':
    application_running=0
print("Good-Bye")
  

