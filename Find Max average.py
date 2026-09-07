class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current= sum(nums[:k])
        maximum = current
        for i in range(k ,len(nums)):
            current = current+nums[i]-nums[i-k]
            if current>maximum:
                maximum = current
        answer = maximum/k
        return answer
        