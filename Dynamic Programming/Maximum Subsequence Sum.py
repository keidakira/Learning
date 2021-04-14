def aux(e, ar):
    if len(ar) == 0:
        return e

    mx = 0

    for i,el in enumerate(ar):
        if el > e:
            mx = max(mx, e + aux(el, ar[i+1:]))

    return mx


def max_subsequence_sum(arr):
    q = -1
    for i, num in enumerate(arr):
        q = max(q, aux(i, arr[i+1:]))
    print(q)


max_subsequence_sum([2, 5, 3, 7])
