def suffix_max(arr):
    n = len(arr)
    sfmax = [0] * n
    max_val = float('-inf')

    for i in range(n-1, -1, -1):
            max_val = max(max_val, arr[i])
            sfmax[i] = max_val

    return sfmax
arr = [3, 10, 6, 7, 0, 2]
print(suffix_max(arr))