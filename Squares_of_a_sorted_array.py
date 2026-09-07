class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s =[]
        maximum = 0
        for i in nums:
            a = i**2
            s.append(a)
            s.sort()
        return s
    
                
            


