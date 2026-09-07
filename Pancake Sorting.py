class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int][3,2,4,1]
        """
        n = len(arr)
        s =[]
        for a in range(n,1,-1):
            r = arr.index(a)
            if r == a-1:
                continue
            if r!=0:
                arr[:r+1]=arr[:r+1][::-1]
            s.append(r+1)
            arr[:a]= arr[:a]
            s.append(a)
            return s
