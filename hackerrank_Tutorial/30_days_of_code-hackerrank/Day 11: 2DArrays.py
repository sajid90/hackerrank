"""Context
Given a 6 X 6 2D Array, A:
Input : 1 1 1 0 0 0
        0 1 0 0 0 0
        1 1 1 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
We define an hourglass in A to be a subset of values with indices falling
in this pattern in A's graphical representation:
    A B C
      D
    E F G
Output : 19
Below is the hour glass with
maximum sum
2 4 4
  2
1 2 4
There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Example:
In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.
"""

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append([int(val) for val in input().strip().split()])

    values = []
    # as hourglass max value is 3.
    for i in range(4):
        for j in range(4):
            values.append(sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3]))
    print(max(values))
