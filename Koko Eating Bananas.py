import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l,r = 1,max(piles)
        def hours(k):
            return sum((p+k-1)//k for p in piles)
        while l<r:
            mid = (l+r)//2
            if hours(mid)<=h:
                r = mid
            else:
                l = mid+1
        return l
        