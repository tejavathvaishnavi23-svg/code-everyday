def water_trapping(arr):
    n = len(arr)
#prefix max
    pfmax = [0] * n
    max_val = float('-inf')

    for i in range(n):
        max_val = max(max_val, arr[i])
        pfmax[i] = max_val

# suffix max
    sfmax = [0] * n
    max_val = float('-inf')

    for i in range(n -1, -1, -1):
        max_val = max(max_val, arr[i])
        sfmax[i] = max_val

    ans = 0

    for i in range(n):
        level = min(pfmax[i], sfmax[i])
        water = level - arr[i]
        ans += water

    return ans

arr = [4, 2, 5, 7, 4, 2, 3, 6, 8, 2, 3]
print(water_trapping(arr))