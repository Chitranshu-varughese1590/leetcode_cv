class Solution(object):
    def intersection(self, nums1, nums2):
        hash = set(nums1)
        result = set()
      
        for num in nums2:
            if num in hash:
                result.add(num)
            
        return list(result) 



        