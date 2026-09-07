class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        result = n
        for i in range(0,len(nums)):
            result = result^i
            result = result^nums[i]
        return result