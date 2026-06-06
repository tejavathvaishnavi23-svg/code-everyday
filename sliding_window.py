def max_subarray_sum(arr, k):
    n = len(arr)
    #Calculate sum of first window
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]
    ans = curr_sum
    #slide the window
    s = 1
    e = k
    while e < n:
        curr_sum = curr_sum - arr[s-1] + arr[e]
        if curr_sum > ans:
           ans = curr_sum
        s += 1
        e += 1
    return ans
arr = [3, 4, -2, 5, 3, -2, 8, 2, 1, 4]
k = 6
print(max_subarray_sum(arr, k))
