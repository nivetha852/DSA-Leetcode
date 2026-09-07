class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        p = list(range(len(edges) + 1))
        def find(i):
            if p[i] == i:
                return i
            p[i] = find(p[i])
            return p[i]

        for u, v in edges:
            u1= find(u)
            v1= find(v)
            if u1== v1:
                return [u, v]
            p[u1] = v1

        