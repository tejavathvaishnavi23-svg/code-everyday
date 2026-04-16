#1.Max consecutive ones
#Given a list of 0s and 1s, find the maximum number of consecutive 1s.

def max_consecutive_ones(nums):
    count = 0
    max_count = 0

    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count

nums = [1, 1, 0, 1, 1, 1]
print("Max consecutive ones:", max_consecutive_ones(nums))

#2.Given a binary array nums (containing only 0s and 1s),
# return the maximum number of consecutive 1s in the array if you can flip at most one 0 to 1.
def max_consecutive_ones(nums):
    left = 0
    zero_count = 0
    max_length = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        # If more than one zero, shrink window
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length

print(max_consecutive_ones([1,0,1,1,0]))
print(max_consecutive_ones([1,1,1]))
print(max_consecutive_ones([0,0,0]))
