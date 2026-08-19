class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i,num in enumerate(nums):
            value = target - num
            if value in hash_map:
                return hash_map[value],i
            else:
                hash_map[num]=i      
        