import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        maximum = []
        for x,y in points:
            dist = -(x**2+y**2)
            heapq.heappush(maximum,(dist,[x,y]))
            if len(maximum)>k:
                heapq.heappop(maximum)
        return [points for dist,points in maximum]
                