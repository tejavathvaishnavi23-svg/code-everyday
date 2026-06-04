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

#another method
def water_trapping(heights):
    n = len(heights)

    prefix = [0] * n
    suffix = [0] * n

    # Prefix max
    prefix[0] = heights[0]
    i = 1
    while i < n:
        prefix[i] = max(prefix[i - 1], heights[i])
        i += 1

    # Suffix max
    suffix[n - 1] = heights[n - 1]
    i = n - 2
    while i >= 0:
        suffix[i] = max(suffix[i + 1], heights[i])
        i -= 1

    # Calculate trapped water
    total_water = 0
    i = 0
    while i < n:
        leftmax = prefix[i]
        rightmax = suffix[i]
        waterlevel = min(leftmax, rightmax)

        if waterlevel > heights[i]:
            total_water += waterlevel - heights[i]

        i += 1

    return total_water


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(water_trapping(arr))