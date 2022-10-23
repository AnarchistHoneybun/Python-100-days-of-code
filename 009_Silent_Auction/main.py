from replit import clear
import art
print(art.logo)
print("Welome to the Secret Auction Program")
log_dict={}
auction_running="yes"
while auction_running=="yes":
  name=input("What is your name? ")
  bid=input("What is your bid? $")
  log_dict[name]=bid
  auction_running=input("Are there any other bidders? Type 'yes' or 'no'\n")
  clear()
highest_bid=0
highest_bidder=""
for name in log_dict:
  if int(log_dict[name])>highest_bid:
    highest_bid=int(log_dict[name])
    highest_bidder=name
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


