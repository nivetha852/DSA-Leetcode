class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [-1]*n
        stack =[]
        for i in range(2*n):
            index =i%n
            while stack and nums[stack[-1]]<nums[index]:
                oldindex = stack.pop()
                result[oldindex]=nums[index]
            if i<n:
                stack.append(index)
        return result