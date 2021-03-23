"""
Task: 
Given an integer, n, print its first 10 multiples. 
Each multiple n * i (where 1<= i <= 10) should be printed 
on a new line in the form: n x i = result.
"""

# This is needed for the program to pass the automated tests on HackerRank
if __name__ == '__main__':
    n = int(input())

for i in range(1,11):
    print(n, "x", i, "=", i * n)