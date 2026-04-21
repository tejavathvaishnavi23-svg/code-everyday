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

#3.Given a string s, find the length of the longest substring without repeating characters.
#input s = "abcabcbb"
def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
print(longest_substring("abcabcbb"))

#4.Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
def subarray_sum(nums, k):
    count = 0
    current_sum = 0
    prefix_map = {0:1}
    for num in nums:
        current_sum += num
        if current_sum - k in prefix_map:
            count += prefix_map[current_sum - k]
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
    return count
print(subarray_sum(nums, 3))

#5.Given an integer n print centered pyramid where each row contains
# increasing numbers starting from 1 upto row numbers then decreasing back to 1.
def print_pyramid(n):
    for i in range(1, n + 1):
        # print spaces
        print(" "* (n-i),end=" ")
        # increasing number
        for j in range(1, i+1):
            print(j,end=" ")
        # decreasing number
        for j in range(i-1,0,-1):
            print(j,end=" ")
        print()
print_pyramid(5)

#6.Given two strigs check they are anagrams?
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
print(is_anagram("listen", "silent"))

#7.Given an array of integer move end while maintaining the relative order
#non zero elements.
def move_zeroes(nums):
    pos = 0
    for  i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1
    for i in range(pos, len(nums)):
        nums[i] = 0
    return nums
print(move_zeroes([1, 0, 1, 0, 13]))

#8.Valid parentheses
def is_valid(s):
    stack = []
    mapping ={
        ')':'(',
        '{':'}',
        '[':']'
    }
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0
print(is_valid("{[()]}"))
print(is_valid("[()}"))

#9.Given a string containing letters and digits extract all groups of
#consecutive digits and return largest number among them.
def largest_number(s):
    numbers = []
    current_num = ""
    for char in s:
        if char.isdigit():
            current_num += char
        else:
            if current_num:
                numbers.append(int(current_num))
                current_num = ""
    if current_num:
        numbers.append(int(current_num))
    return max(numbers) if numbers else 0
print(largest_number(["abc123xyz45ab678"]))

#10.Given an integer array nums, return an array answer such that:
#answer[i] = product of all elements except nums[i]
def product_except(nums):
    n = len(nums)
    answer = [1]*n
    # left products
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]
    # right products
    right = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right
        right *= nums[i]
    return answer
print(product_except([1,2,3,4,5,6,7,8,9]))

#11.Given a 2D matrix, return a new 2D matrix where each element
# result[i][j] is the sum of all elements in row i except nums[i][j] itself.
def sum_except(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = [[1] * n for i in range(m)]
    for i in range(m):
        # left pass:sum of all elements to the left
        left = 0
        for j in range(n):
            result[i][j] = left
            left += matrix[i][j]
        # right pass: add sum of all elements to the right
        right = 0
        for j in range(n-1, -1, -1):
            result[i][j] = right
            right += matrix[i][j]
    return result
print(sum_except([[1,2,3],[4,5,6],[7,8,9]]))

#12.Given an integer array nums, return an array answer such that answer[i]
#is equal to the product of all elements of nums except nums[i].
def productExceptSelf(nums):
    n = len(nums)
    answer = [1]*n
    #fill prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    #multiply suffix products
    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    return answer
print(productExceptSelf([1,2,3,4,]))

#13.Given an array height where each element represents the height of a bar,
#calculate how much rainwater can be trapped between the bars after raining.
def trap(height):
    n = len(height)
    #prefix max
    prefix_max = [0] * n
    prefix_max[0] = height[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i-1], height[i])
    #suffix max
    suffix_max = [0] * n
    suffix_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], height[i])
    #calculate water
    water = 0
    for i in range(n):
        water += min(prefix_max[i], suffix_max[i]) - height[i]
    return water
print(trap([4,2,0,3,2,5]))