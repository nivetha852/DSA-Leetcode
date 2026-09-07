class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        num1 = 0
        frequency = {0:1}
        for num in nums :
            count = count+num
            if count-k in frequency:
                num1 = num1+frequency[count-k]
            frequency[count]=frequency.get(count,0)+1
        return num1