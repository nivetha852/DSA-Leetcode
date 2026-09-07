class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        base = 26
        mod = 10**9+7
        nums=[ord(c)-ord('a')for c in s]
        def check(length):
            if length ==0:
                return ""
            seen ={}
            h =0
            power = pow(base,length-1,mod)
            for i in range(length):
                h= (h*base+nums[i])%mod
            seen[h]=[0]
            for b in range(1,n-length+1):
                h = (h-nums[b-1]*power)%mod
                h = (h*base+nums[b+length-1])%mod
                if h in seen:
                    candidate = s[b:b+length]
                    for start in seen[h]:
                        if s[start:start+length]==candidate:
                            return candidate
                seen.setdefault(h, []).append(b)
            return ""
        left = 1
        right = n-1
        longest=""
        while left<= right:
            mid = (left+right)//2
            result = check(mid)
            if result:
                longest = result
                left = mid+1
            else:
                right = mid-1
        return longest