class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        inf = float("inf")
        dist =[inf]*n
        dist[src]=0
        for _ in range(k+1):
            new_dist = dist[:]
            for from_city,to_city,price in flights:
                if dist[from_city] !=inf:
                    new_dist[to_city]= min(new_dist[to_city],dist[from_city]+price)
            dist = new_dist
        if dist[dst]==inf:
            return -1
        else:
            return dist[dst]      