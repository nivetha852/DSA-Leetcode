class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result =[]
        for i in range(0,len(nums)):
            idx = abs(nums[i])-1
            if nums[idx]>0:
                nums[idx]= - nums[idx]
        for i in range(0,len(nums)):
            if nums[i]>0:
                result .append(i+1)
        return result
        