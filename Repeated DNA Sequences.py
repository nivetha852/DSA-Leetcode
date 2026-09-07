class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        r = set()
        for i in range(len(s)-9):
            sub = s[i:i+10]
            if sub in seen:
                r.add(sub)
            else:
                seen.add(sub)
        return list(r)
        