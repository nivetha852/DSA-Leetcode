class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def back(i,current):
            if i ==len(nums):
                result.append(current[:])
                return 
            back(i+1,current)
            current.append(nums[i])
            back (i+1,current)
            current.pop()
            backtrack(0,[])
            return result