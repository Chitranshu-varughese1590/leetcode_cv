class Solution(object):
    def missingNumber(self, nums):
        seen  = set(nums)    

        for i in range (0,len(nums)+1):
            if i not in seen:
                return i

    
            
        