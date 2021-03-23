"""
Task:
Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
"""

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split())) # this is specified by HackerRank
    rev_array = arr[::-1]
    
    for i in range(0, n):
        print(rev_array[i], end=" ")
