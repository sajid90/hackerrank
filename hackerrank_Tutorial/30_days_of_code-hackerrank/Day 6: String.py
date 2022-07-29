"""Given a string, S, of length N that is indexed from 0 to N – 1,
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line
(see the Sample below for more detail).

Note: 0 is considered to be an even index.
Example
s = adbecf
Print abc def
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
for num in range(N):
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            print(S[i], end="")
    print(" ", end="")

    for i in range(len(S)):
        if i % 2 != 0:
            print(S[i], end="")
    print()
