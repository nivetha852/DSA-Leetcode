class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for num in strs:
            key = ''.join(sorted(num))
            if key not in d:
                d[key]=[]
            d[key].append(num)
        return list(d.values())