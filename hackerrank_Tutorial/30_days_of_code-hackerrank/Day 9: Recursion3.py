""" Task
Write a factorial function that takes a positive integer n, as a parameter and prints the result of  ( factorial).

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial,
 you will get a score of 0

Input Format
A single integer, n (the argument to pass to factorial).
"""
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.


def factorial(n):
    # Write your code here
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    n = int(input().strip())
    print(f"Factorial of {n} is {factorial(n)}")
