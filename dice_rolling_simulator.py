import random
	
min = 1
max = 6

ask = "yes" or "y" or "YES" or "Y"
while (ask == "yes" or ask == "y" or ask == "YES" or ask == "Y"):
	print "Rolling the dices..."
	print "The values are..."
	print random.randint(min, max)
	print random.randint(min, max)
	
	ask = str(raw_input("Would you like to roll the dice again? " ))