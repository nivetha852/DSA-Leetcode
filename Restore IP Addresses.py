class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result=[]
        def backtrack(index,current):
            if len(current)==4:
                if index ==len(s):
                    result.append(".".join(current))
                return
            for i in range(1,4):
                if index+i>len(s):
                    break
                part = s[index:index+i]
                if len(part)>1 and part[0]=='0':
                    continue
                if int(part)>255:
                    continue
                current.append(part)
                backtrack(index+i,current)
                current.pop()
        backtrack(0,[])
        return result