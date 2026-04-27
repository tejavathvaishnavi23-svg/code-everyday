#Given an array of integers nums and an integer target
#return indices of the two numbers such that they add up to target.
#Using Brute force:
def twosum(nums,target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
print(twosum([2,7,11,15],9))

#using HashMap:
def twosum(nums,target):
    hashmap = {}
    for i in range(0,len(nums)):
        search = target - nums[i]
        if search in hashmap:
            return [hashmap[search],i]
        else:
            hashmap[nums[i]] = i
print(twosum([2,7,11,15],9))