#Given a string s, return true if it is a palindrome or false
def isPalindrome(s):
    i, j=0, len(s)-1
    while i < j:
        if not s[i].isalnum():
            i = i+1
        elif not s[j].isalnum():
            j = j-1
        elif s[i].lower() == s[j].lower():
            i = i+1
            j = j-1
        else:
            return False
        return True
print(isPalindrome("A man, a plan, a canal: Panama"))

