class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        k =0
        repeat = ""
        while (repeat+word)in sequence:
            repeat = repeat+word
            k = k+1
        return k