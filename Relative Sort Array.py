class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = {}
        for x in arr1:
            count[x]=count.get(x,0)+1
        result = [] 
        for x in arr2:
            if x in count:
                result.extend([x]*count[x])
                del count[x]
        remaining = []
        for k ,t in count.items():
            remaining.extend([k]*t)
        remaining.sort()
        result.extend(remaining)
        return result

        