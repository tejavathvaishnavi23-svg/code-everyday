def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    writepos = m + n - 1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[writepos] = nums1[p1]
            p1 -= 1
        else:
            nums1[writepos] = nums2[p2]
            p2 -= 1
        writepos -= 1
    return nums1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))

