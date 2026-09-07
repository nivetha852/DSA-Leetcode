class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(left,right):
            while left>=0 and right <len(s) and s[left]==s[right]:
                left = left-1
                right = right+1
            return s[left+1:right]
        longest = ""
        for i in range(0,len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)
            if len(odd)>len(even):
                curr = odd
            else:
                curr = even
            if len(longest)<len(curr):
                longest = curr
        return longest
        