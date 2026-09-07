class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequency = {}
        for i in s:
            if i in frequency:
                frequency[i]= frequency[i]+1      
            else:
                frequency[i]=1
        n =sorted(frequency,key=frequency.get,reverse=True)
        r =""
        for i in n:
            r = r+i*frequency[i]
        return r