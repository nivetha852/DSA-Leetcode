class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result=[]
        path =[]
        def ispalindrome(string):
            return string ==string[::-1]
        def backtrack(start):
            if start ==len(s):
                result.append(path[:])
                return
            for end in range(start+1,len(s)+1):
                substring=s[start:end]
                if ispalindrome(substring):
                    path.append(substring)
                    backtrack(end)
                    path.pop()
        backtrack(0)
        return result
        