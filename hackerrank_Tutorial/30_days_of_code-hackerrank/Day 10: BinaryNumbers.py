""" Task
Given a base-10 integer, n, convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum number of consecutive 1‘s in n‘s binary representation.
When working with different bases, it is common to show the base as a subscript.

Example:
n = 125
The binary representation of 12510 is 11111012.
In base 10, there are 5 and 1 consecutive ones in two groups. Print the maximum, 5.
"""

if __name__ == '__main__':
    n = int(input().strip())
    print(f"Entered number is: {n}")
    temp = bin(n).replace("0b", "")
    temp = temp + '0'
    count = 0
    max_value = 0
    for i in temp:
        if int(i) == 1:
            count = count + 1
        else:
            if count > max_value:
                max_value = count
            count = 0
    print(f"Consecutive ones maximum number is {max_value}")

