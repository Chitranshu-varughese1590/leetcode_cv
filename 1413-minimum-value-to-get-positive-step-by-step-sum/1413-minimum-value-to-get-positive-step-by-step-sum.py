class Solution:
    def minStartValue(self, nums):
        total = 0
        minimum = 0

        for num in nums:
            total += num
            minimum = min(minimum, total)

        return 1 - minimum