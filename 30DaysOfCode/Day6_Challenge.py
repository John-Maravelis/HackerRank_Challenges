"""
Task:
Given a string, S, of length N that is indexed from 0 to N-1,
 print its even-indexed and odd-indexed characters as 2 space-separated 
 strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Example: 
s = adbecf
Print abc def
"""

strings = []
n = int(input())

for i in range(n):
    strings.append(input())

for i in range(n): # iterate over each word
    even, odd = "", ""

    for j in range(len(strings[i])): # iterate over each letter
        if j % 2 == 0:
            even += strings[i][j]
        else:
            odd += strings[i][j]
    print(even, odd)

