def prefix_max(arr):
    n = len(arr)
    pfmax = [0] * n
    max_val = float('-inf')
    for i in range(n):
        if arr[i] > max_val:
            max_val = arr[i]
            pfmax[i] = max_val
    return pfmax
arr = [3, 10, 6, 7, 0, 2]
print(prefix_max(arr))