import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}
        minHeap = [(0, k)]
        while minHeap:
            d, node = heapq.heappop(minHeap)
            if node in dist:
                continue
            dist[node] = d
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(minHeap, (d + weight, neighbor))

        if len(dist) != n:
            return -1
        return max(dist.values())