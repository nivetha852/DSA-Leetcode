class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for i,word in enumerate(words):
            for j,other in enumerate(words):
                if i!=j and word in other:
                    result.append(word)
                    break
        return result
        