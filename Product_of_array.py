
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        answer = [1]*n
        prefix = 1
        suffix = 1
        for i in range(0,n):
            answer[i]=prefix
            prefix= prefix*nums[i]
        for  j in range(n-1,-1,-1):
            answer[j]= answer[j]*suffix
            suffix = suffix*nums[j]
        return answer
        
        