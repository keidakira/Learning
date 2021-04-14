def recursive_lis(x, array):
    if len(array) == 1:
        if x < array[0]:
            return [x] + array
        else:
            return [x]
    else:
        res = recursive_lis(array[0], array[1:])
        if array[0] < res[0]:
            return [array[0]] + res
        else:
            return [array[0]]


result = recursive_lis(10, [22, 9, 33, 21, 50, 41, 60, 80])

print(result)
