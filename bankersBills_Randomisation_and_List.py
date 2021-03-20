import random 

print("This is a simple game")
print("Friends are having dinner in an upscale restaurant.")
print("They are all bankers. When the party is over, they all take out their business cards and put them in a bowl.")
print("It's time for Bankers Roulette! The server will close his eyes and choose a card at random. The card owner will pay everyone's Bills")

for x in range(5): 
	print()

bankers_names = input ("Please enter the names of the bankers at the table separated by a comma ', ' ") 
print("Thank you ! The waiter is comming")
names = bankers_names.split(", ")

waiter_choice = random.randint(0,len(names))

print("The waiter has picked : " + names[waiter_choice] + "'s card")



