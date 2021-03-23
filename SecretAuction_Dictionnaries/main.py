from replit import clear
from art import logo


# function to interact with the user and get his name and his bid
def get_user_data():
    name = input("What is your name? : \n")
    bid = int(input("What is your bid in $ ?: "))
    return name, bid


def get_max(data):
    max_name = " "
    max_bid = 0
    for x in data.keys():
        if max_bid < data[x]:
            max_name = x
            max_bid = data[x]
    return max_name, max_bid


answer = "yes"
auction_data = {"nobody": 0}

print(logo)

while answer == "yes":
    temp_name, temp_bid = get_user_data()
    auction_data[temp_name] = temp_bid
    answer = input("Are they others bidders ? : ").lower()
    clear()


winner_name, bid = get_max(auction_data)
print(f"The winner of this auction is {winner_name} with a bid of {bid} $")
