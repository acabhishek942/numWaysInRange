import operator as op
from functools import reduce
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer//denom


numTestCases = int(input())
LRlist = []
for _ in range(numTestCases):
    LRlist.append(input().split())

for i in LRlist:
    numWays = 0
    for x in range(int(i[0]), int(i[1])+1):
        if x < 3:
            numWays += 2 * ncr(int(i[1]), x)
    print(numWays)
