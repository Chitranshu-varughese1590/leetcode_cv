class Solution(object):
    def containsDuplicate(self, nums):
        hash = set()
        for num in nums:
            if num in hash:
                return True
            hash.add(num)  

        return False    
        