def count_pairs(arr, m):
    freq = [0]*m
    count = 0
    for num in arr:
        rem = num % m

        if rem == 0:
            pair = 0
        else:
            pair = m-rem
        count += freq[pair]
        freq[rem] += 1
    return count
arr = [5, 2, 3, 4, 6]
m = 3
print(count_pairs(arr,m))