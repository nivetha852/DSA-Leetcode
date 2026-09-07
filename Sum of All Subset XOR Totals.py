class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1<<len(nums)):
            xor = 0
            for j in range(len(nums)):
                if i &(1<<j):
                    xor = xor ^ nums[j]
            ans = ans+xor
        return ans       