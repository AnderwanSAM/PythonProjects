from art import logo
from random import randint

print(logo)


class Player:
    cards_list = []

    def __init__(self):
        self.cards_list = []
        self.cards_total = 0

    def get_total(self):
        total = 0
        for x in self.cards_list:
            total += x
        self.cards_total = total
        return total


class Dealer:
    cards_list = []
    is_below17 = True

    def __init__(self):
        self.cards_list = []
        self.is_below17 = True
        self.cards_total = 0

    def get_total(self):
        total = 0
        for x in self.cards_list:
            total += x
        self.cards_total = total
        return total

    def must_add_card(self):
        t = self.get_total()
        if t < 17:
            self.is_below17 = True
            return True
        else:
            return False


def get_a_card(deck):
    index = randint(0, len(deck) - 1)
    return deck[index]


def filter_ace(value, total):
    if value == 11:  # he got an ace
        if total + 11 > 21:  # if adding 11 will cause the total to surpass 21, then consider it as a 1
            return 1
        else:
            return 11
    else:
        return value


answer = "y"
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


while answer == "y":
    player_lost = False
    # create a player and a dealer
    player = Player()
    dealer = Dealer()
    # give them initials cards
    player.cards_list.append(get_a_card(cards))
    player.cards_list.append(filter_ace(get_a_card(cards), player.get_total()))
    dealer.cards_list.append(get_a_card(cards))
    dealer.cards_list.append(filter_ace(get_a_card(cards), dealer.get_total()))
    # inform the player about his cards and the dealer first card
    print(f"Your cards are : {player.cards_list}")
    print(f" The dealer first card is {dealer.cards_list[0]}")
    # ask if the player still wants to get a card
    answer_card = "yes"
    answer_card = input("Would you like to take another card : \n")
    while answer_card == "yes" and player_lost == False:
        card1 = get_a_card(cards)
        t = player.get_total()
        player.cards_list.append(filter_ace(card1, t))
        if player.get_total() > 21:
            player_lost == True
            print("You lost")

    # if the player hasn't lost check the dealer and decide the winner
    if player_lost:
        print("You lost")
        print(f"Your cards are : {player.cards_list}")
        print(f"Your total is {player.get_total()}")
    else:
        # The player doesn't want to take another card
        # check is the dealer must take another card
        if dealer.must_add_card():
            dealer.cards_list.append(get_a_card(cards))

        print()
        # show everyone cards
        print("End of the Game ! ")
        print(f"Your cards are : {player.cards_list}")
        print(f" The dealer's cards are : {dealer.cards_list}")
        player_total = player.get_total()
        dealer_total = dealer.get_total()
        if player_total == dealer_total:
            print("DRAW")
            print(f"Your cards are : {player.cards_list}")
            print(f" The dealer's cards are : {dealer.cards_list}")
        elif dealer_total > 21:
            print("You win")
            print(f"Your cards are : {player.cards_list}")
            print(f" The dealer's cards are : {dealer.cards_list}")
        elif dealer_total > player_total:
            print("You lose")
            print(f"Your cards are : {player.cards_list}")
            print(f" The dealer's cards are : {dealer.cards_list}")
        else:
            print("You win")
            print(f"Your cards are : {player.cards_list}")
            print(f" The dealer's cards are : {dealer.cards_list}")

    answer = input("Would you like to play a game of black jack ? 'y' or 'n' : ").lower()
