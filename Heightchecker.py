class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        x= sorted(heights)
        for i in range(0,len(heights)):
           if heights[i]!= x[i]:
            count = count+1
        return count

        