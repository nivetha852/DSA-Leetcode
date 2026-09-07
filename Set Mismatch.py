class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        actualsum = sum(nums)
        actual = sum(x*x for x in nums)
        expected = n*(n+1)//2
        expectedsums = n*(n+1)*(2*n+1)//6
        sumdiff = actualsum-expected
        sqdiff = actual-expectedsums
        sumtotal = sqdiff//sumdiff
        dup = (sumdiff+sumtotal)//2
        missing = sumtotal-dup
        return [dup,missing]



        