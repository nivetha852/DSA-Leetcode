class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        maximum = 0
        nums.sort()
        for i in range(0,len(nums)-1):
            s =nums[i+1]-nums[i]
            maximum = max(s,maximum)
        return maximum
