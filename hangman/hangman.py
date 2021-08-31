
#imports

import random 


from hangman_art import stages
from hangman_art import logo


print(logo)

#list of words 
from hangman_words import word_list
chosen_word = random.choice(word_list) #random choice of a word 

#create a container to keep track of the game 
container = ["_"]

for x in range(len(chosen_word)-1):
	container.append("_")


#temporary code line to test the code 
print(f'Pssst, the solution is {chosen_word}.')

#game 

lives = 6 #user's lives
count = 0 #tries count
found_one = False # a variable to check wether or not a life is lost 

#invite the user to guess a letter 

while count != len(chosen_word) and  lives > 0 : 
	guess = input("Guess a letter: ").lower()
	
	for x in range(len(chosen_word)):
		if chosen_word[x] ==  guess :
			container[x] = guess
			count +=1 
			found_one = True	
	if found_one == True : 
		print(container)
		found_one = False
	else : 
		lives -=1
		print("wrong choice ")
		print(stages[lives])
		print(container)

if lives > 0 : 
	print("You win")
else :
	print("Game over")
