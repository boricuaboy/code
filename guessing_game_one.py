import random

a = random.randint(1, 9)

ask = int(raw_input("Guess the number: "))

if ask < a:
	print "You guessed too low."
	
elif ask > a:
	print "You guessed too high."
	
else:
	print "You win!"