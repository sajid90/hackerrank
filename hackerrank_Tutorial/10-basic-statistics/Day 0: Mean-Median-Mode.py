"""Objective, In this challenge, we practice calculating the mean, median, and mode.
# Task
Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines.
 If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer),
your answers should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3, 7.0 format).

Example:
N = 6
X = [1, 2, 3, 4, 5, 5]
The mean is 20/6 = 3.3.
The median is 3+4/2 3.5.
The mode is 5 because 5 occurs most frequently.
Input Format

The first line contains an integer, N, the number of elements in the array.
The second line contains N space-separated integers that describe the array’s elements.

Sample Input:
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Sample Output:
43900.6
44627.5
4978
"""
import numpy as np
from scipy import stats
# 4 5 87 24 5 4 9 88
size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))

#OR


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
X = [int(val) for val in input().strip().split()]
print(X)
# print mean (sum of numbers/total element)
print(sum(X) / len(X))

""" Median:
To calculate the median, we need the elements of the array to be sorted in either non-increasing or non-decreasing order
The sorted array X = {4978, 11735, 14216, 14470, 38120, 51135, 64630, 67060, 73429, 99233}. 
We then average the two middle elements: median = 89255/2 = 44627.5
"""
sorted_arr = sorted(X)
first = sorted_arr[int(len(sorted_arr) / 2 - 1)]
second = sorted_arr[int(len(sorted_arr) / 2)]
print((first + second) / 2)

# Mode:
# We can find the number of occurrences of all the elements in the array:
# print mode (Duplicate value) -> If your array contains more than one modal value, choose the numerically smallest one.

# X = [int(i) for i in a.split()]

d = dict()
for i in X:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
dup_key = []
for key, val in d.items():
    if val > 1:
        dup_key.append(key)
if dup_key:
    print(min(dup_key))
else:
    print(min(X))

