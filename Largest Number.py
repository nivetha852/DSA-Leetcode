class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n =[]
        for num in nums:
            n.append(str(num))
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                a = n[i]
                b = n[j]
                if a+b < b+a:
                    n[i]=b
                    n[j]=a
        if n[0]=="0":
            return "0"
        a =""
        for num in n:
            a=a+num
        return a
