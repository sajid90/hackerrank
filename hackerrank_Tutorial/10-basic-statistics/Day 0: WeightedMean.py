# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W

def weighted_mean(X, W):
    # Write your code here
    l = list()
    for x, w in zip(X, W):
        l.append(x * w)
    print(round(sum(l) / sum(W), 1))


if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    # 10 40 30 50 20 10 40 30 50 20
    weights = list(map(int, input().rstrip().split()))
    # 1 2 3 4 5 6 7 8 9 10
    weighted_mean(vals, weights)
