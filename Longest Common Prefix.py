class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if  not strs:
            return ""
        reference = strs[0]
        for i in range(0,len(reference)):
            curr = reference[i]
            for j in strs[1:]:
                if i == len(j) or j[i]!=curr:
                    return reference[:i]
        return reference      