def special_index(arr):
    n = len(arr)
    count = 0
# prefix sum of even indices
    pf_even = [0] * n
    temp = arr.copy()
    for i in range(n):
        if i % 2 == 1:
            temp[i] = 0
    s = 0
    for i in range(n):
        s += temp[i]
        pf_even[i] = s
# prefix sum of odd indices
    pf_odd = [0] * n
    temp = arr.copy()
    for i in range(n):
        if i % 2 == 0:
            temp[i] = 0
    s = 0
    for i in range(n):
        s += temp[i]
        pf_odd[i] = s
# check each index
    for i in range(n):
        if i == 0:
            total_even = pf_even[n -1] - pf_even[i]
            total_odd = pf_odd[n -1] - pf_odd[i]
        else:
            total_even = pf_even[i-1] + (pf_odd[n - 1] - pf_odd[i])
            total_odd = pf_odd[i-1] + (pf_even[n-1] - pf_even[i])
        if total_even == total_odd:
            count += 1
    return count
arr = [2,4,6,7,8,9,10,2,7]
print(special_index(arr))
arr = [2,1,6,4]
print(special_index(arr))

