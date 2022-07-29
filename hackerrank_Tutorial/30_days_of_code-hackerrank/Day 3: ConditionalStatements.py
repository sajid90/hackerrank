""" Task
Given an integer n, perform the following conditional actions:
-> If n is odd, print Weird
-> If n is even and in the inclusive range of 2 to 5, print Not Weird
-> If n is even and in the inclusive range of 6 to 20, print Weird
-> If n is even and greater than 20, print Not Weird

Complete the stub code provided in your editor to print whether n is weird or not.
"""

if __name__ == '__main__':
    N = int(input().strip())
    print(N)
    if N % 2 != 0:
        print("Weird")
    elif N % 2 == 0 and N in list(range(2, 6)):
        print("Not Weird")
    elif N % 2 == 0 and N in list(range(6, 21)):
        print("Weird")
    elif N % 2 == 0 and N > 20:
        print("Not Weird")

