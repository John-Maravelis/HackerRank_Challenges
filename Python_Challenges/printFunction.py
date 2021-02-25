"""
Task: Print the list of integers from 1 through n as a string, without spaces.
"""

# This is needed for the program to pass the automated tests on HackerRank
if __name__ == '__main__':
    n = int(input())

result = ""
for i in range(1,n+1):
    result += str(i) 

print(result)
