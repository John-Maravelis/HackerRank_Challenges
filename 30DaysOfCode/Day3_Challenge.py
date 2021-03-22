"""
Task: 
	Given an integer, n, perform the following conditional actions:
		If n is odd, print Weird
		If n is even and in the inclusive range of 2 to 5, print Not Weird
		If n is even and in the inclusive range of 6 to 20, print Weird
		If n is even and greater than 20, print Not Weird
"""

# This is needed for the program to pass the automated tests on HackerRank
if __name__ == '__main__':
    num = int(input().strip())

if num % 2 != 0 :
    print("Weird")
else:
    if num >= 2 and num <= 5:
        print("Not Weird")
    elif num <= 20:
        print("Weird")
    else:
        print("Not Weird")
