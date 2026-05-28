#using sliding window
def findMaxAverage(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    return float(max_sum) / k
nums = [1,12,-5,-6,50,3]
k = 4
result = findMaxAverage(nums, k)
print("Maximum Average:", result)