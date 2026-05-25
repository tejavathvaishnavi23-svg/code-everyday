def moveZeroes(nums):
    index = 0
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1
    for i in range(index, len(nums)):
        nums[i] = 0
    return nums
nums = [0,1,0,3,12]
print(moveZeroes(nums))