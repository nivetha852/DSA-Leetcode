class Solution(object):
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        memo = {}
        def backtrack(start):
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in words:
                    sentences1 = backtrack(end)  
                    for rest in sentences1:
                        sentences.append(word if rest == "" else word + " " + rest)
            memo[start] = sentences
            return sentences
        return backtrack(0)