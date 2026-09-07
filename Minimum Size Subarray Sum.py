class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        mini = float("inf")
        current = 0
        for i in range(0,len(nums)):
            current = current+nums[i]
            while current>= target:
                mini= min(mini,i-left+1)
                current =current -nums[left]
                left = left+1
        if mini!=float("inf") :
            return mini 
        else:
            return 0