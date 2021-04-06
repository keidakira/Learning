n = 4
L = 3
curr_stage = 0
candies = [-1, 1, 2, 10, 5]
solutions = []


def solution(L, n, path):
    if L == 0 and n != 0:
        return 0, path

    if L >= 0 and n == 0:
        # Successfully reached in <= L steps
        solutions.append(path)
        return 1, path

    if L < 0 or n < 0:
        return 0, path

    q = -1
    index = -1

    for i in range(1, 4):
        if L-1 < 0 or n-i < 0:
            return 0, path

        x, arr = solution(L-1, n-i, path+[i])

        if q <= x:
            # Add this recursion
            q = x
            index = i

    if q == 1:
        path += arr

    return q, path


result = solution(3, 4, [])
print(solutions)
