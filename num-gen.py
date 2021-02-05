import random

prnt = True

# amount of random digits to generate
num_gen = 5000

# current number of digits in a row
run_len = 1

# create a string to hold random integers
num_str = ""

# generate random ints and add them to the string
for _ in range(num_gen):
	
	num = str(random.randrange(0, 10))
	
	num_str += num

# find consecutive runs of repeating integers and print them out
for digit in range(len(num_str)-run_len):

	if (run_len > 1):
		run_len -= 1
		continue

	try:
		while (num_str[digit]) == (num_str[digit+run_len]):
			run_len += 1
	except IndexError:
		pass

	if (run_len >= 2):
		print("\nRepeat found at index " + str(digit) + " : " + num_str[digit:digit+run_len])
		

# print the full list of numbers:
if (prnt):

	start = 0
	end = 100
	
	print("\nNumbers:\n")
	
	while (start < len(num_str)):
		print(num_str[start:end])
		start += 100
		end += 100

	#print("\nNumbers:\n" + num_str)