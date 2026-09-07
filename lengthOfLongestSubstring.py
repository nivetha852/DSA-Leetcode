class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset = set()
        left = 0
        length=0
        for i in range(0,len(s)):
            while s[i] in charset:
                charset.remove (s[left])
                left= left+1
            charset.add (s[i])
            length = max(length,(i-left)+1)
        return length
        