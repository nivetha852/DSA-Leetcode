class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        rev= s[::-1]
        combined =s+"#"+rev
        n = len(combined)
        lps=[0]*n
        for i in range(1,n):
            j = lps[i-1]
            while j>0 and combined [i]!=combined[j]:
                j = lps[j-1]
            if combined[i]==combined[j]:
                j = j+1
            lps[i]=j
        return s[lps[-1]:][::-1]+s