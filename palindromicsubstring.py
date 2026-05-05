#Given a string s, return the longest palindrome substring
#Using Brute force approach
def longestPalindrome(s):
    n = len(s)
    longest = ""
    for i in range(n):
        for j in range(i,n):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                if len(substring) > len(longest):
                    longest = substring
        return longest
print(longestPalindrome("babad"))

#Using Expand Around Center approach
def longestPalindrome(s):
    n = len(s)
    longest = ""
    def expandaroundcenter(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    for i in range(n):
        odd_palindrome = expandaroundcenter(i,i)
        even_palindrome = expandaroundcenter(i,i+1)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    return longest
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))