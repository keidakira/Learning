"""
Problem Statement:
Given two string X and Y, print the length of the longest common subsequence (LCS) Z
LCS(X, Y) = Z. Print length of Z. Another part of the problem is printing Z too.

Subsequence is formed by removing 0 or more characters from a string X.
So, let X = "KEIDA", then Subsequence of X can be {"KEIDA", "KID", "KIA", "A", "KED", "I"}
They need to be in the same order as they are in given string.
These are NOT subsequence of X, {"IAD", "EDI", ..} Since in X, "A" comes after D so "IAD" is wrong

All substrings are subsequences but not all subsequences are substrings

For given X, of length n, there can be 2^n possible subsequences
"""


def recursive_lcs(string_one, string_two):
    m = len(string_one)
    n = len(string_two)

    if m == 0 or n == 0:
        return 0
    elif string_one[-1] == string_two[-1]:
        return 1 + recursive_lcs(string_one[:m-1], string_two[:n-1])
    else:
        return max(recursive_lcs(string_one[:m-1], string_two), recursive_lcs(string_one, string_two[:n-1]))


def dp_lcs(string_one, string_two):
    m = len(string_one)
    n = len(string_two)

    memory = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                memory[i][j] = 0
            elif string_one[i-1] == string_two[j-1]:
                memory[i][j] = memory[i-1][j-1] + 1
            else:
                memory[i][j] = max(memory[i-1][j], memory[i][j-1])

    return memory[m][n]


X = "AGGTAB"
Y = "GXTXAYB"

result = recursive_lcs(X, Y)

print(result)
