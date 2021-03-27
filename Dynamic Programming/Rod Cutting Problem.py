"""
Problem Definition:
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Example:
If the price for length of rod is the following,
length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

Input: 8
Output: 22
When rod of length 8 is given, we can cut it as 2 + 6 whose prices are 5 + 17 = 22

We perform this using Dynamic Programming (DP) using Optimal Substructure i.e sub-problems are independent
of each other and are similar to the main problem.
"""


# Recursive method
def cut_rod(prices, n):
    if n == 0:
        return 0

    q = -1

    for i in range(n):
        q = max(q, prices[i] + cut_rod(prices, n - i - 1))

    return q


# Top-down approach of memoization
def top_down_cut_rod(prices, n):
    r = [-1] * (n+1)

    def aux(p, N):
        if r[N] >= 0:
            return r[N]

        if N == 0:
            q = 0
        else:
            q = -1

            for i in range(N):
                q = max(q, p[i] + aux(p, N-i-1))

        r[N] = q

        return q

    return aux(prices, n)


# Bottom-up approach
def bottom_up_cut_rod(prices, n):
    memory = [0] * (n+1)
    q = -1

    for i in range(1, n+1):
        for j in range(i):
            q = max(q, prices[j] + memory[i-j-1])
        memory[i] = q

    return memory[n]


prices_array = [1, 5, 8, 9, 10, 17, 17, 20]
length_of_rod = 8
result = top_down_cut_rod(prices_array, length_of_rod)

print(result)
