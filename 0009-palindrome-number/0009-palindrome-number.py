# easy way 
class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False      



#brute force 
class solution(object):
    def isPalindrome(self,x):
        if x < 0 :
            return False
        num = x
        palindrome = 0
        while x > 0:
            last = x % 10
            palindrome = (palindrome * 10 ) + last
            x = x // 10
        return palindrome == num :
            
