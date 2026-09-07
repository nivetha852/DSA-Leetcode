=class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k>len(bloomDay):
            return -1
        def bou(day):
            bouquet=0
            flower =0
            for bloom in bloomDay:
                if bloom<=day:
                    flower = flower+1
                    if flower==k:
                        bouquet=bouquet+1
                        flower=0
                else:
                    flower = 0
            return bouquet>=m
        l,r = min(bloomDay),max(bloomDay)
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if bou(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans