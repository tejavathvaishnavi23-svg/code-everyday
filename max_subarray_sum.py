def max_sub_kadanes(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(current_sum + arr[i], arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
arr = [-2, 3, 4, -1, 5, -10, 7]
print(max_sub_kadanes(arr))