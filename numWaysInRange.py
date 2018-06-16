import operator as op
from functools import reduce
def ncr(n, r):
    """
    function to calculate number of ways to select r values from n numbers
    param n: total number of objects
    type n: integer

    param r: no. of objects to be selected
    type r: integer

    return: number of ways to select r values from n numbers
    type: integer
    """
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer//denom

# def recurrenceSolver(n):
#     """
#     Inefficient function
#     Also wrong implementation
#     """
#     if n in (1, 2):
#         return 0
#     elif n == 3:
#         return 1
#     return recurrenceSolver(n-1) + recurrenceSolver(n-2) + recurrenceSolver (n-1) + 2 ** (n-3)

def getNoCasesToRemove(n, r):
    return n - r - 1

numTestCases = int(input())
LRlist = []
# Necessary loop
for _ in range(numTestCases):
    LRlist.append(input().split())

# Need to check if I can avoid any of the below loops to increase efficiency
for i in LRlist:
    numWays = 0
    for x in range(int(i[0]), int(i[1])+1):
        if x < 3:
            numWays += 2 * ncr(int(i[1]), x)
            # print (numWays)
        else:
            # remove number of ways of three consecutive ones or zeroes
            numWays += max(2 * (ncr(int(i[1]), x) - getNoCasesToRemove(int(i[1]), x)), 1)
            # print (numWays)
    print(numWays%(10**9 + 7))
