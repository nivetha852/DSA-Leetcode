class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = nums[0]
        answer = nums[0]
        for i in range(1,len(nums)):
            x = current +nums[i]
            current = max(nums[i],x)
            answer = max(current,answer)
        return answer
        