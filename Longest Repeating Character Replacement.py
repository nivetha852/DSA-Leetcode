class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        maximum = 0 
        d = {}
        result = 0
   
        for right in range(0,len(s)):
            d[s[right]]= d.get(s[right],0)+1
            maximum = max(maximum,d[s[right]])
            w = right -left +1
            if w- maximum >k:
                d[s[left]]= d[s[left]]-1
                left = left+1
            result = max(result,(right-left)+1)
        return result