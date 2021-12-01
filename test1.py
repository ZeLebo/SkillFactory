# Files

with open("README.md", 'r') as my_file:
	for line in my_file:
		print(line[:-1:])