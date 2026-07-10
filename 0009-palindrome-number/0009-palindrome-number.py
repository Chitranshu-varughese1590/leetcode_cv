class Solution(object):
    def isPalindrome(self, x):
        num = x
        palindrome = 0
        while x > 0:
            last = x % 10 
            palindrome = (palindrome * 10) + last
            x = x //10
        if palindrome == num :
            return True
        else :
            return False        