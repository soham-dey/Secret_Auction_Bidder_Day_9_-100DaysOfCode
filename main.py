from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction!")

auction_data={}
name=input("Enter your name: \n")
price=int(input("Enter your amount: $"))

def bidding():
  auction_data[name]=price
  

bidding()
want_to_continue=input("Is there any other bidder? Type 'yes' or 'no'.\n")
clear()
list_price=[]

if want_to_continue=='yes':
  while want_to_continue=='yes':
    name=input("Enter your name: \n")
    price=int(input("Enter your amount: $"))
    if want_to_continue=='yes':
      bidding()
      want_to_continue=input("Is there any other bidder? Type 'yes' or 'no'.\n")
      clear()
      for key in auction_data:
        list_price.append(auction_data[key])
elif want_to_continue=='no':
  print("Okay!")

winning_price=max(list_price)  
for name,price in auction_data.items():
    if price==winning_price:
      winner_name=name


print(f"The highest bidder is {winner_name} with a bidding price of ${winning_price}.")
  

