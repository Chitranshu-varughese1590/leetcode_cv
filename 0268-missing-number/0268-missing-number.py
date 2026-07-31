class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        exp_sum = n*(n+1)//2
        act_sum = sum(nums)

        if exp_sum == act_sum:
            return 0
        else:
            return exp_sum - act_sum    
       

    
            
        