class Solution(object):
    def intersect(self, nums1, nums2):
        hash_map ={}
        result =[]

        for num in nums1:
            if num in hash_map:
                hash_map[num] +=1
            else:    
                hash_map[num] = 1

        for num in nums2:
            if num in hash_map and hash_map[num]> 0:
                result.append(num)
                hash_map[num]-=1
        return result                       


        