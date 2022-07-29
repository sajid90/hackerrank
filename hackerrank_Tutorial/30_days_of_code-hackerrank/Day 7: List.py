"""Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
Example
A = [1,2,3,4]
Print 4 3 2 1. Each integer is separated by one space.
"""

n = int(input().strip())

# Line 10 and 11 is same but different style
# arr = list(map(int, input().strip().split()))
arr = ([int(val) for val in input().strip().split()])
print(*arr[::-1])
