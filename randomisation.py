import random 



print("Hello ! This is also a simple  Program to test randomisation in python ")

# I - Head or tails game 

print("First Game : heads or tails ") 
choice = input("heads or tails ? : \n").lower()
toss  = random.randint(0,1)
toss_result = " "
if toss == 0 :
	toss_result = "heads"
else :
	toss_result = "tails"

if choice == toss_result : 
	print("You won")
else : 
	print("You lost ! the result was : ")
	print(toss_result)




# guess the number 


random_number = random.randint(0,100)
count = 0
print("Game 2 : The computer will generate a random number between 0 and 100 . Try to guess wich one it is ")

choice = -1 

while choice != random_number : 
	choice = int(input("What is your guess ? : \n"))
	if choice > random_number : 
		print("the number is smaller")
	else : 
		print("the number is greater")
	count += 1

print("congratulations! You found the right number after : ") 
print(count)
print(" tries")



