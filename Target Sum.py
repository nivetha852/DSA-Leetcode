class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n ={}
        def solve(i,total):
            if i ==len(nums):
                if total == target:
                    return 1
                return 0
            if (i,total)in n:
                return n[(i,total)]
            plus = solve(i+1,total+nums[i])
            minus=solve(i+1,total-nums[i])
            n[(i,total)]= plus+minus
            return n[i,total]
        return solve(0,0)
        