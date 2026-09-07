class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        need = {}
        for i in t:
            need[i]=need.get(i,0)+1
        have = {}
        req = len(need)
        formed = 0
        left = 0
        best = float("inf")
        bestleft = 0
        for right in range(len(s)):
            i = s[right]
            have[i]= have.get(i,0)+1
            if i in need and have[i]==need[i]:
                formed = formed+1
            while formed == req:
                window = right-left+1
                if window<best:
                    best = window
                    bestleft=left
                left_char = s[left]
                have[left_char]= have[left_char]-1
                if left_char in need and have[left_char]<need[left_char]:
                    formed = formed -1
                left = left+1
        if best == float("inf"):
            return ""
        return s[bestleft:bestleft+best]

        