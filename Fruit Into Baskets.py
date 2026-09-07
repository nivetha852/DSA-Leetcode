class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        basket ={}
        l=0
        length= 0
        for i in range(0,len(fruits)):
            basket[fruits[i]]=basket.get(fruits[i],0)+1
            while len(basket)>2:
                basket[fruits[l]]= basket[fruits[l]]-1
                if basket[fruits[l]]==0:
                    del basket[fruits[l]]
                l=l+1
            length = max(length,i-l+1)
        return length
        