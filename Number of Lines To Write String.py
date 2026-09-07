class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        lines =1 
        curr = 0
        for ch in s:
            width = widths[ord(ch)-ord('a')]
            if curr+width >100:
                lines = lines+1
                curr = width
            else:
                curr = curr+width
        return [lines,curr]
        