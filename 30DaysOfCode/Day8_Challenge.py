"""
Task:
	Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
	You will then be given an unknown number of names to query your phone book for. 
	For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
	if an entry for name is not found, print Not found instead. 
"""

phoneBook = {}
n = int(input())

for _ in range(n):
	pair = input().split(' ')
	phoneBook[pair[0]] = pair[1]

try:
	while True:
		name = input()

		if name == '':
			break

		if name in phoneBook:	
			print(name + '=' + phoneBook[name])
		else:
			print('Not found')

except EOFError:
	pass