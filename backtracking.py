nums = [1,2]
def backtrack(i, subset):
    if i == len(nums):
        print(subset)
        return
    backtrack(i+1, subset+[nums[i]])
    backtrack(i+1, subset)
backtrack(0, [])