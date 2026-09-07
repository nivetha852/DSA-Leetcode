class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=[]
        word =""
        for i in s:
            if i!= " ":
                word = word+i
            else:
                if word !="":
                    words.append(word)
                    word = ""
        if word!="":
            words.append(word)

        words.reverse()
        return " ".join(words)
 








        