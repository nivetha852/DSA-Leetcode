class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        i =[0]*n
        length = 0
        j=1
        while j<n:
            if s[j]==s[length]:
                length = length +1
                i[j]=length
                j =j+1
            elif length >0:
                length = i[length-1]
            else:
                i[j]=0
                j = j+1
        prefix = i[n-1]
        return s[:prefix]