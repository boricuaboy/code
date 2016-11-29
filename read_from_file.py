num_names = 0

with open('nameslist.txt', 'r') as open_file:
	for name in open_file:
		names = name.split()
		
		num_names += len(names)
		
print num_names