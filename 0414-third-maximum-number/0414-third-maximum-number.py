class Solution(object):
    def thirdMax(self, nums):
        first = float("-inf")
        sec = float("-inf")
        third = float("-inf")
        
        for num in nums:
            if num == first or num== sec or num == third:
                continue

            if num > first:
                third = sec 
                sec = first 
                first = num

            elif num > sec:
                third = sec
                sec = num

            elif num > third:
                third = num

        if third == float("-inf"):
                return first
        return third                        