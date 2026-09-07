class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        c = list(range(1,n+1))
        index =0
        while len(c)>1:
            reveal  = (index+k-1)%len(c)
            c.pop(reveal)
            index = reveal
        return c[0]