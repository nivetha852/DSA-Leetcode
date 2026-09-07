class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        remove = set()
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        remove.update(stack)
        result=[]
        for i in range(len(s)):
            if i not in remove:
                result.append(s[i])
        return "".join (result)

        