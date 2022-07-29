"""Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for. For each name queried,
print the associated entry from your phone book on a new line in the form name=phoneNumber;
if an entry for the name is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format:
The first line contains an integer, n, denoting the number of entries in the phone book.
Each of the n subsequent lines describes an entry in the form of 2 space-separated values on a single line.
The first value is a friend's name, and the second value is an 8-digit phone number.

After the n lines of phone book entries, there are an unknown number of lines of queries.
Each line (query) contains name a to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
d = {}
for num in range(N):
    name = input().split()
    d[name[0]] = name[1]

while True:
    try:
        name = input()
        if name in d:
            print(f'{name}={d[name]}')
        elif name.lower() == "quit":
            break
        else:
            print("Not found")
    except EOFError:
        break
