"""
Task: 
	Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
	You are given  scores. Store them in a list and find the score of the runner-up.
"""

# This is needed for the program to pass the automated tests on HackerRank
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
def second_max(n, arr):
    largest = None
    secondLargest = None
    
    for i in range(0, n):
        if largest is None:
            largest = arr[i]
        
        if arr[i] > largest:
            largest = arr[i]
            
    for i in range(0, n):
        if secondLargest is None:
            secondLargest = arr[i]
        
        if arr[i] <= largest - 1:
            secondLargest = arr[i]

    return secondLargest

#implement for a descending sorted list, e.g. [8,7,6,5,4]
print(second_max(n, arr))

