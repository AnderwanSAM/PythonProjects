from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create objects instances for this program

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# interact with the user
entry = " "  # a variable to contain the user choice

# start
entry = input(
    "What would you like? (espresso/latte/cappuccino/) Enter 'report' to see the resources status :")  # Prompt user by asking “What would you like?

while entry != "off":  # keep offering services
    if entry == "espresso":
        selected_drink = menu.find_drink("espresso")
        if coffee_maker.is_resource_sufficient(selected_drink): # check if there are enough resources to proceed
            print("(quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 ) ")
            # proceed with payment
            can_proceed = money_machine.make_payment(selected_drink.cost)
            if can_proceed:
                coffee_maker.make_coffee(selected_drink)

    elif entry == "latte":
        selected_drink = menu.find_drink("latte")
        if coffee_maker.is_resource_sufficient(selected_drink): # check if there are enough resources to proceed
            print("(quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 ) ")
            # proceed with payment
            can_proceed = money_machine.make_payment(selected_drink.cost)
            if can_proceed:
                coffee_maker.make_coffee(selected_drink)

    elif entry == "cappuccino":
        selected_drink = menu.find_drink("cappuccino")
        if coffee_maker.is_resource_sufficient(selected_drink):
            print("(quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 ) ")
            # proceed with payment
            can_proceed = money_machine.make_payment(selected_drink.cost)
            if can_proceed :
                coffee_maker.make_coffee(selected_drink)

    elif entry == "report":
        coffee_maker.report()  # show resources status
    else:
        print("Wrong command. Please Retry")
    # ask the next user
    entry = input("What would you like? (espresso/latte/cappuccino/):")  # Prompt user by asking “What would you like?
